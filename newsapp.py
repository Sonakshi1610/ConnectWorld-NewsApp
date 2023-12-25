import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
import io
import webbrowser

class NewsApp:

    def __init__(self):

        #Fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=36822ec9be854858bab6d006f255f2df').json()


        # initial gui load
        self.load_gui()


    # load first news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.configure(bg="black")
        self.root.title('Connect World')
        self.root.wm_iconbitmap("newsapp_logo.jpg")

    def clear (self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        # clear the screen for the new news item
        self.clear()

        frame = Frame(self.root,  bg = 'black')
        frame.pack(expand=True,fill=BOTH, side=BOTTOM)

        frameb = Frame(frame, bg="black")
        frameb.pack(fill= BOTH,side= BOTTOM)

        #image
        try:
            img_url = self.data['articles'] [index] ['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((250,200))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((250, 200))
            photo = ImageTk.PhotoImage(im)

        label = Label(frame,image=photo).pack(side= TOP)

        heading = Label(frame, text=self.data['articles'] [index] ['title'] , bg='black', fg="white", wraplength=340,  justify="center")
        heading.pack(pady=(2,20))
        heading.config(font=('comicsans',17))

        details = Label(frame, text=self.data['articles'] [index] ['description'] , bg='black', fg="white", wraplength=340,  justify="center")
        details.pack(pady=(20,30), anchor='center')
        details.config(font=('comicsans',12))

        if index != 0:
            previous = Button(frameb, text="previous", width=16, height=3, command= lambda :self.load_news_item(index-1 ))
            previous.pack(side=LEFT)

        if index != 18 :
            next = Button(frameb, text="next", width=16, height=3, command= lambda :self.load_news_item(index+1))
            next.pack(side=RIGHT)

        read= Button(frameb, text="read more", width=16, height=3,
                     command=lambda  : self.open_link(self.data ['articles'] [index] ['url']))
        read.pack(side=LEFT)

        self.root.mainloop()


    def open_link(self, url):
        webbrowser.open(url)




obj = NewsApp()