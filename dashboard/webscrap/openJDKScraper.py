import io

import pandas as pd
import requests
from bs4 import BeautifulSoup


def read_openjdk_version():
    url = "https://wiki.openjdk.java.net/display/jdk8u/Main"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    s = soup.select('html')[0].text.strip('jQuery1720724027235122559_1542743885014(').strip(')')
    s = s.replace('null', '"placeholder"')
    data = io.StringIO(s)
    df = pd.DataFrame(data)
    df_version = df[272:273]
    # df_apache_version = df_version.iloc[-1]
    df_data = df_version[0]
    # print(df_apache_version[0][19:25])
    for version in df_version[0]:
        print("open jdk latest version " + version[650:659])
        return version[650:659]
    # print(df_data[650:659].values)


if __name__ == "__main__":
    a = read_openjdk_version()
    print(a)
