from pathlib import Path

import yaml


class FileReader:
    __ROOT_DIR = Path(__file__).parent.parent.parent
    __CONFIG_PATH = Path.joinpath(__ROOT_DIR, "config/app.yml")

    @staticmethod
    def __read_yml():
        print(FileReader.__CONFIG_PATH)
        with open(FileReader.__CONFIG_PATH, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def read_ips():
        data = FileReader.__read_yml()
        return data.get('servers').get('ip')
        # print(list_data[0])


if __name__ == "__main__":
    FileReader().read_ips()
