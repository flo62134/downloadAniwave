import time

import selenium.webdriver.common.by
from selenium import webdriver


def print_hi():
    # List of URLs to browse
    urls = [
        "https://www.mp4upload.com/8khif8lgoq7o",
        "https://www.mp4upload.com/rh3uyyobjq3x",
        "https://www.mp4upload.com/sje6tfcpmkvo",
        "https://www.mp4upload.com/fb5xsbvmduzf",
    ]

    # Initialize the web driver (in this example, we'll use Chrome)
    options = webdriver.ChromeOptions()
    options.add_extension('./extension_1_52_0_0.crx')
    driver = webdriver.Chrome(options=options)

    # Loop through the URLs
    for url in urls:
        # Browse the URL
        driver.get(url)
        driver.refresh()
        time.sleep(2)

        # Click on the button with attribute name="method_free"
        method_free_button = driver.find_element(selenium.webdriver.common.by.By.NAME, "method_free")
        method_free_button.click()

        # Wait for 40 seconds
        time.sleep(32)

        # Click on the button with attribute id="downloadbtn"
        download_button = driver.find_element(selenium.webdriver.common.by.By.ID, "downloadbtn")
        driver.execute_script("arguments[0].click();", download_button)

        # Wait for 1 minute
        time.sleep(60)

    # Close the web driver
    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
