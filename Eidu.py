   
from addons.android_key_events import AndroidKeyEvents
from addons.mobile_extensions import MobileExtensions
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


@pytest.fixture()
def driver():
    capabilities = {
        "platformName": "Android",
        "udid": "QTC4C19927000131",
        "appPackage": "com.dukatech.digiduka",
        "appActivity": "com.dukatech.digiduka.ui.views.ui.dashboard.DashboardActivity",
    }
    driver = webdriver.Remote(token="c5HvBiBf7jQNX_3S_qLypPeolYqz6t_uB6phQ8kiDYU1",
                              project_name="RejaReja",
                              job_name="Send_Money",
                              desired_capabilities=capabilities)
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # 1. Launch app
    driver.launch_app()

    # 2. Click 'Login'
    login = driver.find_element(By.ID,
                                "com.dukatech.digiduka.onboarding:id/buttonLogin")
    login.click()

    # 3. Click '0712345678'
    _0712345678 = driver.find_element(By.ID,
                                      "com.dukatech.digiduka.onboarding:id/editTextPhone")
    _0712345678.click()

    # 4. Type '720599572' in '0712345678'
    _0712345678 = driver.find_element(By.ID,
                                      "com.dukatech.digiduka.onboarding:id/editTextPhone")
    _0712345678.send_keys("720599572")

    # 5. Type '1958' in 'com.dukatech.digiduka.onboarding:id/l...'
    com_dukatech_digiduka_onboarding_colon_id_slash_l_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.onboarding:id/loginPinView")
    com_dukatech_digiduka_onboarding_colon_id_slash_l_.send_keys("1958")

    # 6. Click 'Login1'
    login1 = driver.find_element(By.ID,
                                 "com.dukatech.digiduka.onboarding:id/buttonComplete")
    login1.click()

    # 7. Click 'com.dukatech.digiduka.home:id/sendIma...'
    com_dukatech_digiduka_home_colon_id_slash_sendima_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.home:id/sendImageView")
    com_dukatech_digiduka_home_colon_id_slash_sendima_.click()

    # 8. Click '07123456781'
    _07123456781 = driver.find_element(By.ID,
                                       "com.dukatech.digiduka.home:id/editTextPhone")
    _07123456781.click()

    # 9. Type '725976369' in '07123456781'
    _07123456781 = driver.find_element(By.ID,
                                       "com.dukatech.digiduka.home:id/editTextPhone")
    _07123456781.send_keys("725976369")

    # 10. Click 'KES. 0.00'
    kes_0_00 = driver.find_element(By.ID,
                                   "com.dukatech.digiduka.home:id/editTextAmount")
    kes_0_00.click()

    # 11. Type '50' in 'KES. 0.00'
    kes_0_00 = driver.find_element(By.ID,
                                   "com.dukatech.digiduka.home:id/editTextAmount")
    kes_0_00.send_keys("50")

    # 12. Hide keyboard
    driver.addons().execute(
        MobileExtensions.hidekeyboardandroid(
        ))

    # 13. Click 'Continue'
    _continue = driver.find_element(By.ID,
                                    "com.dukatech.digiduka:id/buttonContinue")
    _continue.click()

    # 14. Click 'com.dukatech.digiduka.home:id/sendPin...'
    com_dukatech_digiduka_home_colon_id_slash_sendpin_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.home:id/sendPinView")
    com_dukatech_digiduka_home_colon_id_slash_sendpin_.click()

    # 15. Type '1958' in 'com.dukatech.digiduka.home:id/sendPin...'
    com_dukatech_digiduka_home_colon_id_slash_sendpin_ = driver.find_element(By.ID,
                                                                             "com.dukatech.digiduka.home:id/sendPinView")
    com_dukatech_digiduka_home_colon_id_slash_sendpin_.send_keys("1958")

    # 16. Click 'Load Wallet'
    load_wallet = driver.find_element(By.ID,
                                      "com.dukatech.digiduka.home:id/sendButton")
    load_wallet.click()

    # 17. Press Enter
    driver.addons().execute(
        AndroidKeyEvents.pressenter(
        ))

    # 18. Click 'Navigate up'
    navigate_up = driver.find_element(By.XPATH,
                                      "//android.widget.ImageButton[@content-desc = 'Navigate up']")
    navigate_up.click()
