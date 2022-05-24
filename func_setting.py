import os
from tkinter import *

# GUI 색상
backgound_color = "cornsilk"
button_color = "moccasin"


    # Reframework 경로 리턴하기
def getFrameworkPath():
    username_path = os.path.expanduser('~')
    path = "{0}/rpa-scripts/REframework".format(username_path)
    return path

# frame 생성
def create_frame( root, text, y):
    if text == "": 
        frame = Frame(root)
        x = 0
    elif text != "":
        frame = LabelFrame(root, text=text)
        x = 3
    frame.pack(fill="x", expand=False, padx=x, pady=y)
    frame.config(bg=backgound_color)
    return frame

# label 생성
def create_label( frame, text):
    label = Label(frame, text=text, width=8)
    label.pack(side="left", padx=5, pady=3, ipady=3)
    label.config(bg=backgound_color)
    return label

#entry 생성
def create_entry( frame, fill=""):
    entry = Entry(frame)
    if fill == "":
        entry.pack(side="left", expand=False, padx=3, pady=3, ipady=3)
    else:
        entry.pack(side="left", fill="x", expand=True, padx=3, pady=3, ipady=3)
    return entry


#button 생성
def create_button( frame, text, py=3, w=10, by=0, root=None):
    sideVal = "right"
    if text == "초기화":
        sideVal = "left"
    btn = Button(frame, text=text, command="", width=w, pady=by)
    btn.pack(side=sideVal, padx=3, pady=py, ipady=2)
    btn.config(bg=button_color)
    return btn
