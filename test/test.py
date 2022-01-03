import requests

resp = requests.post("https://getprediction-ifrfopxeia-du.a.run.app", files={'file': open('three.png', 'rb')})

print(resp.json())