import requests
from bs4 import BeautifulSoup
import json
from docutils.nodes import label
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from selenium import *
import time
import datetime
from PIL import ImageTk, Image
import os
import tkinter as tk
from PIL import ImageTk, Image
import os


options = Options()
#options.add_argument("--headless")
options.binary_location ='C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe'
brawser = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\wetru\PycharmProjects\freebitco.io(bot)\chromedriver90.exe")
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})


#https://api.blockcypher.com/v1/btc/main/addrs/38DGj87axzmQiZeAd1w1y5FEmuu5a7pfBa
#https://www.blockchain.com/btc/address/38DGj87axzmQiZeAd1w1y5FEmuu5a7pfBa

try:
    def kriptaos():  # btc+проверка 100% работает
        url_ballans = "https://bitinfocharts.com/dogecoin/address/"
        url = "https://walletgenerator.net/?currency=Bitcoin#"
        click = '/html/body/div[2]/div[6]/div[1]/div[1]/div[2]/div[2]/a'
        brawser.get(url)
        brawser.find_element_by_xpath(click).click()
        for iu in range(2500):
            te1s = brawser.find_element_by_id("btcaddress").text
            tea = brawser.find_element_by_id("btcprivwif").text
            string1 = te1s + "::" + tea
            write = open('\\BTCrwallet1.txt', "a")
            write.writelines(string1 + "\n")
            time.sleep(2)
            submit = brawser.find_element_by_id('newaddress').click()
            getbalanceurl = str('https://chain.so/api/v2/get_address_balance/BTC/' + str(te1s))
            balance = requests.get(getbalanceurl)
            jsonresponse = json.loads(balance.text)
            json.JSONDecoder(object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True,
                             object_pairs_hook=None)
            df = jsonresponse['data']['address'] + ':balance:' + jsonresponse['data']['confirmed_balance']
            print(df + "\n")
            write = open('\\BTCballioanses.txt', "a")
            write.writelines(df + "\n")

    kriptaos()
except Exception as e:
    print(e)