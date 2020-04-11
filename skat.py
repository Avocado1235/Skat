# skatspiel mit 2 Bots
# L_Show_Skat_Karten_Beide wird nicht gelöscht 
from tkinter import *
from random import *

root = Tk()

 
Karten = ["Kreuz Bube","Pik Bube", "Herz Bube", "Karo Bube", "Kreuz Ass","Kreuz 10","Kreuz König","Kreuz Dame","Kreuz 9","Kreuz 8","Kreuz 7","Pik Ass","Pik 10","Pik König","Pik Dame","Pik 9","Pik 8","Pik 7", "Herz Ass","Herz 10","Herz König","Herz Dame","Herz 9","Herz 8","Herz 7","Karo Ass","Karo 10","Karo König","Karo Dame","Karo 9","Karo 8","Karo 7"]

Zahlen = [18,20,22,24,27,30,36,40,44,45,48,50,55,60,1000]
Spieler_1 = []
Spieler_2 = []
Spieler_3 = []
Skat = []



global Werte # [a,b,c, e,f] a,b Reizwert von Bot0 und Bot1 und c wer spielt, daher zahl 0,1 oder 2(Spieler spielt) // e,f welche Fabe e,f am Meisten haben. 
                        #Sie können nur diese oder beim reizen höherwertige Karten nehmen, um nicht überprüfen zu müssen ob sie sich sonst überreizt hätten
global Hände # Liste der Karten; ersten jeweils 10 Harten für die Bots und dann 2 für den Skat, diees ist im gesamten Spiel der FAll

#def f_Spieler(): 

def f_Karten():
    """ Karten verteilen"""
    Spieler_1 = []
    Spieler_2 = []
    Spieler_3 = []
    Skat = []
    
    i=0
    while i < 32:
        x = randint(0,32)
        if x >= 0 and x <= 9:
            if len(Spieler_1) > 9:
               i-=1
            else: Spieler_1.append(Karten[i])
        elif x >= 10 and x <= 19:
            if len(Spieler_2) > 9:
                i-=1
            else: Spieler_2.append(Karten[i])
        elif x >= 20 and x <= 29:
            if len(Spieler_3) > 9:
                i-=1
            else: Spieler_3.append(Karten[i])
        elif x >= 30 and x <= 32 :
            if len(Skat) > 1:
                i-=1
            else: Skat.append(Karten[i])
        i+=1
    #temp = Spieler_3[0]; Spieler_3[0] = Spieler_3[9]; Spieler_3[9] = temp
    return Spieler_1 + Spieler_2 + Spieler_3 + Skat

