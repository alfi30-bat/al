from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
# Initialize the Chrome driver
from docx import Document

service = Service("E:/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Now you can access the capabilities attribute
#print(driver.capabilities)
# Open the webpage


######################################################
doc = Document('E:/ktg brisk.docx')
x=0
y=0
# Extract text
full_text = []
page_text = []
for para in doc.paragraphs:
    if 'PAGE BREAK' in para.text: 
        text = '\n'.join(full_text)
        page_text.append(text)
        x=1
        print(x, page_text, text)
    driver.get("https://www.text2latex.com/")
    #s="V_{1}/T_{1} = V_{2}/T_{2} V/T = constant"
    # Locate the textbox (replace 'textbox_id' with the actual ID of the textbox)
    #textbox = driver.find_element(By.ID, "textbox_id")    
    textarea = driver.find_elements(By.CSS_SELECTOR, "textarea")[0]  # First textarea

    #textarea.send_keys(s)
    textarea.send_keys(para.text)
    textarea.send_keys(Keys.RETURN)
    time.sleep(1)

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(3)

    textarea2 = driver.find_elements(By.CSS_SELECTOR, "textarea")[1]  # Second textarea
    # Get the content of the textbox
    content = textarea2.get_attribute("value")
    full_text.append(content)

# Join all paragraphs into a single string
text = '\n'.join(full_text)
print(text)





print("Content of the textbox:", content)

# Close the browser
driver.quit()

# Locate the textarea by its CSS selector
textarea = driver.find_element(By.CSS_SELECTOR, "textarea#input-text")

# Send text to the textarea
