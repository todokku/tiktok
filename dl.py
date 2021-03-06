from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import os


NEW = "new_tiktoks.txt"
OLD = "old_tiktoks.txt"
VIDEO_DIR = os.getcwd() + "/videos"
OPTIONS = Options()
CHROME_PATH = "C:/bin/chromedriver.exe"
VIDEO_CLASS = "jsx-3382097194"

new_links = []
old_links = []


def get_link(link):
    driver = webdriver.Chrome(executable_path=CHROME_PATH, options=OPTIONS)
    driver.get(link)
    video = driver.find_element(By.CLASS_NAME, VIDEO_CLASS)
    if str(driver.current_url) in old_links:
        driver.close()
        return None
    else:
        old_links.append(driver.current_url)
        return video.get_attribute("src")


def download_file(name, url):
    r = requests.get(url)
    f = open(VIDEO_DIR + name, 'wb')
    for chunk in r.iter_content(chunk_size=255):
        if chunk:
            f.write(chunk)
    f.close()


def init():
    for file in os.listdir(VIDEO_DIR):
        if file.endswith(".mp4"):
            os.remove(os.path.join(VIDEO_DIR, file))
    OPTIONS.add_argument("--headless")
    old_file = open(OLD, "r")
    old_links = old_file.readlines()
    new_file = open(NEW, "r")
    new_links = list(dict.fromkeys(new_file.readlines()))
    new_links = list(filter(lambda line: line not in old_links, new_links))
    old_file.close()
    new_file.close()
    return (new_links, old_links)


def exit():
    old_file = open(OLD, "w")
    for link in (old_links + new_links):
        old_file.write(link)
    old_file.close()


def run():
    for i, link in enumerate(new_links):
        url = get_link(link)
        if url is not None:
            download_file("/%d.mp4" % i, url)
            print(i, url)


if __name__ == "__main__":
    (new_links, old_links) = init()
    run()
    exit()
