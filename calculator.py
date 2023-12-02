from tkinter import*
import math

root=Tk()
root.title("Calculator")
root.geometry("350x550")
root.iconbitmap("Metro.ico")
# root.iconphoto(False, PhotoImage(file='Metro.ico'))
output= LabelFrame(root,borderwidth=0)
output.pack( fill="both")
entry_font = ("Roboto", 14, "bold")
entry_font2 = ("Roboto", 20, "bold")
entry_operation=Entry(output, bg="#18181a", borderwidth=0, fg="#fff", font=entry_font,justify=RIGHT )
entry_operation.pack(expand=1, fill="both", ipady=15)
resulet_label=Label(output, text="0", anchor=E , bg="#18181a", fg="#fff", font=entry_font2)
resulet_label.pack(expand=1, fill="both", ipady=15)
btns_container= LabelFrame(root, borderwidth=0)
btns_container.pack(expand=1, fill="both")
btn_color="#d4cfe9"
btn_color2="#b5bfec"
btn_font = ("Lobster", 15, "bold")
btn_font2 = ("Lobster", 17, )
operation=""
resulet="0"
RADIAN = True
#creat entry_operation btns
def creat_spyshel_btns(tex,color, r,c):
    btn=Button(btns_container, text=tex, borderwidth=0, bg=color, font=btn_font2,width=10)
    btn.grid(row=r,column=c, sticky=NSEW , padx=1,pady=1)
    btn.bind("<Enter>", lambda event, x=btn: hover(x))
    btn.bind("<Leave>", lambda event, x=btn: leave(x, btn_color2))
    return btn
def click(num, oper):
    global operation
    entry_operation.insert(END,num)    
    operation+=oper
    if num=="ANS":
        print(oper)
def show_resulet():
    global operation,resulet 
    entry_operation.delete(0,END)
    resulet=str(eval(operation))
    resulet_label["text"]=resulet
    operation=""
def clear():
    global operation
    entry_operation.delete(0,END)
    resulet_label["text"]="0"
    operation=""
def delet():
    global operation
    if len(operation) > 0:
        operation=operation.removesuffix(operation[-1])
        entry_operation.delete(0,END)
        entry_operation.insert(0,operation)
def rad():
    global RADIAN
    RADIAN=True
    deg_btn.config(bg=btn_color2,fg="#222")
    rad_btn.config(bg="#ff8630",fg="#fff")
def deg():
    global RADIAN
    RADIAN=False
    rad_btn.config(bg=btn_color,fg="#222")
    deg_btn.config(bg="#ff8630",fg="#fff")

def trigo(callback, angel) :
    # global RADIAN
    if not RADIAN :
        angel = angel * (math.pi / 180)
    return callback(angel)

def inv_trigo(callback, value) :
    angel = callback(value)
    if not RADIAN :
        angel = angel * (180 / math.pi)
    return angel
rad_btn=creat_spyshel_btns("Rad",btn_color2, 0,0)
rad_btn.config(bg="#ff8630",fg="#fff",command=rad)
deg_btn=creat_spyshel_btns("Deg",btn_color2, 0,1)

deg_btn.config(command=deg)
ans_btn=creat_spyshel_btns("ANS",btn_color2, 6,0)
ans_btn.grid(rowspan=2)
ans_btn.config(command=lambda:click("ANS",resulet))
delet_btn=creat_spyshel_btns("⌫",btn_color2, 3,2)
delet_btn.config(command=delet)
clear_btn=creat_spyshel_btns("C",btn_color2, 3,1)
clear_btn.config(command=clear)
equal_btn=creat_spyshel_btns("=",btn_color2, 7,3)
equal_btn.config(command=show_resulet)
equal_btn.grid(columnspan=2)
#(math.factorial,"x!"), ("**","x²")
dott_btn=creat_spyshel_btns(".",btn_color, 7,2)
dott_btn.config(command=lambda : click(".","."))
ope_spe_list= [ {"name":"√x", "symbol":"√(","formula":"math.sqrt("},
{"name":"Xy", "symbol":"^(","formula":"**"},
{"name":"exp", "symbol":"exp(","formula":"math.exp("},
{"name":"cos", "symbol":"cos(","formula":"trigo(math.cos,"},
{"name":"sin", "symbol":"sin(","formula":"trigo(math.sin,"},
{"name":"tan", "symbol":"tan(","formula":"trigo(math.tan,"},
{"name":"ln", "symbol":"In(","formula":"math.log("},
{"name":"log", "symbol":"log(","formula":"math.log10("},
{"name":"acos", "symbol":"acos(","formula":"inv_trigo(math.acos,"},
{"name":"asin", "symbol":"asin(","formula":"inv_trigo(math.asin,"},
{"name":"atan", "symbol":"atan(","formula":"inv_trigo(math.atan,"},
{"name":"π", "symbol":"π","formula":"math.pi"},
{"name":"÷", "symbol":"÷","formula":"/"},
{"name":"x²", "symbol":"^(2)","formula":"**2"},
{"name":"x", "symbol":"x","formula":"*"},
{"name":"e", "symbol":"e","formula":"math.e"},

]
ope_list= ["(",")", "%", "-", "+"]
grid_ope_list=[(0,3),(0,4),(3,3),(5,4),(6,4)]
grid_ope_list2=[(0,2),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0), (2,1), (2,2),(2,3),(2,4),(3,0),(3,4),(4,0),(4,4),(5,0) ]
for i,oper in enumerate(ope_spe_list):
    btn=Button(btns_container, text=oper["name"], borderwidth=0, bg=btn_color2, font=btn_font2,width=10 , command=lambda y=oper["formula"], x=oper["symbol"], : click(x,y))
    btn.grid(row=grid_ope_list2[i][0],column=grid_ope_list2[i][1],sticky=NSEW , padx=1,pady=1)
    btn.bind("<Enter>", lambda event, x=btn: hover(x))
    btn.bind("<Leave>", lambda event, x=btn: leave(x, btn_color2))
    
for i,oper in enumerate(ope_list):
    btn=Button(btns_container, text=oper, borderwidth=0, bg=btn_color2, font=btn_font2,width=10 ,command=lambda y=oper, x=oper, : click(x,y))
    btn.grid(row=grid_ope_list[i][0],column=grid_ope_list[i][1],sticky=NSEW , padx=1,pady=1)
    btn.bind("<Enter>", lambda event, x=btn: hover(x))
    btn.bind("<Leave>", lambda event, x=btn: leave(x, btn_color2))
#creat numbers
grid_num_list=[(7,1),(6,1),(6,2),(6,3),(5,1),(5,2),(5,3),(4,1),(4,2),(4,3)]
def hover(btn):
    btn.config(bg="#eee")
    
def leave(btn, color):
    if btn["fg"]=="#fff" :
       btn.config(bg="#ff8630")
       return
    btn.config(bg=color)
    
for num in range(0, 10):
    btn=Button(btns_container, text=str(num), borderwidth=0, bg=btn_color, font=btn_font,width=10 , command=lambda x=str(num), y=str(num): click(x,y))
    btn.grid(row=grid_num_list[num][0],column=grid_num_list[num][1],sticky=NSEW , padx=1,pady=1)
    btn.bind("<Enter>", lambda event, x=btn: hover(x))
    btn.bind("<Leave>", lambda event, x=btn: leave(x,btn_color))
for x in range(0,5):
    btns_container.columnconfigure(x, weight=1)
for x in range(0,8):
    btns_container.rowconfigure(x, weight=1)

root.mainloop()
