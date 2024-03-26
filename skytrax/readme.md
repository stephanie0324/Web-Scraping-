# About
There are two ver. of web scraping that I've created.  
Outputs are saved in the `Reviews` folder in `.csv`, a file for an airline.

# Crawled Data
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

# Codes

### [web_scrape_forall](https://github.com/stephanie0324/Web-Scraping-/blob/main/skytrax/web_scrape_forall.ipynb) 
* This for getting all the reviews from all airlines. 
* All review are collected from the moment you run through the codes.
### [web_crawl_func](https://github.com/stephanie0324/Web-Scraping-/blob/main/skytrax/web_crawl_func.ipynb) 
* This version allows people to get reviews after a specific date, which means that you can flexiblely add new datas to your files without 
having to go through all the reviews every time you want to scrape some infos from the website. 

# 參考資料
* [Aviation Scraping using beautiful soup ](https://medium.com/@sven.hafner/aviation-data-web-scraping-part-1-abce2ee992b8)
* [Top 10 Air](https://github.com/freddy90503/SkyTrax_Scraping/tree/master/Top10Air/Top10Air)

