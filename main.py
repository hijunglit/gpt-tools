from requests import get

websites = (
    "httpstat.us/200",
    "httpstat.us/300",
    "httpstat.us/401",
    "httpstat.us/501",
)

results = {}

for website in websites: 
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code >= 200 and response.status_code <= 299:
        results[website] = "OK"
    elif response.status_code >= 300 and response.status_code <= 309:
        results[website] = "redirection"
    elif response.status_code >= 400 and response.status_code <= 499:
        results[website] = "client error"
    elif response.status_code >= 500 and response.status_code < 512:
        results[website] = "server error"

print(results)
# 3xx 코드 핸들링

# 상태 코드 반환 웹사이트
# https://httpstat.us/ 
