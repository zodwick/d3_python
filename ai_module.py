import cohere
from dotenv import load_dotenv
import os
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def web_search(query):
    # print(query)
    msg = co.chat(
        model="command",
      
        message=f" This is how the user is feeling today: {query},  suggest some yoga poses for me to do and other meditation techniques.",
        connectors=[{"id": "web-search"}])
    # print(msg.citations)
   

    return msg.text
