# Web Scrape
_The process of learning how to scrape, some useful tips and projects._

## [SkyTrax ](https://github.com/stephanie0324/Web-Scraping-/tree/main/skytrax)
Skytrax (originally known as Inflight Research Services) is a United Kingdom–based consultancy which runs an airline and airport review and ranking site. [website link](https://www.airlinequality.com/review-pages/a-z-airline-reviews/)
* Crawled Data - total of 19 columns

| column        |  Values         | 注意事項|
| ------------- |:-------------:|:-------------:|
| airline | 航空公司  | |
| datePublished | 發布日期  | |
| review rating | 整體評分 |`ratingValue` (1-10) , `bestRating` (10) |
| text_header   | 評論標題     | |
|review| 評論|`verified` : Our editorial staff have inspected a copy of an e-ticket, booking details or a boarding pass, with the customer name confirming the trip written about in the review. |
|review ratings | 其他瑣碎項目(共11項)| 放置在 `tr`| 
