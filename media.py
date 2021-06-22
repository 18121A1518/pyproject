def url():
    dd=filedialog.askopenfilename()
    audiotrack.set(dd)
def play():
    ms=audiotrack.get()
    mixer.music.load(ms)
    Plabel.grid()
    PVlabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    mixer.music.set_volume(0.4)
    mixer.music.play()
    root.Bmute.grid()
    ProgressbarMusicLabel.grid()
    Alabel.configure(text='playing..')

    song=MP3(ms)
    totalsonglength=int(song.info.length)
    ProgressbarMusic['maximum']=totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        CurrentSongLength=mixer.music.get_pos()//1000
        ProgressbarMusic['value']=CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()    
def pause():
    mixer.music.pause()
    root.button4.grid_remove()
    root.button7.grid()
    Alabel.configure(text='paused...')
def volumein():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.01)
    PVlabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100
def volumede():
     vol=mixer.music.get_volume()
     mixer.music.set_volume(vol-0.01)
     PVlabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
     ProgressbarVolume['value']=mixer.music.get_volume()*100
def stop():
    mixer.music.stop()
    Alabel.configure(text='stopped...')
def resume():
    root.button7.grid_remove()
    root.button4.grid()
    mixer.music.unpause()
    Alabel.configure(text='resumed...')
def mute():
    global cvol
    root.Bmute.grid_remove()
    root.Bunmute.grid()
    cvol=mixer.music.get_volume()
    mixer.music.set_volume(0)
def unmute():
    root.Bunmute.grid_remove()
    root.Bmute.grid()
    mixer.music.set_volume(cvol)
def createwidgets():
    global Alabel,ProgressbarVolume,PVlabel,Plabel,ProgressbarMusicStartTimeLabel,ProgressbarMusicLabel,CurrentSongLength,ProgressbarMusicEndTimeLabel,ProgressbarMusic
    Tlabel=Label(root,text='select Audio Track:',background='lightpink')
    Tlabel.grid(row=0,column=0,padx=20,pady=20)
    Alabel=Label(root,text='',background='lightpink')
    Alabel.grid(row=2,column=1,padx=20,pady=20)
    Tentry=Entry(root,width=60,textvariable=audiotrack)
    Tentry.grid(row=0,column=1,padx=20,pady=20)
    button1=Button(root,text='search',width=20,background='skyblue',activebackground='purple',command=url)
    button1.grid(row=0,column=2,padx=20,pady=20)
    button2=Button(root,text='play',width=20,background='skyblue',activebackground='purple',command=play)
    button2.grid(row=1,column=0,padx=20,pady=20)
    button3=Button(root,text='stop',width=20,background='skyblue',activebackground='purple',command=stop)
    button3.grid(row=2,column=0,padx=20,pady=20)
    root.button4=Button(root,text='pause',width=20,background='skyblue',activebackground='purple',command=pause)
    root.button4.grid(row=1,column=1,padx=20,pady=20)
    root.button7=Button(root,text='resume',width=20,background='skyblue',activebackground='purple',command=resume)
    root.button7.grid(row=1,column=1,padx=20,pady=20)
    root.button7.grid_remove()
    button5=Button(root,text='volumeup',width=20,background='skyblue',activebackground='purple',command=volumein)
    button5.grid(row=1,column=2,padx=20,pady=20)
    button6=Button(root,text='volumedown',width=20,background='skyblue',activebackground='purple',command=volumede)
    button6.grid(row=2,column=2,padx=20,pady=20)
    root.Bmute=Button(root,text='mute',width=10,background='skyblue',activebackground='purple',command=mute)
    root.Bmute.grid(row=4,column=2,padx=20,pady=20)
    root.Bunmute=Button(root,text='unmute',width=10,background='skyblue',activebackground='purple',command=unmute)
    root.Bunmute.grid(row=4,column=2,padx=20,pady=20)
    root.Bunmute.grid_remove()
    root.Bmute.grid_remove()
    Plabel=Label(root,text='',bg='red')
    Plabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    Plabel.grid_remove()
    ProgressbarVolume=Progressbar(Plabel,orient=VERTICAL,mode='determinate',value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)
    PVlabel=Label(Plabel,text='0%',bg='lightgray',width=3)
    PVlabel.grid(row=0,column=0)
    ProgressbarMusicLabel=Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()
    ProgressbarMusicStartTimeLabel=Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)
    ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=50)
    ProgressbarMusic.grid(row=0,column=1,ipadx=300,ipady=3)
    
    ProgressbarMusicEndTimeLabel=Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
cvol=0
root=Tk()
root.geometry('900x600+200+50')
root.title('mediaplayer')
root.resizable(False,False)
root.configure(bg='lightpink')

audiotrack=StringVar()
currentvol=0
totalsonglength=0
createwidgets()
mixer.init()
root.mainloop()
