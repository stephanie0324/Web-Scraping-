# About
This is a project form LinkedIn Learning, to develop a web application by gathering data from web scraping.

# Crawled Data

| column        |  Values         
| ------------- |:-------------:|
| title| 網頁名稱  | 
| phone no. | 公司電話  | 
|  staff | 員工名稱 / 職稱/ 其他事項|  
|testimonial| 評論|

# Codes
### [web scrape](pet-widsom-medicine/web_scrape.py)
This is where we implement webscraping with request and beautiful soup
* Columns we gather: title / staff / phone no. / links
* http status codes
  * 100-199: informational codes, we don't usually see them
  * 200-299: successfull :heavy_check_mark:  
  * 300-399: redirectional codes
  * 400-499: client error code
  * 500-599: server error code
### [rest api](pet-widsom-medicine/rest_api.py)
We explore Alpha Vantage API to better know about Apple stock through this restful api. [website link](https://www.alphavantage.co/)