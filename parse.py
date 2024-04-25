import json

from bs4 import BeautifulSoup

for i in range(1, 3):
    with open(f"./tmp{i}.html", "r", encoding="cp949") as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")
    script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
    # print(script_tag.string)
    with open(f"./tmp{i}_parse.json", "w") as file:
        data = json.loads(script_tag.string)
        base = data["props"]["pageProps"]["initialZustandState"]["intoAPP"]
        token = base["token"]
        _ACCESS_TOKEN = base["_ACCESS_TOKEN"]
        _ACCESS_TOKEN_SHOPBY = base["_ACCESS_TOKEN_SHOPBY"]
        serviceName = base["serviceConfig"]["serviceName"]
        APIKEY = base["serviceConfig"]["firebaseConfig"]["APIKEY"]

        # 값 출력
        print(f"token: {token}")
        print(f"_ACCESS_TOKEN: {_ACCESS_TOKEN}")
        print(f"_ACCESS_TOKEN_SHOPBY: {_ACCESS_TOKEN_SHOPBY}")
        print(f"serviceName: {serviceName}")
        print(f"APIKEY: {APIKEY}")
        file.write(json.dumps(data))
