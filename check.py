import requests
from bs4 import BeautifulSoup
import re


def check_author(name, url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=head)#get the webpage
    content = response.text
    soup = BeautifulSoup(content, "html.parser")#parse the webpage

    items = soup.findAll("div", attrs={"class": "field-item even"})#find the target div
    res = str(items[0])

    pattern = re.compile(r'(.+?)<a href="([^"]+)">Proceedings')
    matches = pattern.findall(res)#find the tuples (title, link)

    published: bool = False

    words = ""
    for title, link in matches:
        if "2025" in title.strip():
            page_content = requests.get(link, headers=head).text #go to the proceeding page
            soup = BeautifulSoup(page_content, "html.parser")#parse the webpage
            papers = soup.findAll("div", attrs={"class": "paper_wrapper"})#find all papers
            for paper in papers:
                paper_title = paper.find('div', class_='title').get_text(strip=True)#get the title
                paper_authors = paper.find('div', class_='authors').get_text(strip=True)#get the authors
                if "Learning" in paper_title and name in paper_authors:#condition to check
                    published = True
                    words = f"The paper titled \"{paper_title}\" authored by \"{paper_authors}\", has been published in the 2025 proceeding."
    return published, words












