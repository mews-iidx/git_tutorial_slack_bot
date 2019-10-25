# coding: utf-8

from slackbot.bot import respond_to     
from slackbot.bot import listen_to      
from slackbot.bot import default_reply  

@respond_to('mension')
def mention_func(message):
    message.reply('mension')

@listen_to('listen')
def listen_func(message):
    message.send('listen')    
    message.reply('are you？')

@respond_to('stamp')
def genie(message):
    message.react('female_genie')
