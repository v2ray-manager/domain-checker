import requests

x = requests.post('https://check-host.net/check-http?host=albalo.store:443&node=ir4.node.check-host.net&node=ir3.node.check-host.net&node=ir1.node.check-host.net',headers={'Accept': 'application/json'})
print(x.json())
