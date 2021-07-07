import scrapy
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

if __name__ == '__main__':

    print("Please Enter a Sheet Name")
    sheet_name = input()

    if (sheet_name == "Magyar" or sheet_name == "Bulgarian" or sheet_name == "Italian" or sheet_name == "Spanish"):

        lang1 = []  # List to store id of English forms
        lang2 = []  # List to store id of Turkish forms
        df = pd.read_excel('Copy of Form Templates of All Languages.xlsx', sheet_name=sheet_name)
        english = df["URL TO THE ENGLISH FORM"]
        other_language = df["CREATED FORM URL"]
        s = "123example456"
        driver = webdriver.Chrome("chromedriver.exe")
        problematicIndexes = []
        problematicIndexes2 = []

        control = 0
        for link in other_language:
            id = re.sub("[^0-9]", "", link)
            lang2.append((id))

        print("The length of" + sheet_name + " is: ", len(lang2))
        filename = sheet_name + ".txt"
        with open(filename, 'w') as f:
            for item in lang2:
                f.write("%s\n" % item)

        control = 0
        for link in english:
            if control in problematicIndexes2:
                control += 1
                continue
            driver.get(link)
            content = driver.page_source
            soup = BeautifulSoup(content, features="lxml")
            container = soup.find('div', class_="modal template-detail")
            result = re.search('data-form-id=(.*)data-template-url', str(container))
            if type(result) == type(s):
                lang1.append(result.group(1).replace('\"', ''))
            else:
                print(control)
                problematicIndexes.append(control)
            control += 1

        print("The length of English is: ", len(lang1))
        engfilename = "English" + sheet_name + ".txt"
        with open(engfilename, 'w') as f:
            for item in lang1:
                f.write("%s\n" % item)

    else:

        lang1 = []  # List to store id of English forms
        lang2 = []  # List to store id of Turkish forms
        df = pd.read_excel('Copy of Form Templates of All Languages.xlsx', sheet_name=sheet_name)
        english = df["URL TO THE ENGLISH FORM"]
        other_language = df["PUBLISHED FORM TEMPLATE URL"]
        s = "123example456"
        driver = webdriver.Chrome("chromedriver.exe")
        problematicIndexes = []
        problematicIndexes2 = []

        control = 0
        for link in other_language:
            driver.get(link)
            content = driver.page_source
            soup = BeautifulSoup(content, features="lxml")
            container = soup.find('div', class_="modal template-detail")
            result = re.search('data-form-id=(.*)data-template-url', str(container))
            if type(result) == type(s):
                lang2.append(result.group(1).replace('\"', ''))
            else:
                print(control)
                problematicIndexes2.append(control)
            control += 1

        print("The length of" + sheet_name + " is: ", len(lang2))
        filename = sheet_name + ".txt"
        with open(filename, 'w') as f:
            for item in lang2:
                f.write("%s\n" % item)

        control = 0
        for link in english:
            if control in problematicIndexes2:
                control += 1
                continue
            driver.get(link)
            content = driver.page_source
            soup = BeautifulSoup(content, features="lxml")
            container = soup.find('div', class_="modal template-detail")
            result = re.search('data-form-id=(.*)data-template-url', str(container))
            if type(result) == type(s):
                lang1.append(result.group(1).replace('\"', ''))
            else:
                print(control)
                problematicIndexes.append(control)
            control += 1

        print("The length of English is: ", len(lang1))
        engfilename = "English" + sheet_name + ".txt"
        with open(engfilename, 'w') as f:
            for item in lang1:
                f.write("%s\n" % item)
