from pytube import YouTube
import tkinter
import customtkinter
import os

app = customtkinter.CTk()
app.geometry("400x240")

app2 = customtkinter.CTk()
app2.geometry("300x240")

def button_close_window():
    app2.withdraw()

def button_click_event():
    yt = YouTube(entry.get())
    yd = yt.streams.get_highest_resolution()
    user = os.getlogin()
    path = "/Users/" + user + "/Desktop/YoutubeDownloads"
    if not os.path.exists(path):
        os.mkdir(path)
    yd.download(path)
    entry.delete(first_index=0, last_index=len(entry.get()))
    app2.deiconify()

entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter Youtube Link")
entry.pack(padx=20, pady=80)
button = customtkinter.CTkButton(app, text="Submit", command=button_click_event)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app2, text="Download finished")
label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(app2, text="Okay", command=button_close_window)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
app2.withdraw()

app.mainloop()
app2.mainloop()