# discord scraper working!!

# Use request library to make a GET request to a particular channel 

import requests
import json

guild_ids = {

    sacra_yc21: "823162729392767017",
    sacra_intros: "746391520026034298",
    siriamk_show-off: "845439475454705714",
    siriamk_community_questions: "844855778677358602"
}

def retrieve_messages():
    headers = {
        "authorization": "NTE3MDE3NjA2NTk5OTk5NTA3.YTje6w.mMF84GyHIdKOSRD5vwxUmqQ67Wo"
    }
    r = requests.get(f"https://discord.com/api/v9/channels/844324992107675690/messages", headers=headers)
    message_obj = json.loads(r.text)
    for value in message_obj:
        print(value["content"], "\n")

retrieve_messages()

























