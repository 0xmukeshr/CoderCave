import tkinter
from tkinter import *
import random
import time

root=Tk()
root.title("Password generator")
root.geometry("1200x450")
color=("#000000")
white_color=("#ffffff")
yellow=("#FFFF00")
red_color=("#FF0000")
green_color=("#0FFF50")
root.configure(bg=color)
root.resizable(0,0)
default_font=("serif,sans",20)

list=""
given_char=[]
font_style=("bold serif,sans bold",30)
stop=False
start_time = 0

sample_txt=["If you want to achieve greatness stop asking for permission."
  ,"Things work out best for those who make the best of how things work out."
  ,"To live a creative life, we must lose our fear of being wrong."
  ,"If you are not willing to risk the usual you will have to settle for the ordinary."
  ,"Trust because you are willing to accept the risk, not because it's safe or certain."
  ,"All our dreams can come true if we have the courage to pursue them."
  ,"Good things come to people who wait, but better things come to those who go out and get them."
  ,"If you do what you always did, you will get what you always got."
  ,"Success is walking from failure to failure with no loss of enthusiasm."
  ,"Just when the caterpillar thought the world was ending, he turned into a butterfly."
  ,"Successful entrepreneurs are givers and not takers of positive energy."
  ,"Whenever you see a successful person you only see the public glories, never the private sacrifices to reach them."
  ,"Opportunities don't happen, you create them."
  ,"Try not to become a person of success, but rather try to become a person of value."
  ,"Great minds discuss ideas; average minds discuss events; small minds discuss people."
  ,"I have not failed. I've just found 10,000 ways that won't work."
  ,"If you don't value your time, neither will others. Stop giving away your time and talents- start charging for it."
  ,"A successful man is one who can lay a firm foundation with the bricks others have thrown at him."
  ,"No one can make you feel inferior without your consent."
  ,"The whole secret of a successful life is to find out what is one's destiny to do, and then do it."
  ,"If you're going through hell keep going."
  ,"The ones who are crazy enough to think they can change the world, are the ones that do."
  ,"Don't raise your voice, improve your argument."
  ,"What seems to us as bitter trials are often blessings in disguise."
  ,"The meaning of life is to find your gift. The purpose of life is to give it away."
  ,"The distance between insanity and genius is measured only by success."
  ,"When you stop chasing the wrong things you give the right things a chance to catch you."
  ,"Don't be afraid to give up the good to go for the great."
  ,"No masterpiece was ever created by a lazy artist."
  ,"If you can't explain it simply, you don't understand it well enough."
  ,"Blessed are those who can give without remembering and take without forgetting."
  ,"Do one thing every day that scares you."
  ,"What's the point of being alive if you don't at least try to do something remarkable."
  ,"Life is not about finding yourself. Life is about creating yourself."
  ,"Nothing in the world is more common than unsuccessful people with talent."
  ,"Knowledge is being aware of what you can do. Wisdom is knowing when not to do it."
  ,"Your problem isn't the problem. Your reaction is the problem."
  ,"You can do anything, but not everything."
  ,"Innovation distinguishes between a leader and a follower. "
  ,"Thinking should become your capital asset, no matter whatever ups and downs you come across in your life."
  ,"I find that the harder I work, the more luck I seem to have."
  ,"The starting point of all achievement is desire."
  ,"Success is the sum of small efforts, repeated day-in and day-out."
  ,"If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work."
  ,"All progress takes place outside the comfort zone."
  ,"Courage is resistance to fear, mastery of fear - not absense of fear."
  ,"Only put off until tomorrow what you are willing to die having left undone."
  ,"People often say that motivation doesn't last. Well, neither does bathing - that's why we recommend it daily."
  ,"We become what we think about most of the time, and that's the strangest secret."
  ,"The only place where success comes before work is in the dictionary."
  ,"The best reason to start an organization is to make meaning; to create a product or service to make the world a better place."
  ,"I find that when you have a real interest in life and a curious life, that sleep is not the most important thing."
  ,"It's not what you look at that matters, it's what you see."
  ,"The road to success and the road to failure are almost exactly the same."
]

def paste(event):
    return "break"

def start():
  global list,stop,start_time
  stop = False
  list=random.choice(sample_txt)
  printable_text = '\n'.join([list[i:i+90] for i in range(0, len(list),90)])
  show_text.config(text=printable_text)
  input.focus()
  input.config(width=84)
  input.delete(0,END)
  result.config(text="")
  note.config(text="Press <enter> to stop.....")
  print("=======================================================")
  starting.config(state=DISABLED)
  stoping.config(state=NORMAL)
  start_time=time.time()

def calulate():
    crrct=0
    global stop,start_time
    if not stop:
      stop= True
      given_char=input.get()
      length=min(len(list) , len(given_char))
      for i in range(length):
        if i >= len(list):
            break
        if list[i] == given_char[i]:
            crrct += 1
      end_time=time.time()
      note.config(text="")
      time_total=(end_time - start_time)
      accuracy=(crrct/len(list))*100
      wpa=(len(given_char.split())/time_total)*60
      print(f"Time taken: {time_total:.2f} seconds")
      print(f"Accuracy: {accuracy:.2f}%")
      print(f"Words per minute :{wpa:.2f}")
      starting.config(state=NORMAL)
      stoping.config(state=DISABLED)
      result.config(text= f"Time : {time_total:.2f} seconds || Accuracy : {accuracy:.2f}% || WPA : {wpa:.2f}")


show_title=Label(root,text="TYPING SPEED TEST",font=(font_style),pady=50,bg=color,fg=white_color)
show_title.place(relx=0.5,rely=0.1,anchor="center")

starting=Button(root,text="Start",width=10,pady=2,command=start,font=("Arial",12))
starting.place(relx=0.85,rely=0.2,anchor="w")
  
show_text=Label(root,text="Type the below text......",font=("Arial",12),bg=color,fg=green_color)
show_text.place(relx=0.15,rely=0.25,anchor="e")
  
show_text=Label(root,text="",font=("Inconsolata, monospace",20),anchor="center",bg=color,fg=yellow)
show_text.place(relx=0.5,rely=0.35,anchor="center")

input = Entry(root, font=("Arial", 19))
input.place(relx=0.5,rely=0.52,anchor="center")
input.bind("<Tab>", lambda e: start())
input.bind("<Return>",lambda e:calulate())
input.bind("<Control-v>",paste)
input.config(width=84)

stoping=Button(root,text="Stop",width=10,pady=2,font=("Arial",12),state=DISABLED,command=calulate)
stoping.place(relx=0.5,rely=0.65,anchor="center")

result = Label(root, text="", font=("Arial", 14),bg=color,fg=white_color)
result.place(relx=0.5,rely=0.80,anchor="center")

note = Label(root, text="", font=("Arial",10 ),bg=color,fg=red_color)
note.place(relx=0.85,rely=0.85,anchor="w")

root.mainloop()
