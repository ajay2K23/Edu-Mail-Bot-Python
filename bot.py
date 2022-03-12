import time
import re
import string
import random
import sys
import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint
from colorama import init, Fore, Style
init(autoreset=True)

# =========================================
fc = Fore.CYAN
fg = Fore.GREEN
fw = Fore.WHITE
fr = Fore.RED
fb = Fore.BLUE
fy = Fore.YELLOW
fm = Fore.MAGENTA
sn = Style.NORMAL
sb = Style.BRIGHT

# =========================================

def banner():
    banner = '''
                        ______________  _______________ 
                       / ____/_  __/ / / /  _/ ____/   |
                      / __/   / / / /_/ // // /   / /| |
                     / /___  / / / __  // // /___/ ___ |
                    /_____/ /_/ /_/ /_/___/\____/_/  |_|\n

                         Telegram - |  @criminalbhai  \n\n\n'''

    colored_chars = [ sb + fy + char for char in banner]

    return ''.join(colored_chars)

# =========================================

country_codes = ['855', '561', '800', '325', '330', '229']
ssn_head = ['479','429','513','612','330','229','336','459','354','218','618','422','522','622']
fake = Faker('en_US')
ex = fake.name().split(' ')
firstName = ex[0]
LastName = ex[1]
studentAddress = fake.address()

def postFix(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_phone_num_generator():
    first = str(random.choice(country_codes))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

def random_ssn_generator():
    first = str(random.choice(ssn_head))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

# =========================================

def start_bot(start_url, email):
    studentPhone = random_phone_num_generator()
    ssn = random_ssn_generator()

    ex_split = studentAddress.split("\n")

    streetAddress = ex_split[0]

    if(re.compile(',').search(ex_split[1]) != None):
        ex_split1 = ex_split[1].split(', ')
        cityAddress = ex_split1[0]
        ex_split2 = ex_split1[1].split(' ')
        stateAddress = ex_split2[0]
        postalCode = ex_split2[1]
    else:
        ex_split3 = ex_split[1].split(' ')
        cityAddress = ex_split3[0]
        stateAddress = ex_split3[1]
        postalCode = ex_split3[2]

    random.seed()

    driver = webdriver.Firefox(executable_path=r'geckodriver')
    driver.maximize_window()
    driver.get(start_url)
    time.sleep(1)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "firstname"))
    ).send_keys(firstName)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "lastname"))
    ).send_keys(LastName)

    time.sleep(0.7)

    dobs = ['08011998', '08011999', '08011997', '08011996', '08011995', '08011994', '08011993', '08011992', '08011991', '08011990']
    dob = random.choice(dobs)
    
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "dob"))
    ).send_keys(dob)
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ssn"))
    ).send_keys(ssn)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "phone"))
    ).send_keys(studentPhone)
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "email"))
    ).send_keys(email)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "street_addr"))
    ).send_keys(streetAddress)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "zip"))
    ).send_keys(postalCode)
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "city"))
    ).send_keys(cityAddress)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "state"))
    ).send_keys(stateAddress)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnlVisa_1"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlbSemester option[value="2021FA"]'))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnlAcadGoals_0"))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnlReasons_3"))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "SELECT FROM LIST"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME, "ctl00$ContentPlaceHolder1$gridDegreeList$ctl04$btnSubmit"))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnSingleParent_1"))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnDisplacedHomemaker_2"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnFosterCare_1"))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnHomeless_1"))
    ).click()

    time.sleep(0.7)
    
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnlGender_1"))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlbLatinoChoice option[value="NHS"]'))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_chbxRacialGroups_5"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlParents option[value="N"]'))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnActiveDutyParent_1"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlbGraduatedHS option[value="N"]'))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnSummerOnly_1"))
    ).click()
    
    time.sleep(1)
    
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_rbtnPartnershipProgramAp_1"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_rbtnExpectGradHS_0"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rbtnlHSArea_1"))
    ).click()
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlbHighestDegree option[value="N"]'))
    ).click()
    
    time.sleep(0.7)    

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlbPrimaryLanguage option[value="EN"]'))
    ).click()
    
    time.sleep(0.7)   

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_chbxDeclineEmer"))
    ).click()

    time.sleep(0.7)


    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "tbxCertification"))
    ).send_keys(firstName)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Terms and Conditions and Privacy Policy"))
    ).click()

    time.sleep(0.7)    

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "chbxDisclaimer"))
    ).click()

    time.sleep(3)
#================================================
    
    print(sb + fg + '\n   Saving Information')
    fp = open('ElginData.txt', 'a')
    fp.write('====================================================================================')
    fp.write('\nEmail - ' + email + ' | First Name - ' + firstName + ' | Last Name - ' + LastName + ' |\nDob - ' + dob + ' | SSN - ' + ssn +'\n')
    fp.write('====================================================================================')
    fp.close()
#================================================
    time.sleep(3)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "btnSubmit"))
    ).click()
    print(sb+fg+"   Application Submited Successfully !  ")
    time.sleep(2)
    driver.close()

# =========================================

def main():
    sys.stdout.write(banner())
    print(fy + sb + '\n   Title |  ' + sb+fg+'Elgin College Edu Bot\n')

    print(fc + sb + '   Enter Your Email | ', end='')
    userEmail = input()

    time.sleep(0.4)

    print('\n' + fm + sb + '   Keep checking this terminal for information')

    time.sleep(1)
    reg_url = "https://apps.elgin.edu/ApplyOnline/ApplyOnlineForm.aspx"
    
    start_bot(reg_url, userEmail)

# =========================================

if __name__ == '__main__':
    main()
