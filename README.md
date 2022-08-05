# Stock_Watcher

The project aims to make recommendations on whether the stock user-selected among a provided Yahoo stock list is a good choice to purchase by comparing the user target price and the latest price of the stock.

Loops through the list of dictionaries to find the URL that corresponds with the user-selected stock, makes an HTTP request to this URL, parses the web page into HTML format using BeautifulSoup, and finds and stores the latest stock price. The program then determined the recommendation status by comparing the latest price with the user_target price.

Project video demonstration: https://youtu.be/lSMO7yTzmik  
