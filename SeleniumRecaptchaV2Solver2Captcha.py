from twocaptcha import TwoCaptcha
import undetected_chromedriver as uc
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webdriver import By
from selenium.common.exceptions import WebDriverException

solver = TwoCaptcha('YOURAPIKEY')
data_sitekey = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "g-recaptcha-"))).get_attribute("data-sitekey")
result = solver.recaptcha(sitekey=data_sitekey, url='YOURURL')
capCode = result['code']
driver.execute_script("""document.querySelector('[name="g-recaptcha-response"]').innerText='{}'""".format(capCode))