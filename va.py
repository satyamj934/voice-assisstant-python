# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:09:00 2020

@author: satyam jaiswal

"""
# importing required libraries
import os
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb
import win32com.client
import datetime
import random
from voice_assist_lib import responces, take_command, wishMe, evaluate
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
wb=wb.get(chrome_path)
# initialising speak module
speaker=win32com.client.Dispatch('SAPI.SpVoice')
vcs=speaker.GetVoices()
speaker.voice
speaker.SetVoice(vcs.Item(1))
assname='ayanhardt'

wishMe(assname,speaker,datetime)
while 1:
    cmd=''
    cmd = take_command(sr,speaker)
    cmd = cmd.lower()
    print('you : '+cmd)
    
    if 'wikipedia' in cmd:
        
        print('searching wikipedia...')
        cmd = cmd.replace('wikipedia','')
        try:
            result = wk.summary(cmd,sentences=2)
            print(result)
            speaker.speak(result)
        except:
            speaker.speak('cannot find any results')
            
            
    elif ('your name' in cmd) or ('yourself' in cmd) or ('who are you' in cmd):
        x=random.choice(responces['introduction'])
        print(x.replace('ayanhardt','Ainhardt'))
        speaker.speak(x)
        if 'introduce yourself' or 'yourself' in cmd:
            print(responces['detailed intro'])
            speaker.speak(responces['detailed intro'])
            
    elif 'how are you' in cmd or 'going on' in cmd:
        x=random.choice(responces['basic'])
        print(x)
        speaker.speak(x)
        
    
        
    elif 'the time' in cmd:
        cur_time=datetime.datetime.now().strftime('%H:%M:%S')
        speaker.speak(f'sir the time is {cur_time}')
        
    elif 'open' and 'youtube' in cmd:
        speaker.speak('opening youtube')
        wb.open('youtube.com')
        
    elif 'open' and 'google' in cmd:
        speaker.speak('opening google')
        wb.open('google.com')
        
    
        
    elif 'open microsoft edge' in cmd:
        speaker.speak('opening microsoft edge')
        path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        os.startfile(path)
    
    elif 'stop' in cmd or 'break' in cmd:
        hour = int(datetime.datetime.now().hour)
        if hour>=20:
            print('good night sir!')
            speaker.speak('good night and sweet dreams')
        else:
            speaker.speak('good bi sir!')
        break
    gs=cmd.replace(' ','')
    if gs.isalpha()==False:
        try:
            res=evaluate(gs)
            print('result :',res)
            speaker.speak('your final result is '+str(res))
        except:
            x=random.choice(responces['math_warning'])
            print(x)
            speaker.speak(x)
            
            
            