import requests as req
from bs4 import BeautifulSoup


req = req.get("https://csie.asia.edu.tw/project/semester-103",verify=False)
req.encoding = "utf8"
if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.select("div.table-responsive p")
    fp = open("outWeb.text","w",encoding="utf8")
    for val in result1:
        text2 = val.text.replace('\n', '')
        print(text2)
        fp.write(text2+"\n")
    fp.close()
else:
    print("no page")