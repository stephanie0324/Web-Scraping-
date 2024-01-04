# Web Scrape
_The process of learning how to scrape, some useful tips and projects._

## [SkyTrax ](https://github.com/stephanie0324/Web-Scraping-/tree/main/skytrax)
Skytrax (originally known as Inflight Research Services) is a United Kingdom–based consultancy which runs an airline and airport review and ranking site. [website link](https://www.airlinequality.com/review-pages/a-z-airline-reviews/)
* Crawled Data - total of 19 columns

| column        |  Values         | 注意事項|
| ------------- |:-------------:|:-------------:|
| airline | 航空公司  | |
| datePublished | 發布日期  | |
| author | 評論者  | |
| review rating | 整體評分 |`ratingValue` (1-10) , `bestRating` (10) |
| text_header   | 評論標題     | |
| aircraft   | 機型     | |
|review| 評論|`verified` : Our editorial staff have inspected a copy of an e-ticket, booking details or a boarding pass, with the customer name confirming the trip written about in the review. |
|review ratings | 其他瑣碎項目(共12項)| 放置在 `tr` ，（1-5）顆星的評分機制| 

## [Indeed](https://github.com/stephanie0324/Web-Scraping-/tree/main/indeed)
Indeed is the #1 job site in the world1 with over 350M+ unique visitors every month2. [website link](https://tw.indeed.com/?r=us)

## [Pet Widsom Medicine](pet-widsom-medicine)
Wisdom Pet Medicine is a fictitious company that offers veterinary and grooming services for its clients. [website link](http://thisisasite.net/)

> This is a project form LinkedIn Learning, to develop a web application by gathering data from web scraping.

| column        |  Values         
| ------------- |:-------------:|
| title| 網頁名稱  | 
| phone no. | 公司電話  | 
|  staff | 員工名稱 / 職稱/ 其他事項|  
|testimonial| 評論|