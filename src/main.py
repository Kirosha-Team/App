from threading import Thread

import numpy

from src.libs.communicator import *
from src.libs.user_interface import *
from src.libs.gesture_recognizer import *
from src.libs.user_interface.windows.devices_settings import DevicesSettings

from src.constants import *

from src.utils import (
    create,
    camera,
    logger,
    landmarks,
    calculate,
    ip_address,
)

class App:
    def __activate_window(self, boolean: bool) -> None:
        self.current_window.window.attributes('-disabled', boolean)

    def __reset_window(self, *args) -> None:
        # Destroy the current window and create a new one with the provided arguments
        self.current_window.window.destroy()
        self.current_window.create(*args)

    def __set_window(self, index=None, *args) -> None:
        # Set the current window to the one at the specified index and create it with arguments
        if index is not None:
            self.current_window = self.windows[index]
            self.current_window.create(*args)
        else:
            if self.current_window:
                self.current_window.window.destroy()
                self.current_window = None

    def __reset_video_capture(self) -> None:
        # Stop the video capture if it is currently running
        if self.video_capture.is_running():
            self.video_capture.stop()

    def __set_video_capture(self, callback: callable, use_thread=True) -> None:
        # Change the video capture settings and start it, optionally in a new thread
        if not self.video_capture.is_running():
            self.video_capture.change(
                callback=callback
            )

            if use_thread:
                self.video_capture_thread = Thread(
                    target=lambda: self.video_capture.start()
                )
                self.video_capture_thread.start()
            else:
                self.video_capture.start()

    def __reset_communicator(self) -> None:
        # Stop the communicator if it is currently running
        if self.communicator.is_running():
            self.communicator.stop()

    def __set_communicator(self) -> None:
        # Start the communicator in a new thread if it is not already running
        if not self.communicator.is_running():
            self.communicator_thread = Thread(
                target=self.communicator.start
            )
            self.communicator_thread.start()

    def __get_hands(self, image: numpy.ndarray) -> list:
        # Process the image to detect hands and return the landmarks
        processed_image = self.hand_detector.process(image)
        return processed_image.multi_hand_landmarks

    def __process_recognition(self, image: numpy.ndarray) -> None:
        # Convert the image to RGB and process it for gesture recognition
        new_image = self.utils.convert(image)

        if self.__get_hands(new_image):
            self.gesture_recognizer.process(
                image=new_image
            )

    def __process_saving(self, image: numpy.ndarray) -> None:
        # Handle the saving of gesture images, resetting video capture if the max count is reached
        if self._count == (MAX_IMAGES + 1):
            self.__reset_video_capture()
            self.utils.destroy_all_windows()

            self.create.box(
                category=0,
                title='Информация',
                text='Жест успешно сохранён'
            )

            return

        # Convert the image to RGB and process it for saving
        new_image = self.utils.convert(image)

        result = self.__get_hands(new_image)

        if result:
            self._count += 1

            self.utils.save(
                image=image,
                name=self._name,
                index=self._count
            )

        landmarks.draw(image, result)

        self.utils.show(image)

    def __on_gesture_received(self, gesture: str) -> None:
        # Process the received gesture and send the corresponding command if found
        if gesture == DEFAULT_GESTURE or gesture == NO_GESTURE:
            return

        if len(self.data) == 0:
            return

        for data in self.data:
            command = None

            for line in data[3:]:
                key, value = line.split('=')

                if value == gesture:
                    command = key
                    break

            if command:
                address = (data[0], int(data[1]))

                self.communicator.send(
                    address=address,
                    command=command
                )

    def __on_server_received(self, data: list[str], address: tuple[str, int]) -> None:
        # Handle data received from the server and update the device registry
        self.communicator.send(address, DEFAULT_COMMAND)

        self.logger.debug(
            f'received message from client$address: {address}'
        )

        if not self.registry.get_device(address):
            self.logger.debug(
                'saving client data'
            )

            self.registry.write_device(address, data)
            self.data = self.registry.get_devices()

            self.create.box(
                category=0,
                title='Уведомление',
                text='Новое умное устройство было обнаружено'
            )

            self.logger.debug(
                f'successfully saved client data$data: {data}'
            )

            self.__reset_window()
            self.__set_communicator()

    def __change(self, index=None, process=True, listen=True, *args) -> None:
        # Change the current window and manage video capture and communicator settings
        self.logger.debug(
            f'changing window$index: {index}'
        )

        try:
            self.__set_window(None)

            if process:
                self.__set_video_capture(
                    callback=self.__process_recognition,
                )
            else:
                self.__reset_video_capture()

            if listen:
                self.__set_communicator()
            else:
                self.__reset_communicator()

            self.__set_window(
                index=index,
                *args
            )
        except OSError as reason:
            self.logger.warning(
                f'failed to open window correctly$reason: {reason}\nthis warning can be ignored'
            )

            self.create.box(
                category=1,
                title='Предупреждение',
                text='Не удалось открыть окно корректно!'
            )

    def __on_save_gesture_pressed(self, name: str) -> None:
        # Validate the gesture name and initiate the saving process if valid
        self.logger.debug(
            'checking gesture name'
        )

        if len(name) == 0:
            self.create.box(
                category=1,
                title='Предупреждение',
                text='Поле ввода не должно быть пустым!'
            )

            return

        if len(name) < MIN_GESTURE_NAME_LENGTH:
            self.create.box(
                category=1,
                title='Предупреждение',
                text=f'В имени должно присутствовать минимум {MIN_GESTURE_NAME_LENGTH} символа!'
            )

            return

        if len(name) > MAX_GESTURE_NAME_LENGTH:
            self.create.box(
                category=1,
                title='Предупреждение',
                text=f'В имени не должно присутствовать более {MAX_GESTURE_NAME_LENGTH} символов!'
            )

            return

        if not name.isalpha():
            self.create.box(
                category=1,
                title='Предупреждение',
                text='В имени должны присутствовать только буквы из алфавита!'
            )

            return

        gesture_path = Path.get_path_to(name, DATASETS_PATH)

        if Path.exists(gesture_path):
            self.create.box(
                category=1,
                title='Предупреждение',
                text='Имя уже занято!'
            )

            return

        self.logger.debug(
            'saving gesture images'
        )

        self.__set_window()

        self.create.box(
            category=0,
            title='Информация',
            text=
            '''
            Следуйте указаниям ниже:

            1. Включите свет в помещении
            2. Держите руку напротив обьектива камеры
            3. Не меняйте жест руки
            '''
        )

        if not self.video_capture.is_running():
            Path.create_directory(gesture_path)

            self._count = 0
            self._name = name

            self.__set_video_capture(
                callback=self.__process_saving,
                use_thread=False,
            )

            self.logger.debug(
                'successfully saved gesture'
            )

            self.__change(
                index=1,
                process=False
            )
        else:
            self.logger.warning(
                'failed to save gesture$reason: unknown'
            )

            self.create.box(
                category=1,
                title='Предупреждение',
                text='Возникли проблемы при сохранении жеста. Рекомендуется повторно выполнить данную операцию'
            )

            self.__change(
                index=1,
                process=False
            )

    def __on_save_device_pressed(self, data: list, input_data: list) -> None:
        # Save the device data after user confirmation
        self.logger.debug(
            'saving devices data'
        )

        box = self.create.box(
            category=2,
            title='Предупреждение',
            text='Вы уверены, что хотите сохранить изменения?'
        )

        if box:
            for key in input_data:
                input_box = input_data[key]
                self.registry.rewrite_device(data[1], key, input_box.get())

            self.logger.debug(
                'successfully saved changes'
            )

            self.data = self.registry.get_devices()
            self.__reset_window(self.registry.read_device(data[1]))

    def __on_retrain_pressed(self) -> None:
        # Retrain the gesture recognition model and provide feedback on the process
        self.logger.debug(
            'retraining model'
        )

        self.__activate_window(False)

        if self.gesture_recognizer:
            self.gesture_recognizer.recognizer.close()

        self.create.box(
            category=0,
            title='Информация',
            text='Обновление жестов. Это займёт некоторое время'
        )

        self.model_trainer.train()

        accuracy = calculate.accuracy(self.model_trainer.get_accuracy()[1])

        self.model_trainer.export()

        if accuracy >= MIN_ACCURACY_PERCENTAGE:
            self.logger.debug(
                'successfully trained model'
            )

            self.create.box(
                category=0,
                title='Информация',
                text='Обновление жестов прошло успешно'
            )
        else:
            self.logger.warning(
                f'training results are lower then expected:$minimum: {MIN_ACCURACY_PERCENTAGE}%$maximum: {MAX_ACCURACY_PERCENTAGE}%$received: {accuracy}%$this warning can be ignored'
            )

            self.create.box(
                category=1,
                title='Предупреждение',
                text='Возникли проблемы при обновлении жестов. Рекомендуется повторно выполнить данную операцию'
            )

        self.gesture_recognizer = GestureRecognizer(self.__on_gesture_received)

        self.__activate_window(True)

    def __on_remove_gesture_pressed(self, name: str) -> None:
        # Remove the specified gesture after user confirmation
        self.logger.debug(
            'removing gesture'
        )

        if name == DEFAULT_GESTURE or name == NO_GESTURE:
            self.create.box(
                category=1,
                title='Предупреждение',
                text='Нельзя удалить данный жест!'
            )

            return

        if Path.size(DATASETS_PATH) <= MIN_GESTURES_AMOUNT:
            self.create.box(
                category=1,
                title='Предупреждение',
                text=f'Для работы программы требуется {MIN_GESTURES_AMOUNT} или более жеста!'
            )

            return

        box = self.create.box(
            category=2,
            title='Предупреждение',
            text='Вы уверены, что хотите удалить жест?'
        )

        if box:
            self.logger.debug(
                'successfully removed gesture'
            )

            gesture_path = Path.get_path_to(name, DATASETS_PATH)
            Path.remove_directory(gesture_path)

            self.__reset_window()

    def __on_display_info_pressed(self) -> None:
        # Display the application version and IP address information
        self.create.box(
            category=0,
            title='Информация',
            text=
            f'''
            Версия: {VERSION}
            IP-адрес станции: {ip_address.get()}
            '''
        )

    def __init__(self):
        # Initialize the application and check for necessary resources
        self.registry = Registry()
        self.communicator = Communicator(self.__on_server_received)

        self.utils = camera.Utils()
        self.create = create.Create()
        self.logger = logger.Logger(__name__)
        self.video_capture = camera.VideoCapture()

        if Path.size(DATASETS_PATH) < 2:
            self.logger.error(
                f"no gestures were found$check {DATASETS_PATH} directory$if it's empty or missing -> run setup.py$then restart main.py"
            )

            self.create.box(
                category=3,
                title='Ошибка',
                text='Отсутствуют жесты!'
            )

            return

        if not Path.exists(ASSET_PATH):
            self.logger.error(
                f"no model was found$check {ASSET_PATH} directory$if it's empty or missing -> run setup.py$then restart main.py"
            )

            self.create.box(
                category=3,
                title='Ошибка',
                text='Отсутствует модель!'
            )

            return

        self.gesture_recognizer = GestureRecognizer(self.__on_gesture_received)
        self.model_trainer = ModelTrainer()
        self.hand_detector = HandDetector()

        self.windows = [
            Menu(self.__change, self.__on_display_info_pressed),
            GesturesEditor(self.__change, self.__on_remove_gesture_pressed, self.__on_retrain_pressed),
            DevicesEditor(self.__change),
            GestureName(self.__change, self.__on_save_gesture_pressed),
            DevicesSettings(self.__change, self.__on_save_device_pressed)
        ]

        self.current_window = None
        self.data = self.registry.get_devices()

        self.__set_communicator()
        self.__set_video_capture(self.__process_recognition)

        self.video_capture_thread.join(INIT_DELAY)

        if not self.video_capture.is_running():
            self.__reset_communicator()
            self.__reset_video_capture()

            self.logger.error(
                "failed to run video capture$check if camera module isn't missing and working correctly$then restart main.py"
            )

            self.create.box(
                category=3,
                title='Ошибка',
                text='Не удалось запустить модуль камеры!'
            )

            return

        self.logger.debug(
            'initialized'
        )

        self.__change(DEFAULT_WIN_INDEX)

if __name__ == "__main__":
    App()