import requests,os,json,sys
    
def send(bot_message):
       bot_token = os.environ.get("TOKEN")
       bot_chatID = os.environ.get("CHATID")
       send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&disable_web_page_preview=true&text=' + bot_message
    
       response = requests.get(send_text)
    
       return response.json()

x = requests.post('https://check-host.net/check-http?host=albalo.store:443&node=ir4.node.check-host.net&node=ir3.node.check-host.net&node=ir1.node.check-host.net',headers={'Accept': 'application/json'})
send(x.text)
