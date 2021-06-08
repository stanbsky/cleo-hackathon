import plaid
import os
import time
import json
from datetime import datetime
from pprint import pprint
client = plaid.Client(client_id=os.getenv('PLAID_CLIENT_ID'),
                      secret=os.getenv('PLAID_CLIENT_APIKEY'), environment='sandbox')

res = client.Sandbox.public_token.create("ins_43", ['transactions', 'liabilities'], override_username='custom_blank', override_password='{}')
res2 = client.Item.public_token.exchange(res['public_token'])
current_date = datetime.now()
year_select = current_date.year
month_select = current_date.month
count = 0
year_amount = 0
account_amounts = {
}
while 1:
    try:
        start = f'{year_select}-%s{month_select-1}-01' % str('0'*(2-len(str(month_select-1))))
        end = f'{year_select}-%s{month_select}-01'% str('0'*(2-len(str(month_select))))
        resp = client.Transactions.get(res2['access_token'], start_date=start, end_date=end)
        with open('resp.json', 'a') as f:
            json.dump(resp, f, indent=4)
        amount_of_transactrions = len(resp["transactions"])
        amount_month = 0
        for i in range(amount_of_transactrions-1):
            amount_month+=resp["transactions"][i]["amount"]
            if resp["transactions"][i]["account_id"] in account_amounts.keys():
                account_amounts[resp["transactions"][i]["account_id"]] = account_amounts[resp["transactions"][i]["account_id"]] + resp["transactions"][i]["amount"]
            else:
                account_amounts[resp["transactions"][i]["account_id"]] = resp["transactions"][i]["amount"]
        month_select -=1
        if month_select <=1:
            year_select -=1
            month_select = 12
            average_month = abs(year_amount) / count
            for user in account_amounts:
                print(f"The average for the user {user} is {float(account_amounts[user])/count}")
            print("average across all accounts per month for the year ", year_select, " is ",average_month )
            count = 0
            account_amounts = {}
        else:
            year_amount += amount_month
            count +=1
        if year_select == 2017:
            #only select data up to 2016
            exit()
    except plaid.errors.ItemError:
        print("Not ready")
    time.sleep(5)
