
from bs4 import BeautifulSoup
import requests

searchprod=input("Enter product to be searched: ")
if " " in searchprod:
    searchprod.replace(" ", "+")   #url-correcter

#get html
h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 #To bypass bot-check

url='https://www.amazon.in/s?k='+searchprod+'&crid=8EC88KDQ73CJ&sprefix=iphone+1%2Caps%2C269&ref=nb_sb_noss_2'
r= requests.get(url, headers=h) 

#parse html
soup=BeautifulSoup(r.content, 'html.parser')

#name
prodname=soup.find('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
print()
print(prodname.text, "(Amazon Exclusive)")

#price
oprice=soup.find('span', class_="a-price a-text-price")
price=soup.find('span', class_="a-price")
def rep(a):
    mid=int(len(a)/2)
    b=a[0:mid]
    return b
print("Old Price: ", rep(oprice.text))
print("New Price: ", rep(price.text))




