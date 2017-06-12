from base64 import b64encode

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

time.sleep(5)

proxy_host = "tnthm5gnofn.SANDBOX.verygoodproxy.io"
proxy_port = 8080
proxy_username = "USoPJ3oKKffD17FjC7FTBN5m"
proxy_password = "611898ed-1995-4d52-aa8b-bc439f616a7e"
SELENIUM_HUB_URL = "http://selenium-hub:4444/wd/hub"

capabilities = webdriver.DesiredCapabilities.FIREFOX
# capabilities['marionette'] = False

firefox_profile = webdriver.FirefoxProfile()

firefox_profile.add_extension('closeproxy.xpi')
firefox_profile.set_preference('network.proxy.type', 1)
firefox_profile.set_preference('network.proxy.http', proxy_host)
firefox_profile.set_preference('network.proxy.http_port', proxy_port)
firefox_profile.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')

proxy_credentials = '{}:{}'.format(proxy_username, proxy_password)
proxy_credentials = b64encode(proxy_credentials.encode('ascii')).decode('utf-8')
firefox_profile.set_preference('extensions.closeproxyauth.authtoken', proxy_credentials)

driver = webdriver.Remote(browser_profile=firefox_profile,
                          command_executor=SELENIUM_HUB_URL,
                          desired_capabilities=capabilities)

# driver = webdriver.Firefox(firefox_profile=firefox_profile,
#                            # capabilities=capabilities
#                            )

driver.get('http://ifconfig.me/ip')

ip_address = driver.find_element(By.XPATH, '//html/body/pre').text

print "*\n*\n*\n*\n* IP Address: %s\n*\n*\n*\n*" % ip_address