def f_alleine(Hände):
    """ spieler ist Zahl zwischen 0 und 2 """
    """ Spieler 0 ist Geber, Spieler 1 ist nach 0 dran"""
    """ möchte der Bot (als Variab) alleine spielen und wie weit kann er reizen"""
    global Werte
    Werte = [0,0,0,0,0]
    
    """[Reizwert Sp 0, Reizwert Sp 1, wer spielt]"""
    for Wer_Spielt in range(2):
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
            if "Kreuz Bube" in Hände[i + Wer_Spielt * 10]:
                Bube += 1
                KB = 1
            if "Pik Bube" in Hände[i + Wer_Spielt * 10]:
                Bube += 1
                PB = 1
            if "Herz Bube" in Hände[i + Wer_Spielt * 10]:
                Bube += 1
                HB = 1
            if "Karo Bube" in Hände[i + Wer_Spielt * 10]:
                Bube += 1
                RB = 1

        
        
        for i in range(10):
            if "Ass" in Hände[i + Wer_Spielt * 10]:
                Ass += 1
            if "Kreuz " in Hände[i + Wer_Spielt * 10]:
                Kreuz += 1
            if "Pik" in Hände[i + Wer_Spielt * 10]:
                Pik += 1
            if "Herz" in Hände[i + Wer_Spielt * 10]:
                Herz += 1
            if "Karo" in Hände[i + Wer_Spielt * 10]:
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
                Werte[Wer_Spielt] = (count + 1)* 12
                Werte[Wer_Spielt + 3] = "Kreuz"
            elif Trumpf == Pik:
                Werte[Wer_Spielt] = (count + 1)* 11
                Werte[Wer_Spielt + 3] = "Pik"
            elif Trumpf == Herz:
                Werte[Wer_Spielt] = (count + 1)* 10
                Werte[Wer_Spielt + 3] = "Herz"
            elif Trumpf == Karo:
                Werte[Wer_Spielt] = (count + 1)* 9
                Werte[Wer_Spielt + 3] = "Karo"

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

    global Werte # um zu merken wer alleine spielt

    if Zahlen[i] > max([Werte[0],Werte[1]]):
        Option_Ja.destroy()
        Option_Nein.destroy()
        Frage.destroy()
        Glückwunsch = Label(root, text = "Glückwunsch, du darfst alleine spielen")
        Glückwunsch.grid(row = 2, column = 0, columnspan = 2)
        Button_Beginn = Button(root, text = "Drücke,um zu beginnen", command = f_clear_Ja, bg = '#90ee90')
        Button_Beginn.grid(row = 1, column = 0, columnspan = 2)
        
        Werte[2] = 2
        
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

    global Werte # um zu merken wer alleine spielt
    
    Option_Ja.destroy()
    Option_Nein.destroy()
    Frage.destroy()
    if Werte[0] > Werte [1]:
        Bot_Spieler = Label(root, text = "Es spielt Spieler 0 alleine")
        Bot_Spieler.grid(row = 0, column = 0, columnspan = 2)
        Werte[2] = 0
    else: 
        Bot_Spieler = Label(root, text = "Es spielt Spieler 1 alleine")
        Bot_Spieler.grid(row = 0, column = 0, columnspan = 2)
        Werte[2] = 1
    Button_Beginn = Button(root, text = "Drücke,um zu beginnen", command = f_clear_Nein, bg = '#90ee90')
    Button_Beginn.grid(row = 1, column = 0, columnspan = 2)

def f_Reizen_Frage(i):
    global Zahlen
    global Option_Ja
    global Option_Nein
    global Frage
    #global wer_spielt
    Frage = Label(root, text = "Möchten Sie "+str(Zahlen[i])+" sagen?")
    Frage.grid(row = 0, column = 0, columnspan = 2)
    Option_Ja = Button(root, text = "Ja", bg = '#90ee90', command =lambda: f_Ja(i))
    Option_Ja.grid(row = 1, column = 0)
    Option_Nein = Button(root, text = "Nein", bg = '#fa8072', command = f_Nein)
    Option_Nein.grid(row = 1, column = 1)

def f_Karte_zeigen(Hände):
    global L_Karten_Zeigen
    L_Karten_Zeigen = Label(root, text = [Hände[i] for i in range(20,30)])
    L_Karten_Zeigen.grid(row = 4, column = 0, columnspan = 2)

def f_Skat_Nein():
    global L_Skat
    global B_Skat_Ja
    global B_Skat_Nein
    L_Skat.destroy()
    B_Skat_Ja.destroy()
    B_Skat_Nein.destroy()


def f_Beginn_KK_clear(): 
    global B_Beginn_KK
    B_Beginn_KK.destroy()

def f_Keine_Karte():
    global B_Beginn_KK #soll in der nächten Funktion gelöscht werden
    B_Beginn_KK = Button(root, text = "Dann kann das Spiel beginnen", command = f_Beginn_KK_clear)
    B_Beginn_KK.grid(row = 0, column = 0)

