from selenium import webdriver
import time


def instagram_login(username, password):

    getdriver = ("https://www.instagram.com/accounts/login/")

    driver = webdriver.Firefox()
    driver.get(getdriver)

    # wait for few second to load the javascript in browser
    time.sleep(3)

    # fill the credentials then logged in
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()


    time.sleep(2)

    # get back to the home page
    driver.get("https://www.instagram.com/")
    time.sleep(1)

    # If Notification box get display then close it by turn on the notification
    if driver.find_element_by_xpath("//div[@role='presentation']") and driver.find_element_by_xpath("//button[contains(text(), 'Turn On')]"):
        driver.find_element_by_xpath("//button[contains(text(), 'Turn On')]").click()

    time.sleep(10)
    # Close the browser
    driver.close()


# if __name__ == "__main__":
#     # credentials
#     instagram_login("your_username", "your_password")