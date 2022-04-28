 #Import Libraries
# from pytube import YouTube

# from tkinter import *
# #creating display window
# root = Tk()
# root.geometry('500x300')
# root.resizable(0,0)
# root.title("Yubi's personal downloader")


# Label(root,text="Youtube Video Downloader", font="arial 20 bold").pack()


# #create field to enter link

# link = StringVar()

# Label(root,text="Paste Link Here:",font="arial 15 bold").place(x=160 ,y=60)

# link_enter = Entry(root,width=70,textvariable=link).place(x=32,y=90)

# def Downloader():
#     url=YouTube(str(link.get()))
#     video= url.streams.first()
#     video.download()
#     Label(root,text="Downloaded", font="arial 15").place(x=180,y=210)

# Button(root,text="DOWNLOAD", font="arial 15 bold", bg="pale violet red", padx=2,command=Downloader).place(x=180, y=150)

# root.mainloop()

from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")



