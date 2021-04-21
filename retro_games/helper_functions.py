# IGDB api requests
import requests
import json

from igdb.wrapper import IGDBWrapper

url = 'https://id.twitch.tv/oauth2/token'
client_id = 'bbi2z3lufqh6td2cfi5tkorsc4h1se'
client_secret = '2drg2w2smx3693nmxnbjbyqxvyxy1h'
data = {
	'client_id': client_id, 
	'client_secret': client_secret, 
	'grant_type': 'client_credentials'
}
response = requests.post(url, data=data).json()

def api_call(endpoint, fields_string):
	wrapper = IGDBWrapper(client_id, response['access_token'])
	res = wrapper.api_request(endpoint, fields_string)
	raw_json = res.decode('utf8').replace("'", '"')
	return json.loads(raw_json)