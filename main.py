from bs4 import BeautifulSoup
import requests

headers = {
"accept": "*/*",
"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Mobile Safari/537.36"

}
for t in range(10):
    req = requests.get(url=f"https://vk.com/id6546619{t}6", headers=headers)
    src = req.text

    soup = BeautifulSoup(src,"lxml")

    name = soup.find(class_="pp_cont").find(class_="op_header").text
    owners = soup.find_all(class_="OwnerInfo__rowCenter")
    variables = ["подписчиков","подписчик","подписчика"]
    town = "Город"
    friends,city = 0,0

    for i in owners:
        for j in i:
            if town in j:
                city = i.text
        for j in variables:
            if j in i.text:
                friends = i.text

    if not isinstance(friends,str):
        friends = "Неизвестно"
    if not isinstance(city,str):
        city = "Город: Неизвестен"

    print(f"{name}\n{city}, {friends}")
