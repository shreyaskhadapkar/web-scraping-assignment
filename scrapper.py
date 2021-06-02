from selenium import webdriver
import time
import csv

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get("https://www.amazon.in/s?i=apparel&bbn=1968543031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1953602031%2Cn%3A11400137031%2Cn%3A1968542031%2Cn%3A1968543031&s=apparels&dc&fst=as%3Aoff&pf_rd_i=1968542031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=629c266a-f7c9-4115-888e-7c3bfa05b9f6&pf_rd_r=JHTVW9BG6GVC4XWDJ6E3&pf_rd_s=merchandised-search-3&qid=1576843301&rnid=11301356031&ref=sr_st_popularity-rank")

listOfDiv = browser.find_elements_by_class_name(
    "s-result-item.sg-col-4-of-16")

listOfUrls = []
for i in listOfDiv:
    listOfUrls.append(i.find_element_by_tag_name("a").get_attribute('href'))


fileName = "result.csv"


with open(fileName, 'w', encoding='UTF-16') as csvfile:

    fieldnames = ["Name_of_the_Product", "Feature_Image", "Category",
                  "Price", "Fit_type", "Product_Images", "ASIN_Number"]

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fieldnames)

    for url in listOfUrls:
        try:
            browser.get(url)
            name = browser.find_element_by_id("title").text

            categoryElement = browser.find_elements_by_css_selector(
                "span.a-text-bold")
            price = browser.find_element_by_id("priceblock_ourprice").text

            category = "Clothing and Accessories"
            for i in categoryElement:
                if(i.get_attribute('innerText') == "ASIN : "):
                    asin = i.find_element_by_xpath("./..").text
                if(i.get_attribute('innerText') == "Generic Name : "):
                    category = i.find_element_by_xpath("./..").text

            category = category if category == "Clothing and Accessories" else category[15:]

            fit_type_list = browser.find_elements_by_css_selector(
                "span.a-list-item")
            for i in fit_type_list:
                if("Fit Type: " in i.get_attribute('innerText')):
                    fitType = i.get_attribute('innerText')
                    fitType = fitType[10:]

            featureImageTag = browser.find_element_by_class_name(
                "a-dynamic-image")
            featureImageUrl = featureImageTag.get_attribute('src')

            listOfButtons = browser.find_elements_by_css_selector(
                "li.imageThumbnail")

            for i in listOfButtons:
                i.find_element_by_css_selector("input.a-button-input").click()
                time.sleep(1)
                imgTag = browser.find_elements_by_class_name(
                    "a-stretch-horizontal")
            listOfImageUrls = []
            for i in imgTag:
                listOfImageUrls.append(i.get_attribute('src'))
            csvwriter.writerow(
                [name, featureImageUrl, category, price, fitType, listOfImageUrls, asin[7:]])
        except:
            pass
browser.quit()
