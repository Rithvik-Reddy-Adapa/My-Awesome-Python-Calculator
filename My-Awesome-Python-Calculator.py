#!/usr/bin/env python3
'''
    My Awesome Python Calculator - A simple scientific calculator using python3.
    Copyright (C) Year: 2020,  Author: Rithvik Reddy Adapa

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

'''
My Awesome Python Calculator
Modified on 05/11/2021
'''
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
from math import *
from math import degrees as deg
from math import radians as rad
from math import factorial as fact
from cmath import polar,rect
import numpy as np
from numpy import array as A

def input_to_input_var(a):
    pos=text.index(tk.INSERT)
    input_var.set(input_var.get()[0:pos]+a+input_var.get()[pos:len(input_var.get())])
    text.icursor(pos+len(a))
    compute_result()

def compute_result():
    if input_var.get()=='':
        result_var.set('------')
    else:
        try:
            result_var.set(str(eval(input_var.get())))
        except:
            result_var.set('error')

def clear_input():
    input_var.set('')
    result_var.set('------')

def save_and_clear_input():
    global Ans
    try: Ans=A(eval(input_var.get()))
    except: pass
    clear_input()

def backspace():
    pos=text.index(tk.INSERT)
    if pos!=0:
        input_var.set(input_var.get()[0:pos-1]+input_var.get()[pos:len(input_var.get())])
    text.icursor(pos-1)
    compute_result()

def resize(event):
    if event==1:
        for i in window.grid_slaves():
            i.config(font=[font_face_var.get(), size_var.get(), 'bold'])
            text.focus_set()
    elif event.keysym=="Return":
        for i in window.grid_slaves():
            i.config(font=[font_face_var.get(), size_var.get(), 'bold'])
            text.focus_set()

def function_select(event):
    global function_list
    if event.keysym=="Return" and function_input_var.get()!='' and (function_input_var.get() in function_list):
        pos=text.index(tk.INSERT)
        input_var.set(input_var.get()[0:pos]+function_input_var.get()+'()'+input_var.get()[pos:len(input_var.get())])
        text.icursor(pos+len(function_input_var.get())+1)
        compute_result()
        text.focus_set()
    elif event.num==1 and function_input_var.get()!='' and (function_input_var.get() in function_list):
        pos=text.index(tk.INSERT)
        input_var.set(input_var.get()[0:pos]+function_input_var.get()+'()'+input_var.get()[pos:len(input_var.get())])
        text.icursor(pos+len(function_input_var.get())+1)
        compute_result()
        text.focus_set()

def sin(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.sin(x)
        else:
            return math.sin(math.radians(x))
    except:
        return cmath.sin(x)

def asin(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.asin(x)
        else:
            return math.degrees(math.asin(x))
    except:
        return cmath.asin(x)

def cos(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.cos(x)
        else:
            return math.cos(math.radians(x))
    except:
        return cmath.cos(x)

def acos(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.acos(x)
        else:
            return math.degrees(math.acos(x))
    except:
        return cmath.acos(x)

def tan(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.tan(x)
        else:
            return math.tan(math.radians(x))
    except:
        return cmath.tan(x)

def atan(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.atan(x)
        else:
            return math.degrees(math.atan(x))
    except:
        return cmath.atan(x)

def atan2(y,x):
    import math
    if deg_rad_var.get()==1:
        return math.atan2(y,x)
    else:
        return math.degrees(math.atan2(y,x))

def cosec(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return 1/math.sin(x)
        else:
            return 1/math.sin(math.radians(x))
    except:
        return 1/cmath.sin(x)

def acosec(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.asin(1/x)
        else:
            return math.degrees(math.asin(1/x))
    except:
        return cmath.asin(1/x)

def sec(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return 1/math.cos(x)
        else:
            return 1/math.cos(math.radians(x))
    except:
        return 1/cmath.cos(x)

def asec(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.acos(1/x)
        else:
            return math.degrees(math.acos(1/x))
    except:
        return cmath.acos(1/x)

def cot(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return 1/math.tan(x)
        else:
            return 1/math.tan(math.radians(x))
    except:
        return 1/cmath.tan(x)

def acot(x):
    import math,cmath
    try:
        if deg_rad_var.get()==1:
            return math.atan(1/x)
        else:
            return math.degrees(math.atan(1/x))
    except:
        return cmath.atan(1/x)

def log(x,y=None):
    import math,cmath
    try:
        if y==None:
            return math.log(x)
        else:
            return math.log(x,y)
    except:
        if y==None:
            return cmath.log(x)
        else:
            return cmath.log(x,y)

def log10(x):
    import math,cmath
    try:
        return math.log10(x)
    except:
        return cmath.log10(x)

def deg_rad_function():
    deg_rad_var.set(int(not deg_rad_var.get()))
    if deg_rad_var.get()==0:
        deg_rad_button.config(text='deg',bg='hot pink')
    else:
        deg_rad_button.config(text='rad',bg='turquoise1')
    compute_result()
    text.focus_set()

def s_l_e(matrix):
        '''
        Consider a system of linear equations
        ax + by = c     and      px + qy = r
                  where,    x and y are variables
                                a , b , p and q are coefficients
                                c and r are constants
        input matrix should be
        np.array([
        [a , b , c]
        [p , q , r]
        ])

        output matrix will be
        np.array([x , y])
        '''
        matrix=np.array(matrix)
        if len(matrix.shape)!=2 or matrix.shape[0]!=matrix.shape[1]-1:
                #raise ValueError('Input matrix is not in proper shape')
                return 'Improper matrix shape'
        return np.linalg.inv(matrix[:,:-1])@matrix[:,-1]

def _help_():
    help_window=tk.Tk()
    help_window.title('HELP')

    text='''
