# Download lookbook images from WWD

import os


def download_images(start, end, base_url, extension, folder_name):
    """
    Download images in a range from start to end, given a base URL and file extension.

    Args:
    start: The starting counter number as an integer.
    end: The ending counter number as an integer.
    base_url: The base URL before the counter and extension.
    extension: The file extension of the images.
    """
    for i in range(start, end + 1):
        # TODO: Format the counter with leading zeros nicely
        counter = f"{i:03}"
        download_link = f"{base_url}{counter}{extension}"
        print("Download", download_link)
        download_image(f"{counter}.png", download_link, folder_name)


def download_image(filename, url, folder_name):
    """
    Download an image from a URL and save it as a PNG file.

    Args:
    filename: The name of the file to save the image as.
    url: The URL of the image to download.
    """
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        print("Save", filename)
        with open(folder_name + '/' + filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download {url}")


# base_url = 'https://wwd.com/wp-content/uploads/2024/01/issey-miyake-mens-fall-24-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/maison-margiela-couture-spring-24-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/fendi-couture-spring-24-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/y-3-rtw-fall-24-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/issey-miyake-mens-fall-24-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/valentino-couture-spring-24-couture-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/chanel-couture-spring-24-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/christian-dior-couture-spring-24-'
# base_url = 'https://wwd.com/wp-content/uploads/2023/09/ralph-lauren-spring-24-GG-'
# base_url = 'https://wwd.com/wp-content/uploads/2023/04/Fear-of-God-Collection-8-CTSY-'
# base_url = 'https://wwd.com/wp-content/uploads/2024/01/ziggy-chen-mens-fall-2024-ctsy-'
# base_url = 'https://wwd.com/wp-content/uploads/2023/09/uma_wang_rtw_ss24_pfw_ctsy_'
# base_url = 'https://wwd.com/wp-content/uploads/2023/03/uma-wang-rtw-fall-2023-'
# base_url = 'https://wwd.com/wp-content/uploads/2022/09/uma-wang-rtw-ss2023-paris'
base_url = 'https://wwd.com/wp-content/uploads/2023/03/uma-wang-rtw-fall-2023-'

folder_name = './data/lookbook/Uma Wang RTW Fall 2023'
lower = 10
upper = 32

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

download_images(lower, upper, base_url, '.jpg', folder_name)