def f_Skat_Tausch(e,i): 
    # i == 0 für 1. karte im skat; i == 1 für 2. karte im Skat
    global Hände
    global L_Karten_Zeigen
    global B_Beginn_KK
    global L_Skat_Deine_Karte # soll eglöscht werden

    # k == 1 falls beide karten getauscht worden sind und im 1. durchlauf, k == 2 falls ~ und im 2. durchlauf
    L_Karten_Zeigen.destroy()
    temp = Hände[20+e]; Hände[20+e] = Hände[30+i]; Hände[30+i] = temp 
    L_Neu_Skat_0 = Label(root, text = [Hände[j] for j in range(20,30)])
    L_Neu_Skat_0.grid(row = 20, column = 0, columnspan = 20)
    
    """if k == 0: 
        B_Beginn_KK = Button(root, text = "Dann kann das Spiel beginnen", command = f_Beginn_KK_clear)
        B_Beginn_KK.grid(row = 0, column = 0)
    if k == 1:
        L_Skat_Deine_Karte.destroy()
        L_Neu_Skat_0.destroy()
        L_Skat_Deine_Karte_Neu = Label(root, text = "Du hast die " + str(Hände[30]) +" gewählt. Welche Karte möchtest du drücken?")
        L_Skat_Deine_Karte_Neu.grid(row = 0, column = 0)
        f_Skat_Karte(1, 2)
    if k == 2:
        print("k = =2")
        f_Skat_clear_1()
        f_Skat_clear_1() 
        L_Skat_Deine_Karte_Neu.destroy()
        L_Neu_Skat_0.destroy()
        L_Neu_Skat_0Neu = Label(root, text = [Hände[i] for i in range(20,30)])
        L_Neu_Skat_0Neu.grid(row = 20, column = 0, columnspan = 20)
        L_Neu_Skat_0.grid(row = 20, column = 0, columnspan = 20)
        B_Beginn_KK = Button(root, text = "Dann kann das Spiel beginnen", command = f_Beginn_KK_clear)
        B_Beginn_KK.grid(row = 5, column = 5) """
        
def f_Skat_clear_1():
    global B_Skat_Opfer_0; global B_Skat_Opfer_1; global B_Skat_Opfer_2; global B_Skat_Opfer_3; global B_Skat_Opfer_4
    global B_Skat_Opfer_5; global B_Skat_Opfer_6; global B_Skat_Opfer_7; global B_Skat_Opfer_8; global B_Skat_Opfer_9; global L_Skat_Deine_Karte

    B_Skat_Opfer_0.destroy(); B_Skat_Opfer_1.destroy(); B_Skat_Opfer_2.destroy(); B_Skat_Opfer_3.destroy(); B_Skat_Opfer_4.destroy(); B_Skat_Opfer_5.destroy(); B_Skat_Opfer_6.destroy(); B_Skat_Opfer_7.destroy(); B_Skat_Opfer_8.destroy(); B_Skat_Opfer_9.destroy(); L_Skat_Deine_Karte.destroy()

