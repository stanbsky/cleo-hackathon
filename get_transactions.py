import plaid
import os
from dotenv import load_dotenv
import time
import json

load_dotenv()

client = plaid.Client(client_id=os.getenv('PLAID_CLIENT_ID'),
                      secret=os.getenv('PLAID_SECRET'), environment='sandbox')

with open('user_1.json') as json_file:
    user = json.load(json_file)

res = client.Sandbox.public_token.create("ins_43", ['transactions',
                                                    'liabilities'],
                                         override_username=user['override_username'],
                                         override_password=json.dumps(user['override_password']))
access_token = client.Item.public_token.exchange(res['public_token'])['access_token']
time.sleep(10)
resp = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2021-06-07')
trans = resp['transactions']
while len(trans) < resp['total_transactions']:
    resp = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2021-06-07', offset=len(trans))
    trans.extend(resp['transactions'])

lias = client.Liabilities.get(access_token)
with open('transactions.json','w') as f:
    json.dump(trans, f, indent=4)
with open('liabilities.json', 'w') as f:
    json.dump(lias, f, indent=4)
