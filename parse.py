from bs4 import BeautifulSoup

for i in range(1, 3):
    with open(f"./tmp{i}.html", "r", encoding="cp949") as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")
    with open(f"./tmp2_parse_{i}.html", "w") as file:
        file.write(soup.prettify())
