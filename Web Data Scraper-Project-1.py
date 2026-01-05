import requests
from bs4 import BeautifulSoup
import pandas as pd


url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req=requests.get(url)
#print(req)

soup = BeautifulSoup(req.text, features="html.parser")
#print(soup)

titles=[item.text.strip() for item in soup.find_all(name="a",class_="title")]
prices=[item.text.strip() for item in soup.find_all(name="h4",class_="price float-end card-title pull-right")]
descriptions=[item.text.strip() for item in soup.find_all(name="p",class_="description card-text")]
noOfReviews=[item.text.strip() for item in soup.find_all(name="a",class_="title")]

#step-4 Storing Data in Dataframe
df = pd.DataFrame({
    "Title":titles,
    "Description":descriptions,
    "Price":prices,
    "Reviews":noOfReviews
    })

df.to_excel(excel_writer="laptop_data.xlsx",index=False)
print("Data has been save successfully.!")

#titles=soup.find_all(name="a",class_="title")
#print(titles)
#productCards=soup.find_all(name="div",class_="col-md-4 col-xl-4 col-lg-4")
#print(len(productCards))

#prices=soup.find_all(name="h4",class_="price float-end card-title pull-right")
#print(titles)
#for item in prices:
    #print(item.text)
    
#descriptions=soup.find_all(name="p",class_="description card-text")
#print(titles)
#for item in descriptions:
#    print(item.text)
    
#noOfReviews=soup.find_all(name="p",class_="review-count float-end")
#print(titles)
#for item in noOfReviews:
#   print(item.text)