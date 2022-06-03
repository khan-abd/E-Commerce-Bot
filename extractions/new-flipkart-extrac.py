from bs4 import BeautifulSoup
import requests

searchprod=input("Enter product to be searched: ")
if " " in searchprod:
    searchprod.replace(" ", "%20")   #url-correcter

#get html
h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#To bypass bot-check

url='https://www.flipkart.com/search?q='+searchprod+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r= requests.get(url, headers=h) 

#parse html
soup=BeautifulSoup(r.content, 'html.parser')

#pre-dec variables
Names=[]
Old_Prices=[]
New_Prices=[]

 #1st way of listing 
 
#name
prodname=soup.find_all('div', attrs={'class' :"_4rR01T"} )
if bool(prodname)==True:
        print("Search results for", searchprod,"->")
        print()

        for i in prodname:
            Names.append(i.text)
        print(Names[:3])
        #price
        oprice=soup.find_all('div', class_="_3I9_wc _27UcVY")
        nprice=soup.find_all('div', class_="_30jeq3 _1_WHN1")

        for i in oprice:
            Old_Prices.append(i.text)
        print(Old_Prices[:3])

        for i in nprice:
            New_Prices.append(i.text)
        print(New_Prices[:3])
 
# 2nd way of listing

if Names==[]:  #If code for first listing doesn't work
        #name
        prodname=soup.find_all('a' , class_="s1Q9rs")
        print("Search results for", searchprod,"->")
        print()

        for i in prodname:
            Names.append(i.text)
        print(Names[:3])
        #price
        oprice=soup.find_all('div', class_="_3I9_wc")
        nprice=soup.find_all('div', class_="_30jeq3") 
        for i in oprice:
            Old_Prices.append(i.text)
        print(Old_Prices[:3])
        
        for i in nprice:
            New_Prices.append(i.text)
        print(New_Prices[:3])




