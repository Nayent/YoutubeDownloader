from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Downloader")

Label(root, text = 'Youtube Downloader', font = 'arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x = 160, y = 60)
link_enter = Entry(root, width = 60, textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download('/home/nomura/Documents/Github/Python/Youtube_Downloader/downloads')
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x = 180 ,y = 150)

root.mainloop()