def f_Skat_Karte(i,k = "0"):
    """ i ist 0 für keine, 1 bzw. 2 für erste bzw. 2. Karte und 3 für beide"""
    """ Auswahl welche Karte abgelgegt wird"""
    global B_Skat_Opfer_0; global B_Skat_Opfer_1; global B_Skat_Opfer_2; global B_Skat_Opfer_3; global B_Skat_Opfer_4; global B_Skat_Opfer_5
    global B_Skat_Opfer_6; global B_Skat_Opfer_7; global B_Skat_Opfer_8; global B_Skat_Opfer_9; global L_Skat_Deine_Karte

    L_Skat_Deine_Karte = Label(root, text = "Du hast die " + str(Hände[30]) +" gewählt. Welche Karte möchtest du drücken?")
    L_Skat_Deine_Karte.grid(row = 0, column = 0)

    B_Skat_Opfer_0 = Button(root, text = [Hände[20]], command = lambda: [f_Skat_Tausch(0,i), f_Skat_clear_1()])
    B_Skat_Opfer_0.grid(row = 1, column = 0)
    B_Skat_Opfer_1 = Button(root, text = [Hände[21]], command = lambda: [f_Skat_Tausch(1,i), f_Skat_clear_1()])
    B_Skat_Opfer_1.grid(row = 1, column = 1)
    B_Skat_Opfer_2 = Button(root, text = [Hände[22]], command = lambda: [f_Skat_Tausch(2,i), f_Skat_clear_1()])
    B_Skat_Opfer_2.grid(row = 1, column = 2)
    B_Skat_Opfer_3 = Button(root, text = [Hände[23]], command = lambda: [f_Skat_Tausch(3,i), f_Skat_clear_1()])
    B_Skat_Opfer_3.grid(row = 1, column = 3)
    B_Skat_Opfer_4 = Button(root, text = [Hände[24]], command = lambda: [f_Skat_Tausch(4,i), f_Skat_clear_1()])
    B_Skat_Opfer_4.grid(row = 1, column = 4)
    B_Skat_Opfer_5 = Button(root, text = [Hände[25]], command = lambda: [f_Skat_Tausch(5,i), f_Skat_clear_1()])
    B_Skat_Opfer_5.grid(row = 1, column = 5)
    B_Skat_Opfer_6 = Button(root, text = [Hände[26]], command = lambda: [f_Skat_Tausch(6,i), f_Skat_clear_1()])
    B_Skat_Opfer_6.grid(row = 1, column = 6)
    B_Skat_Opfer_7 = Button(root, text = [Hände[27]], command = lambda: [f_Skat_Tausch(7,i), f_Skat_clear_1()])
    B_Skat_Opfer_7.grid(row = 1, column = 7)
    B_Skat_Opfer_8 = Button(root, text = [Hände[28]], command = lambda: [f_Skat_Tausch(8,i), f_Skat_clear_1()])
    B_Skat_Opfer_8.grid(row = 1, column = 8)
    B_Skat_Opfer_9 = Button(root, text = [Hände[29]], command = lambda: [f_Skat_Tausch(9,i), f_Skat_clear_1()])
    B_Skat_Opfer_9.grid(row = 1, column = 9)

def f_Skat_Clear_0():
    """ von f_Skat_Ja aufgerufen, falls """ 
    global L_Show_Skat_Text   # soll in der  Funktion gelöscht werden
    global L_Show_Skat_Karten; global L_welche_Karte; global B_Keine_Karte; global B_Keine_Karte; global B_2Karte; global B_1Karte; global B_Beide_Karte
    
    L_Show_Skat_Text.destroy()   # soll in der Funktion gelöscht werden
    L_Show_Skat_Karten.destroy(); L_welche_Karte.destroy(); B_Keine_Karte.destroy(); B_Keine_Karte.destroy()
    B_2Karte.destroy(); B_1Karte.destroy(); B_Beide_Karte.destroy()

def f_Skat_Beide(i): 
    # Skat in die Skat tun
    global  Wie_Oft_Durchlaufen_Skat
    global  L_Karten_Zeigen; global L_Show_Skat_Karten_Beide
    temp_Skat_Beide = Hände[20 + int(i)]; Hände[20 + int(i)] = Hände[30+Wie_Oft_Durchlaufen_Skat]; Hände[30 + Wie_Oft_Durchlaufen_Skat] = temp_Skat_Beide
    
    L_Show_Skat_Karten_Beide = Label(root, text = [Hände[i] for i in range(20,30)], bg = "green")
    L_Show_Skat_Karten_Beide.grid(row = 8, column = 0)
    L_Karten_Zeigen.destroy()
    
    # zum löschen
    global B_Skat_Opfer_0; global B_Skat_Opfer_1; global B_Skat_Opfer_2; global B_Skat_Opfer_3; global B_Skat_Opfer_4; global B_Skat_Opfer_5; global B_Skat_Opfer_6; global B_Skat_Opfer_7; global B_Skat_Opfer_8; global B_Skat_Opfer_9; 

    global L_Skat_Deine_Karte_Beide #; global L_Show_Skat_Karten
    if Wie_Oft_Durchlaufen_Skat > 0:
        L_Show_Skat_Karten_Beide.destroy()
        L_Show_Skat_Karten_Beide.destroy()
        L_Show_Skat_Karten_Beide.destroy()
        L_Skat_Deine_Karte_Beide.destroy()
        B_Skat_Opfer_0.destroy(); B_Skat_Opfer_1.destroy(); B_Skat_Opfer_2.destroy(); B_Skat_Opfer_3.destroy(); B_Skat_Opfer_4.destroy(); B_Skat_Opfer_5.destroy(); B_Skat_Opfer_6.destroy(); B_Skat_Opfer_7.destroy(); B_Skat_Opfer_8.destroy(); B_Skat_Opfer_9.destroy(); 
        L_Show_Skat_Karten_Beide_Neu = Label(root, text = [Hände[i] for i in range(20,30)])
        L_Show_Skat_Karten_Beide_Neu.grid(row = 9, column = 0)
    Wie_Oft_Durchlaufen_Skat += 1

