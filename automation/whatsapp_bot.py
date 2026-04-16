from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WhatsAppBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com")

        print("📱 Scan QR Code...")
        input("Press ENTER after scanning...")

    def get_unread_chats(self):
        try:
            return self.driver.find_elements(By.XPATH, '//span[@aria-label="Unread"]')
        except:
            return []

    def open_chat(self):
        
        try:
            
         chats = self.driver.find_elements(By.XPATH, '//div[@role="row"]')

         if chats:
             chats[0].click()
             print("Opened latest chat")
             time.sleep(2)
             return True

        except Exception as e:
            
             print(e)
             return False

    
    def get_contact_name(self):
        try:
            name = self.driver.find_element(By.XPATH, '//header//span[@dir="auto"]').text
            return name
        except:
            return None

    def send_reply(self, message):
        
         try:
             box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
             box.send_keys(message)
             box.send_keys("\n")
             time.sleep(1)
        
             
         except Exception as e:
             print("Send error:", e)
    
    def get_last_message(self):
        
         try:
             msgs = self.driver.find_elements(By.XPATH, '//div[contains(@class,"message-in")]')
             if msgs:
                 return msgs[-1].text
         except:
             return None