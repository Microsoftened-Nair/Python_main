# def progress(stream, chunk, remaining):
#     flb = stream.filesize
#     flmb = flb//(1048576)
#     rmb = remaining//(1048576)
#     done = flmb-rmb
#     if rmb != 0:
#         percent = 100 * done/flmb
#         progressbar['value'] = percent
#         root.update_idletasks()
#         time.sleep(0.01)

# print("{:00.0f}% downloaded".format(percent))

# for i in range(1, int(p1)):
# if i==1:
#     progressbar['value'] = i
#     root.update_idletasks()
#     time.sleep(0.01)
# if i > 1

import webbrowser as wb
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import *
import time

def directory():
    global path
    if len(entry1.get()) > 0:
        path=entry1.get()

    if len(entry1.get()) == 0:
        path = filedialog.askdirectory()
        entry1.insert(1, path)

def get_info():
    link = entry.get()
    yt1 = YouTube(link)
    chlink = yt1.channel_url
    ch_name = Channel(chlink)
    l3.configure(text='Video title: ' + yt1.title)
    l6.configure(text='Channel: ' + ch_name.channel_name)
    l7.configure(text='Video length: ' + str(round(yt1.length/60, 1))+'min')

# path = "D:\\Meghraj"

def download_video():
    def progress(stream=None, chunk=None, remaining=None):
        file_size = stream.filesize
        p1 = (100 * (file_size - remaining)) / file_size

        for i in range(1, int(p1+1)):
            progressbar['value'] = p1
            l4.configure(text= 'Downloaded ' + str(round(p1,1)) + "%")
            root.update_idletasks()
            time.sleep(0.01)
            if p1 == 100:
                l4.configure(text='Done')

    link = entry.get()
    yt = YouTube(link, on_progress_callback=progress)

    if clicked.get() == '360p':
        stream = yt.streams.get_by_itag(18)
        stream.download(path)

    if clicked.get() == '720p':
        stream = yt.streams.get_by_itag(22)
        stream.download(path)

    if clicked.get() == 'Audio only':
        stream = yt.streams.get_by_itag(136)
        stream.download(path)
        wb.open_new_tab("https://convertio.co/mp4-mp3/")

    if clicked.get() == '360p video-only':
        stream = yt.streams.get_by_itag(243)
        stream.download(path)

    if clicked.get() == '720p video-only':
        stream = yt.streams.get_by_itag(247)
        stream.download(path)

    if clicked.get() == '1080p video-only':
        stream = yt.streams.get_by_itag(248)
        stream.download(path)


root = Tk()
root.title('YouTube Downloader')
root.geometry('500x500')
root.configure(bg="#2c3038")
imgpath = "C:\\Users\\nairm\\OneDrive\\Pictures\\Icons\\YouTube_downloader.png"
icon = PhotoImage(file=imgpath)
root.iconphoto(True, icon)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", background='#00fff7')

head = Label(root, text='Youtube downloader ',
             font=('Segoe UI', 30, 'bold'),
             bg="#2c3038",
             fg="#00fff7")

head.place(x=0, y=0)

l1 = Label(root, text='Enter link:',
           font=('Segoe UI', 20),
           bg="#2c3038",
           fg="#00fff7")
l1.place(x=40, y=50)

entry = Entry(root, font=('Segoe UI', 20),
              bg="#2c3038",
              fg="#00fff7")
entry.place(x=40, y=90)

b1 = Button(root, text='    Go     ',
            font=('Segoe UI', 14),
            bg="#2c3038",
            fg="#00fff7",
            command=get_info,
            activebackground="#495251")
b1.place(x=345, y=89)

l2 = Label(root, text='Download path',
           font=('Segoe UI', 20),
           bg="#2c3038",
           fg="#00fff7")
l2.place(x=40, y=140)

entry1 = Entry(root,
               font=('Segoe UI', 20),
               bg="#2c3038",
               fg="#00fff7")
entry1.place(x=40, y=180)

b2 = Button(root, text='Browse..',
            font=('Segoe UI', 14),
            bg="#2c3038",
            fg="#00fff7",
            command=directory,
            activebackground="#495251")
b2.place(x=345, y=179)

l3 = Label(root, text='Video title:',
           font=('Segoe UI', 15),
           bg="#2c3038",
           fg="#00fff7")
l3.place(x=0, y=250)

l6 = Label(root, text='Channel:',
           font=('Segoe UI', 15),
           bg="#2c3038",
           fg="#00fff7")
l6.place(x=0, y=280)

l7 = Label(root, text='Video length:',
           font=('Segoe UI', 15),
           bg="#2c3038",
           fg="#00fff7")
l7.place(x=0, y=310)

clicked = StringVar()
clicked.set('720p')

opt_lst = ['360p', '720p', 'Audio only',
           '360p video-only', '720p video-only',
           '1080p video-only']

options = OptionMenu(root, clicked, *opt_lst)
options.place(x=310, y=350)
options.config(bg="#2c3038",
               fg="#00fff7",
               activebackground="#495251")

Download_button = Button(root, text='Download',
                       font=('Segoe UI', 15),
                       bd=5,
                       command=download_video,
                       bg="#2c3038",
                       fg="#00fff7",
                       activebackground="#495251")
Download_button.place(x=200, y=350)

l4 = Label(root, text='Progress:',
           font=('Segoe UI', 15),
           bg="#2c3038",
           fg="#00fff7" )
l4.place(x=0, y=410)

progressbar = ttk.Progressbar(root,
                              style='red.Horizontal.TProgressbar',
                              orient="horizontal",
                              length=500,
                              mode='determinate')
progressbar.place(x=0, y=440)

root.mainloop()
