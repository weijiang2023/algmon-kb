# download the nce english content from the website: https://en-nce.xiao84.com/
import requests
import os

# url = 'https://en-nce.xiao84.com/nce1/19991.html'
# url = 'https://en-nce.xiao84.com/nce1/19992.html'
url = 'https://en-nce.xiao84.com/nce1/19993.html'
response = requests.get(url)
content = response.text

# extract the useful info from this raw content

with open('./raw.data/3.raw.data.md', 'w') as file:
    file.write(content)
