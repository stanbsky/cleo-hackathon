import plaid
import os
from dotenv import load_dotenv
import time
import json
from datetime import date
from dateutil.relativedelta import relativedelta

def get_access_token(user, pword, ins="ins_43"):
    pub_token = client.Sandbox.public_token.create(ins, ['transactions', 'liabilities'],
                                             override_username=user,
                                             override_password=pword)['public_token']
    access_token = client.Item.public_token.exchange(pub_token)['access_token']
    return access_token

def get_transactions(token, start):
    end = (start + relativedelta(months=+1)).strftime('%Y-%m-%d')
    start = start.strftime('%Y-%m-%d')
    response = None
    while True:
        try:
            response = client.Transactions.get(token, start_date=start,
                                               end_date=end)
        except plaid.errors.ItemError:
            print("Not ready, retrying in 5")
            time.sleep(5)
        if (
            type(response) == dict and
            'transactions' in response and
            response['transactions']
        ):
            break;
        else:
            print("No transactions returned")
            time.sleep(2)
    # import pdb;pdb.set_trace()
    transactions = response['transactions']
    while len(transactions) < response['total_transactions']:
        while True:
        # while not response['transactions']:
            try:
                response = client.Transactions.get(token, start_date=start,
                                                   end_date=end,
                                                   offset=len(transactions))
            except plaid.errors.ItemError:
                print("Not ready, retrying in 5")
                time.sleep(5)
            if (
                type(response) == dict and
                'transactions' in response and
                response['transactions']
            ):
                break;
            else:
                print("No transactions returned")
                time.sleep(2)
        transactions.extend(response['transactions'])
    return transactions

# Connect to Plaid API
load_dotenv()
client = plaid.Client(client_id=os.getenv('PLAID_CLIENT_ID'),
                      secret=os.getenv('PLAID_SECRET'), environment='sandbox')

# Load user data from json
# with open('user_1.json') as json_file:
#     user = json.load(json_file)

# token = get_access_token(user['override_username'],
#                          json.dumps(user['override_password']))
token = get_access_token('custom_blank', '{}')
time.sleep(5)
print("Access token granted")

# Fetch 24 months of user transactions
start_date = date(2020,1,1)
transactions = {}
liabilities = client.Liabilities.get(token)

for i in range(12):
    trans = None
    trans = get_transactions(token, start_date)
    if trans:
        print("Got transactions for the month of " + start_date.strftime('%Y-%m-%d'))
    transactions[start_date.strftime('%Y-%m-%d')] = trans
    start_date = start_date + relativedelta(months=+1)

# time.sleep(10)
# resp = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2021-06-07')
# trans = resp['transactions']
# while len(trans) < resp['total_transactions']:
#     resp = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2021-06-07', offset=len(trans))
#     trans.extend(resp['transactions'])

# lias = client.Liabilities.get(access_token)
with open('b_transactions.json','w') as f:
    json.dump(transactions, f, indent=4)
with open('b_liabilities.json', 'w') as f:
    json.dump(liabilities, f, indent=4)