def f_Beide_Karte():
    """falls er beide Karten haben möchte"""
    global L_Show_Skat_Text; global L_Show_Skat_Karten; global L_welche_Karte; global B_Keine_Karte; global B_Keine_Karte 
    global B_2Karte; global B_1Karte; global B_Beide_Karte; global L_Skat_Deine_Karte_Beide

    L_Show_Skat_Text.destroy(); L_Show_Skat_Karten.destroy(); L_welche_Karte.destroy(); B_Keine_Karte.destroy()
    B_Keine_Karte.destroy(); B_2Karte.destroy(); B_1Karte.destroy(); B_Beide_Karte.destroy()
    
    #global k 
    #k = 0 # Zählt wie viele Karten ausgewählt worden sind 
    global temp_Beide_Karten 
    temp_Beide_Karten = []
    # Auswahl von 2 Karten 
    L_Skat_Deine_Karte_Beide = Label(root, text = "Du hast die " + str(Hände[30]) +" und die " + str(Hände[31]) +" gewählt. Welche Karten möchtest du drücken?")
    L_Skat_Deine_Karte_Beide.grid(row = 0, column = 0)
    
    #global machen, um sie danach zu löschen
    global B_Skat_Opfer_0; global B_Skat_Opfer_1; global B_Skat_Opfer_2; global B_Skat_Opfer_3; global B_Skat_Opfer_4; global B_Skat_Opfer_5; global B_Skat_Opfer_6; global B_Skat_Opfer_7; global B_Skat_Opfer_8; global B_Skat_Opfer_9; 

    global Wie_Oft_Durchlaufen_Skat
    Wie_Oft_Durchlaufen_Skat= 0

    B_Skat_Opfer_0 = Button(root, text = [Hände[20]], command = lambda: f_Skat_Beide(0))
    B_Skat_Opfer_0.grid(row = 1, column = 0)
    B_Skat_Opfer_1 = Button(root, text = [Hände[21]], command = lambda: f_Skat_Beide(1))
    B_Skat_Opfer_1.grid(row = 1, column = 1)
    B_Skat_Opfer_2 = Button(root, text = [Hände[22]], command = lambda: f_Skat_Beide(2))
    B_Skat_Opfer_2.grid(row = 1, column = 2)
    B_Skat_Opfer_3 = Button(root, text = [Hände[23]], command = lambda: f_Skat_Beide(3))
    B_Skat_Opfer_3.grid(row = 1, column = 3)
    B_Skat_Opfer_4 = Button(root, text = [Hände[24]], command = lambda: f_Skat_Beide(4))
    B_Skat_Opfer_4.grid(row = 1, column = 4)
    B_Skat_Opfer_5 = Button(root, text = [Hände[25]], command = lambda: f_Skat_Beide(5))
    B_Skat_Opfer_5.grid(row = 1, column = 5)
    B_Skat_Opfer_6 = Button(root, text = [Hände[26]], command = lambda: f_Skat_Beide(6))
    B_Skat_Opfer_6.grid(row = 1, column = 6)
    B_Skat_Opfer_7 = Button(root, text = [Hände[27]], command = lambda: f_Skat_Beide(7))
    B_Skat_Opfer_7.grid(row = 1, column = 7)
    B_Skat_Opfer_8 = Button(root, text = [Hände[28]], command = lambda: f_Skat_Beide(8))
    B_Skat_Opfer_8.grid(row = 1, column = 8)
    B_Skat_Opfer_9 = Button(root, text = [Hände[29]], command = lambda: f_Skat_Beide(9))
    B_Skat_Opfer_9.grid(row = 1, column = 9)


