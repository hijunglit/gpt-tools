import requests

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

response.status_code

print(response.content)