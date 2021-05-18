from tkinter import *
import string
import random




def generateFunc():
    is_char = char_val.get()
    is_number = number_val.get()
    is_special = special_val.get()
    digits_num = int(digit_val.get())

    c = ['']*digits_num
    for i in range(digits_num):
        if(is_char==1 and is_number==0 and is_special==0):
            c[i]=random.choice(string.ascii_letters)
        elif(is_char==1 and is_number==1 and is_special==0):
            c[i]=random.choice(string.ascii_letters+'0123456789')
        elif(is_char==0 and is_number==1 and is_special==1):
            c[i]=random.choice('0123456789!@#$%^&*')
        elif(is_char==1 and is_number==0 and is_special==1):
            c[i]=random.choice(string.ascii_letters+'!@#$%^&*')
        elif(is_char==1 and is_number==1 and is_special==1):
            c[i]=random.choice(string.ascii_letters+'0123456789!@#$%^&*')
        elif(is_char==0 and is_number==1 and is_special==0):
            c[i]=random.choice('0123456789')
        else:
            print("can not make password out of special only")
    pass_val.set(''.join(c))

master = Tk()

char_val = IntVar()
number_val = IntVar()
special_val = IntVar()
digit_val = StringVar()
pass_val = StringVar()

check_chars = Checkbutton(master, text="Include chars",variable=char_val).grid(row=0,column=0,sticky="news")
check_specials = Checkbutton(master, text="Include special chars",variable=special_val).grid(row=0,column=1,sticky="news")
check_numbers = Checkbutton(master, text="Include numbers",variable=number_val).grid(row=0,column=2,sticky="news")

digit_number = Entry(master,text="Number of digits",textvariable=digit_val).grid(row=1,column=1,sticky="new")


generate_button = Button(master,text="Generate Password", command=generateFunc).grid(row=2,column=1,sticky="news")

new_pass_label = Label(master,textvariable=pass_val).grid(row=3,column=1,sticky="news")

mainloop()
