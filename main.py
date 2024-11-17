import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)
jobs = soup.find("section",
class_="jobs").find_all("li")

for job in jobs:
    title = job.find("span", class_="title")
    region = job.find("span", class_="region")
    company, position, _ =  job.find_all("span", class_ ="company")
