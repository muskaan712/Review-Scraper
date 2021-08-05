<h2>Walmart Product Review Scraper using Selenium</h2>

## Imports
- Selenium (for chromedriver)
- Dateutil Parser (for parsing)
- Pandas (for generating data frame and CSV from it)


## Process of Making

1. Used Selenium and Python functions to visit the given product link and to scroll down to required section.
2. Then the script moves to  **'See all reviews'** Button to get all reviews.
3. Then it sorts the reviews from newest to oldest till December 2020.
4. Then the script scraps the review details as mentioned in the problem from all pages till December 2020.
5. After the above process the code generates the required output.csv file.

## Challenges
1. The empty titles were making different sized lists in the beginning.
2. The date has to be converted to datetime format from string format.

## Future Improvements
1. Scrapy or BeautifulSoup can be used for easy and fast implementation as compared to selenium.
2. It will be reusable code for other products, time/date range.
3. It can also be used for other retailing websites by changing the url link of product/retailer and taking the limitations of script blocking etc into consideration.