def f_Skat_Ja():
    "Der Skat wird aufgeomen, welche Karten möchte er haben"
    global L_Skat # zum löschen 
    global B_Skat_Ja; global B_Skat_Nein
    
    global Hände # wird in der Funktion genutzt 

    global L_Show_Skat_Text   # soll in der nächten Funktion gelöscht werden
    global L_Show_Skat_Karten; global L_welche_Karte; global B_Keine_Karte; global B_Keine_Karte; global B_2Karte; global B_1Karte; global B_Beide_Karte

    L_Skat.destroy(); B_Skat_Ja.destroy(); B_Skat_Nein.destroy()
    
    L_Show_Skat_Text = Label(root, text = "Dies ist der Skat:")
    L_Show_Skat_Text.grid(row = 1, column = 0)
    L_Show_Skat_Karten = Label(root, text = [Hände[i] for i in range(30,32)])
    L_Show_Skat_Karten.grid(row = 1, column = 1)

    L_welche_Karte = Label(root, text = " welche Karte möchtest du haben?")
    L_welche_Karte.grid(row = 2, column = 0, columnspan = 2)
    
    B_Keine_Karte = Button(root, text = "Keine", command = lambda:[f_Skat_Clear_0(), f_Keine_Karte()])
    B_Keine_Karte.grid(row = 3, column = 0)

    B_1Karte = Button(root, text = [Hände[30]], command = lambda:[f_Skat_Clear_0(), f_Skat_Karte(0)])
    B_1Karte.grid(row = 3, column = 1)

    B_2Karte = Button(root, text = [Hände[31]], command = lambda:[f_Skat_Clear_0(), f_Skat_Karte(1)])
    B_2Karte.grid(row = 3, column = 2)
    
    B_Beide_Karte = Button(root, text = "beide", command = lambda:[f_Skat_Clear_0(), f_Beide_Karte()])
    B_Beide_Karte.grid(row = 3, column = 3)



def f_Skat(): 
    """ wird von f_Reizen_Frage aufgerufen"""
    global L_Skat
    global B_Skat_Ja
    global B_Skat_Nein
    Skat = [Hände[i] for i in range(30,32)]
    L_Skat = Label(root, text = "möchtest du den Skat aufnehmen?")
    L_Skat.grid(row = 0, column = 0, columnspan = 2)
    B_Skat_Ja = Button(root, text = "Ja", bg = '#90ee90', command = f_Skat_Ja)
    B_Skat_Ja.grid(row = 1, column = 0)
    B_Skat_Nein = Button(root, text = "Nein", bg = '#fa8072', command = f_Skat_Nein)
    B_Skat_Nein.grid(row = 1, column = 1)



#Hände = ["Kreuz Bube","Pik Bube", "Herz Bube", "Karo Bube", "Karo Ass","Kreuz 10","Kreuz König","Kreuz Dame","Kreuz 9","Kreuz 8","Kreuz 7","Pik Ass","Pik 10","Pik König","Pik Dame","Pik 9","Pik 8","Pik 7", "Herz Ass","Herz 10","Herz König","Herz Dame","Herz 9","Herz 8","Herz 7","Karo Ass","Karo 10","Karo König","Karo Dame","Karo 9","Karo 8","Karo 7"]
#Werte = [0,0,1, "Pik", "Karo"]

