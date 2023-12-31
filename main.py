import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Today_Top_Hits import Top_50, Top_50_Artists

if __name__ == "__main__":
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=2560,14400")
    url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    time.sleep(2)

    print("#   Title")

    for i in range(0, len(Top_50)):
        Song = browser.find_element(By.CSS_SELECTOR, Top_50[i])

        print(i + 1, ":", Song.get_property("innerHTML"))

        time.sleep(0.5)

        Song.click()

        time.sleep(2)

        Image = browser.find_element(By.CSS_SELECTOR, ".\\_EShSNaBK1wUIaZQFJJQ").get_property("currentSrc")

        print(Image)

        time.sleep(0.5)

        browser.back()

        time.sleep(i / 5)


    print("\n#   Artist")

    for i in range(0, len(Top_50_Artists)):
        Artist = browser.find_element(By.CSS_SELECTOR, Top_50_Artists[i]).get_property("innerText")

        print(i + 1, ":", Artist)

        time.sleep(0.5)
