from pathlib import Path

import yaml


class FileReader:
    __ROOT_DIR = Path(__file__).parent.parent.parent
    __CONFIG_PATH = Path.joinpath(__ROOT_DIR, "config/app.yml")
    __ANSIBLE_JAVA_OUT_PATH = Path.joinpath(__ROOT_DIR, "ansible/output/java_version")
    __ANSIBLE_APACHE_OUT_PATH = Path.joinpath(__ROOT_DIR, "ansible/output/apache_server_version")
    __ANSIBLE_MYSQL_OUT_PATH = Path.joinpath(__ROOT_DIR, "ansible/output/mysql_version")
    __ANSIBLE_START_SH_PATH = Path.joinpath(__ROOT_DIR, "ansible/start.sh")

    @staticmethod
    def __read_yml():
        print(FileReader.__CONFIG_PATH)
        with open(FileReader.__CONFIG_PATH, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def read_ansible_out():
        # print(FileReader.__ANSIBLE_JAVA_OUT_PATH)
        # print(FileReader.__ANSIBLE_APACHE_OUT_PATH)
        # print(FileReader.__ANSIBLE_MYSQL_OUT_PATH)

        return {"ANSIBLE_JAVA_OUT_PATH": FileReader.__ANSIBLE_JAVA_OUT_PATH,
                "ANSIBLE_APACHE_OUT_PATH": FileReader.__ANSIBLE_APACHE_OUT_PATH,
                "ANSIBLE_MYSQL_OUT_PATH": FileReader.__ANSIBLE_MYSQL_OUT_PATH}
        # read java version
        # df = pd.read_csv(FileReader.__ANSIBLE_JAVA_OUT_PATH, sep=" ", header=None)
        # java_version_arr = df[8].str.split("-")
        # ip_arr = df[0]
        # count = 0
        # for data in java_version_arr:
        #     print(ip_arr[count] + " " + data[1] + "-" + data[2])
        #     count += 1
        #
        # # read apache version
        # df = pd.read_csv(FileReader.__ANSIBLE_APACHE_OUT_PATH, sep=" ", header=None)
        # apache_version_arr = df[3].str.split("/")
        # ip_arr = df[0]
        # count = 0
        # for data in apache_version_arr:
        #     print(ip_arr[count] + " " + data[1])
        #     count += 1
        #
        # # read mysql version
        # df = pd.read_csv(FileReader.__ANSIBLE_MYSQL_OUT_PATH, sep=" ", header=None)
        # mysql_version_arr = df[4]
        # ip_arr = df[0]
        # count = 0
        # for data in mysql_version_arr:
        #     print(ip_arr[count] + " " + data)
        #     count += 1

    @staticmethod
    def ansible_start_sh_path():
        return FileReader.__ANSIBLE_START_SH_PATH

    @staticmethod
    def scheduler_time():
        data = FileReader.__read_yml()
        return data.get('schedule').get('seconds')


if __name__ == "__main__":
    a = FileReader().get_app_root_path()
    print(a)
