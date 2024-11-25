import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", class_ = "jobs").find_all("li") ## class라는 단어는 python 언어. class 를 만들 때 사용하는 것으로 예약되어 있다.

print(jobs)

manufacture = jobs[0:-1]
print(manufacture)

for job in jobs:
    title = job.find("span", class_="title").text() # 텍스트를 추출하고 싶으면 text() method
    region = job.find("span", class_="region").text()
    print(title, "-----", region)