from tkinter import *
def clicked():
  txt=entry1.get()
  if len(txt)==0 or txt.isspace():
    button1.configure(background="red")
  else:
    button1.configure(text="clear",background="white", command=cancel)
    label1.configure(text=txt)

def cancel():
  txt=entry1.get()
  entry1.delete(0,len(txt))
  button1.configure(text="Copy Text",background="white", command=clicked)
  label1.configure(text=txt)
app=Tk()
app.title("Trial101")
app.geometry("200x120")

entry1=Entry(app, text="Text is displayed Here",)
entry1.place(relx=0.5, rely=0.4, anchor="center")

button1=Button(app, text="Copy Text", command=clicked)
button1.place(relx=0.5, rely=0.6, anchor="center")

label1=Label(app,text="Text is displayed here", )
label1.pack(side="bottom")
app.mainloop()
