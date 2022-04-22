# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MyLib.py
from logging import NullHandler
import string
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import urllib3, requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support as EC
import time, os, io, csv, pathlib
from urllib.parse import urlparse
import win32com
import MySQLdb as mysql
from selenium.webdriver.chrome.options import Options
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import win32com.client as win32
import selenium.webdriver.chrome.service as service
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.chrome import service
import win32com.client as win32
import requests, threading, time, sqlite3, win32api, pyinstaller_versionfile, uuid, random
from datetime import datetime
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import pandas as pd
from fuzzywuzzy import fuzz, process


class AESCipher:
    __doc__ = "\n    Usage:\n        c = AESCipher('password').encrypt('message')\n        m = AESCipher('password').decrypt(c)\n    Tested under Python 3 and PyCrypto 2.6.1.\n    "

    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()
        BLOCK_SIZE = 16
        self.pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encrypt(self, raw):
        raw = self.pad(raw)
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw.encode('utf8')))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_ECB)
        return self.unpad(cipher.decrypt(enc)).decode('utf8')


def sqlescape(str):
    # print('Step 1')
    _ = str.encode('utf-8')
    # print('Step 2')
    # _ = mysql.escape_string(_)
    # print('Step 3')
    _ = _.decode('utf-8')
    # print(_)
    return '{}'.format(_)


def rcurr(str):
    class _:
        pass

    _.X = str
    [setattr(_, 'X', _.X.replace(i, '').strip()) for i in ('جنية', 'LE', 'EGP', 'جنيه')]
    return _.X


