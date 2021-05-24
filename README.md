# skynet_mod_bot_discord
a simple moderation bot for discord that applies filters to filter out undesirable words.

# overview 
this repository is ment to provide the base package of the bot, no models are imcluded here as well as token to the bot,
in order to get the bot working got to https://discord.com/developers/applications to get a bot token

intents.json is a blank template where you can train your bot on catagories, the sample one has the lableing normal, cussing and explicit for reference. 
these tags are used throughtout main.py and modifications for the json structure and model must be taken into consideration.

.env file has been provided for a blank template, this is where your bots api token is going to be placed.

# there are 3 python scripts included in this repository

main.py - bot

train.py - create the modle based on intents.json

training_client.py - allows the user to either input raw text to be split and trained, or have the bot listen in defined channels to add to intents.json


# system of testing
below is the specs of the system used to develope this bot.
This is not a list of system requirements, this is to be used as reference or for the currious.

OS: Arch Linux X86_64
Kernel:
CPU: ryzen 5 2600
GPU: NVIDIA GeForce RTX 2070
Memory: 15.6 GB
SWAP: 8GB


# requirements
this bot has been tested in python 3.6.x and requires the apropriet libraries to be installed  through pip
note: I used Conda to set up the specific enviorment and I strongly recomend anyone who wants to clone dose the same

# Libaries:

 nltk
 pickle
 keras
 numpy
 dotenv
 discord

# bot commands: 
this can be accessed using !help:

!config 
makes changes to the server config. so far config is only used for applying filters.

to do so run !config setfilter <X>
  
  x can be 0 1 or 2. 
  0 - nofilter
  1 - explicit words
  2 - swear words and explicite words.
  
 # DISCLAIMER
  
for the bot that you will be able to invite to your server running on my system, some of the choices of words may be biased by my opinion, 
other words may be censored by accident. this is an experimental bot, only the message will be deleted. if there is a word that is censored for an unfair reason
please report so in issues. 
  
the bot invite is here: 

https://discord.com/api/oauth2/authorize?client_id=748994704686710885&permissions=8&scope=bot



