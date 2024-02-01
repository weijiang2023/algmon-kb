print("Algmon Lookbook is running ...")

def get_links():
    """
    get links from source from the webpages
    """
    webpage_links = []

    base_link = "https://wwd.com/fashion-news/shows-reviews/gallery/gabriela-hearst-mens-fall-1236156052/"
    file_name = "gabriela-hearst-mens-fall-2024/"
    num_looks = 25
    for i in range(0, 26):
        if i == 0:
            webpage_link = base_link + file_name
        else:
            webpage_link = base_link + file_name[:-1] + "-" + str(i) + "/"
        print("webpage_link:", webpage_link)
        webpage_links.append(webpage_link)

def download_source():
    """
    download the page source
    """
    import requests
    for idx,link in enumerate(webpage_links):
        url = link
        response = requests.get(url)
        html_content = response.text
        with open('./data/pagesource/' + str(idx) + '.html','wb') as f:
            f.write(response.content)

def download_image(filename):
    """
    Download the lookbook image
    
    Args:
    filename: the input lookbook name

    """
    import requests

    url = 'https://wwd.com/wp-content/uploads/2024/01/' + filename
    response = requests.get(url)
    with open('./data/lookbook/' + filename, 'wb') as f:
        f.write(response.content)

def extract_lookbook_image_links_from_page():
    with open("./data/pagesource/0.html", "r", encoding="utf-8") as file:
        content = file.read()
        #print(content)

        import re
        #text = "Your text containing the pattern <img width=\"240\" height=\"300\" src=\"https://wwd.com/wp-content/uploads/2024/01/"
        pattern = r'<img width="240" height="300" src="https://wwd.com/wp-content/uploads/2024/01/(.*?)\"'
        matches = re.findall(pattern, content)

        for match in matches:
            filename = match[:-6]
            download_image(filename)

extract_lookbook_image_links_from_page()
print("Algmon Lookbook is closed ...")