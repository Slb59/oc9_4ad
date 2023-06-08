from selenium import webdriver
from selenium.webdriver.edge.options import Options


from selenium.webdriver.common.by import By
import time


def test_mysite_is_online(live_server):
    """ test if the site is online """
    options = Options()
    options.add_argument("headless")

    driver = webdriver.Edge(options=options)

    driver.get(live_server.url)

    assert driver.title != "Not Found"