def Jumia(driver, hostname, TableWidget=QTableWidget, data=string, parent=None):
    Old_Data = FN_Old_Data(parent)
    _ = Page_loaded(driver)
    _.Wait()
    if driver.find_element_by_xpath("//span[@class='-dif -i-ctr -fs12']").text == 'English':
        try:
            driver.find_element_by_xpath("//button[@aria-label='newsletter_popup_close-cta']").click()
        except:
            pass
        # time.sleep(0.3)
        _.Wait()
        element_to_hover_over = driver.find_element_by_xpath("//span[@class='-dif -i-ctr -fs12']")
        ActionChains(driver).move_to_element(element_to_hover_over).perform()
        # time.sleep(0.3)
        _.Wait()
        driver.find_element_by_xpath("//span[@class='-dif -i-ctr -fs12']").click()

    Names = []
    href = []
    ID = []
    Discount = []
    Price = []
    SKUs = []

    while True:
        _.Wait()
        with Obj(driver.execute_script(
                '\n                 if (document.querySelectorAll("[class=\'core\']").length>0) { \n                 return 1;\n                 }  else {\n                 return 0; \n                 }  \n             ')) as (
        f):
            if f == 0:
                break
            else:
                if f == 1:
                    product_row = driver.execute_script('return document.querySelectorAll("[class=\'core\']").length')
                    for x in range(0, product_row, 1):
                        product_href = driver.execute_script(
                            'return document.querySelectorAll("[class=\'core\']")[' + str(x) + '].href')
                        product_id = 'JU:' + driver.execute_script(
                            'return document.querySelectorAll("[class=\'core\']")[' + str(
                                x) + "].getAttribute('data-id')")
                        product_name = driver.execute_script(
                            'return document.querySelectorAll("[class=\'core\']")[' + str(
                                x) + "].querySelector('.name').textContent")
                        product_discount_price = driver.execute_script(
                            'return document.querySelectorAll("[class=\'core\']")[' + str(
                                x) + "].querySelector('.prc').textContent")
                        product_original_price = driver.execute_script(
                            'var x=document.querySelectorAll("[class=\'core\']")[' + str(
                                x) + "].querySelectorAll('.old');if (x.length==1) {return x[0].textContent;} else {return '';}")
                        if product_original_price == '':
                            product_original_price = product_discount_price
                            product_discount_price = ''
                        product_discount_price = rcurr(product_discount_price)
                        product_original_price = rcurr(product_original_price)
                        Names.append(product_name)
                        ID.append(product_id)
                        Price.append(product_original_price)
                        Discount.append(product_discount_price)
                        href.append(product_href)
                        parent.cur.execute(
                            "SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
                        SKU = parent.cur.fetchall()
                        SKU = '' if len(SKU) == 0 else SKU[0][0]
                        SKUs.append(SKU)
                        # parent.cur.execute(
                        #     "SELECT BAR FROM data, data1 WHERE data1.DESC = data.`Product Name` and `Product Id` = '{}';".format(
                        #         sqlescape(product_id)))
                        # Desc, Match_SKU = Matching(parent, product_original_price, product_discount_price,
                        #                      product_name, Old_Data)
                        # parent.cur.execute(
                        #     "SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
                        # SKU = parent.cur.fetchall()
                        # SKU = '' if len(SKU) == 0 else SKU[0][0]
                        # SKU = Match_SKU
                        # SKU, Desc = '', ''
                        Desc = ''
                        cell = TableWidget.rowCount()
                        TableWidget.setRowCount(cell + 1)
                        [TableWidget.setItem(cell, x, QTableWidgetItem(str(y).strip())) for x, y in enumerate(
                            [hostname, data, SKU, Desc, product_name, '', '', product_original_price,
                             product_discount_price, product_href, product_id])]
                        # parent.cur.execute('REPLACE data (`Product Name`,SKU, Link , `Product Original Price`,`Product Discount Price`,`Date Update`,`Product Id`) VALUES ("{}","{}","{}","{}","{}","{}","{}");'.format(sqlescape(product_name.replace('"', '').strip()), SKU, product_href, product_original_price, product_discount_price, datetime.today(), product_id))
                        # parent.con.commit()

                    if not driver.execute_script(
                            '\n               with (document) {        \n                nPage_0=querySelectorAll("[aria-label=\'الصفحة التالية\']");\n                nPage_1=querySelectorAll("[aria-label=\'Next Page\']");\n                 \n                if (nPage_1.length==1) {\n                if (nPage_1[0].getAttribute("href") !=null) {\n                  nPage_1[0].click()\n                  ;return 1;\n                  } else {return 0;}\n \n \n \n                } else if (nPage_0.length==1) {\n                if (nPage_0[0].getAttribute("href") !=null) {\n                  nPage_0[0].click()\n                  ;return 1;\n                  } else {return 0;}\n \n \n                } else {return 0;}}\n                '):
                        break

    Scraped_Date = [Names, Price, Discount, href, ID, SKUs]

    return Scraped_Date, Old_Data


def BTECH(driver, hostname, TableWidget=QTableWidget, data=string, parent=None):
    Old_Data = FN_Old_Data(parent)
    _ = Page_loaded(driver)
    _.Wait()
    # if driver.find_element_by_xpath("//li[@class='view-en switcher-option']").text == 'English':
    try:
        driver.find_element_by_xpath("//li[@class='view-en switcher-option']").click()
    except:
        pass
    while 1:
        _.Wait()
        if not driver.execute_script(
                '\n              function findPos(obj) {var curtop = 0;if (obj.offsetParent) {do {curtop += obj.offsetTop;} while (obj = obj.offsetParent);return [curtop];}}\n              x = document.querySelectorAll("[amscroll_type=\'after\']");\n              if(x.length==1) {window.scroll(0,findPos(x[0]));x[0].click();return true;} else {return false;}\n              '):
            break

    Names = []
    href = []
    ID = []
    Discount = []
    Price = []
    SKUs = []

    product_count = driver.execute_script(
        'window.product=document.querySelectorAll("[class=\'plpContentWrapper\']");\n  return window.product.length;\n    ')
    for x in range(0, product_count, 1):
        product_href = driver.execute_script(
            'return product[{}].closest(".product-item-view").querySelector("[class=\'listingWrapperSection\']").href;'.format(
                x))
        product_id = 'BT:' + driver.execute_script(
            'return product[{}].closest(".product-item-view").querySelector("[class=\'price-box price-final_price\']").getAttribute(\'data-product-id\');'.format(
                x))
        product_name = driver.execute_script(
            'return product[{}].closest(".product-item-view").querySelector("[class=\'plpTitle\']").textContent;'.format(
                x))
        p = driver.execute_script(
            'var n=product[{}].closest(".product-item-view").querySelector("[data-price-type=\'finalPrice\']");\n          if  (n) {{return n.textContent;}}\n          '.format(
                x))
        d = driver.execute_script(
            'var n=product[{}].closest(".product-item-view").querySelector("[data-price-type=\'oldPrice\']");\n          if  (n) {{return n.textContent;}}\n          '.format(
                x))
        if p == None:
            p = ''
        if d == None:
            d = ''
            d = p
            p = ''
        d = rcurr(d)
        p = rcurr(p)
        Names.append(product_name)
        ID.append(product_id)
        Price.append(p)
        Discount.append(d)
        href.append(product_href)
        parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
        SKU = parent.cur.fetchall()
        SKU = '' if len(SKU) == 0 else SKU[0][0]
        SKUs.append(SKU)
        # parent.cur.execute(
        #     "SELECT BAR FROM data, data1 WHERE data1.DESC = data.`Product Name` and `Product Id` = '{}';".format(
        #         sqlescape(product_id)))
        # Desc, Match_SKU = Matching(parent, p, d, product_name, Old_Data)
        # parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
        # SKU = parent.cur.fetchall()
        # SKU = '' if len(SKU) == 0 else SKU[0][0]
        # SKU = Match_SKU
        # SKU, Desc = '', ''
        Desc = ''
        cell = TableWidget.rowCount()
        TableWidget.setRowCount(cell + 1)
        [TableWidget.setItem(cell, x, QTableWidgetItem(str(y).strip())) for x, y in
         enumerate([hostname, data, SKU, Desc, product_name, '', '', d, p, product_href, product_id])]
        # parent.cur.execute("REPLACE data (`Product Name`,SKU, Link , `Product Original Price`,`Product Discount Price`,`Date Update`,`Product Id`) VALUES ('{}','{}','{}','{}','{}','{}','{}');".format(sqlescape(product_name.replace('"', '').strip()), SKU, product_href, d, p, datetime.today(), product_id))
        # parent.con.commit()

    Scraped_Date = [Names, Price, Discount, href, ID, SKUs]

    return Scraped_Date, Old_Data


def Cairosales(driver, hostname, TableWidget=QTableWidget, data=string, parent=None):
    Old_Data = FN_Old_Data(parent)
    _ = Page_loaded(driver)
    # print('Cairo')
    _.Wait(0.01, 3)
    if driver.find_element_by_xpath("//div[@class='languages-block show_mobile active']").text != 'عربى':
        driver.find_element_by_xpath("//div[@class='languages-block show_mobile active']").click()

    Names = []
    href = []
    ID = []
    Discount = []
    Price = []
    SKUs = []

    while 1:
        _.Wait(0.01, 3)
        # time.sleep(5)
        # print('Cairo')
        if not driver.execute_script(
                '\n                 with (document) {\n                 function findPos(obj) {var curtop = 0;if (obj.offsetParent) {do {curtop += obj.offsetTop;} while (obj = obj.offsetParent);return [curtop];}}\n                 items=querySelectorAll(\'.product-container\')\n                 nlast_item=items.length-1;\n                 window.scroll(0,findPos(items[nlast_item]));\n                 if (querySelectorAll("[class=\'loadMore next button lnk_view btn btn-default\']").length==1) {return 1;} else {return 0;}\n                 }\n                 '):
            break

    driver.execute_script("window.prc=document.querySelectorAll('.product-container')")
    product_count = driver.execute_script('return window.prc.length')
    # print(product_count)
    for x in range(0, product_count, 1):
        # print('Step: ', x)
        product_href = driver.execute_script(
            'return window.prc[' + str(x) + '].querySelector("[class=\'product-name\']").href')
        # print(product_href)
        product_id = 'CS:' + driver.execute_script(
            'return window.prc[' + str(x) + "].parentElement.getAttribute('data-id-product')")
        # print(product_id)
        product_name = driver.execute_script(
            'return window.prc[' + str(x) + '].querySelector("[class=\'product-name\']").textContent')
        # print(product_name)

        product_discount_price = driver.execute_script('x=window.prc[' + str(
            x) + '].querySelector("[class=\'price product-price\']");if(x !== null) {return x.textContent;} else {return \'\'} ;')
        # print(product_discount_price)


        driver.execute_script(f"window.open('{product_href}')")

        window_name = driver.window_handles[-1]

        driver.switch_to.window(window_name=window_name)

        try:
            li = driver.find_elements_by_xpath("//ul[@id = 'combinationswithimages']")[0].text.split('\n')
            li = [li[i + 1].replace('EGP ', '').replace(',', '') for i in range(0, len(li), 2)]
            product_discount_price = min(li)
        except:
            pass

        driver.close()

        driver.switch_to.window(driver.window_handles[0])

        product_original_price = driver.execute_script('x=window.prc[' + str(
            x) + '].querySelector("[class=\'old-price product-price\']");if(x !== null) {return x.textContent;} else {return \'\'} ;')
        # print(product_original_price)
        product_discount_price = rcurr(product_discount_price)
        # print(product_discount_price)
        product_original_price = rcurr(product_original_price)
        # print(product_original_price)
        # parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
        # # print('Done 1')
        # SKU = parent.cur.fetchall()
        # SKU = '' if len(SKU) == 0 else SKU[0][0]
        # parent.cur.execute(
        #     "SELECT BAR FROM data, data1 WHERE data1.DESC = data.`Product Name` and `Product Id` = '{}';".format(
        #         sqlescape(product_id)))
        # Desc, Match_SKU = Matching(parent, product_original_price, product_discount_price, product_name, Old_Data)
        parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
        SKU = parent.cur.fetchall()
        SKU = '' if len(SKU) == 0 else SKU[0][0]
        Names.append(product_name)
        ID.append(product_id)
        Price.append(product_original_price)
        Discount.append(product_discount_price)
        href.append(product_href)
        SKUs.append(SKU)
        # SKU = ''
        Desc = ''
        # print(SKU)
        cell = TableWidget.rowCount()
        TableWidget.setRowCount(cell + 1)
        [TableWidget.setItem(cell, x, QTableWidgetItem(str(y).strip())) for x, y in enumerate(
            [hostname, data, SKU, Desc, product_name, '', '', product_original_price, product_discount_price,
             product_href, product_id])]
        # parent.cur.execute('REPLACE data (`Product Name`,SKU, Link , `Product Original Price`,`Product Discount Price`,`Date Update`,`Product Id`) VALUES ("{}","{}","{}","{}","{}","{}","{}");'.format(sqlescape(product_name.replace('"', '').strip()), SKU, sqlescape(product_href), product_original_price, product_discount_price, datetime.today(), product_id))
        # parent.con.commit()

    Scraped_Date = [Names, Price, Discount, href, ID, SKUs]

    return Scraped_Date, Old_Data


def Amazon(driver, hostname, TableWidget=QTableWidget, data=string, parent=None):
    try:

        print('Amazon Here')

        Old_Data = FN_Old_Data(parent)
        _ = Page_loaded(driver)
        _.Wait()
        try:
            driver.find_element_by_xpath("//span[@class='a-size-medium a-color-link a-text-bold']").click()
        except:
            pass
        # while 1:
        # print('here')
        _.Wait()
        # time.sleep(4)
        # print('here')

        # print(driver.find_element_by_xpath("//div[@class='a-section a-text-center s-pagination-container']").text)

        # try:

        element_to_hover_over = driver.find_element_by_xpath("//span[@class='nav-icon nav-arrow']")
        ActionChains(driver).move_to_element(element_to_hover_over).perform()

        # time.sleep(0.3)
        _.Wait()

        driver.find_element_by_xpath("//*[contains(text(), 'English')]").click()

        # driver.find_element_by_xpath("//a[@href='#switch-lang=en_AE']").click()

        # while True:
        #     try:
        #         if driver.find_element_by_xpath("//i[@class='icp-radio']").text == 'English'
        #             driver.find_element_by_xpath("//i[@class='icp-radio']").click()
        #             break
        #         else:
        #             break
        #     except:
        #         continue

        # _.Wait()
        #
        # # driver.find_element_by_xpath("//span[@class='a-size-medium a-color-link a-text-bold']").click()
        #
        # try:
        #     driver.find_element_by_xpath("//span[@class='a-size-medium a-color-link a-text-bold']").click()
        # except:
        #     pass

        _.Wait()

        Pages = int(
            driver.find_element_by_xpath("//div[@class='a-section a-text-center s-pagination-container']").text.replace(
                'Previous', '').replace('Next', '').split('.')[-1])

        # print(Pages)
        # except:
        #     Pages = int(
        #         driver.find_element_by_xpath(
        #             "//div[@class='a-section a-text-center s-pagination-container']").text.replace(
        #             'السابق', '').replace('التالي', '')[-1])

        # print(Pages)

        Names = []
        href = []
        ID = []
        Discount = []
        Price = []
        SKUs = []

        for i in range(Pages):

            # while True:

            _.Wait()

            product_row = driver.execute_script(
                'window.data_asin=document.querySelectorAll("[data-asin][data-uuid]");\n  return window.data_asin.length;\n    ')

            print('Row:', product_row)

                # print(product_row)

                # print(int(driver.find_elements_by_xpath("//span[@dir = 'auto']")[0].text.split('-')[-1].split('من')[0]))
                # print('\n', int(driver.find_elements_by_xpath("//span[@dir = 'auto']")[0].text.split('-')[0]))

                # try:
                # print('test: ', driver.find_elements_by_xpath("//span[contains(text(), 'results')]")[0].text.split('–')[-1].split(
                #         'of')[0], driver.find_elements_by_xpath("//span[contains(text(), 'results')]")[0].text.split('–')[0])
                # n = 1 + int(
                #     driver.find_elements_by_xpath("//span[contains(text(), 'results')]")[0].text.split('–')[-1].split(
                #         'of')[0]) - int(
                #     driver.find_elements_by_xpath("//span[contains(text(), 'results')]")[0].text.split('–')[0])
                # except:
                #     n = 1 + int(driver.find_elements_by_xpath("//span[@dir = 'auto']")[0].text.split('-')[-1].split('من')[0]) - int(driver.find_elements_by_xpath("//span[@dir = 'auto']")[0].text.split('-')[0])

                # print(n)

                # if product_row == n:
                #     break
                # else:
                #     # time.sleep(1)
                #     _.Wait()
                #     continue

            # product_row = driver.execute_script('window.data_asin=document.querySelectorAll("[data-asin][data-uuid]");\n  return window.data_asin.length;\n    ')
            for x in range(0, product_row, 1):
                product_href = driver.execute_script(
                    'return data_asin[{}].querySelector("a[class~=\'a-link-normal\'][class~=\'a-text-normal\']").href;'.format(
                        x))
                product_id = 'AM:' + driver.execute_script("return data_asin[{}].getAttribute('data-asin');".format(x))
                product_name = driver.execute_script(
                    'return data_asin[{}].querySelector("a[class~=\'a-link-normal\'][class~=\'a-text-normal\']").textContent;'.format(
                        x))
                p = driver.execute_script(
                    'var n=data_asin[{}].querySelector("[class=\'a-price\'] > span.a-offscreen");\n      if  (n) {{return n.textContent;}}\n      '.format(
                        x))
                d = driver.execute_script(
                    'var n=data_asin[{}].querySelector("[class=\'a-price a-text-price\'] > span.a-offscreen");\n      if  (n) {{return n.textContent;}}\n      '.format(
                        x))
                if p == None:
                    p = ''
                if d == None:
                    d = ''
                    d = p
                    p = ''
                d = rcurr(d)
                p = rcurr(p)
                Names.append(product_name)
                ID.append(product_id)
                Price.append(p)
                Discount.append(d)
                href.append(product_href)
                # print(Names, Price, Discount, href, ID)
                # print('Amazon ID : ', product_id)
                # print(sqlescape(product_id))
                parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
                SKU = parent.cur.fetchall()
                # # print('SKU: ', SKU)
                SKU = '' if len(SKU) == 0 else SKU[0][0]
                SKUs.append(SKU)
                # parent.cur.execute(
                #     "SELECT BAR FROM data, data1 WHERE data1.DESC = data.`Product Name` and `Product Id` = '{}';".format(
                #         sqlescape(product_id)))
                # Desc, Match_SKU = Matching(parent, p, d, product_name, Old_Data)
                # parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
                # SKU = parent.cur.fetchall()
                # SKU = '' if len(SKU) == 0 else SKU[0][0]
                # SKU = Match_SKU
                # SKU, Desc = '', ''
                Desc = ''
                cell = TableWidget.rowCount()
                TableWidget.setRowCount(cell + 1)
                [TableWidget.setItem(cell, x, QTableWidgetItem(str(y).strip())) for x, y in
                 enumerate([hostname, data, SKU, Desc, product_name, '', '', d, p, product_href, product_id])]
                # parent.cur.execute("REPLACE data (`Product Name`,SKU, Link , `Product Original Price`,`Product Discount Price`,`Date Update`,`Product Id`) VALUES ('{}','{}','{}','{}','{}','{}','{}');".format(sqlescape(product_name.replace('"', '').strip()), SKU, product_href, d, p, datetime.today(), product_id))
                # parent.con.commit()

            try:
                driver.find_element_by_xpath(
                    "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']").click()
            except:
                break

            # if driver.execute_script('\n  var n=document.querySelector("ul[class=\'a-pagination\'] > li.a-last > a");\n    \n  if  (n) {\n    n.click();\n    return 1;\n  } else {\n    return 2;\n  }\n  ') == 2:
            # if driver.execute_script('\n  var n=document.querySelector("#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div.a-section.a-spacing-none.s-result-item.s-flex-full-width.s-widget > span > div > div > ul > li.a-last > a")\n  if  (n) {\n    n.click();\n    return 1;\n  } else {\n    return 2;\n  }\n  ') == 2:
            #     break

        Scraped_Date = [Names, Price, Discount, href, ID, SKUs]

        print(Scraped_Date, Old_Data)

        return Scraped_Date, Old_Data

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        print(e)
        print('Done')


def Carrefouregypt(driver, hostname, TableWidget=QTableWidget, data=string, parent=None):
    Old_Data = FN_Old_Data(parent)
    _ = Page_loaded(driver)
    _.Wait()
    driver.find_element_by_xpath("//*[@class='css-anesr6']").click()
    _.Wait()
    if driver.find_element_by_xpath("//*[@class='css-1kddnjl']").text == 'English':
        driver.find_element_by_xpath("//*[@class='css-1kddnjl']").click()
    else:
        driver.find_element_by_xpath("//*[@data-testid='close-icon']").click()
    while 1:
        _.Wait()
        y = int(driver.execute_script('return window.scrollY;'))
        h = int(driver.execute_script('return document.body.scrollHeight;'))
        s = int(0.01 * h)
        for i in range(y, h, s):
            time.sleep(0.05)
            driver.execute_script('window.scrollTo(0,' + str(i) + ');')

        if not driver.execute_script(
                '\n               function findPos(obj) {var curtop = 0;if (obj.offsetParent) {do {curtop += obj.offsetTop;} while (obj = obj.offsetParent);return [curtop];}}\n               with (document) {       \n               items=querySelectorAll("[data-testid=\'trolly-button\']")\n               if(items.length>0) {\n               window.scroll(0,findPos(items[0]));\n               items[0].click();\n               return 1;\n               } else {\n                 return 0};\n               }\n              '):
            break

    Names = []
    href = []
    ID = []
    Discount = []
    Price = []
    SKUs = []

    product_row = driver.execute_script("return document.getElementsByClassName('css-5kig18').length")
    for x in range(0, product_row, 1):
        product_cells = driver.execute_script("return document.getElementsByClassName('css-5kig18')[" + str(
            x) + '].childNodes[0].childNodes[0].childNodes.length')
        for y in range(0, product_cells, 1):
            product_href = driver.execute_script("return document.getElementsByClassName('css-5kig18')[" + str(
                x) + '].childNodes[0].childNodes[0].childNodes[' + str(
                y) + '].querySelector("[data-testid=\'product_card_image_container\']").getElementsByTagName(\'a\')[0].href')
            product_id = 'CR:' + product_href[product_href.rfind('/') + 1:]
            product_name = driver.execute_script("return document.getElementsByClassName('css-5kig18')[" + str(
                x) + '].childNodes[0].childNodes[0].childNodes[' + str(
                y) + '].querySelector("[data-testid=\'product_name\']").textContent')
            product_price_length = driver.execute_script("return document.getElementsByClassName('css-5kig18')[" + str(
                x) + '].childNodes[0].childNodes[0].childNodes[' + str(
                y) + '].querySelector("[data-testid=\'product_price\']").childNodes.length')
            try:
                product_card_original_price = driver.execute_script(
                    "return document.getElementsByClassName('css-5kig18')[" + str(
                        x) + '].childNodes[0].childNodes[0].childNodes[' + str(
                        y) + '].querySelector("[data-testid=\'product-card-original-price\']").textContent')
            except:
                product_card_original_price = driver.execute_script(
                    "return document.getElementsByClassName('css-5kig18')[" + str(
                        x) + '].childNodes[0].childNodes[0].childNodes[' + str(
                        y) + '].querySelector("[data-testid=\'product-card-discount-price\']").textContent')
            product_card_discount_price = ''
            if product_price_length == 2:
                product_card_discount_price = driver.execute_script(
                    "return document.getElementsByClassName('css-5kig18')[" + str(
                        x) + '].childNodes[0].childNodes[0].childNodes[' + str(
                        y) + '].querySelector("[data-testid=\'product-card-discount-price\']").textContent')
            product_card_discount_price = rcurr(product_card_discount_price)
            product_card_original_price = rcurr(product_card_original_price)
            Names.append(product_name)
            ID.append(product_id)
            Price.append(product_card_original_price)
            Discount.append(product_card_discount_price)
            href.append(product_href)
            # parent.cur.execute(
            #     "SELECT BAR FROM data, data1 WHERE data1.DESC = data.`Product Name` and `Product Id` = '{}';".format(
            #         sqlescape(product_id)))
            # Desc, Match_SKU = Matching(parent, product_card_original_price, product_card_discount_price, product_name, Old_Data)
            parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
            SKU = parent.cur.fetchall()
            SKU = '' if len(SKU) == 0 else SKU[0][0]
            SKUs.append(SKU)
            # SKU = Match_SKU
            # SKU, Desc = '', ''
            Desc = []
            cell = TableWidget.rowCount()
            TableWidget.setRowCount(cell + 1)
            [TableWidget.setItem(cell, x, QTableWidgetItem(str(y).strip())) for x, y in enumerate(
                [hostname, data, SKU, Desc, product_name, '', '', product_card_original_price,
                 product_card_discount_price, product_href, product_id])]
            # parent.cur.execute("REPLACE data (`Product Name`,SKU, Link , `Product Original Price`,`Product Discount Price`,`Date Update`,`Product Id`) VALUES ('{}','{}','{}','{}','{}','{}','{}');".format(sqlescape(product_name.replace('"', '').strip()), SKU, product_href, product_card_original_price, product_card_discount_price, datetime.today(), product_id))
            # parent.con.commit()

    Scraped_Date = [Names, Price, Discount, href, ID, SKUs]

    return Scraped_Date, Old_Data


def TWO_B(driver, hostname, TableWidget=QTableWidget, data=string, parent=None):
    Old_Data = FN_Old_Data(parent)
    _ = Page_loaded(driver)
    _.Wait()
    if driver.find_element_by_xpath("//*[@class='switcher language switcher-language']").text == 'ENGLISH':
        # print('English')
        element = driver.find_element_by_xpath("//*[@class='switcher language switcher-language']")
        webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

    Names = []
    href = []
    ID = []
    Discount = []
    Price = []
    SKUs = []

    while 1:
        _.Wait()
        driver.execute_script(
            '\n              function findPos(obj) {var curtop = 0;if (obj.offsetParent) {do {curtop += obj.offsetTop;} while (obj = obj.offsetParent);return [curtop];}}\n              window.pro=document.querySelectorAll("[class=\'product details product-item-details\']");\n              B=pro.length-1;\n              window.scroll(0,findPos(pro[B]));\n              \n              ')
        product_row = driver.execute_script('return window.pro.length;')
        for x in range(0, product_row, 1):
            product_href = driver.execute_script(
                'return window.pro[' + str(x) + '].querySelector("[class=\'product-item-link\']").href;')
            product_id = '2B:' + driver.execute_script(
                'return window.pro[{}].querySelector("[class=\'price-box price-final_price\']").getAttribute(\'data-product-id\');'.format(
                    x))
            product_name = driver.execute_script(
                'return window.pro[' + str(x) + '].querySelector("[class=\'product-item-link\']").textContent;')
            product_original_price = driver.execute_script('x =window.pro[' + str(
                x) + '].querySelector("[data-price-type=\'oldPrice\']"); if(x !== null) {return x.textContent;} else {return\'\';}')
            product_discount_price = driver.execute_script(
                'return window.pro[' + str(x) + '].querySelector("[data-price-type=\'finalPrice\']").textContent')
            if not product_original_price:
                product_original_price = product_discount_price
                product_discount_price = ''
            product_discount_price = rcurr(product_discount_price)
            product_original_price = rcurr(product_original_price)
            Names.append(product_name)
            ID.append(product_id)
            Price.append(product_original_price)
            Discount.append(product_discount_price)
            href.append(product_href)
            parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
            SKU = parent.cur.fetchall()
            SKU = '' if len(SKU) == 0 else SKU[0][0]
            SKUs.append(SKU)
            # parent.cur.execute(
            #     "SELECT BAR FROM data, data1 WHERE data1.DESC = data.`Product Name` and `Product Id` = '{}';".format(
            #         sqlescape(product_id)))
            # Desc, Match_SKU = Matching(parent, product_original_price, product_discount_price, product_name, Old_Data)
            # parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
            # SKU = parent.cur.fetchall()
            # SKU = '' if len(SKU) == 0 else SKU[0][0]
            # SKU = Match_SKU
            # SKU, Desc = '', ''
            Desc = []
            cell = TableWidget.rowCount()
            TableWidget.setRowCount(cell + 1)
            [TableWidget.setItem(cell, x, QTableWidgetItem(str(y).strip())) for x, y in enumerate(
                [hostname, data, SKU, Desc, product_name, '', '', product_original_price, product_discount_price,
                 product_href, product_id])]
            # parent.cur.execute("REPLACE data (`Product Name`,SKU, Link , `Product Original Price`,`Product Discount Price`,`Date Update`,`Product Id`) VALUES ('{}','{}','{}','{}','{}','{}','{}');".format(sqlescape(product_name.replace('"', '').strip()), SKU, product_href, product_original_price, product_discount_price, datetime.today(), product_id))
            # parent.con.commit()

        if not driver.execute_script(
                '\n     items = document.querySelectorAll("[class=\'item pages-item-next\'] a");\n     if(items.length>0) {\n       items[0].click();\n       return 1;\n       } else {return 0;}\n     '):
            break

    Scraped_Date = [Names, Price, Discount, href, ID, SKUs]

    return Scraped_Date, Old_Data


def Dream2000(driver, hostname, TableWidget=QTableWidget, data=string, parent=None):
    Old_Data = FN_Old_Data(parent)
    _ = Page_loaded(driver)
    _.Wait()
    if driver.find_elements_by_xpath("//div[@class = 'ui-dialog "
                                     "ui-widget ui-widget-content "
                                     "ui-corner-all ui-front "
                                     "mage-dropdown-dialog']")[0].text == 'English':
        # print('English')
        element = driver.find_elements_by_xpath("//div[@class = 'ui-dialog "
                                                "ui-widget ui-widget-content "
                                                "ui-corner-all ui-front "
                                                "mage-dropdown-dialog']")[0]
        webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

    Names = []
    href = []
    ID = []
    Discount = []
    Price = []
    SKUs = []

    while 1:
        _.Wait()
        products = driver.find_elements_by_xpath("//a[@class = 'product-item-link']")
        prices = driver.find_elements_by_xpath("//div[@class = 'price-box price-final_price']")
        elems = driver.find_elements_by_css_selector(".product-item-link")
        links = [elem.get_attribute('href') for elem in elems]

        elems = driver.find_elements_by_xpath("//div[@class = 'price-box price-final_price']")
        IDs = [elem.get_attribute('data-product-id') for elem in elems]

        for x in range(0, len(products), 1):
            product_href = links[x]
            product_id = 'DM:' + IDs[x]
            product_name = products[x].text
            product_original_price = prices[x].text
            product_discount_price = prices[x].text
            product_discount_price = rcurr(product_discount_price)
            product_original_price = rcurr(product_original_price)
            Names.append(product_name)
            ID.append(product_id)
            Price.append(product_original_price)
            Discount.append(product_discount_price)
            href.append(product_href)
            parent.cur.execute("SELECT SKU FROM data WHERE `Product Id` = '{}';".format(sqlescape(product_id)))
            SKU = parent.cur.fetchall()
            SKU = '' if len(SKU) == 0 else SKU[0][0]
            SKUs.append(SKU)
            Desc = []
            cell = TableWidget.rowCount()
            TableWidget.setRowCount(cell + 1)
            [TableWidget.setItem(cell, x, QTableWidgetItem(str(y).strip())) for x, y in enumerate(
                [hostname, data, SKU, Desc, product_name, '', '', product_original_price, product_discount_price,
                 product_href, product_id])]
            # parent.cur.execute("REPLACE data (`Product Name`,SKU, Link , `Product Original Price`,`Product Discount Price`,`Date Update`,`Product Id`) VALUES ('{}','{}','{}','{}','{}','{}','{}');".format(sqlescape(product_name.replace('"', '').strip()), SKU, product_href, product_original_price, product_discount_price, datetime.today(), product_id))
            # parent.con.commit()

        if not driver.find_elements_by_xpath("//a[@class = 'action  next']"):
            break
        else:
            driver.find_elements_by_xpath("//a[@class = 'action  next']")[-1].click()

    Scraped_Date = [Names, Price, Discount, href, ID, SKUs]

    return Scraped_Date, Old_Data


# Matching
def Matching(parent, Price, Discount, Name, Old_Data):
    # Old_Data = pd.read_sql_query('Select * from hyper_pos', parent.con)
    #
    # Mapping = {'SKU': 'BARCODE',
    #            'Product Name': 'DESC',
    #            'Product Original Price': 'SELL_PRICE',
    #            'Product Discount Price': 'PROM_PRICE',
    #            'Branch': 'BRANCH'}
    #
    # Old_Data.rename(columns=Mapping, inplace=True)
    #
    # Old_Data.DESC = Old_Data.DESC.apply(lambda x: x.replace('\n', ''))
    #
    # Old_Data.DESC = Old_Data.DESC.apply(lambda x: x.replace('Name: DESC, dtype: object', ''))

    if Price == '':
        Price = 0

        m = process.extractOne(Name,
                               # Old_Data[Old_Data.PROM_PRICE.astype(float) >= 1000].DESC.apply
                               Old_Data.DESC.to_list(),
                               scorer=fuzz.token_set_ratio)

        # print(m, m[1])

        if m[1] > 80:
            return m[0], Old_Data[Old_Data.DESC == m[0]].BARCODE.to_list()[0].strip()
        else:
            return '', '0'

    else:
        if len(Discount) == 0:
            Price = float(Price.replace(',', '').replace('\u200f', ''))
        else:
            Price = float(Discount.replace(',', '').replace('\u200f', ''))

        # print(Price, type(Price))

        m = process.extractOne(Name,
                               Old_Data[(Old_Data.PROM_PRICE.astype(float) < Price * 1.25) &
                                        (Old_Data.PROM_PRICE.astype(float) > Price * .95)].DESC.to_list(),
                               scorer=fuzz.token_set_ratio)

        # print('Step 1: ', m)
        # print('Step 2: ', m[0])
        # print('Step 3: ', m, Old_Data[Old_Data.DESC == m[0]].BARCODE.to_list()[0].strip())

        if m == None:
            return '', '0'
        else:
            if m[1] > 80:
                return m[0], Old_Data[Old_Data.DESC == m[0]].BARCODE.to_list()[0].strip()
            else:
                return '0', '0'


def FN_Old_Data(parent):
    Old_Data = pd.read_sql_query('Select * from hyper_pos', parent.con)

    Mapping = {'SKU': 'BARCODE',
               'Product Name': 'DESC',
               'Product Original Price': 'SELL_PRICE',
               'Product Discount Price': 'PROM_PRICE',
               'Branch': 'BRANCH'}

    Old_Data.rename(columns=Mapping, inplace=True)

    Old_Data.DESC = Old_Data.DESC.apply(lambda x: x.replace('\n', ''))

    Old_Data.DESC = Old_Data.DESC.apply(lambda x: x.replace('Name: DESC, dtype: object', ''))

    return Old_Data


class Page_loaded:

    def __init__(self, driver):
        try:
            self._driver = driver
            self._page_source = self._driver.page_source
        except Exception as e:
            show_pop('Error', str(e),
                     QMessageBox.Critical)

    def Wait(self, secs=0.1, cnt=10):
        i = 0
        while 1:
            time.sleep(secs)
            if self._driver.execute_script('return document.readyState;') == 'complete':
                if self._page_source != self._driver.page_source:
                    self._page_source = self._driver.page_source
                elif self._page_source == self._driver.page_source:
                    if i == cnt:
                        break
                    i += 1


def Add_toolbar(self, ToolBar=QToolBar, Icon=QIcon, text=None, setCheckable=False):
    _ = QAction(Icon, text, self)
    _.triggered.connect(self.btn_click)
    _.setCheckable(setCheckable)
    ToolBar.addAction(_)


def show_pop(title, txt, icon):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(txt)
    msg.setIcon(icon)
    msg.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
    msg.exec_()


def res(filename):
    if getattr(sys, 'frozen', False):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, 'res', filename)
    return os.path.join(os.getcwd(), 'res', filename)


class Obj(object):

    def __init__(self, object):
        self.Obj_obj = object

    def __enter__(self):
        return self.Obj_obj

    def __exit__(self, type, value, traceback):
        pass
