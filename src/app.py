from threading import (
    Thread,
)

from src.libs.gesture_recognizer import *
from src.libs.user_interface import *
from src.utils import *


class App:
    def __deactivate_window(
        self,
        boolean: bool,
    ) -> None:
        self.__current_window.roots[
            "window"
        ].attributes(
            "-disabled",
            boolean,
        )

    def __reset_window(
        self,
        *args,
    ) -> None:
        self.__current_window.roots[
            "window"
        ].destroy()
        self.__current_window.create(
            *args
        )

    def __set_window(
        self,
        index=None,
        *args,
    ) -> None:
        if (
            index
            is not None
        ):
            self.__current_window = self.__windows[
                index
            ]
            self.__current_window.create(
                *args
            )
            self.__current_window.roots[
                "window"
            ].mainloop()
        else:
            if (
                self.__current_window
            ):
                self.__current_window.roots[
                    "window"
                ].destroy()
                self.__current_window = None

    def __reset_video_capture(
        self,
    ) -> None:
        if (
            self.video_capture.is_running()
        ):
            self.video_capture.stop()

    def __set_video_capture(
        self,
        callback: callable,
        use_thread=True,
    ) -> None:
        if (
            not self.video_capture.is_running()
        ):
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

    def __reset_communicator(
        self,
    ) -> None:
        if (
            self.communicator.is_running()
        ):
            self.communicator.stop()

    def __set_communicator(
        self,
    ) -> None:
        if (
            not self.communicator.is_running()
        ):
            self.communicator_thread = Thread(
                target=self.communicator.start
            )
            self.communicator_thread.start()

    def __get_hands(
        self,
        image: numpy.ndarray,
    ) -> list:
        processed_image = self.hand_detector.process(
            image
        )
        return (
            processed_image.multi_hand_landmarks
        )

    def __process_recognition(
        self,
        image: numpy.ndarray,
    ) -> None:
        new_image = CameraUtils.convert(
            image
        )

        if self.__get_hands(
            new_image
        ):
            self.gesture_recognizer.process(
                image=new_image
            )

    def __process_saving(
        self,
        image: numpy.ndarray,
    ) -> None:
        if (
            self._count
            == (
                MAX_IMAGES
                + 1
            )
        ):
            self.__reset_video_capture()
            CameraUtils.destroy_all_windows()

            self.create.box(
                category=0,
                title="Информация",
                text="Жест успешно сохранён",
            )

            return

        new_image = CameraUtils.convert(
            image
        )

        result = self.__get_hands(
            new_image
        )

        if result:
            self._count += 1

            CameraUtils.save(
                image=image,
                name=self._name,
                index=self._count,
            )

        HandDetectorUtils.draw_landmarks(
            image,
            result,
        )

        CameraUtils.show(
            image
        )

    def __on_gesture_received(
        self,
        gesture: str,
    ) -> None:
        if (
            gesture
            == DEFAULT_GESTURE
            or gesture
            == NO_GESTURE
        ):
            return

        if (
            len(
                self.__devices_data
            )
            == 0
        ):
            return

        for data in (
            self.__devices_data
        ):
            command = None

            for line in data[
                3:
            ]:
                (
                    key,
                    value,
                ) = line.split(
                    "="
                )

                if (
                    value
                    == gesture
                ):
                    command = key
                    break

            if command:
                address = (
                    data[
                        0
                    ],
                    int(
                        data[
                            1
                        ]
                    ),
                )

                self.communicator.send(
                    address=address,
                    command=command,
                )

    def __on_server_received(
        self,
        data: list[
            str
        ],
        address: tuple[
            str,
            int,
        ],
    ) -> None:
        self.communicator.send(
            address,
            DEFAULT_COMMAND,
        )

        self.logger.debug(
            f"received message from client$address: {address}"
        )

        if not self.registry.get_device(
            address
        ):
            self.logger.debug(
                "saving client data"
            )

            self.registry.write_device(
                address,
                data,
            )
            self.data = (
                self.registry.get_devices()
            )

            self.create.box(
                category=0,
                title="Уведомление",
                text="Новое умное устройство было обнаружено",
            )

            self.logger.debug(
                f"successfully saved client data$data: {data}"
            )

            self.__reset_window()
            self.__set_communicator()

    def __change(
        self,
        index=None,
        process=True,
        listen=True,
        *args,
    ) -> None:
        self.logger.debug(
            f"changing window$index: {index}"
        )

        try:
            self.__set_window(
                None
            )

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
                index,
                *args,
            )
        except Exception as reason:
            self.logger.warning(
                f"failed to open window correctly$reason: {reason}\nthis warning can be ignored"
            )

            self.create.box(
                category=1,
                title="Предупреждение",
                text="Не удалось открыть окно корректно!",
            )

    def __on_save_gesture_pressed(
        self,
        name: str,
    ) -> None:
        self.logger.debug(
            "checking gesture name"
        )

        if (
            len(
                name
            )
            == 0
        ):
            self.create.box(
                category=1,
                title="Предупреждение",
                text="Поле ввода не должно быть пустым!",
            )

            return

        if (
            len(
                name
            )
            < MIN_GESTURE_NAME_LENGTH
        ):
            self.create.box(
                category=1,
                title="Предупреждение",
                text=f"В имени должно присутствовать минимум {MIN_GESTURE_NAME_LENGTH} символа!",
            )

            return

        if (
            len(
                name
            )
            > MAX_GESTURE_NAME_LENGTH
        ):
            self.create.box(
                category=1,
                title="Предупреждение",
                text=f"В имени не должно присутствовать более {MAX_GESTURE_NAME_LENGTH} символов!",
            )

            return

        if (
            not name.isalpha()
        ):
            self.create.box(
                category=1,
                title="Предупреждение",
                text="В имени должны присутствовать только буквы из алфавита!",
            )

            return

        gesture_path = Path.get_path_to(
            name,
            DATASETS_PATH,
        )

        if Path.exists(
            gesture_path
        ):
            self.create.box(
                category=1,
                title="Предупреждение",
                text="Имя уже занято!",
            )

            return

        self.logger.debug(
            "saving gesture images"
        )

        self.__set_window()

        self.create.box(
            category=0,
            title="Информация",
            text="""
            Следуйте указаниям ниже:

            1. Включите свет в помещении
            2. Держите руку напротив обьектива камеры
            3. Не меняйте жест руки
            """,
        )

        if (
            not self.video_capture.is_running()
        ):
            Path.create_directory(
                gesture_path
            )

            self._count = 0
            self._name = name

            self.__set_video_capture(
                callback=self.__process_saving,
                use_thread=False,
            )

            self.logger.debug(
                "successfully saved gesture"
            )

            self.__change(
                index=1,
                process=False,
            )
        else:
            self.logger.warning(
                "failed to save gesture$reason: video capture is still running"
            )

            self.create.box(
                category=1,
                title="Предупреждение",
                text="Возникли проблемы при сохранении жеста. Рекомендуется повторно выполнить данную операцию",
            )

            self.__change(
                index=1,
                process=False,
            )

    def __on_save_device_pressed(
        self,
        data: list,
        input_data: list,
    ) -> None:
        self.logger.debug(
            "saving devices data"
        )

        box = self.create.box(
            category=2,
            title="Предупреждение",
            text="Вы уверены, что хотите сохранить изменения?",
        )

        if box:
            for key in input_data:
                input_box = input_data[
                    key
                ]
                self.registry.rewrite_device(
                    data[
                        1
                    ],
                    key,
                    input_box.get(),
                )

            self.logger.debug(
                "successfully saved changes"
            )

            self.data = (
                self.registry.get_devices()
            )
            self.__reset_window(
                self.registry.read_device(
                    data[
                        1
                    ]
                )
            )

    def __on_retrain_pressed(
        self,
    ) -> None:
        self.logger.debug(
            "retraining model"
        )

        self.__deactivate_window(
            True
        )

        if (
            self.gesture_recognizer
        ):
            self.gesture_recognizer.recognizer.close()

        self.create.box(
            category=0,
            title="Информация",
            text="Обновление жестов. Это займёт некоторое время",
        )

        self.model_trainer.train()

        accuracy_results = accuracy(
            self.model_trainer.get_accuracy()[
                1
            ]
        )

        self.model_trainer.export()

        if (
            accuracy_results
            >= MIN_ACCURACY_PERCENTAGE
        ):
            self.logger.debug(
                "successfully trained model"
            )

            self.create.box(
                category=0,
                title="Информация",
                text="Обновление жестов прошло успешно",
            )
        else:
            self.logger.warning(
                f"training results are lower then expected:$minimum: {MIN_ACCURACY_PERCENTAGE}%$maximum: {MAX_ACCURACY_PERCENTAGE}%$received: {accuracy_results}%$this warning can be ignored"
            )

            self.create.box(
                category=1,
                title="Предупреждение",
                text="Возникли проблемы при обновлении жестов. Рекомендуется повторно выполнить данную операцию",
            )

        self.gesture_recognizer = GestureRecognizer(
            self.__on_gesture_received
        )

        self.__deactivate_window(
            False
        )

    def __on_remove_gesture_pressed(
        self,
        name: str,
    ) -> None:
        self.logger.debug(
            "removing gesture"
        )

        if (
            name
            == DEFAULT_GESTURE
            or name
            == NO_GESTURE
        ):
            self.create.box(
                category=1,
                title="Предупреждение",
                text="Нельзя удалить данный жест!",
            )

            return

        if (
            Path.size(
                DATASETS_PATH
            )
            <= MIN_GESTURES_AMOUNT
        ):
            self.create.box(
                category=1,
                title="Предупреждение",
                text=f"Для работы программы требуется {MIN_GESTURES_AMOUNT} или более жеста!",
            )

            return

        box = self.create.box(
            category=2,
            title="Предупреждение",
            text="Вы уверены, что хотите удалить жест?",
        )

        if box:
            self.logger.debug(
                "successfully removed gesture"
            )

            gesture_path = Path.get_path_to(
                name,
                DATASETS_PATH,
            )
            Path.remove_directory(
                gesture_path
            )

            self.__reset_window()

    def __on_display_info_pressed(
        self,
    ) -> None:
        self.create.box(
            category=0,
            title="Информация",
            text=f"""
            Версия: {VERSION}
            IP-адрес станции: {CommunicatorUtils.get_ip_address()}
            """,
        )

    def __run_ui(
        self,
    ) -> None:
        try:
            self.__windows = [
                MainMenu(
                    self.__change,
                    self.__on_display_info_pressed,
                ),
                GesturesEditor(
                    self.__change,
                    self.__on_remove_gesture_pressed,
                    self.__on_retrain_pressed,
                ),
                DevicesEditor(
                    self.__change
                ),
                GestureName(
                    self.__change,
                    self.__on_save_gesture_pressed,
                ),
                DevicesSettings(
                    self.__change,
                    self.__on_save_device_pressed,
                ),
            ]

            self.__change(
                DEFAULT_WIN_INDEX
            )
        except AttributeError as result:
            self.logger.error(
                f"failed to initialize ui$info: {result}$if this error occur -> restart main.py"
            )

            self.create.box(
                category=3,
                title="Ошибка",
                text="Не удалось запустить интерфейс!",
            )

            breakpoint()

    def __run_modules(
        self,
    ) -> None:
        try:
            self.__set_communicator()
            self.__set_video_capture(
                self.__process_recognition
            )

            self.video_capture_thread.join(
                INIT_DELAY
            )
        except AttributeError as result:
            self.logger.error(
                f"failed to initialize components$info: {result}$if this error occur -> run setup.py$then restart main.py"
            )

            self.create.box(
                category=3,
                title="Ошибка",
                text="Не удалось запустить модули программы!",
            )

            breakpoint()

    def __import_modules(
        self,
    ) -> None:
        try:
            self.registry = (
                Registry()
            )
            self.communicator = Communicator(
                self.__on_server_received
            )

            self.create = (
                Create()
            )
            self.logger = Logger(
                __name__
            )
            self.video_capture = (
                VideoCapture()
            )

            self.gesture_recognizer = GestureRecognizer(
                self.__on_gesture_received
            )
            self.model_trainer = (
                ModelTrainer()
            )
            self.hand_detector = (
                HandDetector()
            )
        except (
            ImportError,
            OSError,
        ) as result:
            self.logger.error(
                f"failed to load components$info: {result}$if this error occur -> run setup.py$then restart main.py"
            )

            self.create.box(
                category=3,
                title="Ошибка",
                text="Не удалось импортировать модули программы!",
            )

            breakpoint()

    def __init__(
        self,
    ):
        self.__import_modules()
        self.__run_modules()

        self.logger.debug(
            "attempting to initialize application..."
        )

        self.__current_window = None
        self.__devices_data = (
            self.registry.get_devices()
        )

        self.__run_ui()


if (
    __name__
    == "__main__"
):
    App()
