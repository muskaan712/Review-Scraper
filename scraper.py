# Importing lib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from dateutil.parser import parse
import time
import pandas as pd

# Dataframe
df = pd.DataFrame(columns = ['Review_Date', 'Reviewer_Name', 'Review_title', 'Review_description', 'Rating'])

# Intializing Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('D:\scraper\chromedriver.exe', options=options)

# Link for Product
url='https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365'
driver.get(url)
driver.find_element_by_xpath("//*[@id='customer-reviews-header']/div[2]/div/div[3]/a[2]/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/select/option[3]").click()
reviewsURL = driver.current_url

flag  = False
pagenum = 1

print("begin scraping")
while True:
    time.sleep(1)
    reviews = driver.find_elements_by_class_name("review")
    print("Page No.",pagenum)
    for review in reviews:
        # Convert the date string to datetime object
        date_in_num = parse(review.find_element_by_class_name("review-date-submissionTime").get_attribute("content"))

        if date_in_num.year == 2020 and date_in_num.month == 12:
            # if this condition is true we will come out of the loop
            flag = True
            print("All reviews Scraped!")
            break
        # Name
        reviewer_name = review.find_element_by_class_name("review-footer-userNickname").text
        # Rating
        rating = int(float(review.find_element_by_class_name("seo-avg-rating").text))
        # Title
        try:
            review_title = review.find_element_by_class_name("review-title").text
        except: 
            # Filling it with blank/not a number
            review_title= None
        # Description
        review_desc = review.find_element_by_class_name("review-text").text
        df.loc[len(df.index)] = [date_in_num,reviewer_name,review_title,review_desc,rating]

    if flag:
         break
    driver.find_element_by_class_name("paginator-btn-next").click()
    pagenum+=1

driver.quit()
df.to_csv("output.csv")
print("output csv file generated")
