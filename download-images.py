import json
import requests

posts = 'https://qagg.news/json/qposts.json'      # download the JSON file full of the posts
r = requests.get(posts)
r.json()

with open('qposts.json', 'w') as f:               # save the JSON data as a local file
  f.write(r.text)

with open('qposts.json', 'r') as f:               # open the saved file and let's get to work..
    posts = json.load(f)

z = 0
for x in posts:
    try:
        for i in x['media']:
            if len(str(i['filename'])) > 4:
                img = i['filename'][:-4]
                img = str(img).strip('.')

                response = requests.get("https://qagg.news/" + i['url'])
                file = open("images/" + i['filename'], "wb")
                file.write(response.content)
                file.close()
                print("downloaded - " + i['filename'])
    except:
        pass
