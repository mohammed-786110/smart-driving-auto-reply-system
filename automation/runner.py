import os
import sys
sys.path.append(
    "C:/Users/HP/Desktop/MINOR PROJECT/AI_Scheduler(ProjectH2S)/backend"
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')



import django
django.setup()


from django.contrib.auth.models import User
from auto_messaging.views import handle_incoming_message
from automation.whatsapp_bot import WhatsAppBot

import time




last_messages = {}
replied = {}

bot = WhatsAppBot()
user = User.objects.first()

print("Bot started...")

while True:
    try:
        if bot.open_chat():
            print("Chat opened.")

            sender = bot.get_contact_name()

            if sender:
                print(f"Message from: {sender}")

                # geeting the last message to check if it's new or not
                current_message = bot.get_last_message()

                #Check if new message
                if sender not in last_messages or last_messages[sender] != current_message:

                    #  Check cooldown (30 sec)
                    if sender not in replied or time.time() - replied[sender] > 30:

                        result = handle_incoming_message(user, sender)
                        print("DEBUG:", result)
                        if result.get("reply_sent"):
                            bot.send_reply(result["message"])
                            print(f"Replied to {sender}")

                            replied[sender] = time.time()
                            last_messages[sender] = current_message

                    else:
                        print(">>> Waiting due to timer")

                else:
                    print(">>> Same message, skipping")

        time.sleep(3)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
                    
                

                

       

   
        


# SELENIUM INTEGRATION : THIS WILL HELP IN READING WHATSAPP MESAGES AND EXTRACT NAME OF SENDER
#  UNIQUE IS THAT IT WILL HELP IN AUTOMATING WHATSAPP REPLY OR INFORM SENDER BASE D ON THEIR RELATION
# WHILE A PERSON IS DRIVING BY TOGGLING SWITCH. FURTHER NLP BASED CUSTOMIZED REPLY WILL BE SENT 
#  AND ALSO IOT OR MOBILE SENSORS WILL BE INTEGARTED TO AUTOMATE THE WHATSAPP REPLY IF A PERSON 

# IS DRIVING WITHOUT TOGGLING THE SWITCH
# SPEED WILL BE DETECTED: IF SPEED IS > 20 KM/H THEN THE SETTINGS WILL BE SET TO DRIVING AUTOMATICALLY
# AND REPLY WILL BE GIVEN TO MSG SENDER WAITING FOR 2SEC FOR A CLICK TO BE MADE.


# IN CARS A SMALL SWITCH FUNCTIONALITY FOR WHATSAPP CAN BE PLACED IN APPLE CAR PLAY/ANDROID AUTO WHICH CAN BE TOGGLED TO ENABLE OR DISABLE THE AUTO REPLY FEATURE.
# THIS WILL HELP IN CASE IF SENSORS FAIL TO INFORM THE SPEED SO THE USER WILL TOGGLE THE SWITCH MANUALLY WHILE DRIVING.
# IF IN CASE MOBILE SENSORS OR IOT INTEGRATION FAILS THEN ALSO THIS BUTTON CAN BE TOGGLED TO ENABLE THE AUTO REPLY FEATURE.

# NLP 
