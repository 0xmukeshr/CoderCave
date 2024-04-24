import tkinter
from tkinter import *
import string
import random
import pyperclip

root=Tk()
root.title("Password generator")
root.geometry("370x350")
root.resizable(0,0)
default_font=("serif,sans",12)
fg_="#000000"
bg="#A9A9A9"
warn="#FF0000"
password=""

def passwd():
    global password
    char=""
 
    length=int(pass_len.get())   
    spcl_var=spcl.get()
    num_var=num.get()
    upr_var=upr_case.get()
    lwr_var=lwr_case.get()
 
    if num_var:
      char += string.digits
    if spcl_var:
      char += string.punctuation
    if lwr_var:
       char += string.ascii_lowercase
    if upr_var:
      char += string.ascii_uppercase
    if not length:
       print("Insufficient length")
       empty.config(text="Insufficient length",fg=warn)
    if not char:
      print("Please select one parameter")
      null.config(text="Please select any one type of chraracter",fg=warn)
      return
   
    password = ''.join(random.choice(char) for _ in range(length))
    generated.delete(0,END)
    generated.insert(0,password)
    copies.config(text="Copy_to_clipboard")
  
def copy():
   global password
   pyperclip.copy(password)
   copies.config(text=" Password has been copied to clipboard")

spcl=BooleanVar()
num=BooleanVar()
upr_case=BooleanVar()
lwr_case=BooleanVar()

p_length=Label(root,text="Enter the length of the password:",font=default_font)
p_length.grid(row=0,column=0,columnspan=5,sticky=NSEW)

pass_len=Entry(root,width=20)
pass_len.grid(row=1,column=0,columnspan=5,sticky=NSEW)

spcl_char=Checkbutton(root,text="Special characters",variable=spcl,font=default_font,fg=fg_)
spcl_char.grid(row=2,column=0,columnspan=5,sticky=NSEW)

num_char=Checkbutton(root,text="Numbers",variable=num,font=default_font)
num_char.grid(row=3,column=0,columnspan=5,sticky=NSEW)

upper_char=Checkbutton(root,text="Uppercase Alphabets",variable=upr_case,font=default_font)
upper_char.grid(row=4,column=0,columnspan=5,sticky=NSEW)

lower_char=Checkbutton(root,text="Lowercase Alphabets",variable=lwr_case,font=default_font,padx=100)
lower_char.grid(row=5,column=0,columnspan=5,sticky=NSEW)

p_length=Label(root,text="")
p_length.grid(row=6,column=0,columnspan=5,sticky=NSEW)

button_genetrate=Button(root,text="Generate Password",font=default_font,command=passwd,bg=bg)
button_genetrate.grid(row=8,column=0,columnspan=5)

empty=Label(root,text="")
empty.grid(row=9,column=0,columnspan=5,sticky=NSEW)

null=Label(root,text="")
null.grid(row=10,column=0,columnspan=5,sticky=NSEW)

generated=Entry(root,text="") 
generated.grid(row=11,column=0,columnspan=5,sticky=NSEW)

p_length=Label(root,text="")
p_length.grid(row=12,column=0,columnspan=5,sticky=NSEW)

copies=Button(root,text="Copy_to_clipboard",command=copy,pady=2,bg=bg)
copies.grid(row=13,column=0,columnspan=5)
copied = Label(root,text="",)
copied.grid(row=14,column=2,columnspan=1)

root.mainloop()
