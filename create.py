import bs4
import urllib.request
import smtplib
import time

url = "https://books.toscrape.com/catalogue/thomas-jefferson-and-the-tripoli-pirates-the-forgotten-war-that-changed-american-history_867/index.html"
Required_price = 40
EMAIL_ADDRESS= "Samplework123@outlook.com"

def TitlePrice():
    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")
    title = soup.find("h1").get_text()
    prices=soup.find("p",class_="price_color").get_text()
    prices=prices[1:]
    prices = float(prices)

    print(title,prices)
    return prices

def compare():

    price =TitlePrice()
    if price>=Required_price:
        diff= price - Required_price
        print("the required price is still {}".format(diff))
    else:
        print("the price of the product is cheaper now ... Hurry up !!!")
        sendmail()

def sendmail():
    subject= "Hey there bud !! the price has been dropped hurry Up !!!!"
    body = "subject:" + subject+'\n\n'+url
    server = smtplib.SMTP(host='smtp.outlook.com', port = 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, '12345samplework')
    server.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS, body)
    print("mail sent sucessfully")
    pass

if __name__=="__main__":
    while True:
        compare()
        time.sleep(44000)












