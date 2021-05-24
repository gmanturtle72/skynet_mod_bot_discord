#skynet mod bot v0.a

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import random
import time
import sys
import json
import subprocess 
import os 
from dotenv import load_dotenv
import numpy as np
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


load_dotenv() #loads the dotenv file
token = os.getenv("DISCORD_TOKEN")

is_learning=[False,None,None]
client = commands.Bot(command_prefix='!')

train_option={
    "regular":0,
    "cussing":1,
    "explicit":2,

}



@client.event  # event signifier
async def on_ready():# when bot boots up
    print("online")

@client.command()
async def open_learn(message,arg1='null',arg2='null'):
    global is_learning
    print(arg1)
    if arg1=='null':
        await message.channel.send(f'```{train_option}```')
        return
    if arg1=='off':
            is_learning[0]=False
            is_learning[1]=None
            is_learning[2]=None
            return is_learning
        
    else:
        if str(message.author.id)=='347155299733471233':
            
            is_learning[0]=True
            is_learning[1]=train_option[arg1]
            is_learning[2]=arg2
            return is_learning
        
        else:
            await message.channel.send("You are not approved to use this command.")
            return





@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    if is_learning[0]:
        if str(message.channel.id)==str(is_learning[2]):
            with open('intents.json','r') as f:
              intents = json.load(f)
            intents["intents"][int(is_learning[1])]['patterns'].append(message.content)
            with open("intents.json",'w') as f:
            	json.dump(intents,f,indent=1)
    await client.process_commands(message)


print("debug menu")
sel=input("1-run bot 2-train")
if sel=="1":
    client.run(token)

if sel=="2":
    while sel=="2":
        bulk=input("enter in the text to train")
        words=bulk.split()
        print("what catagory to train to?")
        catagory=input(f"select catagory {train_option}")
        

        with open('intents.json','r') as f:
            intents = json.load(f)
        for i in words:
            if i not in intents["intents"][int(catagory)]['patterns']:
                intents["intents"][int(catagory)]['patterns'].append(i)
        with open("intents.json",'w') as f:
              json.dump(intents,f,indent=1)

        sel=input("2-continue, else-exit")
