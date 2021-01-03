# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:31:23 2020

@author: LENOVO
"""
responces={'basic':['Somewhere between better and best','Much better now that you are with me',
                    'Overworked and underpaid','Nice and dandy like cotton candy','If I were any better i would be illegal',
                    'Happy and content, thank you','Doing well, unless you have intentions of shooting me','If I had a tail, I would wag it',
                    'I have a pulse, so I must be okay','Surviving, I guess','Under renovation'],
           'introduction':['my name is ayanhardt','i am ayanhardt','myself ayanhardt'],
           'greetings':['good to see you','nice to meet you','Dancing to the rhythm of life'],
           'detailed intro':'i am a human friendly machine designed for assisting humans',
           'math_warning':['please be more specific, i cannot understand it.','i cannot interpret what you are saying, please say again']}

def wishMe(assname,speaker,datetime):
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speaker.speak("Good Morning Sir!")
  
    elif hour>= 12 and hour<18:
        speaker.speak("Good Afternoon Sir!")   
  
    else:
        speaker.speak("Good Evening Sir!")  
  
    
    speaker.speak("I am your assistant,"+assname+'. how may i help you?')
  
    
  
def take_command(sr,speaker):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source,phrase_time_limit=15)

    try:
        print('recognizing...')
        query = r.recognize_google(audio,language='en-in')
        
    except Exception as e:
        print('say that again please...')
        speaker.speak('say that again please')
        return 'None'
    return query
    
def evaluate(arg):
    
    if arg.isalnum()==True:
        if ('add' in arg) or ('sum' in arg):
            arg=arg.replace('add','')
            if ('and' in arg):
                arg=arg.replace('and','+')
            if 'to' in arg:
                arg.replace('to','+')
                
        elif 'subtract' in arg:
            arg=arg.replace('subtract','-')
            arg=arg.replace('from','+')
    
        
                
    if ('multiply' in arg):
        if 'and' in arg:
            arg=arg.replace('multiply','')
            arg=arg.replace('and','*')
        elif 'to' in arg:
            arg=arg.replace('multiply','')
            arg=arg.replace('to','*')
        elif 'multiply' in arg:
            arg=arg.replace('multiply','*')
    if 'multiplied by' in arg:
        arg=arg.replace('multiplied by','*')
    if 'into' in arg:
        arg=arg.replace('into','*')
    if 'x' in arg:
        arg=arg.replace('x','*')
    if 'divided by' in arg:
        arg=arg.replace('divided by','')
        
    if 'divide' in arg:
        if 'by' in arg:
            arg=arg.replace('divide','')
            arg=arg.replace('by','/')
        else:
            arg=arg.replace('divide','/')
    elif 'by' in arg:
        arg=arg.replace('by','/')
        
    for i in arg:
        if i.isalpha()==True:
            arg=arg.replace(i,'')
    return eval(arg)