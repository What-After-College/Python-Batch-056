import requests as req

url = "https://sv443.net/jokeapi/v2/joke/Programming"

res = req.get(url)

rec_data = res.json()

# print(rec_data)
for data in rec_data.keys():
    if data != 'flags' and data !='id' and data !='lang':
        print("{}: {}".format(data, rec_data[data]))