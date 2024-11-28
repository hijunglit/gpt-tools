import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    print(f"Scrapping {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_ = "jobs").find_all("li")[0:-1] ## class라는 단어는 python 언어. class 를 만들 때 사용하는 것으로 예약되어 있다.
    for job in jobs:
        title = job.find("span", class_="title").text ## 텍스트를 추출하고 싶으면 text() method
        company, position, region = job.find_all("span", class_="company")
        url = job.find("div", class_="tooltip").next_sibling["href"]
        job_data = {
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)
        company = company.text
        position = position.text
        region = region.text
        print(title, company, region, "------\n")

response = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")
soup = BeautifulSoup(response.content, "html.parser")

buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))

for x in rage(buttons):
    url=f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))
