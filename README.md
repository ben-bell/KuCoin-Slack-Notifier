# KuCoin-Slack-Notifier
Python script to run as a bot that will notify you when you have dealt orders on KuCoin (maybe KuCoin does this, but I couldnt work out how).

The script will send to a Slack Channel which you can setup with push notifications (cheap as)

Prerequisites

This uses Sam McHardy's unofficial Python wrapper for KuCoin API: https://github.com/sammchardy/python-kucoin

To install the wrapper:

pip install python-kucoin

Make sure you have a KuCoin account and API key generated (under the Settings menu)

Setup your slack token.  This uses a legacy token, set it up on Slack here: https://api.slack.com/custom-integrations/legacy-tokens

Setup:

1. Hardcode the API Key and Secret into the file (not recommended but easier - however remember KuCoin API has no read-only version)

2. Hardcode your slack token

or 

1. Wait for the prompts and enter API Key and Secret, and Slack token


Running:

python Slack-Notifier.py

Notes:

You may get some errors, this bot will just ignore and try again.

If you expect more than 12 deals during the check interval this will not work as KuCoin will paginate results and you'll get only the first 12


Donations:

If this helps you, feel free to send a coin :P

ETH/ETC: 0x5986591391B5Dd78c7170e6e16A17aEd05b50B1d

Waves: 3PL6V1dcNgajfEx5YbMAZJ8xKkVHJkm9Uba

LTC: LVJ4EFyPRPUMZEt4ird88CrtrRtDoK2vKP

BTC: 1MRKyWeUV15VguoruyPVZpveTTT9yKZjMo