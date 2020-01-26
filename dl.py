from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests


NEW = "new_tiktoks.txt"
OLD = "old_tiktoks.txt"
OPTIONS = Options()
CHROME_PATH = "C:/bin/chromedriver.exe"
VIDEO_CLASS = "jsx-3382097194"

new_links = []
old_links = []


def get_link(link):
    driver = webdriver.Chrome(executable_path=CHROME_PATH, options=OPTIONS)
    driver.get(link)
    video = driver.find_element(By.CLASS_NAME, VIDEO_CLASS)
    return video.get_attribute("src")
    driver.close()


def download_file(name, url):
    r = requests.get(url)
    f = open(name, 'wb')
    for chunk in r.iter_content(chunk_size=255):
        if chunk:
            f.write(chunk)
    f.close()


def init():
    OPTIONS.add_argument("--headless")
    in = open()


def close():
    print("Closing")


def run():
    for i, link in enumerate(links):
        url = get_link(link)
        download_file(str(i)+".mp4", url)
        print(i, url)


if __name__ == "__main__":
    init()
    run()
