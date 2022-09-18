
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 21:23:30 2022

@author: Aavish and Arnav
"""

import nltk
import random
import string 
import wikipedia
from termcolor import colored
import pyttsx3
import tkinter 
from tkinter import *
import ctypes as ct
import warnings
warnings.filterwarnings('ignore')


#definr window
root=tkinter.Tk()
root.title("WIKI-BOT")
root.geometry("1300x700")
root.configure(bg='grey5')
root.resizable(0,0)
root.update()
set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
get_parent = ct.windll.user32.GetParent
hwnd = get_parent(root.winfo_id())
value = 2
value = ct.c_int(value)
set_window_attribute(hwnd, 20, ct.byref(value), ct.sizeof(value))

def description():
    new_window=Toplevel(frame_1, bg='grey7')
    new_window.title("Instructions!!")
    new_window.geometry("500x710+1000+150")
    
    #Changing title color
    new_window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(new_window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), ct.sizeof(value))
    
    Label(new_window, fg='cyan',bg='grey7',text =" ").pack()
    Label(new_window, fg='cyan',bg='grey7',text ="INSTRUCTIONS",font=(10)).pack()
    Label(new_window, fg='cyan',bg='grey7',text =" ").pack()
    Label(new_window, fg='cyan',bg='grey7',text ="Enter the topic you want to ask questions about.").pack()
    Label(new_window, fg='cyan',bg='grey7',text ="You can ask simple questions based on topic you’ve entered in the \n entry bar located at the bottom.").pack()
    Label(new_window, fg='cyan',bg='grey7',text ="Use the following commands to access all functionalities by typing \n it at the entry bar located at the bottom :-").pack()
    Label(new_window, fg='cyan',bg='grey7',text ="%title - It is a title generator which suggests you with topics based \n on the topic title you’ve entered previously.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%page - It extracts text from the wikipedia page and prints it",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%read - It is a text to speech engine which reads out the summary to \n the user in English.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%readn - It is similar to read but reads out ‘n’ sentences. Where n \n is an integer. ie, read2 command reads two sentences.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%hindi - It gives a brief summary of the entered topic in Hindi.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%kannada - It gives a brief summary of the entered topic in Kannada.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%tamil - It gives a brief summary of the entered topic in Tamil.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%telugu - It gives a brief summary of the entered topic in Telugu.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%malayalam - It gives a brief summary of the entered topic in Malayalam.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%link - It generates a wikipedia link for the topic entered.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%thanks - To move to a new topic.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)
    Label(new_window, fg='cyan',bg='grey7',text ="%bye - To exit.",relief='sunken').pack(ipadx=5,ipady=5,pady=5)


#define frames

frame_1=tkinter.Frame(root, bg='grey10')
frame_2=tkinter.LabelFrame(root, bg='grey10',relief='sunken',borderwidth=3)
frame_3=tkinter.Frame(root,bg='grey10')
iframe=tkinter.Text(frame_3,width=20,height=2,bg='grey10',fg='white',font=("Lucida",10,"bold"),padx=5,pady=5,borderwidth=3)


#pack frames

frame_1.pack(fill='x',expand=True,padx='5',pady='5',ipady='10',anchor='n')
frame_2.pack(side='right',fill=BOTH,padx='5',pady='5',expand=True,ipady='350')
frame_3.pack(side='left',fill=BOTH,padx='5',pady='5',expand=True,ipady='350')
iframe.place(x=10,y=10,height=530,width=600)
iframe.configure(cursor="arrow",state=DISABLED)
iframe.tag_config('start',foreground='cyan')
iframe.tag_config('li',foreground='blue')

scrollf3=Scrollbar(frame_3,bg='grey5')
scrollf3.place(y=10,relheight=0.884,relx=0.965)
scrollf3.configure(command=iframe.yview)



btn = Button(frame_1, text ="Instructions",bg='grey30',fg='black',activebackground='grey30',borderwidth=6, command = description)
btn.place(x=1140,y=20,width=130,height=42)

def enter1():
    wdat=entryf1.get()
    wikipedia.set_lang("en")
    tdat=str(wikipedia.summary(wdat,sentences=400))
    label2=tkinter.Label(frame_2,bg='grey10',fg='yellow',text=str.upper(wdat),font=('Algerian',16,"bold"))
    label21.configure(text=tdat)
    label2.place(bordermode='inside',relwidth=1,rely=0.06)
    return wdat,tdat

def title():
    wdat=entryf1.get()
    wikipedia.set_lang("en")
    search=wikipedia.search(wdat)
    iframe.configure(state=NORMAL)
    iframe.insert(END,"WIKI-BOT: \n",'start')
    iframe.configure(cursor="arrow",state=DISABLED)
    for titl in search:
        iframe.configure(state=NORMAL)
        iframe.insert(END,">>"+titl+"\n")
        iframe.configure(cursor="arrow",state=DISABLED)
    iframe.configure(state=NORMAL)
    iframe.insert(END,"     \n")
    iframe.configure(cursor="arrow",state=DISABLED)
    iframe.see("end")
    
    
btn1=Button(frame_1, text ="Generate Title",bg='grey30',fg='black',activebackground='grey30',borderwidth=6, command = title)
btn1.place(x=980,y=20,width=140,height=43)

label21=tkinter.Label(frame_2,bg='grey10',fg='white',wraplength=500,text=' ')
label21.place(bordermode='inside',relx=0.1,rely=0.15,relwidth=0.81)

#frame1

labelf1=tkinter.Label(frame_1,text="Enter the topic you want to search about:                                                                                                                             ",bg='grey10',fg='white',padx=5,pady=5)
labelf1.grid(row=0,column=0)

entryf1=tkinter.Entry(frame_1,bg='grey98',bd='2',width=100,borderwidth=4)
entryf1.grid(row=1,column=0,padx=10)

buttonf1=tkinter.Button(frame_1,text="Enter",bg='grey30',fg='black',activebackground='grey30',padx=10,borderwidth=4,width=6,command=enter1)
buttonf1.grid(row=1,column=1)


def chat1():
    
    wdat=entryf1.get()
    
    wikipedia.set_lang("en")
    f=str(wikipedia.summary(wdat,sentences=400))
    tdat=f.lower()
    
    def readf(x):
    
        # init function to get an engine instance for the speech synthesis 
        engine = pyttsx3.init()
        # say method on the engine that passing input text to be spoken
        engine.say(x)
        # run and wait method, it processes the voice commands. 
        engine.runAndWait()
        
        iframe.configure(state=NORMAL)
        iframe.insert(END,"WIKI-BOT: Reading done...")
        iframe.configure(cursor="arrow",state=DISABLED)
        iframe.see("end")
        return ' '

    #nltk.download('punkt')                # first-time use only
    #nltk.download('wordnet')              # first-time use only
    sent_tokens = nltk.sent_tokenize(tdat)        # converts to list of sentences 
    word_tokens = nltk.word_tokenize(tdat)        # converts to list of words

    lemmer = nltk.stem.WordNetLemmatizer()
    def LemTokens(tokens):                #Lemmatizing
        return [lemmer.lemmatize(token) for token in tokens]
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    def LemNormalize(text):               #Tokenizing
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

    def greeting(sentence):                #Greeting function
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)
            
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    def response(user_response):              #User-Response function
        wiki_response=''
        sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
    
        if(user_response=="%read"):
            return readf(f)
        elif user_response == "%link": 
            lin=wikipedia.page(wdat).url
            iframe.configure(state=NORMAL)
            iframe.insert(END, lin,'li')
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
        elif user_response=="%page":
            pag=wikipedia.page(wdat).content
            iframe.configure(state=NORMAL)
            iframe.insert(END, pag)
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
            iframe.see("end")
        elif user_response[5] in ['0','1','2','3','4','5','6','7','8','9']:
            st=str(wikipedia.summary(wdat,sentences=int(user_response[5])))
            return readf(st)
        elif user_response== "%title":
            wikipedia.set_lang("en")
            search=wikipedia.page(wdat).links
            for titl in search:
                iframe.configure(state=NORMAL)
                iframe.insert(END,">"+titl+"\n")
                iframe.configure(cursor="arrow",state=DISABLED)
            iframe.configure(state=NORMAL)
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
            iframe.see("end")
        elif user_response == "%hindi":   
            wikipedia.set_lang("hi")
            HI=wikipedia.summary(wdat)
            iframe.configure(state=NORMAL)
            iframe.insert(END,HI)
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
            iframe.see("end")
        elif user_response == "%kannada":    
            wikipedia.set_lang("kn")
            KN=wikipedia.summary(wdat)
            iframe.configure(state=NORMAL)
            iframe.insert(END,KN)
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
            iframe.see("end")
        elif user_response == "%tamil":   
            wikipedia.set_lang("ta")
            TA=wikipedia.summary(wdat)
            iframe.configure(state=NORMAL)
            iframe.insert(END,TA)
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
            iframe.see("end")
        elif user_response == "%telugu":    
            wikipedia.set_lang("te")
            TE=wikipedia.summary(wdat)
            iframe.configure(state=NORMAL)
            iframe.insert(END,TE)
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
            iframe.see("end")
        elif user_response == "%malayalam":   
            wikipedia.set_lang("ml")
            ML=wikipedia.summary(wdat)
            iframe.configure(state=NORMAL)
            iframe.insert(END,ML)
            iframe.insert(END,"     \n")
            iframe.configure(cursor="arrow",state=DISABLED)
            iframe.see("end")
        elif(req_tfidf==0):
            wiki_response=wiki_response+"I am sorry! I don't understand you"
            return wiki_response.capitalize()
        else:
            wiki_response = wiki_response+sent_tokens[idx]
            return wiki_response.capitalize()
        return user_response
    flag=True
    while(flag==True):
        user_response = entryf3.get()
        entryf3.delete(0,END)
        user_response=user_response.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                entryf1.delete(0,END)
                iframe.configure(state=NORMAL)
                iframe.insert(END,"WIKI-BOT: You are welcome..\n")
                iframe.configure(cursor="arrow",state=DISABLED)
                iframe.see("end")
            else:
                if(greeting(user_response)!=None):
                    iframe.configure(state=NORMAL)
                    iframe.insert(END,user_response.capitalize()+'\n','start')
                    iframe.configure(cursor="arrow",state=DISABLED)
                    iframe.configure(state=NORMAL)
                    iframe.insert(END,"WIKI-BOT: "+greeting(user_response)+'\n')
                    iframe.configure(cursor="arrow",state=DISABLED)
                    iframe.see("end")
                else:
                    iframe.configure(state=NORMAL)
                    iframe.insert(END,user_response.capitalize()+'\n','start')
                    iframe.configure(cursor="arrow",state=DISABLED)
                    iframe.configure(state=NORMAL)
                    iframe.insert(END,"WIKI-BOT: "+response(user_response)+'\n')
                    iframe.configure(cursor="arrow",state=DISABLED)
                    sent_tokens.remove(user_response)
                    iframe.see("end")
        else:
            flag=False
            def destroy():
                root.destroy()
            destroy()
           
            
#frame3

buttonf3=tkinter.Button(frame_3,text="Enter",bg='grey30',fg='black',activebackground='grey30',padx=15,borderwidth=7,command=chat1)
buttonf3.place(x=510,y=555,height=37,width=114)

entryf3=tkinter.Entry(frame_3,bg='grey98',bd='2',width=60,borderwidth=4)
entryf3.place(x=15,y=555,height=37,width=480)


entryf1.delete(0,END)

root.mainloop()
