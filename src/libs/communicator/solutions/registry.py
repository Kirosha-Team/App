"""
NAME: registry.py
DESC: solution for adding, removing, rewriting devices data

CLASS REGISTRY:
    STATIC METHODS:
        write_device --> saves device id_address, port, name, functions in file
        rewrite --> changes specific device data in file
        read_device --> returns device id_address, port, name, functions
        remove_device --> removes device file
        get_device --> returns file existence
"""

from src.utils import *
from src.constants import *


class Registry:
    @staticmethod
    def write_device(
        address: tuple[
            str,
            int,
        ],
        data: list[
            str
        ],
    ) -> None:
        port = address[
            1
        ]

        file = (
            DEVICES_PATH
            + f"/{port}.txt"
        )

        if not Path.exists(
            file
        ):
            with open(
                file,
                "w",
            ) as file:
                file.write(
                    address[
                        0
                    ]
                    + "\n"
                )  # Write the device address to the file
                file.write(
                    str(
                        address[
                            1
                        ]
                    )
                    + "\n"
                )  # Write the port number to the file
                file.write(
                    data[
                        0
                    ]
                    + "\n"
                )  # Write the first data entry to the file

                for value in data[
                    1:
                ]:
                    file.write(
                        value
                        + "=none\n"
                    )  # Write each function with a default value of 'none'

                file.close()

    @staticmethod
    def rewrite_device(
        port: str,
        key: str,
        value: str,
    ) -> None:
        assert (
            type(
                key
            )
            is str
        )
        assert (
            type(
                port
            )
            is str
        )
        assert (
            type(
                value
            )
            is str
        )

        file = (
            DEVICES_PATH
            + f"/{port}.txt"
        )

        if Path.exists(
            file
        ):
            old_data = Registry.read_device(
                port
            )

            Registry.remove_device(
                port
            )

            new_file = open(
                file,
                "w",
            )

            for line in old_data:
                if (
                    list(
                        line.split(
                            "="
                        )
                    )[
                        0
                    ]
                    == key
                ):
                    new_file.write(
                        key
                        + "="
                        + value
                        + "\n"
                    )
                else:
                    new_file.write(
                        line
                        + "\n"
                    )

            new_file.close()

    @staticmethod
    def read_device(
        port: str,
    ) -> list[
        str
    ]:
        assert (
            type(
                port
            )
            is str
        )

        file = (
            DEVICES_PATH
            + f"/{port}.txt"
        )

        if Path.exists(
            file
        ):
            with open(
                file,
                "r",
            ) as file:
                lines = [
                    line.split(
                        "\n"
                    )[
                        0
                    ]
                    for line in file.readlines()
                ]

            file.close()

            return lines

    @staticmethod
    def remove_device(
        port: str,
    ) -> None:
        assert (
            type(
                port
            )
            is str
        )

        file = (
            DEVICES_PATH
            + f"/{port}.txt"
        )

        Path.remove_file(
            file
        )

    @staticmethod
    def get_device(
        address: tuple[
            str,
            int,
        ],
    ) -> bool:
        port = address[
            1
        ]

        file = (
            DEVICES_PATH
            + f"/{port}.txt"
        )

        return Path.exists(
            file
        )

    @staticmethod
    def get_devices() -> (
        list
    ):
        devices_data = (
            []
        )

        if Path.empty(
            DEVICES_PATH
        ):
            return devices_data

        for device in os.listdir(
            DEVICES_PATH
        ):
            (
                port,
                file_format,
            ) = device.split(
                "."
            )

            data = Registry.read_device(
                port
            )

            devices_data.append(
                data
            )

        return devices_data
