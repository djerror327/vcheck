from .models import Version
from .webscrap import apacheServerScraper as ApacheScraper
from .webscrap import mysqlSaraper as MySQLScraper
from .webscrap import openJDKScraper as OpenJDKScraper


class Instances:
    # create a cron for refresh
    __mysql_8_latest_version = MySQLScraper.read_mysql_version()
    __apache_latest_version = ApacheScraper.read_apache_server_version()
    __openjdk_latest_version = OpenJDKScraper.read_openjdk_version()
    __instances = []

    def __init__(self):
        ips = ["10.120.50.40", "10.120.50.50", "10.120.50.60", "10.120.50.70", "110.120.50.90", "110.120.50.35"]

        # clear static array
        Instances.__instances = []

        # mysql 8 list
        for ip in ips:
            Instances.__instances.append(
                Version(ip, "MySQL update : " + Instances.__mysql_8_latest_version, "MySQL installed : 8.0.55")
            )

        # apache server list
        for ip in ips:
            Instances.__instances.append(
                Version(ip, "Apache update : " + Instances.__apache_latest_version, "Apache installed : 2.2.0")
            )

        # OpenJDK list
        for ip in ips:
            Instances.__instances.append(
                Version(ip, "OpenJDK update : " + Instances.__openjdk_latest_version, "OpenJDK installed : 8u200-b01")
            )

    @staticmethod
    def get_instances_details():
        return Instances.__instances


if __name__ == "__main__":
    a = Instances()
    b = a.get_instances_details()
    for i in b:
        print(i.instance_id, i.installed_version, i.release_version)