Usage:
    # Just type in the Input area and you will get the results instantly in the Output area, no need to press 'Enter' or click on '==' button.
    # 'Tab' key focuses only on Input area, Output area, Degrees \u27f7 Radians toggle button, Function drop down and Spin box to vary size of the user interface (UI).
    # Clicking on 'Enter' when in Output area changes the focus from Output area to Input area.
    # Degrees \u27f7 Radians toggle button works for all trignometric functions on all real numbers, it does not work for trignometric operations on imaginary numbers (Only Radians is used for trignometric operations on imaginary numbers).
    # Imaginary numbers can be typed as '1+1j' (Python Syntax)
    # Double clicking on the selected function in the function drop down inputs the function into Input area.
    # Pressing 'Control + Backspace' or clicking \u239a clears Input area and does not store Output the last stored Output remains.
    # Pressing 'Shift + Backspace' or clicking \u21ba clears Input area and saves the Output into 'Ans' variable.
    # 'Ans' variable saves last saved variable, it is initiated with 'None'.
    # Pressing 'Backspace' or clicking \u232b clears one character from the current cursor position.
    # Number 25 in the Spinbox is the size of text, you can change size by typing your custom value or by clicking on up and down arrow buttons to increase and decrease size respectively.
    # Power of a number can be calculated by typing '8**7' (Python Syntax) or 'pow()' function as 'pow(8,7)'.
    # <, \u2264, >, \u2265, == and \u2260 can be used to check inequalities. They can be used by clicking respective buttons or by pressing '<', '<=', '>', '>=', '==' and '!=' respectively. This outputs boolean value 'True' or 'False'.
    # There are no seperate trignometric functions for degrees and radians just toggle between degrees and radians according to your requirement.
    # 'A((1,2,3))' creates an array '[1,2,3]'.
    # '(1,2,3)' creates a tuple '(1,2,3)'.
    # '[1,2,3]' creates a list '[1,2,3]'.
    # '1,2,3' creates a tuple '(1,2,3)'.
    # Typing 'pi' or clicking \u03c0 inputs the value of \u03c0 i.e. 3.141592653589793
    # Typing 'e' or clicking e inputs the value of e i.e. 2.718281828459045
    # Typing 'tau' or clicking \u03c4 inputs the value of \u03c4 i.e. 6.283185307179586
    # Typing 'inf' or clicking \u221e inputs infinity(\u221e)