def Bot_Skat():
    """ Auswahl der Karten, die der Botaufnimmt"""
    global Hände
    global Werte

    Kreuz = 0; Pik = 0; Herz = 0; Karo = 0

    Bot_Skat = [Hände[i] for i in range(0+Werte[2]*10,10+Werte[2]*10)] + [Hände[30]] + [Hände[31]]
    Bot_Skat_Value = [0 for i in range(12)]

    for i in range(12):
        """ Zählen einiger Werte, die in der 2. Schleife genutzt werden"""
        if "Kreuz" in Bot_Skat[i]:
            Kreuz += 1  
        if "Pik" in Bot_Skat[i]:
            Pik += 1 
        if "Herz" in Bot_Skat[i]:
            Herz += 1 
        if "Karo" in Bot_Skat[i]:
            Karo += 1 

    Skat_Farben = [Kreuz, Pik, Herz, Karo]
    Skat_Farben_Value = [0,0,0,0] # ob die Farbe gedrückt ewrden sollte

    for i in range(12):
        if "Bube" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 1000000 # es ist illegal Buben zu drücken daher sollte dieser Wert niemals von anderen übertroffen werden
        if "Ass" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 1000
            if "Kreuz Ass" in Bot_Skat[i]:    # es soll keine Farbe gedrückt werden von der man ein Ass hat
                Skat_Farben_Value[0] = 100
            if "Pik Ass" in Bot_Skat[i]:
                Skat_Farben_Value[1] = 100
            if "Herz Ass" in Bot_Skat[i]:
                Skat_Farben_Value[2] = 100
            if "Karo Ass" in Bot_Skat[i]:
                Skat_Farben_Value[3] = 100
        if "10" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 80
        if "König" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 65
        if "Dame" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 60
        if "9" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 55
        if "8" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 53
        if "7" in Bot_Skat[i]:
            Bot_Skat_Value[i] = 51
        if str(Werte[Werte[2]+3]) in Bot_Skat[i]: # Trumpfkarte
            Bot_Skat_Value[i] =int(Bot_Skat_Value[i]) + 40

        #if "10" in Bot_Skat[i] and str(Hände[5])[:-3] == 1: # 'blanke 10'
        #    Bot_Skat_Value[i] = 0
    
    for i in range(4): # punkte, falls man eine Farbe drücken kann
        if Skat_Farben[i] == 1 and Skat_Farben[i] != Werte[3+Werte[2]] and Skat_Farben_Value[i] < 100: # nicht Trumpf  und kein Ass 
            Skat_Farben_Value[i] += -200 
        if Skat_Farben[i] == 2 and Skat_Farben[i] != Werte[3+Werte[2]] and Skat_Farben_Value[i] < 100: # nicht Trumpf # eigendlich eh nicht mgl.  und kein Ass 
            Skat_Farben_Value[i] += -80 

    for i in range(12):
        if "Kreuz" in Bot_Skat[i]:
            Bot_Skat_Value[i] = Kreuz * 20
        if "Pik" in Bot_Skat[i]:
            Bot_Skat_Value[i] += Pik * 20
        if "Herz" in Bot_Skat[i]:
            Bot_Skat_Value[i] += Herz * 20
        if "Karo" in Bot_Skat[i]:
            Bot_Skat_Value[i] += Karo * 20 
    #finden der beiden Werte mit dem niedrigsten score
    Skat_min0_Value = min(Bot_Skat_Value); Skat_min0_ind = Bot_Skat_Value.index(Skat_min0_Value);Bot_Skat_Value[Skat_min0_ind] = 400
    Skat_min1_Value = min(Bot_Skat_Value); Skat_min1_ind = Bot_Skat_Value.index(Skat_min1_Value)

    # drücken: 
    temp_Skat_Bot_0 = Hände[Werte[2] * 10 + Skat_min0_ind]; Hände[Werte[2] * 10 + Skat_min0_ind] = Hände[30]; Hände[30] = temp_Skat_Bot_0
    temp_Skat_Bot_1 = Hände[Werte[2] * 10 + Skat_min1_ind]; Hände[Werte[2] * 10 + Skat_min0_ind] = Hände[31]; Hände[31] = temp_Skat_Bot_1

