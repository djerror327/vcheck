import pandas as pd

from .models import Version
from .util.filereader import FileReader
from .webscrap import apacheServerScraper as ApacheScraper
from .webscrap import mysqlSaraper as MySQLScraper
from .webscrap import openJDKScraper as OpenJDKScraper


class Instances:
    # create a cron for refresh
    __mysql_8_latest_version = MySQLScraper.read_mysql_version()
    __apache_latest_version = ApacheScraper.read_apache_server_version()
    __openjdk_latest_version = OpenJDKScraper.read_openjdk_version()
    __instances = []
    __sorted_instances = []

    def __init__(self):
        # clear static array
        Instances.__instances = []
        Instances.__sorted_instances = []

        # read output files
        file_list = FileReader.read_ansible_out()
        java_out_file = file_list["ANSIBLE_JAVA_OUT_PATH"]
        apache_out_file = file_list["ANSIBLE_APACHE_OUT_PATH"]
        mysql_out_file = file_list["ANSIBLE_MYSQL_OUT_PATH"]
        # read java version
        df = pd.read_csv(java_out_file, sep=" ", header=None)
        java_version_arr = df[8].str.split("-")
        ip_arr = df[0]
        count = 0
        for data in java_version_arr:
            # print(ip_arr[count] + " " + data[1] + "-" + data[2])
            Instances.__instances.append(
                Version(ip_arr[count], "OpenJDK latest : " + Instances.__openjdk_latest_version,
                        "OpenJDK installed : " + data[1] + "-" + data[2])
            )
            count += 1
        # read apache version
        df = pd.read_csv(apache_out_file, sep=" ", header=None)
        apache_version_arr = df[3].str.split("/")
        ip_arr = df[0]
        count = 0
        for data in apache_version_arr:
            # print(ip_arr[count] + " " + data[1])
            Instances.__instances.append(
                Version(ip_arr[count], "Apache latest : " + Instances.__apache_latest_version,
                        "Apache installed : " + data[1])
            )
            count += 1
        # read mysql version
        df = pd.read_csv(mysql_out_file, sep=" ", header=None)
        mysql_version_arr = df[4]
        ip_arr = df[0]
        count = 0
        for data in mysql_version_arr:
            # print(ip_arr[count] + " " + data)
            Instances.__instances.append(
                Version(ip_arr[count], "MySQL latest : " + Instances.__mysql_8_latest_version,
                        "MySQL installed : " + data)
            )
            count += 1
        # sort ip fo instances
        Instances.__sort_instances_ips()

    @staticmethod
    def __sort_instances_ips():
        ips = []
        for version in Instances.__instances:
            ips.append(version.instance_id)

        # remove duplicates
        ips = list(set(ips))
        for ip in ips:
            for instance in Instances.__instances:
                if ip == instance.instance_id:
                    Instances.__sorted_instances.append(instance)

    @staticmethod
    def get_instances_details():
        return Instances.__sorted_instances

    @staticmethod
    def read_ansible_out():
        file_list = FileReader.read_ansible_out()
        print(file_list["ANSIBLE_JAVA_OUT_PATH"])


if __name__ == "__main__":
    a = Instances()
    # a.read_ansible_out()
    # b = a.get_instances_details()
    # for i in b:
    #     print(i.instance_id, i.installed_version, i.release_version)
