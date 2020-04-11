# skatspiel mit 2 Bots

from tkinter import *
from random import *

root = Tk()


Karten = ["Kreuz Bube","Pik Bube", "Herz Bube", "Karo Bube", "Kreuz Ass","Kreuz 10","Kreuz König","Kreuz Dame","Kreuz 9","Kreuz 8","Kreuz 7","Pik Ass","Pik 10","Pik König","Pik Dame","Pik 9","Pik 8","Pik 7", "Herz Ass","Herz 10","Herz König","Herz Dame","Herz 9","Herz 8","Herz 7","Karo Ass","Karo 10","Karo König","Karo Dame","Karo 9","Karo 8","Karo 7"]

Zahlen = [18,20,22,24,27,30,36,40,44,45,48,50,55,60,1000]
Spieler_1 = []
Spieler_2 = []
Spieler_3 = []
Skat = []



#def f_Spieler(): 

def f_Karten():
    """ Karten verteilen"""
    Spieler_1 = []
    Spieler_2 = []
    Spieler_3 = []
    Skat = []
    
    i=0
    while i < 32:
        x = randint(0,3)
        if x == 0:
            if len(Spieler_1) > 9:
               i-=1
            else: Spieler_1.append(Karten[i])
        elif x == 1:
            if len(Spieler_2) > 9:
                i-=1
            else: Spieler_2.append(Karten[i])
        elif x == 2:
            if len(Spieler_3) > 9:
                i-=1
            else: Spieler_3.append(Karten[i])
        elif x == 3:
            if len(Skat) > 1:
                i-=1
            else: Skat.append(Karten[i])
        i+=1
    #temp = Spieler_3[0]; Spieler_3[0] = Spieler_3[9]; Spieler_3[9] = temp
    return Spieler_1 + Spieler_2 + Spieler_3 + Skat

def f_alleine(Hände):
    """ spieler ist Zahl zwischen 0 und 2 """
    """ Spieler 0 ist Geber, Spieler 1 ist nach 0 dran"""
    """ möchte Spieler alleine spielen und wie weit kann er reizen"""
    global Werte
    Werte = [0,0]
    
    """[Reizwert Sp 0, Reizwert Sp 1, Trumpffarbe Sp0, Trumpffarbe Sp1]"""
    for Spieler in range(2):
        Bube = 0
        KB = 0
        PB = 0
        HB = 0
        RB = 0
        Ass = 0
        Kreuz = 0 
        Pik = 0
        Herz = 0
        Karo = 0
        Trumpf = 0
        
        for i in range(4):
            if "Kreuz Bube" in Hände[i + Spieler * 10]:
                Bube += 1
                KB = 1
            if "Pik Bube" in Hände[i + Spieler * 10]:
                Bube += 1
                PB = 1
            if "Herz Bube" in Hände[i + Spieler * 10]:
                Bube += 1
                HB = 1
            if "Karo Bube" in Hände[i + Spieler * 10]:
                Bube += 1
                RB = 1

        
        
        for i in range(10):
            if "Ass" in Hände[i + Spieler * 10]:
                Ass += 1
            if "Kreuz " in Hände[i + Spieler * 10]:
                Kreuz += 1
            if "Pik" in Hände[i + Spieler * 10]:
                Pik += 1
            if "Herz" in Hände[i + Spieler * 10]:
                Herz += 1
            if "Karo" in Hände[i + Spieler * 10]:
                Karo += 1
                                
        
        Trumpf = max(Kreuz, Pik, Herz, Karo)
      
        if Trumpf + Ass + Bube >= 7:
            count = 0
            if KB == 1: 
                count += 1
                if PB == 1:
                    count += 1
                    if HB == 1:
                        count += 1
                        if RB == 1:
                            count += 1
            if KB == 0: 
                count += 1
                if PB == 0:
                    count += 1
                    if HB == 0:
                        count += 1
                        if RB == 0:
                            count += 1
            if Trumpf == Kreuz:
                Werte[Spieler] = (count + 1)* 12
                #Trumpffarbe = "Kreuz"
            elif Trumpf == Pik:
                Werte[Spieler] = (count + 1)* 11
                #Trumpffarbe = "Pik"
            elif Trumpf == Herz:
                Werte[Spieler] = (count + 1)* 10
                #Trumpffarbe = "Herz"
            elif Trumpf == Karo:
                Werte[Spieler] = (count + 1)* 9
                #Trumpffarbe = "Karo"

    return Werte

def f_clear_Ja():
    global Button_Beginn
    global Glückwunsch
    Button_Beginn.destroy()
    Glückwunsch.destroy()
    f_Skat()
