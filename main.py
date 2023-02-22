import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import os
save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
headers = { 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
query="kartik aryan"
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzWDE8GCyDbRmLx6N2xcY6XpqrBcTg:1677094638704&source=lnms&tbm=isch&sa=X&sqi=2&ved=2ahUKEwi3icex8Kn9AhVXR2wGHYlNBcIQ_AUoAnoECAEQBA&biw=1280&bih=569&dpr=1.5")
soup=BeautifulSoup(response.content, "html.parser")
img_tags = soup.find_all("img")
del img_tags[0]
print(len(img_tags))
img_data_mongo = []
for i in img_tags:
    img_url = i["src"]
    img_data = requests.get(img_url).content
    my_dict = {"index":img_url, "Data":img_data}
    img_data_mongo.append(my_dict)
    with open(os.path.join(save_dir,f"{query}_{img_tags.index(i)}.jpg") ,"wb") as imgg:
        imgg.write(img_data)

