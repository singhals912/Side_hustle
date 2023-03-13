"""
A sample Hello World server.
"""
import os
import schedule
import time
import requests
import re
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template
import datetime
# pylint: disable=C0103
app = Flask(__name__)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

def send_email():
    # browser = webdriver.Chrome('chromedriver.exe')
    browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/252/420")
    date=browser.find_element(By.XPATH,"//div[@class='col-sm-6 text-center col-md-8 col-lg-8']//label[@class='control-label']")
    newark=date.text.split("for")[1].strip().split(":")[0]
    newark = datetime.datetime.strptime(newark, '%B %d, %Y').date()

    browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/252/417")
    date=browser.find_element(By.XPATH,"//div[@class='col-sm-6 text-center col-md-8 col-lg-8']//label[@class='control-label']")
    lodi=date.text.split("for")[1].strip().split(":")[0]
    lodi = datetime.datetime.strptime(lodi, '%B %d, %Y').date()

    browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/252/424")
    date=browser.find_element(By.XPATH,"//div[@class='col-sm-6 text-center col-md-8 col-lg-8']//label[@class='control-label']")
    wayne=date.text.split("for")[1].strip().split(":")[0]
    wayne = datetime.datetime.strptime(wayne, '%B %d, %Y').date()

    if (newark < datetime.date(2023,6,30))  & (newark > datetime.date(2023,3,20)):
        browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/252/420")
        continue_button = browser.find_element(By.XPATH, value="//div[@id='timeslots']//a[@href][1]")
        continue_button.click()
        first_name = browser.find_element(By.ID, "firstName")
        last_name = browser.find_element(By.ID, "lastName")
        email =  browser.find_element(By.ID, "email")
        phone =  browser.find_element(By.ID, "phone")
        permitclass =  browser.find_element(By.ID, "permitClass")
        driverlicense = browser.find_element(By.ID, "driverLicense")
        validationnum = browser.find_element(By.ID, "validationNum")
        first_name.send_keys("Sachin")
        last_name.send_keys("Singhal")
        email.send_keys("SS@gmail.com")
        phone.send_keys("XXX-XX-XXXX")
        permitclass.send_keys("D")
        driverlicense.send_keys("ABCDEFG")
        validationnum.send_keys("ABCDS")
        terms = browser.find_element(By.XPATH, value="//input[@data-val-required='The Attest field is required.']")
        terms.click()
        terms1 = browser.find_element(By.XPATH, value="//input[@data-val-required='The PtaAttest field is required.']")
        terms1.click()
        continue_button = browser.find_element(By.XPATH, value="//input[@type='submit']")
        continue_button.click()
    
    elif (lodi < datetime.date(2023,3,31)) & (lodi > datetime.date(2023,3,20)):
        browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/252/417")
        continue_button = browser.find_element(By.XPATH, value="//div[@id='timeslots']//a[@href][1]")
        continue_button.click()
        first_name = browser.find_element(By.ID, "firstName")
        last_name = browser.find_element(By.ID, "lastName")
        email =  browser.find_element(By.ID, "email")
        phone =  browser.find_element(By.ID, "phone")
        permitclass =  browser.find_element(By.ID, "permitClass")
        driverlicense = browser.find_element(By.ID, "driverLicense")
        validationnum = browser.find_element(By.ID, "validationNum")
        first_name.send_keys("Sachin")
        last_name.send_keys("Singhal")
        email.send_keys("SS@gmail.com")
        phone.send_keys("XXX-XX-XXXX")
        permitclass.send_keys("D")
        driverlicense.send_keys("ABCDEFG")
        validationnum.send_keys("ABCDS")
        terms = browser.find_element(By.XPATH, value="//input[@data-val-required='The Attest field is required.']")
        terms.click()
        terms1 = browser.find_element(By.XPATH, value="//input[@data-val-required='The PtaAttest field is required.']")
        terms1.click()
        continue_button = browser.find_element(By.XPATH, value="//input[@type='submit']")
        continue_button.click() 

    elif (wayne < datetime.date(2023,3,31)) &  (wayne > datetime.date(2023,3,20)):
        browser.get("https://telegov.njportal.com/njmvc/AppointmentWizard/252/424")
        continue_button = browser.find_element(By.XPATH, value="//div[@id='timeslots']//a[@href][1]")
        continue_button.click()
        first_name = browser.find_element(By.ID, "firstName")
        last_name = browser.find_element(By.ID, "lastName")
        email =  browser.find_element(By.ID, "email")
        phone =  browser.find_element(By.ID, "phone")
        permitclass =  browser.find_element(By.ID, "permitClass")
        driverlicense = browser.find_element(By.ID, "driverLicense")
        validationnum = browser.find_element(By.ID, "validationNum")
        first_name.send_keys("Sachin")
        last_name.send_keys("Singhal")
        email.send_keys("SS@gmail.com")
        phone.send_keys("XXX-XX-XXXX")
        permitclass.send_keys("D")
        driverlicense.send_keys("ABCDEFG")
        validationnum.send_keys("ABCDS")
        terms = browser.find_element(By.XPATH, value="//input[@data-val-required='The Attest field is required.']")
        terms.click()
        terms1 = browser.find_element(By.XPATH, value="//input[@data-val-required='The PtaAttest field is required.']")
        terms1.click()
        continue_button = browser.find_element(By.XPATH, value="//input[@type='submit']")
        continue_button.click()
         
    if (newark < datetime.date(2023,3,31)) or (lodi < datetime.date(2023,3,31)) or (wayne < datetime.date(2023,3,31)):
        sender = "singhals912@gmail.com"
        recipient = "singhals912@gmail.com"
        subject = "Road test appointments by location"
        body = f"""Newark: {newark} \n For Lodi: {lodi} \n For Wayne: {wayne} \n"""
        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        # Connect to the SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login('singhals912@gmail.com', 'password')
        # Send the email
        smtp_server.sendmail(sender, recipient, msg.as_string())
        smtp_server.quit()
    return 'hello'

send_email()
