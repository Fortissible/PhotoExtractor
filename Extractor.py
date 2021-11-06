import json,requests,urllib.request
from bs4 import BeautifulSoup

websites = f"http://hatoking.com/journal/4352.html?fbclid=IwAR0-uNqUGoLVN9de-rLiKCXwypakhMo64dRO45QQFYgH1uhRYOhlfUol7c8"
response = requests.get(websites)
soup = BeautifulSoup(response.text, 'html.parser')
count = 1
if response.status_code == 200:
    paragraph = soup.find_all("a")
    for i in paragraph:
        if (i['href']).endswith("jpg"):
            print(i['href'])
            saves = i['href']
            urllib.request.urlretrieve(saves, str(count)+".jpg")
        elif (i['href']).endswith("png"):
            print(i['href'])
            saves = i['href']
            urllib.request.urlretrieve(saves, str(count)+".png")
        count+=1