s_l_e():
    # This function is meant to solve system of linear equations.
    #        Consider a system of linear equations
               ax + by = c     and      px + qy = r
                       where,    x and y are variables
                                     a , b , p and q are coefficients
                                     c and r are constants
               input matrix should be
               np.array([
               [a , b , c]
               [p , q , r]
               ])

               output matrix will be
               np.array([x , y])

Examples:
    # Input \u2b62 sin(90) \u21d2 Output \u2b62 1.0      (degrees)
    # Input \u2b62 sin(pi) \u21d2 Output \u2b62 1.2246467991473532e-16      (radians)
    # Input \u2b62 sin(1+1j) \u21d2 Output \u2b62 (1.2984575814159773+0.6349639147847361j)      (Only in radians for imaginary numbers)
    # Input \u2b62 asin(90) \u21d2 Output \u2b62 (1.5707963267948966+5.192925985263684j)      (Only in radians for imaginary numbers)
    # Input \u2b62 acos(0.5) \u21d2 Output \u2b62 1.0471975511965979       (radians)
    # Input \u2b62 acos(0.5) \u21d2 Output \u2b62 60.00000000000001       (degrees)
    # Input \u2b62 atan(90) \u21d2 Output \u2b62 89.36340642403653      (degrees)
    # Input \u2b62 atan(90) \u21d2 Output \u2b62 1.5596856728972892      (radians)
    # Input \u2b62 atan(inf) \u21d2 Output \u2b62 90.0      (degrees)
    # Input \u2b62 acot(inf) \u21d2 Output \u2b62 0.0      (radians)
    # Input \u2b62 asin(inf) \u21d2 Output \u2b62 error
    # Input \u2b62 log(10,2) \u21d2 Output \u2b62 3.3219280948873626
    # Input \u2b62 log10(2) \u21d2 Output \u2b62 0.3010299956639812
    # Input \u2b62 log(2,10) \u21d2 Output \u2b62 0.3010299956639812
    # Input \u2b62 log(e) \u21d2 Output \u2b62 1.0
    # Input \u2b62 log10(10) \u21d2 Output \u2b62 1.0
    # Input \u2b62 log(10,10) \u21d2 Output \u2b62 1.0
    # Input \u2b62 10**3 \u21d2 Output \u2b62 1000
    # Input \u2b62 10.0**3 \u21d2 Output \u2b62 1000.0
    # Input \u2b62 pow(10,3) \u21d2 Output \u2b62 1000
    # Input \u2b62 1<2 \u21d2 Output \u2b62 True
    # Input \u2b62 1>=2 \u21d2 Output \u2b62 False
    # Input \u2b62 1!=2 \u21d2 Output \u2b62 True
    # Input \u2b62 1,2<1 \u21d2 Output \u2b62 (1,False)
    # Input \u2b62 (1,2<1) \u21d2 Output \u2b62 (1,False)
    # Input \u2b62 (1,2)<1 \u21d2 Output \u2b62 error
    # Input \u2b62 A((1,2))<1 \u21d2 Output \u2b62 [False False]
    # Input \u2b62 A((1,2))+1 \u21d2 Output \u2b62 [2 3]
    # Input \u2b62 A((sin(9)*6,34.89,90))**5 \u21d2 Output \u2b62 [7.28481385e-01 5.17017028e+07 5.90490000e+09]
    # Input \u2b62 s_l_e(((90,78,1,89),(78,67,90))) \u21d2 Output \u2b62 Improper matrix shape
    # Input \u2b62 s_l_e(((90,78,1,89),(78,34,67,90),(1,2,3,4))) \u21d2 Output \u2b62 [0.18753168 0.91618094 0.66003548]
    # Input \u2b62 s_l_e(((90,78,1,89),(78,34,67,90),(1,2,3,4)))/8 \u21d2 Output \u2b62 [0.02344146 0.11452262 0.08250443]
    # Input \u2b62 None \u21d2 Output \u2b62 None
    # Input \u2b62 12%8 \u21d2 Output \u2b62 4

