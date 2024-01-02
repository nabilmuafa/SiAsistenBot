from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

# credentials
load_dotenv()
USERNAME = os.getenv("SSO_USN")
PASSWORD = os.getenv("SSO_PASS")


class Scraper(webdriver.Chrome):
    def __init__(self):
        options = Options()
        options.headless = True
        options.add_argument("--headless=new")
        super().__init__(options=options)

    def get_lowongan(self):
        # login
        self.get('https://siasisten.cs.ui.ac.id/login/')
        self.find_element(By.ID, "id_username").send_keys(USERNAME)
        self.find_element(By.ID, "id_password").send_keys(PASSWORD)
        self.find_element(By.CLASS_NAME, "submit").click()

        # WebDriverWait(driver=self, timeout=10).until(
        #     lambda x: x.execute_script(
        #         "return document.readyState === 'complete'")
        # )
        texts = []
        xpath = "/html/body/div[1]/div[3]/div/div[1]/table[1]/tbody"
        element_list = self.find_elements(By.XPATH, xpath+"/tr")
        for element in element_list[1:]:
            texts.append(element.find_element(By.XPATH, "td[2]").text)

        return texts
