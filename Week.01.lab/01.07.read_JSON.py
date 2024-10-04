import requests

url ="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data['bpi']['EUR']['rate_float'])

#Q: Is this a JSON or a Dict object that is outputted?
#A: The output of the JSON in this case is a Dict Object because the response.json() method in requests library reads in the input from the .json using the API and converts it to a python dict object 

