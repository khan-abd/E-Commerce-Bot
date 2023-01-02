'''AIM OF THIS PROJECT:
To compare the prices of a user defined product from two e-commerce websites
-Amazon and Flipkart through web scraping and web formatting
Features of this version:'''

#Top 3 search results will be displayed when the user inputs the product name

import requests
from bs4 import BeautifulSoup

searchprod=input("Enter product to be searched: ")

h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

'''The above string is a specified user agent developed by Google Inc to render 
web pages and bypassing the bot check in amazon and flipkart firewall system'''


#AMAZON EXTRACTION


Asearchprod=searchprod #Assigning to new variable since searchprod variable is also used later
if " " in Asearchprod:
    Asearchprod.replace(" ", "+")   #url-correcter


url='https://www.amazon.in/s?k='+Asearchprod+'&crid=8EC88KDQ73CJ&sprefix=iphone+1%2Caps%2C269&ref=nb_sb_noss_2'
r= requests.get(url, headers=h) 

#parse html
soup=BeautifulSoup(r.content, 'html.parser')

#pre-declared variables
ANames=[]
AOld_Prices=[]
ANew_Prices=[]
A_olist=[]

#Name

prodname=soup.find_all('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
print()
print("Amazon Exclusive Products:")
for i in prodname:
    ANames.append(i.text)
print(ANames[2:5])         

#Amazon always displays 2 sponsored prodducts initially rather than actual product, so we start from 2nd index

#Old Prices
oprice=soup.find_all('span', class_="a-price a-text-price") 

def rep(x,y): #Function to eliminate of repetition on strings
	mid=int(len(x)/2)
	b=x[0:mid]
	y.append(b)

    
for i in oprice:
    AOld_Prices.append(i.text)

for a in AOld_Prices[2:5]:
	rep(a,A_olist)
print(A_olist)

#In AOldprices, the value of the old price is repeted twice due to a bug in the website
#We fixed that bug using the rep() function and print old prices through A_olist

#New Prices
nprice=soup.find_all('span', class_="a-price-whole")

for i in nprice:
    ANew_Prices.append(i.text)
ANew_Prices= ["₹"+ e for e in ANew_Prices]
print(ANew_Prices[2:5])
print()

#FLIPKART EXTRACTION


Fsearchprod=searchprod
if " " in Fsearchprod:
    Fsearchprod.replace(" ", "%20")   #url-correcter


url='https://www.flipkart.com/search?q='+Fsearchprod+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r= requests.get(url, headers=h) 

#parse html
soup=BeautifulSoup(r.content, 'html.parser')

#pre-declared variables
FNames=[]
FOld_Prices=[]
FNew_Prices=[]

#name
prodname=soup.find_all('div', attrs={'class' :"_4rR01T"} )


print("Flipkart Assured Products: ")


for i in prodname:
    FNames.append(i.text)
print(FNames[:3])

#Old prices
oprice=soup.find_all('div', class_="_3I9_wc _27UcVY")

for i in oprice:
            FOld_Prices.append(i.text)
print(FOld_Prices[:3])

#New prices
nprice=soup.find_all('div', class_="_30jeq3 _1_WHN1")

for i in nprice:
            FNew_Prices.append(i.text)
print(FNew_Prices[:3]) 

        
#HTML
#Now we display all the collected data on an HTML webpage titled 'index.html'   


import pandas as pd

d_amazon=pd.DataFrame({'Amazon Products':ANames[2:5],'Old Prices':A_olist,'New Prices':ANew_Prices[2:5]})

d_flipkart=pd.DataFrame({'Flipkart Products':FNames[:3],'Old Prices':FOld_Prices[:3],'New Prices':FNew_Prices[:3]})

pd.set_option('display.colheader_justify','center') #To centre align column headers

d_amazon.head(4)
d_flipkart.head(4)

htmla = d_amazon.to_html()
htmlf = d_flipkart.to_html()

#To write to html file

html_prefix = '''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
  <style>
    table{
      width: 50%;
      margin: auto;
    }
  </style>
</head>
<body bgcolor='#3AAFA9'>
<h1 align='center'><font color='#025043'> AMAZON vs FLIPKART | WHO IS THE BEST? </font></h1>

'''
html_suffix = '''</body>
</html>'''


#To create file index.html in user's directory and store data

with open('index.html',"w", encoding="utf-8") as text_file:
    text_file.write(html_prefix)
    text_file.write(htmla)
    text_file.write(htmlf)
    text_file.write(html_suffix)

print("Done.")
