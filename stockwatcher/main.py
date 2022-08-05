#import libraries
from bs4 import BeautifulSoup
import requests

#creation of the list of dictionaries
list_stocks = [
  {
      'name' : 'Google',
      'url' : 'https://finance.yahoo.com/quote/GOOG?p=GOOG',
  },
  {
      'name' : 'Amazon',
      'url' : 'https://finance.yahoo.com/quote/AMZN?p=AMZN',
  },
  {
      'name' : 'Facebook',
      'url' : 'https://finance.yahoo.com/quote/FB?p=FB',
  },
  {
      'name' : 'Netflix',
      'url' : 'https://finance.yahoo.com/quote/NFLX?p=NFLX',
  },
  {
      'name' : 'Apple',
      'url' : 'https://finance.yahoo.com/quote/AAPL?p=AAPL',
  },
  {
      'name' : 'Tesla',
      'url' : 'https://finance.yahoo.com/quote/TSLA?p=TSLA',
  },
]

#watcher procedure
def watcher(sure, user_stock, user_target):
  global price, Status
  count = 0
  if sure == "yes":
    for s in list_stocks: 
      count += 1 
      if s['name'] == user_stock: 
        #user agents(headers) found on Jovian, author: landryroni, title: Scraping Amazon.com Best Sellers in Baby clothing and Shoes using Python, URL: https://jovian.ai/landryroni/data-analyst-project-1-web-scraping/v/93
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        page = requests.get(s['url'], headers = headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        res = soup.find_all('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
        price = float(res[0].text.replace(',', ''))
        Status = price < float(user_target)
        break
      else:
        if (count == len(list_stocks)):
          print("The stock input is not in the list")
          quit()
  else: 
    Exit = input("Do you want to exit the program? ")
    if Exit == "yes":
      print("Thanks for using!")
      quit()
    else: 
      user_stock = input("\nEnter the name of the stock: ")
      user_target = input("Enter the target price(Integer or decimal only): ")
      sure = input("Are you sure to track " + user_stock + " with " + user_target + " target price? ")
      watcher(sure, user_stock, user_target)

#print result
def result(Status, user_stock, user_target, price):
  if Status:
    print("\n" + user_stock + " is recommended. Current price " + str(price) + " is lower than your target price " + str(user_target) + ". \n")
  else: 
    print("\n" + user_stock + " is not recommended. Current price " + str(price) + " is higher than your target price " + str(user_target) + ". \n")

#asking for user inputs
print("Welcome to the stock watcher! Please select a stock to track in the following list: \n")
for stock in list_stocks:
  print(stock['name'])

user_stock = input("\nEnter the name of the stock: ")
user_target = float(input("Enter the target price (Integer or decimal only): "))
sure = input("Are you sure to track " + user_stock + "? ")

#call the watcher and result procedure
watcher(sure, user_stock, user_target)
result(Status, user_stock, user_target, price)

#ask for another try
check = 0
while check != -1: 
  answer = input("Do you want to try another product? ")
  if answer == "yes":
    user_stock = input("\nEnter the name of the stock: ")
    user_target = float(input("Enter the target price(Integer or decimal only): ") )
    sure = input("Are you sure to predict " + user_stock + "? ")
    watcher(sure, user_stock, user_target)
    result(Status, user_stock, user_target, price)
  else: 
    check = -1
    print("Thanks for using the program!")
