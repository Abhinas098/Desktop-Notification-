from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time


t = Tk()
t.title('Notifier')
t.geometry("400x300")
img = Image.open("untitled-2.gif")
tkimage = ImageTk.PhotoImage(img)


def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="notify.ico",
                            toast=True,
                            timeout=15)

img_label = Label(t, image=tkimage).grid()

t_label = Label(t, text="Notify for ",font=("poppins", 10))
t_label.place(x=10, y=70)

title = Entry(t, width="30",font=("poppins", 11))
title.place(x=83, y=70)


m_label = Label(t, text="Message",font=("poppins", 10))
m_label.place(x=10, y=120)


msg = Entry(t, width="40", font=("poppins", 10))
msg.place(x=90,height=30, y=116)


time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=90, y=175)


time_min_label = Label(t, text="in min", font=("poppins", 10))
time_min_label.place(x=135, y=205)

but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#5c29c4", width=20,
             relief="raised",
             command=get_details)
but.place(x=120, y=250)

t.resizable(0,0)
t.mainloop()