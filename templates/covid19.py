import requests
from bs4 import BeautifulSoup

def cornoa_summary():
    url = "http://ncov.mohw.go.kr/"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml')
    p = soup.select("table.ds_table thead tr th span")
    t = soup.select("table.ds_table tbody tr td span")

    for n in range(0, len(p)):
        print(t[n].text + " : " + p[n].text)

if __name__ == "__main__":
    cornoa_summary()