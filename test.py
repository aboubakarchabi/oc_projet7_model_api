import requests

data = {'param1':0, 'param2': 0, 'param3': 0, 'param4': 0, 'param5': 0,'param6': 0,'param7': 0,'param8': 0,'param9': 0,'param10': 0}

url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json=data)
print(r.json())