def f_Trumpf_Speichern(Farbe):
    global Trumpf_Farbe # hier wird gespeicht was trumpf ist und 

    # zum löschen
    global L_Trumpf_Frage; global B_Trumpf_Frage_Kreuz; global B_Trumpf_Frage_Pik; global B_Trumpf_Frage_Herz; global B_Trumpf_Frage_Karo; 
    L_Trumpf_Frage.destroy(); B_Trumpf_Frage_Kreuz.destroy(); B_Trumpf_Frage_Pik.destroy();B_Trumpf_Frage_Herz.destroy();B_Trumpf_Frage_Karo.destroy();

    Trumpf_Farbe = Farbe

def  f_Trumpf_Frage():
    """ fragt welche Farbe trumpf sein soll und ruft dann F_Trumpf_Speichern auf, um dies zu Speichern und und die widges zu löschen """
    # global machen, um sie in der aufzurufenden Funktion zu löschen
    global L_Trumpf_Frage; global B_Trumpf_Frage_Kreuz; global B_Trumpf_Frage_Pik; global B_Trumpf_Frage_Herz; global B_Trumpf_Frage_Karo; 
    B_Trumpf_Frage_Kreuz.destroy(); B_Trumpf_Frage_Pik.destroy();B_Trumpf_Frage_Herz.destroy();B_Trumpf_Frage_Karo.destroy();

    L_Trumpf_Frage = Label(root, text = "Welche Farbe soll Trumpf sein?")
    L_Trumpf_Frage.grid(row = 0, column = 0, columnspan = 4)
    
    B_Trumpf_Frage_Kreuz = Button(root, text = "Kreuz", comamnd = lambda: f_Trumpf_Speichern(Kreuz))
    B_Trumpf_Frage_Kreuz.grid(row = 0, column = 0)
    B_Trumpf_Frage_Pik = Button(root, text = "Pik", comamnd = lambda: f_Trumpf_Speichern(Pik))
    B_Trumpf_Frage_Pik.grid(row = 0, column = 1)
    B_Trumpf_Frage_Herz = Button(root, text = "Herz", comamnd = lambda: f_Trumpf_Speichern(Herz))
    B_Trumpf_Frage_Herz.grid(row = 0, column = 2)
    B_Trumpf_Frage_Karo = Button(root, text = "Karo", comamnd = lambda: f_Trumpf_Speichern(Karo))
    B_Trumpf_Frage_Karo.grid(row = 0, column = 3)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        # Hauptspiel





def f_Wer_Gewinnt():
    "gibt den Spieler zurück der den Stich gewinnt, nimmt die Karten in der Reinfolge, wie sie gelegt worde sind und gibt auch den Spieler zurück der "

def f_Haupt(): 
    return



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        # Aufrufen der Funktionen
def f_Spiel():
    global Hände
    global Werte 
    #global wer_spielt
    Hände = f_Karten() # Karten geben; gibt Karten als Liste zurück in der Spieler 1 2 3 und dann der Skat steht (eine lange Liste)
    Werte = f_alleine(Hände)
    f_Karte_zeigen(Hände)
    f_Reizen_Frage(0) # ruft f_skat auf
        print("1")
        if Werte[2] == 0 or Werte[2] == 1: #Bots spielen alleine --> bot nimmt skat auf 
            Bot_Skat() 
        print(Werte[2])
        if Werte[2] == 2: 
            f_Trumpf_Frage()
    
    f_Haupt
    root.mainloop() 
f_Spiel()