END
ENJOY USING THE CALCULATOR \u263a
            '''
    scrollbar_y=tk.Scrollbar(help_window,bg="White",activebackground="Grey")
    scrollbar_y.pack(side=tk.RIGHT,fill=tk.Y)
    scrollbar_x=tk.Scrollbar(help_window,orient=tk.HORIZONTAL,bg="White",activebackground="Grey")
    scrollbar_x.pack(side=tk.BOTTOM,fill=tk.X)
    help_text=tk.Text(help_window,font=font,fg="Black",background='White',yscrollcommand=scrollbar_y.set,xscrollcommand=scrollbar_x.set,wrap='none',width=1000)
    help_text.insert(tk.END,text)
    help_text.pack(side=tk.LEFT,fill=tk.BOTH)
    scrollbar_y.config(command=help_text.yview)
    scrollbar_x.config(command=help_text.xview)
    help_text.config(state=tk.DISABLED)



class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<FocusIn>",self.on_enter)
        self.bind("<FocusOut>", self.on_leave)

    def on_enter(self, e):
        self['background'] = 'MediumPurple1'

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        text.focus_set()


window=tk.Tk()
window.config(bg='black')
window.resizable(width=False,height=False)
try:
    title_icon=tk.PhotoImage(file='My-Awesome-Python-Calculator.png')
    window.iconphoto(True,title_icon)
except:
    pass
window.title('My Awesome Python Calculator')


input_var=tk.StringVar()
result_var=tk.StringVar()
result_var.set('------')
function_input_var=tk.StringVar()
font_face_var=tk.StringVar()
font_face_var.set('Comic Sans MS')
size_var=tk.IntVar()
size_var.set(25)
deg_rad_var=tk.IntVar()
deg_rad_var.set(0)
global Ans
Ans=None


window.bind('<Key>',lambda event: compute_result())
font=[font_face_var.get(), size_var.get(), 'bold']
active_button_background='MediumPurple3'
global function_list
function_list=['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc','sec','cosec','cot','asec','acosec','acot','deg','rad','polar','rect','s_l_e']

window_menus=tk.Menu(window)
window_menus.config(background="Black",font=[font_face_var.get(),9,"bold"],fg="White",activebackground=active_button_background,borderwidth=0)
window.config(menu=window_menus)
window_menus.add_command(label='! HELP !',command=_help_)


tk.Label(window,background='cornflower blue',borderwidth=0).grid(row=0,column=0,columnspan=6,sticky='news',padx=5,pady=5)

text=tk.Entry(window,textvariable=input_var,background='cornflower blue',font=font,fg="Black",borderwidth=0,highlightthickness=0,justify='center')
text.bind('<Return>',lambda event: result_area.focus_set())
text.bind('<Control-BackSpace>',lambda event: clear_input())
text.bind('<Shift-BackSpace>',lambda event: save_and_clear_input())
text.grid(row=0,column=0,columnspan=6,sticky='news',padx=15,pady=5)

tk.Label(window,background='DarkSeaGreen1',borderwidth=0).grid(row=1,column=0,columnspan=6,sticky='news',padx=5,pady=5)

result_area=tk.Entry(window,textvariable=result_var,background='DarkSeaGreen1',font=font,fg="Black",borderwidth=0,highlightthickness=0,justify='center')
result_area.bind('<Return>',lambda event: text.focus_set())
result_area.grid(row=1,column=0,columnspan=6,sticky='news',padx=15,pady=5)

button1=HoverButton(window,text=' 1 ',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('1'),activebackground=active_button_background,takefocus=0)
button1.grid(row=2,column=0,sticky='news',padx=5,pady=5)

button2=HoverButton(window,text='2',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('2'),activebackground=active_button_background,takefocus=0)
button2.grid(row=2,column=1,sticky='news',padx=5,pady=5)

button3=HoverButton(window,text='3',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('3'),activebackground=active_button_background,takefocus=0)
button3.grid(row=2,column=2,sticky='news',padx=5,pady=5)

button4=HoverButton(window,text='4',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('4'),activebackground=active_button_background,takefocus=0)
button4.grid(row=3,column=0,sticky='news',padx=5,pady=5)

button5=HoverButton(window,text='5',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('5'),activebackground=active_button_background,takefocus=0)
button5.grid(row=3,column=1,sticky='news',padx=5,pady=5)

button6=HoverButton(window,text='6',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('6'),activebackground=active_button_background,takefocus=0)
button6.grid(row=3,column=2,sticky='news',padx=5,pady=5)

button7=HoverButton(window,text='7',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('7'),activebackground=active_button_background,takefocus=0)
button7.grid(row=4,column=0,sticky='news',padx=5,pady=5)

button8=HoverButton(window,text='8',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('8'),activebackground=active_button_background,takefocus=0)
button8.grid(row=4,column=1,sticky='news',padx=5,pady=5)

button9=HoverButton(window,text='9',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('9'),activebackground=active_button_background,takefocus=0)
button9.grid(row=4,column=2,sticky='news',padx=5,pady=5)

button0=HoverButton(window,text='0',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('0'),activebackground=active_button_background,takefocus=0)
button0.grid(row=5,column=0,sticky='news',padx=5,pady=5)

button_plus=HoverButton(window,text='+',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('+'),activebackground=active_button_background,takefocus=0)
button_plus.grid(row=2,column=3,sticky='news',padx=5,pady=5)

button_minus=HoverButton(window,text='-',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('-'),activebackground=active_button_background,takefocus=0)
button_minus.grid(row=3,column=3,sticky='news',padx=5,pady=5)

button_asterisk=HoverButton(window,text='*',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('*'),activebackground=active_button_background,takefocus=0)
button_asterisk.grid(row=4,column=3,sticky='news',padx=5,pady=5)

button_divide=HoverButton(window,text='/',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('/'),activebackground=active_button_background,takefocus=0)
button_divide.grid(row=5,column=3,sticky='news',padx=5,pady=5)

button_open_bracket=HoverButton(window,text='(',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('('),activebackground=active_button_background,takefocus=0)
button_open_bracket.grid(row=5,column=1,sticky='news',padx=5,pady=5)

button_close_bracket=HoverButton(window,text=')',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var(')'),activebackground=active_button_background,takefocus=0)
button_close_bracket.grid(row=5,column=2,sticky='news',padx=5,pady=5)

button_decimals=HoverButton(window,text='.',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('.'),activebackground=active_button_background,takefocus=0)
button_decimals.grid(row=6,column=0,sticky='news',padx=5,pady=5)

deg_rad_button=tk.Button(window,text='deg',font=font,fg="Black",borderwidth=0,bg='hot pink',command=lambda: deg_rad_function(),activebackground=active_button_background)
deg_rad_button.grid(row=6,column=1,sticky='news',padx=5,pady=5)
deg_rad_button.bind('<Return>',lambda event: deg_rad_function())
deg_rad_button.bind('<FocusIn>',lambda event: deg_rad_button.config(bg='MediumPurple1'))
deg_rad_button.bind('<FocusOut>',lambda event: deg_rad_button.config(bg='hot pink') if deg_rad_var.get()==0 else deg_rad_button.config(bg='turquoise1'))

button_backspace=HoverButton(window,text='\u232b',font=font,fg="Black",borderwidth=0,bg='white',command=backspace,activebackground=active_button_background,takefocus=0)
button_backspace.grid(row=6,column=2,sticky='news',padx=5,pady=5)

button_clear_all=HoverButton(window,text='\u239a',font=font,fg="Black",borderwidth=0,bg='white',command=clear_input,activebackground=active_button_background,takefocus=0)
button_clear_all.grid(row=6,column=3,sticky='news',padx=5,pady=5)

function_dropdown=AutocompleteCombobox(window,width=5,textvariable=function_input_var,font=font)
function_dropdown['completevalues']=function_list
function_dropdown.bind('<Key>',function_select)
function_dropdown.bind('<Double-Button-1>',function_select)
function_dropdown.autocomplete(delta=-6)
function_dropdown.current()
function_dropdown.grid(row=7,column=0,sticky='news',padx=5,pady=5,columnspan=3)

save_and_clear_all=HoverButton(window,text='\u21ba',font=font,fg="Black",borderwidth=0,bg='white',command=save_and_clear_input,activebackground=active_button_background,takefocus=0)
save_and_clear_all.grid(row=7,column=3,sticky='news',padx=5,pady=5)

button_Ans=HoverButton(window,text='Ans',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('Ans'),activebackground=active_button_background,takefocus=0)
button_Ans.grid(row=7,column=4,sticky='news',padx=5,pady=5)

size_spinbox=tk.Spinbox(window,from_=0,to=100,font=font,fg="Black",bg="white",textvariable=size_var,width=4,command=lambda: resize(1),takefocus=1)
size_spinbox.bind('<Key>',resize)
size_spinbox.grid(row=2,column=4,sticky='news',padx=5,pady=5)

button_pi=HoverButton(window,text='\u03c0',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('pi'),activebackground=active_button_background,takefocus=0)
button_pi.grid(row=3,column=4,sticky='news',padx=5,pady=5)

button_e=HoverButton(window,text='e',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('e'),activebackground=active_button_background,takefocus=0)
button_e.grid(row=4,column=4,sticky='news',padx=5,pady=5)

button_tau=HoverButton(window,text='\u03c4',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('tau'),activebackground=active_button_background,takefocus=0)
button_tau.grid(row=5,column=4,sticky='news',padx=5,pady=5)

button_inf=HoverButton(window,text='\u221e',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('inf'),activebackground=active_button_background,takefocus=0)
button_inf.grid(row=6,column=4,sticky='news',padx=5,pady=5)

button_less_than=HoverButton(window,text='<',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('<'),activebackground=active_button_background,takefocus=0)
button_less_than.grid(row=2,column=5,sticky='news',padx=5,pady=5)

button_less_than_equal=HoverButton(window,text='\u2264',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('<='),activebackground=active_button_background,takefocus=0)
button_less_than_equal.grid(row=3,column=5,sticky='news',padx=5,pady=5)

button_greater_than=HoverButton(window,text='>',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('>'),activebackground=active_button_background,takefocus=0)
button_greater_than.grid(row=4,column=5,sticky='news',padx=5,pady=5)

button_greater_than_equal=HoverButton(window,text='\u2265',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('>='),activebackground=active_button_background,takefocus=0)
button_greater_than_equal.grid(row=5,column=5,sticky='news',padx=5,pady=5)

button_equal=HoverButton(window,text='==',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('=='),activebackground=active_button_background,takefocus=0)
button_equal.grid(row=6,column=5,sticky='news',padx=5,pady=5)

button_not_equal=HoverButton(window,text='\u2260',font=font,fg="Black",borderwidth=0,bg='white',command=lambda: input_to_input_var('!='),activebackground=active_button_background,takefocus=0)
button_not_equal.grid(row=7,column=5,sticky='news',padx=5,pady=5)

text.focus_set()

tk.mainloop()
