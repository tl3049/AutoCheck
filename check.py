import requests
from bs4 import BeautifulSoup
import re


def check_author(name, url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=head)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")

    items = soup.findAll("div", attrs={"class": "field-item even"})
    res = str(items[0])

    pattern = re.compile(r'(.+?)<a href="([^"]+)">Proceedings')
    matches = pattern.findall(res)

    published: bool = False

    words = ""
    for title, link in matches:
        if "2024" in title.strip():
        #if "2025" in title.strip():
            #print(title.strip(), "=>", link)
            page_content = requests.get(link, headers=head).text
            soup = BeautifulSoup(page_content, "html.parser")
            papers = soup.findAll("div", attrs={"class": "paper_wrapper"})
            for paper in papers:
                # 假设你的tag对象是paper_tag
                paper_title = paper.find('div', class_='title').get_text(strip=True)
                paper_authors = paper.find('div', class_='authors').get_text(strip=True)
                if "Detecting Change" in paper_title and name in paper_authors:
                #if "Learning" in paper_title and name in paper_authors:
                    published = True
                    words = f"The paper titled \"{paper_title}\" authored by \"{paper_authors}\", has been published in IJCAI 2025."

    return published, words












