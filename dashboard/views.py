from django.shortcuts import render

from .models import Version
from .webscrap import mysqlSaraper as MySQLScraper


def index(request):
    # version = Version()
    # version.release_version = "MySQL update : " + MySQLScraper.read_mysql_version()
    # version.installed_version = "MySQL installed : 8.1.10"
    # version.instance_id = "10.120.50.40"
    v1 = Version("10.120.50.40", "MySQL update : " + MySQLScraper.read_mysql_version(), "MySQL installed : 8.1.10")
    v2 = Version("10.120.50.50", "MySQL update : " + MySQLScraper.read_mysql_version(), "MySQL installed : 8.0.1")
    v3 = Version("10.120.50.60", "MySQL update : " + MySQLScraper.read_mysql_version(), "MySQL installed : 8.0.12")

    list = []
    list.append(v1)
    list.append(v2)
    list.append(v3)

    return render(request, "index.html", {'list': list})
