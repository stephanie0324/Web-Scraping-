#%%
# Install packages
import requests
from bs4 import BeautifulSoup
# %%
#　Retrive web page info
response = requests.get('http://thisisasite.net/')

## check if you got the page or web status
response.url
response.status_code #200

# %%
# Retrive html code
# response.content # the original from web without transforming to text
response.text

# better visualization for the text
soup = BeautifulSoup(response.text)
print(soup.prettify)

# %%
# Find and Find_All
soup.find("title")
soup.find_all("article") # find services
print(soup.find("span", class_="phone").text)

# %%
# Testimonials
freatured_testimonial = soup.find_all("div", class_="quote")
for testimonial in freatured_testimonial:
    print(testimonial.text)
# %%
# Staff
staffs = soup.find_all("div",class_ = 'info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8')
for staff in staffs:
    print(staff.text)
# %%
# Finding all the links
links = soup.find_all("a")
for link in links:
    print(link.test, link.get('href'))
# %%
# output the html codes
with open('./output/widsom_vet.txt', "w") as f:
    f.write(soup.prettify())

# %%
