from selenium import webdriver
browser = webdriver.Chrome('d:\\webdrivers\\chromedriver.exe')
browser.get('https://www.facebook.com/')
user_id=input("enter the email or phone number:")
password=input("enter the password:")
print(user_id)
print(password)
cd='d:\\webdrivers\\chromedriver.exe' #path to your chrome driver


#browser= webdriver.Chrome(cd)
#browser.get('https://www.facebook.com/')


user_box = browser.find_element_by_id("email")       # For detecting the user id box
user_box.send_keys(user_id)                                               # Enter the user id in the box 

password_box = browser.find_element_by_id("pass")    # For detecting the password box
password_box.send_keys(password)                                          # For detecting the password in the box

login_box = browser.find_element_by_id("u_0_b")      # For detecting the Login button
login_box.click()