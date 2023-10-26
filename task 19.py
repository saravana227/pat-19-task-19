from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class WebpageScraper:
    def __init__(self):
        # Initialize the WebDriver for Firefox
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def login(self, username, password):
        # Open the URL
        self.driver.get("https://www.saucedemo.com/")

        self.driver.maximize_window()
        # Find and fill in the username and password fields using XPATH
        username_input = self.driver.find_element(by=By.XPATH, value="//input[@data-test='username']")
        password_input = self.driver.find_element(by=By.XPATH, value="//input[@data-test='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        sleep(4)

        # Find and click the login button using XPATH
        login_button = self.driver.find_element(by=By.XPATH, value="//input[@id='login-button']")
        login_button.click()

    def fetch_webpage_info(self):
        # Fetch the title of the webpage
        webpage_title = self.driver.title

        # Fetch the current URL of the webpage
        current_url = self.driver.current_url

        # Extract the entire contents of the webpage
        webpage_content = self.driver.page_source

        return webpage_title, current_url, webpage_content

    def save_webpage_content(self, content, filename):
        # Save the webpage content to a text file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

    def close_browser(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    # Create an instance of the WebpageScraper class
    scraper = WebpageScraper()

    # Login with the provided credentials
    scraper.login("standard_user", "standard_user")

    # Fetch webpage information
    title, current_url, content = scraper.fetch_webpage_info()

    # Print the title and current URL
    print("Title of the webpage:", title)
    print("Current URL of the webpage:", current_url)

    # Save the webpage content to a text file
    scraper.save_webpage_content(content, "webpage_task_11.txt")

    # Close the browser
    scraper.close_browser()