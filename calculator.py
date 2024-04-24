import tkinter  
from tkinter import *
root=Tk()

main_bg="#000000"
sec_bg="#FF0000"
arith_color="#FFFF00"
fg_f="#ffffff"
disp2_color="#F9F6EE"
disp1_color="#FFFFF0"

arith_font=("Consolas",30)
console_font=("Consolas",30)
disp1_font=("Consolas",25)
disp2_font=("Consolas",45)

root.title("Calculator")

root.geometry("400x550")
root.resizable(1,1)
root.configure(bg=main_bg)

calc=""
givenexp=""

disp1=Label(root, width=50,height=2,text=calc,bg=disp1_color,font=disp1_font,anchor=NE,padx=25,pady=5,fg=main_bg)   
disp1.pack(expand=True,fill="both")
disp2=Label(root, width= 50,height=1,text=givenexp,bg=disp2_color,font=disp2_font,anchor=SE,padx=25,fg=main_bg)  
disp2.pack(expand=True,fill="both")

disp=Frame(root,bg=main_bg)
disp.pack(expand=True,fill="both")
buttn=Frame(root,bg=main_bg)
buttn.pack(expand=True,fill="both") 

buttons = {
    7: (1, 1), 8: (1, 2), 9: (1, 3),4: (2, 1), 5: (2, 2), 6: (2, 3),1: (3, 1), 2: (3, 2), 3: (3, 3), '.': (4, 3)
}

arith ={
    "/":(0,3), "*":(0,4),"-":(1,4),"+":(2,4)
}

for i in range(1,5):
     buttn.rowconfigure(i,weight=1)
     buttn.columnconfigure(i,weight=1)
         
def all_button():
     for  num,grid in buttons.items():
          button=Button(buttn,text=str(num),borderwidth=0,bg=main_bg,font=console_font,fg=fg_f,command=lambda y=num :convey(y))
          button.grid(row=grid[0],column=grid[1],sticky=NSEW)

def O_button():
     for  num,grid in arith.items():
          button=Button(buttn,text="0",borderwidth=0,font=console_font,bg=main_bg,fg=fg_f,command=lambda y=num :convey(y) )
          button.grid(row=4,column=1,columnspan=2,sticky=NSEW)

def arith_button():
     for  symbol,grid in arith.items():
          button=Button(buttn,text=str(symbol),borderwidth=0,bg=main_bg,font=arith_font,fg=arith_color,command=lambda y=symbol :solution(y) ) 
          button.grid(row=grid[0],column=grid[1],sticky=NSEW)
          
def c_button():
     for  symbol,grid in arith.items():
          button=Button(buttn,text="C",bg=main_bg,borderwidth=0,font=arith_font,fg=arith_color,command=lambda y='C' :clear())
          button.grid(row=0,column=2,sticky=NSEW)
           
def equal_button():
     for  digit,grid in arith.items():
          button=Button(buttn,text="=",borderwidth=0,bg=main_bg,font=console_font,fg=arith_color,command=lambda :solve())
          button.grid(row=3,column=4,rowspan=2,sticky=NSEW)
          
def clear_button():
     for  digit,grid in arith.items():
          button=Button(buttn,text="AC",borderwidth=0,bg=main_bg,font=console_font,fg=arith_color,command=AC)
          button.grid(row=0,column=1,sticky=NSEW)
          
def solve():
	global calc
	global givenexp
	global retun
	calc +=givenexp
	disp1.config(text=calc)
	try:
		givenexp =str(eval(str(calc)))
		calc=""
	except Exception as e:
		givenexp ="Error"
	finally:
		disp2.config(text=givenexp)
retun = 1
    
def convey(y):
    global givenexp
    givenexp += str(y)
    disp2.config(text=givenexp)

def solution(y):
    global givenexp
    givenexp += str(y)
    disp2.config(text=givenexp)
    
def AC():
      global calc
      global givenexp
      givenexp=""
      calc=""
      disp1.config(text="")
      disp2.config(text="")
      
def clear():
      global calc
      global givenexp
      givenexp=givenexp[:-1]
      disp2.config(text=givenexp) 
     
arith_button()   
c_button()
equal_button()
all_button()
O_button()
clear_button()

root.mainloop()
