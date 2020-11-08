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
Made on 10/08/2020
'''
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
from math import *
from math import degrees as deg
from math import radians as rad
from math import factorial as fact
from cmath import polar,rect

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
            if notation_var.get()==0:
                result_var.set(str(eval(input_var.get())))
            else:
                result_var.set(str(format(eval(input_var.get()),'10,.10e')))
        except:
            result_var.set('error')

def clear_input():
    input_var.set('')
    result_var.set('------')

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
    elif event.keycode==13:
        for i in window.grid_slaves():
            i.config(font=[font_face_var.get(), size_var.get(), 'bold'])

def function_select(event):
    if event==1:
        pos=text.index(tk.INSERT)
        input_var.set(input_var.get()[0:pos]+function_input_var.get()+'('+input_var.get()[pos:len(input_var.get())])
        text.icursor(pos+len(function_input_var.get())+1)
        compute_result()
        text.focus_set()
    elif event.keycode==13 and function_input_var.get()!='':
        pos=text.index(tk.INSERT)
        input_var.set(input_var.get()[0:pos]+function_input_var.get()+'('+input_var.get()[pos:len(input_var.get())])
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

def function_notation():
    notation_var.set(int(not notation_var.get()))
    if notation_var.get()==0:
        button_notation.config(text='Com',bg='hot pink')
    else:
        button_notation.config(text='Sci',bg='turquoise1')
    compute_result()
    text.focus_set()



class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = 'MediumPurple1'

    def on_leave(self, e):
        self['background'] = self.defaultBackground


window=tk.Tk()
window.config(bg='black')
window.resizable(width=False,height=False)
try:
    title_icon=tk.PhotoImage(file='Calculator_icon.png')
    window.iconphoto(False,title_icon)
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
notation_var=tk.IntVar()
notation_var.set(0)

window.bind('<Key>',lambda event: compute_result())
font=[font_face_var.get(), size_var.get(), 'bold']
active_button_background='MediumPurple3'
function_list=['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc','sec','cosec','cot','asec','acosec','acot','deg','rad','polar','rect']


tk.Label(window,background='cornflower blue',borderwidth=0).grid(row=0,column=0,columnspan=6,sticky='news',padx=5,pady=5)

text=tk.Entry(window,textvariable=input_var,background='cornflower blue',font=font,borderwidth=0,justify='center')
text.bind('<Key>',lambda event: result_area.focus_set() if (event.keycode==13) else None)
text.grid(row=0,column=0,columnspan=6,sticky='news',padx=15,pady=5)

tk.Label(window,background='DarkSeaGreen1',borderwidth=0).grid(row=1,column=0,columnspan=6,sticky='news',padx=5,pady=5)

result_area=tk.Entry(window,textvariable=result_var,background='DarkSeaGreen1',font=font,borderwidth=0,justify='center')
result_area.bind('<Key>',lambda event: text.focus_set() if (event.keycode==13) else None)
result_area.grid(row=1,column=0,columnspan=6,sticky='news',padx=15,pady=5)

button1=HoverButton(window,text='1',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('1'),activebackground=active_button_background)
button1.grid(row=2,column=0,sticky='news',padx=5,pady=5)

button2=HoverButton(window,text='2',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('2'),activebackground=active_button_background)
button2.grid(row=2,column=1,sticky='news',padx=5,pady=5)

button3=HoverButton(window,text='3',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('3'),activebackground=active_button_background)
button3.grid(row=2,column=2,sticky='news',padx=5,pady=5)

button4=HoverButton(window,text='4',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('4'),activebackground=active_button_background)
button4.grid(row=3,column=0,sticky='news',padx=5,pady=5)

button5=HoverButton(window,text='5',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('5'),activebackground=active_button_background)
button5.grid(row=3,column=1,sticky='news',padx=5,pady=5)

button6=HoverButton(window,text='6',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('6'),activebackground=active_button_background)
button6.grid(row=3,column=2,sticky='news',padx=5,pady=5)

button7=HoverButton(window,text='7',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('7'),activebackground=active_button_background)
button7.grid(row=4,column=0,sticky='news',padx=5,pady=5)

button8=HoverButton(window,text='8',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('8'),activebackground=active_button_background)
button8.grid(row=4,column=1,sticky='news',padx=5,pady=5)

button9=HoverButton(window,text='9',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('9'),activebackground=active_button_background)
button9.grid(row=4,column=2,sticky='news',padx=5,pady=5)

button0=HoverButton(window,text='0',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('0'),activebackground=active_button_background)
button0.grid(row=5,column=0,sticky='news',padx=5,pady=5)

button_plus=HoverButton(window,text='+',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('+'),activebackground=active_button_background)
button_plus.grid(row=2,column=3,sticky='news',padx=5,pady=5)

button_minus=HoverButton(window,text='-',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('-'),activebackground=active_button_background)
button_minus.grid(row=3,column=3,sticky='news',padx=5,pady=5)

button_asterisk=HoverButton(window,text='*',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('*'),activebackground=active_button_background)
button_asterisk.grid(row=4,column=3,sticky='news',padx=5,pady=5)

button_divide=HoverButton(window,text='/',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('/'),activebackground=active_button_background)
button_divide.grid(row=5,column=3,sticky='news',padx=5,pady=5)

button_open_bracket=HoverButton(window,text='(',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('('),activebackground=active_button_background)
button_open_bracket.grid(row=5,column=1,sticky='news',padx=5,pady=5)

button_close_bracket=HoverButton(window,text=')',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var(')'),activebackground=active_button_background)
button_close_bracket.grid(row=5,column=2,sticky='news',padx=5,pady=5)

button_decimals=HoverButton(window,text='.',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('.'),activebackground=active_button_background)
button_decimals.grid(row=6,column=0,sticky='news',padx=5,pady=5)

deg_rad_button=tk.Button(window,text='deg',font=font,borderwidth=0,bg='hot pink',command=lambda: deg_rad_function(),activebackground=active_button_background)
deg_rad_button.grid(row=6,column=1,sticky='news',padx=5,pady=5)

button_backspace=HoverButton(window,text='\u232b',font=font,borderwidth=0,bg='white',command=backspace,activebackground=active_button_background)
button_backspace.grid(row=6,column=2,sticky='news',padx=5,pady=5)

button_clear_all=HoverButton(window,text='\u239a',font=font,borderwidth=0,bg='white',command=clear_input,activebackground=active_button_background)
button_clear_all.grid(row=6,column=3,sticky='news',padx=5,pady=5)

function_dropdown=AutocompleteCombobox(window,width=5,textvariable=function_input_var,font=font)
function_dropdown['completevalues']=function_list
function_dropdown.bind('<Key>',function_select)
function_dropdown.autocomplete(delta=-6)
function_dropdown.current()
function_dropdown.grid(row=7,column=0,sticky='news',padx=5,pady=5,columnspan=3)

function_select_button=HoverButton(window,text='\u23ce',font=font,borderwidth=0,bg='white',command=lambda: function_select(1))
function_select_button.grid(row=7,column=3,sticky='news',padx=5,pady=5)

button_notation=tk.Button(window,text='Com',font=font,borderwidth=0,bg='hot pink',command=lambda: function_notation(),activebackground=active_button_background)
button_notation.grid(row=7,column=4,sticky='news',padx=5,pady=5)

size_spinbox=tk.Spinbox(window,from_=0,to=100,font=font,textvariable=size_var,width=4,command=lambda: resize(1))
size_spinbox.bind('<Key>',resize)
size_spinbox.grid(row=2,column=4,sticky='news',padx=5,pady=5)

button_pi=HoverButton(window,text='\u03c0',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('pi'),activebackground=active_button_background)
button_pi.grid(row=3,column=4,sticky='news',padx=5,pady=5)

button_e=HoverButton(window,text='e',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('e'),activebackground=active_button_background)
button_e.grid(row=4,column=4,sticky='news',padx=5,pady=5)

button_tau=HoverButton(window,text='tau',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('tau'),activebackground=active_button_background)
button_tau.grid(row=5,column=4,sticky='news',padx=5,pady=5)

button_inf=HoverButton(window,text='\u221e',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('inf'),activebackground=active_button_background)
button_inf.grid(row=6,column=4,sticky='news',padx=5,pady=5)

button_less_than=HoverButton(window,text='<',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('<'),activebackground=active_button_background)
button_less_than.grid(row=2,column=5,sticky='news',padx=5,pady=5)

button_less_than_equal=HoverButton(window,text='<=',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('<='),activebackground=active_button_background)
button_less_than_equal.grid(row=3,column=5,sticky='news',padx=5,pady=5)

button_greater_than=HoverButton(window,text='>',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('>'),activebackground=active_button_background)
button_greater_than.grid(row=4,column=5,sticky='news',padx=5,pady=5)

button_greater_than_equal=HoverButton(window,text='>=',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('>='),activebackground=active_button_background)
button_greater_than_equal.grid(row=5,column=5,sticky='news',padx=5,pady=5)

button_equal=HoverButton(window,text='==',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('=='),activebackground=active_button_background)
button_equal.grid(row=6,column=5,sticky='news',padx=5,pady=5)

button_not_equal=HoverButton(window,text='\u2260',font=font,borderwidth=0,bg='white',command=lambda: input_to_input_var('!='),activebackground=active_button_background)
button_not_equal.grid(row=7,column=5,sticky='news',padx=5,pady=5)

text.focus_set()

tk.mainloop()
