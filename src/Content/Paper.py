import requests
from bs4 import BeautifulSoup

class Papers_With_Code():
    def __init__(self, url='https://paperswithcode.com/'):
        self.url = url
        self.Content = self.__Parse_URL()

    def __Get_Abstract(self, arxiv):
        response = requests.get(f"https://paperswithcode.com{arxiv}")
        soup = BeautifulSoup(response.content, "html.parser")
        paper_abstract_div = soup.select_one(".paper-abstract")
        abstract = paper_abstract_div.find("p").text.strip()
        arxiv_url = paper_abstract_div.find("a", class_="badge badge-light")["href"]
        return (abstract, arxiv_url)

    def __Parse_URL(self):
        response = requests.get("https://paperswithcode.com/")
        soup = BeautifulSoup(response.content, "html.parser")
        results = []
        idx = 0
        for row in soup.select(".infinite-container .row.infinite-item.item.paper-card"):
            idx += 1
            paper_dict = {
                "Title": row.select_one("h1 a").get_text(strip=True),
                "Media": row.select_one(".item-image")["style"]
                .split("('")[1]
                .split("')")[0],
                "Stars": int(
                    row.select_one(".entity-stars .badge")
                    .get_text(strip=True)
                    .split(" ")[0]
                    .replace(",", "")
                ),
                "Github": row.select_one(".item-github-link a")["href"],
                "Arxiv": row.select_one("h1 a")["href"],
            }
            paper_dict['Abstract'], paper_dict['Arxiv'] = self.__Get_Abstract(paper_dict["Arxiv"])
            results.append(paper_dict)
        return results
    
    def Get_Content(self):
        return max(self.Content, key=lambda x:x['Stars'])
