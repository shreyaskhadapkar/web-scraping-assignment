from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get("https://www.amazon.in/s?i=apparel&bbn=1968543031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1953602031%2Cn%3A11400137031%2Cn%3A1968542031%2Cn%3A1968543031&s=apparels&dc&fst=as%3Aoff&pf_rd_i=1968542031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=629c266a-f7c9-4115-888e-7c3bfa05b9f6&pf_rd_r=JHTVW9BG6GVC4XWDJ6E3&pf_rd_s=merchandised-search-3&qid=1576843301&rnid=11301356031&ref=sr_st_popularity-rank")

listOfDiv = browser.find_elements_by_class_name(
    "s-result-item.sg-col-4-of-16")

listOfUrls = []
for i in listOfDiv:
    listOfUrls.append(i.find_element_by_tag_name("a").get_attribute('href'))

# browser.quit()

browser.get(listOfUrls[4])
'''
name =
featureImage
Category = 
Price =
Fit type =
Product Image
asin number =
'''
name = browser.find_element_by_id("title").text
print(name)
categoryElement = browser.find_elements_by_css_selector("span.a-text-bold")
price = browser.find_element_by_id("priceblock_ourprice").text
print(price)
category = "Clothing and Accessories"
for i in categoryElement:
    if(i.get_attribute('innerText') == "ASIN : "):
        asin = i.find_element_by_xpath("./..").text
        print(asin[7:])
    if(i.get_attribute('innerText') == "Generic Name : "):
        category = i.find_element_by_xpath("./..").text
        # print(category.split()[3])
category = category if category == "Clothing and Accessories" else category[15:]
print(category)
fit_type_list = browser.find_elements_by_css_selector("span.a-list-item")
for i in fit_type_list:
    if("Fit Type: " in i.get_attribute('innerText')):
        fitType = i.get_attribute('innerText')
        fitType = fitType[10:]
        print(fitType)
print("==============e")
