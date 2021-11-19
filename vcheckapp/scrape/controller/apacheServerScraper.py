import io

import pandas as pd
import requests
from bs4 import BeautifulSoup


def read_apache_server_version():
    url = 'https://httpd.apache.org/download.cgi'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    s = soup.select('html')[0].text.strip('jQuery1720724027235122559_1542743885014(').strip(')')
    s = s.replace('null', '"placeholder"')
    data = io.StringIO(s)
    df = pd.DataFrame(data)
    df_version = df[0:107]
    df_apache_version = df_version.iloc[-1]

    print(df_apache_version[0][19:25])


if __name__ == "__main__":
    read_apache_server_version()
