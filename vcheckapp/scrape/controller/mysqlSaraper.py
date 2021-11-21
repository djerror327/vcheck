import pandas as pd


def read_mysql_version():
    url = "https://dev.mysql.com/downloads/mysql/8.0.html?tpl=files&os=22&osva=Ubuntu+Linux+20.04+(x86%2C+64-bit)"
    pd_list = pd.read_html(url)
    data=pd_list[0][1]
    print(data[0])


if __name__ == "__main__":
    read_mysql_version()
