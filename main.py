import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


if __name__ == "__main__":
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=2560,1440")
    url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    time.sleep(2)

    song = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(1) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")

    print(song)

    time.sleep(1)

    song2 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(2) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song2)

    time.sleep(1)

    song3 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(3) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song3)

    browser.quit()

