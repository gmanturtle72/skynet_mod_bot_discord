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
import numpy as np
import os
from dotenv import load_dotenv
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
model = load_model('chatbot_model.h5')
import pickle
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

load_dotenv() #loads the dotenv file
token = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

client = commands.Bot(command_prefix='!')



async def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

async def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = await clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

async def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = await bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    tag = return_list[0]['intent']
    return tag


async def get_intents(msg):
    list_ints=[]
    for i in msg:
        ints = await predict_class(i, model)
        print(ints)
        list_ints.append(ints)
    return list_ints
   
@client.command()
@commands.has_permissions(manage_guild=True)
async def config(message,arg1=None, arg2=None,):
    if arg1 ==None or arg2==None:
        embed=discord.Embed(title="configuration menu",description="configurates the bot.")
        embed.add_field(name="set filter", value="!config setfilter <0,1 or 2> ---0 no filter, 1-explictit filter 2-swaer & explicit")
        await message.channel.send(embed=embed)
    
    if arg1 =="setfilter" and int(arg2)>=0:
        with open ('config.json','r')as f:
            config=json.load(f)

        if str(message.guild.id) not in config:
            config[str(message.guild.id)] = {}
            config[str(message.guild.id)]['filter']=arg2
            with open ('config.json','w')as f:
                config=json.dump(config,f,indent=1)
        else:
            config[str(message.guild.id)]['filter']=arg2
            with open ('config.json','w')as f:
                config=json.dump(config,f,indent=1)


@client.event
async def on_ready():
    print(f"{client.user} is watching")




@client.event
async def on_message(message):
        if message.author ==client.user:
            return
        if "!config" in message.content.lower() or "!help" in message.content.lower():
            await client.process_commands(message)

        server=str(message.guild.id)
        text=message.content
        msg=text.split()
        msg.append(text)
        list_ints=await get_intents(msg)

        with open ('config.json','r')as f:
            config=json.load(f)
        if config[server]['filter']=="0":
            return

        flagmessage=False
        tags=[]
        for i in msg:
            tag=await predict_class(i,model)
            tags.append(tag)
            print(tags)
        
        if config[server]['filter']=="1":
            if "explicit" in tags:
                try:
                    await message.author.send("the server you are in has a filter enabled and your message just sent was removed as it matched a filter inplace")
                except:
                    print('l')

                await message.delete()

        if config[server]['filter']=="2":
            if "explicit" in tags or "cussing" in tags:
                try:
                    await message.author.send("the server you are in has a filter enabled and your message just sent was removed as it matched a filter inplace")
                except:
                    print('l')
                    

                await message.delete()

        

        if flagmessage==True:
            await message.delete(message)

client.run(token)