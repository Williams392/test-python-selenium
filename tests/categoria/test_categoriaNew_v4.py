# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCategorianewv4():

  def setup_method(self, method):
    self.driver = webdriver.Chrome()  # Initialize the driver here
  
  def teardown_method(self, method):
    self.driver.quit()

  @pytest.fixture(scope="class")
  def driver(self):
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
  
  # def test_categorianewv4(self):
  #   self.driver.get("http://localhost:4200/login")
  #   self.driver.set_window_size(1128, 1142)
  #   time.sleep(1)
  #   self.driver.find_element(By.CSS_SELECTOR, ".sm\\3Ainline").click()
  #   self.driver.find_element(By.ID, "email").click()
  #   self.driver.find_element(By.ID, "email").send_keys("williams@gmail.com")
  #   self.driver.find_element(By.ID, "password").click()
  #   self.driver.find_element(By.ID, "password").send_keys("admin123456")
  #   self.driver.find_element(By.CSS_SELECTOR, ".bg-indigo-600").click()
  #   element = self.driver.find_element(By.CSS_SELECTOR, ".bg-indigo-600")
  #   actions = ActionChains(self.driver)
  #   actions.move_to_element(element).perform()
  #   self.driver.find_element(By.ID, "titulo").click()
  #   self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) .flex-1").click()
  #   self.driver.find_element(By.ID, "title_categoria").click()
  #   self.driver.find_element(By.ID, "button_categoria").click()
  #   self.driver.find_element(By.ID, "nombreCategoria").click()
  #   time.sleep(1)
  #   self.driver.find_element(By.ID, "nombreCategoria").send_keys("COMPUTADORAS")
  #   self.driver.find_element(By.ID, "descripcionCategoria").click()
  #   time.sleep(1)
  #   self.driver.find_element(By.ID, "descripcionCategoria").send_keys("computadora de escritorio")
  #   self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3)").click()
  #   time.sleep(1)
  #   self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
  #   self.driver.find_element(By.CSS_SELECTOR, ".text-gray-400").click()
  
