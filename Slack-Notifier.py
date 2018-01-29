#!/usr/bin/env python

from kucoin.client import Client
from datetime import datetime
import json
import sys
import csv
import time
from slackclient import SlackClient
import traceback

# enter your apiKey and apiSecret
# remember that KuCoin has read/write permissions, you cannot have a read only API!
apiKey = ""
apiSecret = ""

# enter your Slack token here - less risk, someone could spam you or read your messages
slack_token = ""

# bot details
botname = "KuCoin notifier"
channelname = "#general"

# format of date output
dateformat = '%Y-%m-%d %H:%M:%S'

# check interval in seconds
checkInterval = 10

# how many times to retry on each callable
maxretries = 3

# this the time to pickup deals from, you could override this to some other time
# you will be limited to a set number of deals, if you did too many it would probably page and this script doesnt support that
lastDealsCheck = round(time.time()*1000)


# prompt user if not hardcoded here
if (apiKey == ""):
	apiKey = input("Please enter your API Key: ")

if (apiSecret == ""):
	apiSecret = input("Please enter your API Secret: ")

if (slack_token == ""):
	slack_token = input("Please enter your Slack Legacy Token: ")	

client = Client(apiKey, apiSecret)
sc = SlackClient(slack_token)


while True:
	try:
	
		print("Starting loop at {0}".format(time.strftime(dateformat)))
			
		#get my dealt orders
		retry = 0
		while (retry < maxretries):
			try:
				dealtOrders = client.get_dealt_orders(since=lastDealsCheck)
				data = dealtOrders['datas']
				
				break
			except:
				retry = retry + 1
				# quit if we hit the limit
				if (retry >= maxretries):
					raise
				else:
					# have a rest for 2 seconds
					time.sleep(2)
		
		print("Found {0} new deals".format(dealtOrders['total']))
		
		# reset the deal time now
		lastDealsCheck = round(time.time()*1000)
					
		if (data):
			
			for thisOrder in data:

				msg = "{0} - {1}-{2} {3} order completed: {4} VOL at {5}".format(datetime.fromtimestamp(thisOrder['createdAt']/1000).strftime('%Y-%m-%d %H:%M:%S'), thisOrder['coinType'],thisOrder['coinTypePair'], thisOrder['direction'], thisOrder['amount'], thisOrder['dealPrice'])

				sc.api_call(
				  "chat.postMessage",
				  channel=channelname,
				  username=botname,
				  text=msg
				)
				
				print(msg)
			
		time.sleep(int(checkInterval))

	except:
		print("Unexpected error:", traceback.format_exc())
		time.sleep(int(checkInterval))
		#raise
		#continue