from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore
from time import sleep
import os

magenta = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

useragent = UserAgent()

WINDOW_SIZE = "1920,1080"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f"user-agent={useragent.chrome}")
options.add_argument("--window-size=%s" % WINDOW_SIZE)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

os.system("cls")
print(f"""{magenta}
Telegram channel - https://t.me/mctsh\n
Donate (ERC20) - 0xdd8185984AC02E5d9394a278d23271Fb1C9DC54c\n""")

Maillist = open("mails.txt", "r").readlines()
print('Opening a mails file...')

for combo in Maillist:
    seq = combo.strip()
    acc = seq

    Mail = acc

    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
    driver.get("https://www.moonpay.com/web3-passport")
    sleep(0.1)

    usernameInput = driver.find_element(By.CLASS_NAME, 'newsletter_email__RNnZ_')
    usernameInput.send_keys(Mail)
    print('Successfully Pasted An Email, now clicking on cookie...')
    sleep(0.1)
    CookieClick = driver.find_element(By.ID , 'onetrust-accept-btn-handler')
    CookieClick.click()
    print('Successfully Clicked on Cookie, now clicking on CheckBox...')
    sleep(0.1)
    CheckBoxClick = driver.find_element(By.CLASS_NAME, 'newsletter_checkbox__p2LO8')
    CheckBoxClick.click()
    print('Successfully Clicked on CheckBox, sending a request...')
    sleep(0.1)
    lBtn = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div/section[1]/div/div[1]/form/div[1]/button")
    lBtn.click()
    print('Successfully Sent a Request, now checking if everything works fine...')
    sleep(0.1)
    try:
        driver.find_element(By.CLASS_NAME, "newsletter_newsletterSubmitted__TYyPD hero_newsletter__q_4M6")
        sleep(5)
        driver.close()
        print(f"[!] {red}BAD: {combo} {reset}")
    except NoSuchElementException:
        print(f"[!] {green}GOOD: {combo} {reset}")
        driver.close()

    input('Proccess is finished, Press ENTER to exit')
