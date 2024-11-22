import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)
jobs = soup.find("section",
class_="jobs").find_all("li")[1:-1] # 맨 위 li 하나, 맨 아래 li 하나 필요 없음.

all_jobs=[]

for job in jobs:
    title = job.find("span", class_="title").text
    company, position, region =  job.find_all("span", class_ ="company")
    company = company.text
    position = position.text
    region = region.text
    print(title, company, position, region, "--------\n")
    url = job.find("href")
    job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region.text,
        "url": f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)

print(all_jobs)