def f_Ja(i):
    global Option_Ja # widges
    global Option_Nein
    global Frage
    global Button_Beginn
    global Glückwunsch
    
    
    if Zahlen[i] > max(Werte):
        #global wer_spielt # merkt sich wer spielt (1-3)
        Option_Ja.destroy()
        Option_Nein.destroy()
        Frage.destroy()
        Glückwunsch = Label(root, text = "Glückwunsch, du darfst alleine spielen")
        Glückwunsch.grid(row = 2, column = 0)
        Button_Beginn = Button(root, text = "Drücke,um zu beginnen", command = f_clear_Ja, bg = '#90ee90')
        Button_Beginn.grid(row = 1, column = 0)
        
        
    else: 
        Frage.destroy()
        Option_Ja.destroy()
        Option_Nein.destroy()
        f_Reizen_Frage(i+1)
    
def f_clear_Nein(): #macht nach f_Nein das Fester leer
    global Bot_Spieler
    global Button_Beginn
    Bot_Spieler.destroy()
    Button_Beginn.destroy()

def f_Nein():
    global Option_Ja # ersten 5 sind widges
    global Option_Nein
    global Frage
    global Bot_Spieler
    global Button_Beginn
    
    #global wer_spielt  merkt sich wer alleine spielt (1-3)
    
    Option_Ja.destroy()
    Option_Nein.destroy()
    Frage.destroy()
    if Werte[0] > Werte [1]:
        Bot_Spieler = Label(root, text = "Es spielt Spieler 0 alleine")
        Bot_Spieler.grid(row = 0, column = 0)
        #wer_spielt = 0
    else: 
        Bot_Spieler = Label(root, text = "Es spielt Spieler 1 alleine")
        Bot_Spieler.grid(row = 0, column = 0)
        #wer_spielt = 1

    Button_Beginn = Button(root, text = "Drücke,um zu beginnen", command = f_clear_Nein, bg = '#90ee90')
    Button_Beginn.grid(row = 1, column = 0)


def f_Reizen_Frage(i):
    global Zahlen
    global Option_Ja
    global Option_Nein
    global Frage
    #global wer_spielt
    Frage = Label(root, text = "Möchten Sie "+str(Zahlen[i])+" sagen?")
    Frage.grid(row = 0, column = 0)
    Option_Ja = Button(root, text = "Ja", bg = '#90ee90', command =lambda: f_Ja(i))
    Option_Ja.grid(row = 1, column = 0)
    Option_Nein = Button(root, text = "Nein", bg = '#fa8072', command = f_Nein)
    Option_Nein.grid(row = 1, column = 1)

def f_Karte_zeigen(Hände):
    #pieler_1 = [Hände[i] for i in range(10)]
    #pieler_2 = [Hände[i] for i in range(10,20)]
    Spieler_3 = [Hände[i] for i in range(20,30)]
    L_Karten_Zeigen = Label(root, text = Spieler_3)
    L_Karten_Zeigen.grid(row = 4, column = 0)

def f_Hand_Ja():
    global L_Hand
    global B_Hand_Ja
    global B_Hand_Nein
    L_Hand.destroy()
    B_Hand_Ja.destroy()
    B_Hand_Nein.destroy()

def f_Hand_Nein():
    global L_Hand
    global B_Hand_Ja
    global B_Hand_Nein
    global Hände 
    L_Hand.destroy()
    B_Hand_Ja.destroy()
    B_Hand_Nein.destroy()
    L_Show_Skat = Label(root, text = "Dies ist der Skat" + str([Hände[i] for i in range(30,32)]))
    
def f_Skat(): 
    """ wird von f_Reizen_Frage aufgerufen"""
    global L_Hand
    global B_Hand_Ja
    global B_Hand_Nein
    Skat = [Hände[i] for i in range(30,32)]
    L_Hand = Label(root, text = "willst du Hand spielen?")
    L_Hand.grid(row = 0, column = 0)
    B_Hand_Ja = Button(root, text = "Ja", bg = '#90ee90', command = f_Hand_Ja)
    B_Hand_Ja.grid(row = 1, column = 0)
    B_Hand_Nein = Button(root, text = "Nein", bg = '#fa8072', command = f_Hand_Nein)
    B_Hand_Nein.grid(row = 1, column = 1)


def f_Spiel():
    global Hände
    global Werte
    #global wer_spielt
    Hände = f_Karten() # Karten geben; gibt Karten als Liste zurück in der Spieler 1 2 3 und dann der Skat steht (eine lange Liste)
    Werte = f_alleine(Hände)
    f_Karte_zeigen(Hände)
    f_Reizen_Frage(0) # ruft f_skat auf



    root.mainloop() 
f_Spiel()