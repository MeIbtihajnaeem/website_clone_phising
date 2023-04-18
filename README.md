# website_clone_phising
This script is an example of how to clone a login webpage and redirect the request to your server

## Steps to Run 
  1.Clone the script <br />
  2.Run command `python3 main.py` <br />
  3.Enter the url of webpage you want to clone <br />
  4.Wait for the script to open the login page on the browser <br />
  5.Enter the url of the rest api where you want to recieve the request <br />
  6.Test by clicking the login button <br />
  
 
 ### How to prevent web page from being cloned 
 
 1. Encoding: Use of different encoding technique.

 2. JavaScript: If the original website uses JavaScript to generate the content of the login page, Python scripts may not be able to properly clone it. In this case, you may need to use a headless browser like Selenium to clone the page.

 3. Anti-scraping measures: Some websites may use anti-scraping measures like CAPTCHAs or IP blocking to prevent automated scripts from accessing their content.


 ## Note
 ~~This example doesn't work for all the webpages~~




