import requests
from bs4 import BeautifulSoup

result = requests.get("http://localhost:8080/tasks")

#result = requests.get("http://drdelozier.pythonanywhere.com/tasks")
assert result.status_code == 200
#print(result.text)
#exit()
soup = BeautifulSoup(result.text, 'html.parser')
#print(soup)
table = soup.find('table')
print(table)
for tr in table.find_all("tr"):
    print('---')
    print(tr)
    id = tr.find(contents="id").text
    text = tr.find(contents="text").text
    print(id,text)
