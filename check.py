import requests,os,json,sys,time

def send(bot_message):
       bot_token = os.environ.get("TOKEN")
       bot_chatID = os.environ.get("CHATID")
       send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&disable_web_page_preview=true&text=' + bot_message
    
       response = requests.get(send_text)
    
       return response.json()

domain = []
domain[0] = os.environ.get("DOMAIN")
domain[1] = os.environ.get("DOMAIN1")
domain[2] = os.environ.get("DOMAIN2")
domain[3] = os.environ.get("DOMAIN3")
domain[4] = os.environ.get("DOMAIN4")


for d in domain:
    x = requests.post('https://check-host.net/check-http?host='+d+'&node=ir4.node.check-host.net&node=ir3.node.check-host.net&node=ir1.node.check-host.net',headers={'Accept': 'application/json'})
    send(x.json()["request_id"])
    time.sleep(10)
    xx = requests.post('https://check-host.net/check-result/'+x.json()["request_id"],headers={'Accept': 'application/json'})
    send(xx.text)
    if "Connection timed out" in xx.text:
        send("ITS FUCKEDDDD⚠️⚠️⚠️⚠️⚠️⚠️")
