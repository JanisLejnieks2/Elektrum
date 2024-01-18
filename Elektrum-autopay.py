import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
option = webdriver.ChromeOptions()
option.add_argument('--incognito')
driver = webdriver.Chrome(service=service, options=option)
#Palaiž lapu
url = "https://www.elektrum.lv/"
driver.get(url)
time.sleep(2)

accept_button = driver.find_element(By.ID, "ccc-notify-accept")
accept_button.click()
link_href = "https://www.elektrum.lv/lv/maksat-par-elektribu/"
link = driver.find_element(By.XPATH, f'//a[@href="{link_href}"]') #path to link
link.click()
while True:
    #user_code = input("Ievadiet rēķina nummuru") 
    input_name = "number"
    input_field = driver.find_element(By.NAME, input_name)
    input_field.clear()
    #input_field.send_keys(user_code)  #
    input_field.send_keys("36189900008", Keys.RETURN)  #nokomentēt šo un noņemt komentus no pārējā koda - būs jāievada manuāli rēķina nummurs
    #search_button = driver.find_element(By.ID, "public-payments-search-submit")
    #search_button.click()
    #checking for errors
    #EC - expected condition check if in html dom appears error notification
    error_notification = EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.notification.error[data-notification="error"]')) #path to error not..

    try:
        WebDriverWait(driver, 3).until(error_notification)
        print("Nekorekts rēķina numurs.")
    except:
        #Atrod un uzrāda <p> elementa tekstu ar klasi "total"
        total_elements = WebDriverWait(driver, 1).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'total'))
        )
        if total_elements:
            total_text = total_elements[0].text.strip()
            print(f"{total_text}")
            # Pieprasa samaksas daudzumu// izmantojot xpath lai atrastu elementus izmasntojot id ar vārdu "paymentAmount_field" 
            while True:
                payment_amount_input = driver.find_element(By.XPATH, '//input[contains(@id, "paymentAmount_field")]')
                payment_amount_input.click()
                payment_amount_input.clear()
                payment_amount = input("Es maksāšu: ")
                payment_amount_input.send_keys(payment_amount)
                # nospiež uz swedbank
                radio_button_selector = 'input[type="radio"][name="paymentProvider"][value="leafPaymentProviderKevin::SWEDBANK_LV"]'
                radio_button = driver.find_element(By.CSS_SELECTOR, radio_button_selector)
                radio_button.click()
                time.sleep(1)
                # nospiež pogu samaksāt
                submit_button_selector = 'button[type="submit"].button#cart-submit'
                submit_button = driver.find_element(By.CSS_SELECTOR, submit_button_selector)
                submit_button.click()
                #kļūdu apstrāde - ja ievadīts 0 vai nepareizs simbols
                error_span_format = EC.visibility_of_element_located((By.XPATH, '//span[@class="error" and text()="Nepareizs formāts"]'))
                error_span_required = EC.visibility_of_element_located((By.XPATH, '//span[@class="error" and text()="Lūdzu, aizpildiet šo lauku!"]'))
                try:
                    WebDriverWait(driver, 3).until(error_span_format)
                    print("Nepareizs formāts. Lūdzu, ievadiet pareizu summu.")
                    continue #Iet caur while loop atkal
                except:
                    try:
                        WebDriverWait(driver, 3).until(error_span_required)
                        print("Aizpildiet šo lauku!")
                        continue #Iet caur while loop atkal
                    except:
                        break
            while True:
                #ielogošanās swedbank
                user_id_input = WebDriverWait(driver, 6).until(
                EC.presence_of_element_located((By.ID, "login-widget-user-id-sid")))
                your_user_id = input("Ievadiet bankas lietotāja kodu:")
                user_id_input.send_keys(your_user_id) 

                #Personas koda apstrādāšana
                personal_code_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "login-widget-identity-number-smart-id")))
                personal_code_input.click()
                your_personal_code = input("Ievadiet personas kodu: ")
                personal_code_input.send_keys(your_personal_code)

                #Poga - pievienoties
                pievienoties_button2 = EC.element_to_be_clickable((By.CLASS_NAME, 'button.-positive'))
                pievienoties_button2 = WebDriverWait(driver, 5).until(pievienoties_button2)
                pievienoties_button2.click()
                #time.sleep(1)
                #error apstrāde - tālāka apmaksa
                error =  EC.visibility_of_element_located((By.XPATH, '//ui-message[@type="error"]//div[@class="ui-message__content"]'))  
                try:
                    error_message = WebDriverWait(driver, 5).until(error)
                    print("Nepareizs lietotāja kods vai persoans kods")
                    user_id_input.clear()
                    personal_code_input.clear()
                    continue
                except:
                    PIN2_button_id = "execute-button"
                    PIN2_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.ID, PIN2_button_id)))
                    PIN2_button.click()
                try: 
                    payment_thank_you_class = "payment-thank-you"
                    payment_thank_you_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, payment_thank_you_class)))
                    #prints the message
                    message_element = payment_thank_you_element.find_element(By.XPATH, './/div[@class="text"]/p[2]')
                    print(message_element.text)
                except:
                    break
        time.sleep(5)
    driver.quit()

