# Try-Selenium
Automated Spotify login and play ur favourite playlist 

Requirements-
  Selenium
  
To install selenium selenium run the following command

python -m pip install selenium

This is code uses the Chrome Web Driver, download the webdriver for your version from here
https://sites.google.com/a/chromium.org/chromedriver/

If you are using Linux -
  Extract the downloaded chrome driver and run the following command in terminal
  
  sudo mv chromedriver /usr/local/bin
  
If you are using Windows - 
  Paste the path of installed Driver in the code in line 14 like this
  
  driver = webdriver.Chrome(<Your path>)
