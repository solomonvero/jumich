from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.Generated.Tests.MyFirstProject
    Test: Jumia2
    Generated by: Solomon W (solomonvero@gmail.com)
    Generated on 01/22/2022, 03:06:35
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="nYfYmVqyv2N8kBH92g1MwwoRcTRzD9ZPdizpkdTqIzQ1",
                              project_name="My first Project",
                              job_name="Jumia2")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://www.jumia.co.ke/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'use'
    use = driver.find_element(By.XPATH,
                              "//section/button//*[name()='use']")
    use.click()

    # 3. Click 'LABEL'
    label = driver.find_element(By.XPATH,
                                "//div[2]/div[1]/label")
    label.click()

    # 4. Click 'SIGN IN'
    sign_in = driver.find_element(By.XPATH,
                                  "//a[. = 'Sign In']")
    sign_in.click()

    # 5. Click 'E-mail'
    e_mail = driver.find_element(By.XPATH,
                                 "//div[1]/form//label[. = 'E-mail']")
    e_mail.click()

    # 6. Type 'solomonvero@gmail.com' in 'email'
    email = driver.find_element(By.CSS_SELECTOR,
                                "#fi-email")
    email.send_keys("solomonvero@gmail.com")

    # 7. Type '1100solo' in 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#fi-password")
    password.send_keys("1100solo")

    # 8. Click 'LOGIN'
    login = driver.find_element(By.XPATH,
                                "//span[. = 'Login']")
    login.click()

    # 9. Scroll window by ('0','400')
    driver.execute_script("window.scrollBy(0,400)")

    # 10. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 11. Click 'IMG'
    img = driver.find_element(By.XPATH,
                              "//div[3]/article//img")
    img.click()

    # 12. Click 'ADD TO CART'
    add_to_cart = driver.find_element(By.XPATH,
                                      "//div/form//span[. = 'Add to cart']")
    add_to_cart.click()

    # 13. Click 'Cart'
    cart = driver.find_element(By.XPATH,
                               "//a[. = 'Cart']")
    cart.click()

    # 14. Click 'IMG1'
    img1 = driver.find_element(By.XPATH,
                               "//header//img")
    img1.click()

    # 15. Click 'LABEL1'
    label1 = driver.find_element(By.XPATH,
                                 "//div[2]/div[1]/label")
    label1.click()

    # 16. Click 'LOGOUT'
    logout = driver.find_element(By.XPATH,
                                 "//button[. = 'Logout']")
    logout.click()
