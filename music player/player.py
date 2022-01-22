from tkinter import*
import os
import pygame
player = Tk()
class musicplayer():
    def __init__(self, player):
        self.player = player
        self.player.geometry("365x667")
        self.player.title("Andemoli Music Player")
        self.player.resizable(0,0)

        #initiating pygame
        pygame.init()

        #initiating pygame mixer
        pygame.mixer.init() 

        #declaring track variable
        self.track = StringVar()

        #declaring status variable
        self.status = StringVar()



        #declaring track frame to hold song and status label
        trackframe = LabelFrame(self.player, text = "Songs", font = ("arial", 17,"bold"),bg = "gray", fg = "white", padx =0)
        trackframe.place(x =3, y = 0, width = 360, height = 500)

        statusframe = LabelFrame(self.player, text = "status", bg = "teal", fg ="white",font = ("arial", 17,"bold"), )
        statusframe.place(x = 3, y =505, width = 360, height = 60)

        songtrack = Label(statusframe, textvariable = self.track, width = 20, height =1, font = ("arial", 12,"bold"))
        songtrack.grid(row = 0, column = 0, padx =1, pady=4)
        songstatus = Label(statusframe, textvariable = self.status, width = 14, height=1,font = ("arial", 12,"bold"))
        songstatus.grid (row =0,column =1, padx =1, pady = 4)

        btnframe = LabelFrame(self.player, text = "Controls", bg = "teal", fg ="white",font = ("arial", 17,"bold"), )
        btnframe.place(x = 3, y =567, width = 360, height = 90)        


        #inserting buttons
        playbtn = Button(btnframe, text = "play",  width = 5,height = 1, command = self.playsong(),font = ("arial", 12,"bold") , bg= "aqua", fg = "black", cursor = "hand2" )
        playbtn.grid(row =1, column = 0,padx =8, pady =9)

        #inserting pause button
        pausebtn = Button(btnframe, text = "pause",  width = 5,height = 1,command =self.pausesong(), font = ("arial", 12,"bold") , bg= "aqua", fg = "black", cursor = "hand2" )
        pausebtn.grid(row = 1, column = 1,padx =8, pady = 9)

        #inserting unpause button
        unpausebtn = Button(btnframe, text = "unpause",  width = 7,height = 1,command =self.unpausesong(),font = ("arial", 12,"bold") , bg= "aqua", fg = "black", cursor = "hand2" )
        unpausebtn.grid(row = 1, column = 2,padx =8, pady = 9)

        #inserting stop button
        stopbtn = Button(btnframe, text = "stop",  width = 4,height = 1,command = self.stopsong(),font = ("arial", 12,"bold") , bg= "aqua", fg = "black" , cursor = "hand2")
        stopbtn.grid(row = 1, column = 3, padx =8, pady = 9)

        scroll_y = Scrollbar(trackframe, orient="vertical")
        #inserting playlist
        self.playlist = Listbox(trackframe, yscrollcommand=scroll_y.set, selectmode = SINGLE, font = ("arial", 12,"bold"), bd =5, relief = GROOVE)
        self.playlist.place(x =4, y = 0, width = 356, height = 500)

        #applying scrollbar to listbox
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH,expand = TRUE, padx =2, pady=1)

        #directory of the songs
        os.chdir("C:/Users/ADMIN/Music")

        # fetching songs
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END,track)

    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        # Displaying Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()




musicplayer(player)
player.mainloop()