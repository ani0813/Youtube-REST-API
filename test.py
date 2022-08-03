import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes":100000, "name":"Ani", "views":1000},
        {"likes":1000, "name":"Not Ani", "views":100},
        {"likes":35, "name":"Other people", "views":1000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

# response = requests.delete(BASE + "video/0")
# print(response)

# input()

response = requests.get(BASE + "video/7")
print(response.json())