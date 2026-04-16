# from django.shortcuts import render
# import google  import genai

# from dotenv import load_dotenv
# load_dotenv()

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()



api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)
# for model in client.models.list():
#     print(model.name)



# API_KEY = os.getenv("GEMINI_API_KEY")

# genai.configure(api_key=API_KEY)
# model=genai.GenerativeModel("gemini-pro")


# Create your views here.
# 
def generate_reply(relation, sender):
    relation=relation.lower()
    try:
        prompt = f"""
        Generate a short WhatsApp auto-reply.
        Context: User is driving.
        Sender: {sender}
        Relation: {relation}
        Rules:
        - Keep it short
        - No emojis
        - Human-like tone
        """

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        print("AI Error:", e)

        # fallback (VERY IMPORTANT)
        return "I'm driving right now, will reply later."
    
    
    
    
    
    
    # PREVIOUS MANUAL RESPONSES (BEFORE AI IMPLEMENTATION):
    # if relation == "family":
    #     return f"Hii {sender}! I'm driving right now, will call you shortly after reaching my destination. Call me please."

    # elif relation == "boss":
    #     return f"Hello {sender}! I'm currently driving, will respond as soon as possible."

    # elif relation == "friend":
    #     return f"Hello {sender}! Driving bro, will text you later 😄"

    # elif relation == "emergency":
    #     return f"Hello {sender}! I'm driving right now. If urgent, please call again!"

    # else:
    #     return f"Hello {sender}! I'm driving, will reply later."