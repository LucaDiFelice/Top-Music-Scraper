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

    song1 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(1) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song1)

    time.sleep(1)

    song2 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(2) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song2)

    time.sleep(1)

    song3 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(3) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song3)

    time.sleep(1)

    song4 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(4) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song4)

    time.sleep(1)

    song5 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(5) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song5)

    time.sleep(1)

    song6 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(6) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song6)

    time.sleep(1)

    song7 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(7) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song7)

    time.sleep(1)

    song8 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(8) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song8)

    time.sleep(1)

    song9 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(9) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song9)

    time.sleep(1)

    song10 = browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(10) > .h4HgbO_Uu1JYg5UGANeQ .t_yrXoUO3qGsJS4Y6iXX > \
                                .Type__TypeElement-sc-goli3j-0").get_property("innerHTML")
    print(song10)

    browser.quit()

