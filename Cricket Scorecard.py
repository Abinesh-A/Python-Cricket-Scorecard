import random
import operator
from tkinter import *

window = Tk()
window.geometry('500x500')
window.resizable(0, 0)
window.title('Teams and Players Selection')
Label(window, text="GIVE TEAM AND PLAYERS NAMES", font="rockwell 15 bold").place(x=90, y=0)
Label(window, text="TEAM 1", font="rockwell 15 bold", fg="white", bg="red").place(x=50, y=30)
Label(window, text="TEAM 2", font="rockwell 15 bold", fg="white", bg="blue").place(x=330, y=30)
team1 = StringVar()
team2 = StringVar()
team1_enter = Entry(window, textvariable=team1).place(x=50, y=65)
team2_enter = Entry(window, textvariable=team2).place(x=330, y=65)

def ac(*arg):
    team1.set(team1.get().upper())
    team2.set(team2.get().upper())

team1.trace("rwua", ac)
team2.trace("rwua", ac)
Label(window, text="Vs", font="roman 20 bold").place(x=230, y=60)
Label(window, text="PLAYERS", font="rockwell 10 bold", fg="black", bg="gray").place(x=60, y=90)
Label(window, text="PLAYERS", font="rockwell 10 bold", fg="black", bg="gray").place(x=300, y=90)
teamplayers1 = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                StringVar(), StringVar(), StringVar()]
teamplayers2 = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                StringVar(), StringVar(), StringVar()]
j = 90
for i in range(11):
    teamplayers1_entry = Entry(window, textvariable=teamplayers1[i]).place(x=60, y=j + 30)
    j += 30
j = 90
for i in range(11):
    teamplayers2_entry = Entry(window, textvariable=teamplayers2[i]).place(x=300, y=j + 30)
    j += 30

global window2, tosswon, visitbat, visitbowl, frombat, frombowl,k
visitbat = 0
visitbowl = 0
frombat = 0
frombowl = 0
k=0

def checkname():
    global k
    k=0
    for i in range(11):
        if teamplayers1[i].get():
            k += 1
    print(k)
    flag = 0
    for i in range(k):
        for j in range(i + 1, k):
            if teamplayers1[i].get() == teamplayers1[j].get():
                flag += 1
                break
            if teamplayers2[i].get() == teamplayers2[j].get():
                flag += 1
                break
    print(flag)
    if flag>=1:Label(window, text="Names are repeated", font="bold").place(x=150, y=90)
    elif k<4:Label(window, text="Give atleast 4 players", font="bold").place(x=145, y=90)
    else:
        if team1.get() and team2.get():
            toss()
        else:
            Label(window, text="Type team name", font="bold").place(x=160, y=90)


global overs, tosswon
tosswon = StringVar()


def toss():
    window.destroy()
    global window2, tosswon, overs, k
    window2 = Tk()
    window2.geometry('500x200')
    window2.title('Toss')
    window2.columnconfigure(0, weight=1)
    window2.resizable(0, 0)

    def t():
        global tosswon
        tosses = [team1.get(), team2.get()]
        tosswon = random.choice(tosses)
        if tosswon == team1.get():
            Label(window2, text=tosswon, font="rockwell  15 bold", fg="white", bg="red").place(x=222, y=5)
        elif tosswon == team2.get():
            Label(window2, text=tosswon, font="rockwell  15 bold", fg="white", bg="blue").place(x=222, y=5)

    def select(n):
        global tosswon
        tosswon = StringVar()
        tosswon = n
        if tosswon == team1.get():
            Label(window2, text=tosswon, font="rockwell  15 bold", fg="white", bg="red").place(x=222, y=5)
        elif tosswon == team2.get():
            Label(window2, text=tosswon, font="rockwell  15 bold", fg="white", bg="blue").place(x=222, y=5)

    Button(window2, text="Toss", font="rockwell 13 bold", fg="black", bg="white", command=t).place(x=10, y=90)
    Label(window2, text="Manual:").place(x=5, y=5)
    Button(window2, text=team1.get(), font="rockwell 13 bold", fg="black", bg="white",
           command=lambda: select(team1.get())).place(x=10, y=20)
    Button(window2, text=team2.get(), font="rockwell 13 bold", fg="black", bg="white",
           command=lambda: select(team2.get())).place(x=10, y=55)
    Label(window2, text="won the toss", font="rockwell  15 bold", fg="black").place(x=180, y=30)
    overs = IntVar()
    Label(window2, text="Select the number of over", font="bold").place(x=155, y=60)
    overs_entry = Entry(window2, textvariable=overs).place(x=180, y=90)
    Button(window2, text=" BATTING ", font="rockwell 15 bold", bg="gray", command=choosebatsman).place(x=70, y=130)
    Button(window2, text="BOWLLING", font="rockwell 15 bold", bg="gray", command=choosebowler).place(x=300, y=130)


Button(window, text="NEXT", font="rockwell 15 italic", fg="white", bg="black",borderwidth=5,command=checkname).place(x=200, y=450)

global window3, playdone
playdone = 0


def choosebatsman():
    global teamplayers1, window3, window2, tosswon, teamplayers2, visitbat, visitbowl, team2, team1, overs, window4, frombat, frombowl, fromplay
    global striker, non_striker, fromstriker1, fromstriker2, window5, playdone, k
    if overs.get() >= 1 and overs.get() is not None and (tosswon == team1.get() or tosswon == team2.get()):
        visitbat = 1
        if fromplay == 0:
            if visitbowl == 0:
                if playdone == 0:
                    window2.destroy()
            else:
                window4.destroy()
        window3 = Tk()
        window3.geometry('400x450')
        window3.title('player choosing')
        window3.resizable(0, 0)
        Label(window3, text="CHOOSE THA PLAYER FOR BATTING", font="comicsamms 15 bold").place(x=20, y=5)
        global label1
        label1 = Label(window3, text="")

        def showbat():
            global label1, window3, batsman, visitbat, visitbowl, frombat, frombowl, striker, non_striker, fromstriker1, fromstriker2, window5
            global team1isbat, team2isbat, team1isbowl, team2isbowl, fromplay, playdone
            count = 0
            batsman = []
            cname = lb.curselection()
            for i in cname:
                op = lb.get(i)
                batsman.append(op)
                count += 1
            if count == 2 or count == 1:
                for val in batsman:
                    print(val)
                if visitbowl == 0:
                    choosebowler()
                else:
                    frombat = 1
                    if fromplay == 1:
                        if fromstriker1 == 1:
                            fromstriker1 = 0
                            striker = Label(window5, text=batsman[0], font="rockwell 15 bold")
                            striker.place(x=20, y=35)
                            window3.destroy()
                        else:
                            fromstriker2 = 0
                            non_striker = Label(window5, text=batsman[0], font="rockwell 15 bold")
                            non_striker.place(x=20, y=70)
                            window3.destroy()
                    else:
                        play()
            else:
                label1.destroy()
                label1 = Label(window3, text="")
                label1.config(text="Select only 2 player", font="rockwell 15")
                label1.place(x=110, y=300)

        lb = Listbox(window3, selectmode="multiple", height=11)
        lb.pack(padx=20, pady=70, fill="both")
        for i in range(k):
            if fromplay == 0 and playdone == 0:
                if tosswon == team1.get():
                    if visitbowl == 1:
                        lb.insert(END, teamplayers2[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
                    else:
                        lb.insert(END, teamplayers1[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
                elif tosswon == team2.get():
                    if visitbowl == 1:
                        lb.insert(END, teamplayers1[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
                    else:
                        lb.insert(END, teamplayers2[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
            elif team1isbat == 1:
                lb.insert(END, teamplayers1[i].get())
                lb.itemconfig(i, bg="#bdc1d6")
            elif team2isbat == 1:
                lb.insert(END, teamplayers2[i].get())
                lb.itemconfig(i, bg="#bdc1d6")
        Button(window3, text="Select", font="rockwell 15 bold", command=showbat).place(x=160, y=350)

    else:
        if tosswon != team1.get() and tosswon != team2.get():
            Label(window2, text="*select toss won team", font="bold", fg="red").place(x=300, y=5)
        elif overs.get() is None or overs.get() <= 0:
            Label(window2, text="*Type the overs", font="bold", fg="red").place(x=210, y=90)


global window4, fromplay, bowlerlabel1
fromplay = 0


def choosebowler():
    global teamplayers1, window4, label2, teamplayers2, tosswon, visitbat, visitbowl, team2, team1, overs, window2, window3, frombat, frombowl
    global fromplay, window5, bowlerlabel, k
    if overs.get() >= 1 and overs.get() is not None and (tosswon == team1.get() or tosswon == team2.get()):
        visitbowl = 1
        if fromplay == 0:
            if visitbat == 0:
                if playdone == 0:
                    window2.destroy()
            else:
                window3.destroy()
        window4 = Tk()
        window4.geometry('400x450')
        window4.title('player choosing')
        window4.resizable(0, 0)
        Label(window4, text="CHOOSE THA PLAYER FOR BOWLING", font="comicsamms 15 bold").place(x=20, y=5)
        global label2
        label2 = Label(window4, text="")

        def showbowl():
            global label2, window4, bowler, visitbat, visitbowl, frombat, frombowl, window5, bowlerlabel, fromplay, team1isbat, team2isbat, team1isbowl, team2isbowl
            global playdone
            count = 0
            bowler = []
            cname = lb.curselection()
            for i in cname:
                op = lb.get(i)
                bowler.append(op)
                count += 1
            if count == 1:
                for val in bowler:
                    print(val)
                if visitbat == 0:
                    choosebatsman()
                else:
                    frombowl = 1
                    if fromplay == 1:
                        bowlerlabel = Label(window5, text=bowler[0], font="rockwell 15 bold")
                        bowlerlabel.place(x=240, y=35)
                        window4.destroy()
                    else:
                        play()
            else:
                label2.destroy()
                label2 = Label(window4, text="")
                label2.config(text="Select only 1 player", font="rockwell 15")
                label2.place(x=110, y=300)

        lb = Listbox(window4, selectmode="multiple", height=11)
        lb.pack(padx=20, pady=70, fill="both")
        for i in range(k):
            if fromplay == 0 and playdone == 0:
                if tosswon == team1.get():
                    if visitbat == 1:
                        lb.insert(END, teamplayers2[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
                    else:
                        lb.insert(END, teamplayers1[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
                elif tosswon == team2.get():
                    if visitbat == 1:
                        lb.insert(END, teamplayers1[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
                    else:
                        lb.insert(END, teamplayers2[i].get())
                        lb.itemconfig(i, bg="#bdc1d6")
            elif team1isbowl == 1:
                lb.insert(END, teamplayers1[i].get())
                lb.itemconfig(i, bg="#bdc1d6")
            elif team2isbowl == 1:
                lb.insert(END, teamplayers2[i].get())
                lb.itemconfig(i, bg="#bdc1d6")
        Button(window4, text="Select", font="rockwell 15 bold", command=showbowl).place(x=160, y=350)
    else:
        if tosswon != team1.get() and tosswon != team2.get():
            Label(window2, text="*select toss won team", font="bold", fg="red").place(x=300, y=5)
        elif overs.get() is None or overs.get() <= 0:
            Label(window2, text="*Type the overs", font="bold", fg="red").place(x=210, y=90)


global window5, ball, completeover, totalscore, player1over, player2over, player1score, player2score, bowlball, completeoverbowl, widerun
global bowlerlabel, striker, non_striker, striker1, striker2, fromstriker1, fromstriker2, overball
global team1isbat, team2isbat, team1isbowl, team2isbowl, count, count2, wicket1, wicket2, nb, nb1, widerun1
global team1batscore, team2batscore, team1bowlscore, team2bowlscore, fromout, tsbowl, in1score, fromchas, fromdefend
completeoverbowl = IntVar()
bowlball = IntVar()
totalscore = IntVar()
tsbowl = IntVar()
completeover = IntVar()
ball = IntVar()
player1score = IntVar()
player2score = IntVar()
player1over = IntVar()
player2over = IntVar()
widerun = IntVar()
fromstriker1 = 0
fromstriker2 = 0
count = 0
count2 = 0
team1batscore = {}
team2batscore = {}
team1bowlscore = {}
team2bowlscore = {}
fromout = 0
in1score = IntVar()
wicket1 = 0
wicket2 = 0
fromchas = 0
fromdefend = 0
nb = IntVar()
overball = 0


def play():
    global window5, batsman, bowler, ball, completeover, totalscore, player1over, player2over, player1score, player2score, bowlball, completeoverbowl, tsbowl, in1score, overball
    global strike1, strike2, visitbat, visitbowl, window3, window4, frombat, frombowl, fromplay, widerun, bowlerlabel, striker, non_striker, fromstriker1, fromstriker2
    global tosswon, overs, team1isbat, team2isbat, team1isbowl, team2isbowl, overs, playdone, count, count2, team1batscore, team2batscore, team1bowlscore, team2bowlscore
    if playdone == 1:
        completeoverbowl.set(0)
        bowlball.set(0)
        totalscore.set(0)
        tsbowl.set(0)
        completeover.set(0)
        ball.set(0)
        player1score.set(0)
        player2score.set(0)
        player1over.set(0)
        player2over.set(0)
        widerun.set(0)
        nb.set(0)
    fromplay = 1
    if frombat == 1 and playdone == 0:
        window3.destroy()
    elif frombowl == 1:
        window4.destroy()

    window5 = Tk()
    window5.geometry('440x450')
    window5.title('score pannel')
    window5.resizable(0, 0)
    Label(window5, text="BATSMAN:", font="rockwell 17 bold").grid()
    Label(window5, text="BOWLER:", font="rockwell 17 bold").place(x=240, y=0)
    striker = Label(window5, text=batsman[0], font="rockwell 15 bold")
    striker.place(x=20, y=35)
    non_striker = Label(window5, text=batsman[1], font="rockwell 15 bold")
    non_striker.place(x=20, y=70)
    bowlerlabel = Label(window5, text=bowler[0], font="rockwell 15 bold")
    bowlerlabel.place(x=240, y=35)
    t_overbowler = Label(window5, text=str(completeoverbowl.get()) + "." + str(bowlball.get()), font="rockwell 15 bold",
                         bg="white")
    t_overbowler.place(x=360, y=35)
    Label(window5, text="Extras:", font="rockwell 15 bold").place(x=20, y=120)
    t_wide = Label(window5, text=widerun.get(), font="rockwell 15 bold", bg="white")
    t_wide.place(x=160, y=120)
    Label(window5, text="Total score:", font="rockwell 15 bold").place(x=20, y=150)
    t_score = Label(window5, text=totalscore.get(), font="rockwell 15 bold", bg="white")
    t_score.place(x=160, y=150)
    Label(window5, text="Over          :", font="rockwell 15 bold").place(x=20, y=180)
    t_over = Label(window5, text=str(completeover.get()) + "." + str(ball.get()), font="rockwell 15 bold", bg="white")
    t_over.place(x=160, y=180)
    score1 = Label(window5, text=str(player1score.get()) + "(" + str(player1over.get()) + ")", font="rockwell 15 bold",
                   bg="white")
    score1.place(x=160, y=35)
    score2 = Label(window5, text=str(player2score.get()) + "(" + str(player2over.get()) + ")", font="rockwell 15 bold",
                   bg="white")
    score2.place(x=160, y=70)
    strike = Label(window5, text="#", font="rockwell 15 bold", fg="red", bg="white")
    if playdone == 1:
        overball = overs.get() * 6
        notice = Label(window5,
                       text="Need " + str(in1score.get() - totalscore.get()) + " run'd from " + str(overball) + " ball's",
                       font="rockwell 15 italic bold")
        notice.place(x=20, y=400)
    strike1 = 1
    strike2 = 0
    teambat1 = 0
    teambat2 = 0
    teambowl1 = 0
    teambowl2 = 0
    team1isbat = 0
    team2isbat = 0
    team1isbowl = 0
    team2isbowl = 0
    if playdone == 0:
        if tosswon == team1.get():
            if frombat == 1:
                teambowl1 = 1
                teambat2 = 1
                for i in range(k):
                    team1bowlscore[teamplayers1[i].get()] = [0, 0, 0, 0]
                    team1isbowl = 1
                    team2batscore[teamplayers2[i].get()] = [0, 0, 0]
                    team2isbat = 1
            elif frombowl == 1:
                teambowl2 = 1
                teambat1 = 1
                for i in range(k):
                    team2bowlscore[teamplayers2[i].get()] = [0, 0, 0, 0]
                    team2isbowl = 1
                    team1batscore[teamplayers1[i].get()] = [0, 0, 0]
                    team1isbat = 1
        if tosswon == team2.get():
            if frombowl == 1:
                teambowl1 = 1
                teambat2 = 1
                for i in range(k):
                    team1bowlscore[teamplayers1[i].get()] = [0, 0, 0, 0]
                    team1isbowl = 1
                    team2batscore[teamplayers2[i].get()] = [0, 0, 0]
                    team2isbat = 1
            elif frombat == 1:
                teambowl2 = 1
                teambat1 = 1
                for i in range(k):
                    team2bowlscore[teamplayers2[i].get()] = [0, 0, 0, 0]
                    team2isbowl = 1
                    team1batscore[teamplayers1[i].get()] = [0, 0, 0]
                    team1isbat = 1
    elif count == 1:
        teambowl1 = 1
        teambat2 = 1
        for i in range(k):
            team1bowlscore[teamplayers1[i].get()] = [0, 0, 0, 0]
            team1isbowl = 1
            team2batscore[teamplayers2[i].get()] = [0, 0, 0]
            team2isbat = 1
    elif count2 == 1:
        teambowl2 = 1
        teambat1 = 1
        for i in range(k):
            team2bowlscore[teamplayers2[i].get()] = [0, 0, 0, 0]
            team2isbowl = 1
            team1batscore[teamplayers1[i].get()] = [0, 0, 0]
            team1isbat = 1

    print(team1bowlscore)
    print(team2bowlscore)
    print(team1batscore)
    print(team2batscore)

    def function(n):
        global ball, completeover, completeoverbowl, strike1, strike2, bowlball, totalscore, visitbat, visitbowl, bowler, bowlerlabel
        global frombat, frombowl, fromnb, overs, team1isbat, team2isbat, team1isbowl, team2isbowl, fromplay, playdone, overball
        global team1batscore, team2batscore, team1bowlscore, team2bowlscore, count, count2, fromout, tsbowl, fromchas, fromdefend
        if completeover.get() != overs.get():
            if strike1 == 0:
                player1score.set(player1score.get() + n)
                player1over.set(player1over.get() + 1)
                score1.config(text=str(player1score.get()) + "(" + str(player1over.get()) + ")",
                              font="rockwell 15 bold",
                              bg="white")
                if teambat1 == 1:
                    team1batscore[batsman[0]] = [0, player1score.get(), player1over.get()]
                else:
                    team2batscore[batsman[0]] = [0, player1score.get(), player1over.get()]
            else:
                player2score.set(player2score.get() + n)
                player2over.set(player2over.get() + 1)
                score2.config(text=str(player2score.get()) + "(" + str(player2over.get()) + ")",
                              font="rockwell 15 bold",
                              bg="white")
                if fromout == 0:
                    if teambat2 == 1:
                        team2batscore[batsman[1]] = [0, player2score.get(), player2over.get()]
                    elif teambat1 == 1:
                        team1batscore[batsman[1]] = [0, player2score.get(), player2over.get()]
                else:
                    if teambat1 == 1:
                        team1batscore[batsman[0]] = [0, player2score.get(), player2over.get()]
                    else:
                        team2batscore[batsman[0]] = [0, player2score.get(), player2over.get()]

            totalscore.set(totalscore.get() + n)
            tsbowl.set(tsbowl.get() + n)
            t_score.config(text=totalscore.get(), font="rockwell 15 bold", bg="white")
            if in1score.get() < totalscore.get() and playdone == 1:
                fromchas = 1
                theend()
        else:
            Label(window5, text="1st round over", font="rockwell 30 bold").place(x=700, y=200)
        if fromnb == 0:
            if completeover.get() != overs.get():
                if ball.get() < 5 and bowlball.get() < 5:
                    ball.set(ball.get() + 1)
                    overball -= 1
                    if playdone == 1:
                        notice.config(
                            text="Need " + str(in1score.get() - totalscore.get()) + " run's from " + str(overball) + " ball's")
                    if teambowl1 == 1:
                        team1bowlscore[bowler[0]][1] = team1bowlscore[bowler[0]][1] + 1
                        team1bowlscore[bowler[0]][3] = tsbowl.get()
                        t_overbowler.config(text=str(team1bowlscore[bowler[0]][0]) + "." + str(
                            team1bowlscore[bowler[0]][1]) + "/" + str(team1bowlscore[bowler[0]][2]) + "-" + str(
                            team1bowlscore[bowler[0]][3]),
                                            font="rockwell 15 bold",
                                            bg="white")
                    else:
                        team2bowlscore[bowler[0]][1] = team2bowlscore[bowler[0]][1] + 1
                        team2bowlscore[bowler[0]][3] = tsbowl.get()
                        t_overbowler.config(text=str(team2bowlscore[bowler[0]][0]) + "." + str(
                            team2bowlscore[bowler[0]][1]) + "/" + str(team2bowlscore[bowler[0]][2]) + "-" + str(
                            team2bowlscore[bowler[0]][3]),
                                            font="rockwell 15 bold",
                                            bg="white")
                    t_over.config(text=str(completeover.get()) + "." + str(ball.get()), font="rockwell 15 bold",
                                  bg="white")

                else:
                    completeover.set(completeover.get() + 1)
                    overball -= 1
                    if playdone == 1:
                        notice.config(
                            text="Need " + str(in1score.get() - totalscore.get()) + " run's from " + str(overball) + " ball's")
                    if teambowl1 == 1:
                        team1bowlscore[bowler[0]] = [team1bowlscore[bowler[0]][0] + 1, 0, team1bowlscore[bowler[0]][2],
                                                     tsbowl.get()]
                    else:
                        team2bowlscore[bowler[0]] = [team2bowlscore[bowler[0]][0] + 1, 0, team2bowlscore[bowler[0]][2],
                                                     tsbowl.get()]
                    strikeswap()
                    bowlerlabel.destroy()
                    ball.set(0)
                    if completeover.get() != overs.get():
                        tsbowl.set(0)
                        choosebowler()
                    else:
                        fordone()
                    if teambowl1 == 1:
                        t_overbowler.config(text=str(team1bowlscore[bowler[0]][0]) + "." + str(
                                team1bowlscore[bowler[0]][1]) + "/" + str(team1bowlscore[bowler[0]][2]) + "-" + str(
                                team1bowlscore[bowler[0]][3]),
                            font="rockwell 15 bold",
                            bg="white")
                    else:
                        t_overbowler.config(
                            text=str(team2bowlscore[bowler[0]][0]) + "." + str(
                                team2bowlscore[bowler[0]][1]) + "/" + str(team2bowlscore[bowler[0]][2]) + "-" + str(
                                team2bowlscore[bowler[0]][3]),
                            font="rockwell 15 bold",
                            bg="white")
                    t_over.config(text=str(completeover.get()) + "." + str(ball.get()), font="rockwell 15 bold",
                                  bg="white")
                if n == 3 or n == 1:
                    strikeswap()
            else:
                Label(window5, text="INNINGS OVER", font="rockwell 30 bold").place(x=70, y=200)
        else:
            fromnb = 0
        print(team1bowlscore)
        print(team2bowlscore)
        print(team1batscore)
        print(team2batscore)

    def fordone():
        global ball, completeover, completeoverbowl, strike1, strike2, bowlball, totalscore, visitbat, visitbowl, bowler, bowlerlabel
        global frombat, frombowl, fromnb, overs, team1isbat, team2isbat, team1isbowl, team2isbowl, fromplay, playdone
        global team1batscore, team2batscore, team1bowlscore, team2bowlscore, count, count2, fromout, tsbowl, fromchas, fromdefend, nb1, widerun1
        if playdone == 0:
            in1score.set(totalscore.get())
            fromout = 0
            fromplay = 0
            visitbowl = 0
            playdone = 1
            nb1 = nb.get()
            widerun1 = widerun.get()
            if visitbat == 1: visitbat = 0
            if visitbowl == 1: visitbowl = 0
            if team1isbat == 1:
                count = 1;
                team2isbat = 1;
                team1isbowl = 1;
                team2isbowl = 0;
                team1isbat = 0
            else:
                count2 = 1;
                team2isbat = 0;
                team1isbowl = 0;
                team2isbowl = 1;
                team1isbat = 1
            window5.destroy()
            choosebatsman()
        else:
            if in1score.get() > totalscore.get():
                fromdefend = 1
            elif in1score.get() < totalscore.get():
                fromchase = 1
            theend()

    def strikeswap():
        global strike1, strike2
        if strike1 == 1:
            strike.place(x=0, y=35)
            strike1 = 0
            strike2 = 1
        elif strike2 == 1:
            strike.place(x=0, y=70)
            strike1 = 1
            strike2 = 0

    strikeswap()

    def wide():
        global widerun, totalscore, nb
        widerun.set(widerun.get() + 1)
        t_wide.config(text="W:" + str(widerun.get()) + " NB:" + str(nb.get()), font="rockwell 15 bold", bg="white")
        totalscore.set(totalscore.get() + 1)
        tsbowl.set(tsbowl.get() + 1)
        if teambowl1 == 1:
            team1bowlscore[bowler[0]][3] = tsbowl.get()
            t_overbowler.config(text=str(team1bowlscore[bowler[0]][0]) + "." + str(
                team1bowlscore[bowler[0]][1]) + "/" + str(team1bowlscore[bowler[0]][2]) + "-" + str(
                team1bowlscore[bowler[0]][3]),
                                font="rockwell 15 bold",
                                bg="white")
        else:
            team2bowlscore[bowler[0]][3] = tsbowl.get()
            t_overbowler.config(
                text=str(team1bowlscore[bowler[0]][0]) + "." + str(team1bowlscore[bowler[0]][1]) + "/" + str(
                    team1bowlscore[bowler[0]][2]) + "-" + str(team1bowlscore[bowler[0]][3]), font="rockwell 15 bold",
                bg="white")
        t_score.config(text=totalscore.get(), font="rockwell 15 bold", bg="white")

    def out():
        global fromstriker1, fromstriker2, strike1, strike2, striker, non_striker, fromplay, frombat, frombowl, overs, window5, fromout, tsbowl, wicket1, wicket2, overball
        global ball, completeover, completeoverbowl, strike1, strike2, bowlball, totalscore, visitbat, visitbowl, teamplayers1, bowler, bowlerlabel, fromchas, fromdefend
        if completeover.get() != overs.get():
            if strike1 == 0:
                player1score.set(player1score.get())
                player1over.set(player1over.get() + 1)
                score1.config(text=str(player1score.get()) + "(" + str(player1over.get()) + ")",
                              font="rockwell 15 bold",
                              bg="white")
                if teambat1 == 1:
                    team1batscore[batsman[0]] = [0, player1score.get(), player1over.get()]
                else:
                    team2batscore[batsman[0]] = [0, player1score.get(), player1over.get()]
            else:
                player2score.set(player2score.get())
                player2over.set(player2over.get() + 1)
                score2.config(text=str(player2score.get()) + "(" + str(player2over.get()) + ")",
                              font="rockwell 15 bold",
                              bg="white")
                if fromout == 0:
                    if teambat2 == 1:
                        team2batscore[batsman[1]] = [0, player2score.get(), player2over.get()]
                    elif teambat1 == 1:
                        team1batscore[batsman[1]] = [0, player2score.get(), player2over.get()]
                else:
                    if teambat1 == 1:
                        team1batscore[batsman[0]] = [0, player2score.get(), player2over.get()]
                    else:
                        team2batscore[batsman[0]] = [0, player2score.get(), player2over.get()]
            if ball.get() < 5 and bowlball.get() < 5:
                ball.set(ball.get() + 1)
                overball -= 1
                if playdone == 1:
                    notice.config(
                        text="Need " + str(in1score.get() - totalscore.get()) + "runs's from " + str(overball) + " ball's")
                if teambowl1 == 1:
                    team1bowlscore[bowler[0]][1] = team1bowlscore[bowler[0]][1] + 1
                    team1bowlscore[bowler[0]][2] = team1bowlscore[bowler[0]][2] + 1
                    team1bowlscore[bowler[0]][3] = tsbowl.get()
                    t_overbowler.config(
                        text=str(team1bowlscore[bowler[0]][0]) + "." + str(team1bowlscore[bowler[0]][1]) + "/" + str(
                            team1bowlscore[bowler[0]][2]) + "-" + str(team1bowlscore[bowler[0]][3]),
                        font="rockwell 15 bold",
                        bg="white")
                else:
                    team2bowlscore[bowler[0]][1] = team2bowlscore[bowler[0]][1] + 1
                    team2bowlscore[bowler[0]][2] = team2bowlscore[bowler[0]][2] + 1
                    team2bowlscore[bowler[0]][3] = tsbowl.get()
                    t_overbowler.config(
                        text=str(team2bowlscore[bowler[0]][0]) + "." + str(team2bowlscore[bowler[0]][1]) + "/" + str(
                            team2bowlscore[bowler[0]][2]) + "-" + str(team2bowlscore[bowler[0]][3]),
                        font="rockwell 15 bold",
                        bg="white")
                t_over.config(text=str(completeover.get()) + "." + str(ball.get()), font="rockwell 15 bold", bg="white")

            else:
                completeover.set(completeover.get() + 1)
                overball -= 1
                if playdone == 1:
                    notice.config(
                        text="Need " + str(in1score.get() - totalscore.get()) + " run's from " + str(overball) + " ball's")
                if teambowl1 == 1:
                    team1bowlscore[bowler[0]] = [team1bowlscore[bowler[0]][0] + 1, 0]
                    team1bowlscore[bowler[0]][2] = team1bowlscore[bowler[0]][2] + 1
                    team1bowlscore[bowler[0]][3] = [team1bowlscore[bowler[0]][3], tsbowl.get()]
                else:
                    team2bowlscore[bowler[0]] = [team2bowlscore[bowler[0]][0] + 1, 0]
                    team2bowlscore[bowler[0]][2] = team2bowlscore[bowler[0]][2] + 1
                    team2bowlscore[bowler[0]][3] = [team1bowlscore[bowler[0]][3], tsbowl.get()]
                strikeswap()
                bowlerlabel.destroy()
                ball.set(0)
                tsbowl.set(0)
                choosebowler()
                if teambowl1 == 1:
                    t_overbowler.config(
                        text=str(team1bowlscore[bowler[0]][0]) + "." + str(team1bowlscore[bowler[0]][1]) + "/" + str(
                            team1bowlscore[bowler[0]][2]) + "-" + str(team1bowlscore[bowler[0]][3]),
                        font="rockwell 15 bold",
                        bg="white")
                else:
                    t_overbowler.config(
                        text=str(team2bowlscore[bowler[0]][0]) + "." + str(team2bowlscore[bowler[0]][1]) + "/" + str(
                            team1bowlscore[bowler[0]][2]) + "-" + str(team2bowlscore[bowler[0]][3]),
                        font="rockwell 15 bold",
                        bg="white")
                t_over.config(text=str(completeover.get()) + "." + str(ball.get()), font="rockwell 15 bold", bg="white")
            if strike1 == 0:
                fromstriker1 = 1
                striker.destroy()
                if teambat1 == 1:
                    team1batscore[batsman[0]] = [0, player1score.get(), player1over.get()]
                else:
                    team2batscore[batsman[0]] = [0, player1score.get(), player1over.get()]
                player1score.set(0)
                player1over.set(0)
                score1.config(text=str(player1score.get()) + "(" + str(player1over.get()) + ")",
                              font="rockwell 15 bold",
                              bg="white")
                fromout = 1
                if playdone == 0:
                    wicket1 += 1
                    if wicket1 == k:
                        fordone()
                    choosebatsman()
                elif playdone == 1:
                    wicket2 += 1
                    if wicket2 == k:
                        fromdefend = 1
                        theend()
                    choosebatsman()
            elif strike2 == 0:
                fromstriker2 = 1
                non_striker.destroy()
                if fromout == 0:
                    if teambat2 == 1:
                        team2batscore[batsman[1]] = [0, player2score.get(), player2over.get()]
                    elif teambat1 == 1:
                        team1batscore[batsman[1]] = [0, player2score.get(), player2over.get()]
                else:
                    if teambat1 == 1:
                        team1batscore[batsman[0]] = [0, player2score.get(), player2over.get()]
                    else:
                        team2batscore[batsman[0]] = [0, player2score.get(), player2over.get()]
                player2score.set(0)
                player2over.set(0)
                score2.config(text=str(player2score.get()) + "(" + str(player2over.get()) + ")",
                              font="rockwell 15 bold",
                              bg="white")
                fromout = 1
                if playdone == 0:
                    wicket1 += 1
                    if wicket1 == k:
                        fordone()
                    choosebatsman()
                elif playdone == 1:
                    wicket2 += 1
                    if wicket2 == k:
                        fromdefend = 1
                        theend()
                    choosebatsman()

        else:
            Label(window5, text="INNINGS OVER", font="rockwell 30 bold").place(x=70, y=200)
        print(team1bowlscore)
        print(team2bowlscore)
        print(team1batscore)
        print(team2batscore)

    global fromnb
    fromnb = 0

    def nob():
        global widerun, totalscore, fromnb, nb
        widerun.set(widerun.get())
        nb.set(nb.get() + 1)
        t_wide.config(text="W:" + str(widerun.get()) + " NB:" + str(nb.get()), font="rockwell 15 bold", bg="white")
        totalscore.set(totalscore.get() + 1)
        tsbowl.set(tsbowl.get() + 1)
        t_score.config(text=totalscore.get(), font="rockwell 15 bold", bg="white")
        fromnb = 1

    Button(window5, text="0", font="rockwell 20 bold", fg="red", bg="black", command=lambda: function(0)).place(x=60,
                                                                                                                y=250)
    Button(window5, text="1", font="rockwell 20 bold", fg="red", bg="black", command=lambda: function(1)).place(x=100,
                                                                                                                y=250)
    Button(window5, text="2", font="rockwell 20 bold", fg="red", bg="black", command=lambda: function(2)).place(x=140,
                                                                                                                y=250)
    Button(window5, text="3", font="rockwell 20 bold", fg="red", bg="black", command=lambda: function(3)).place(x=180,
                                                                                                                y=250)
    Button(window5, text="4", font="rockwell 20 bold", fg="red", bg="black", command=lambda: function(4)).place(x=220,
                                                                                                                y=250)
    Button(window5, text="6", font="rockwell 20 bold", fg="red", bg="black", command=lambda: function(6)).place(x=260,
                                                                                                                y=250)
    Button(window5, text="WD", font="rockwell 20 bold", fg="red", bg="black", command=wide).place(x=95, y=310)
    Button(window5, text="NB", font="rockwell 20 bold", fg="red", bg="black", command=nob).place(x=165, y=310)
    Button(window5, text="OUT", font="rockwell 20 bold", fg="red", bg="black", command=out).place(x=225, y=310)
    Button(window5, text="Change Strike", font="rockwell 13 bold", fg="red", bg="black", command=strikeswap).place(
        x=230, y=90)


def theend():
    global t1sbat, t2sbowl, t2sbat, t1sbowl, teamplayers1, teamplayers2, team1batscore, team2batscore, team1bowlscore, team2bowlscore, in1score, totalscore
    global count, wicket1, wicket2, fromdefend, fromchas, nb1, widerun1, nb, widerun, window, k
    window5.destroy()
    try:
        for i in range(k):
            try:
                team1batscore[teamplayers1[i].get()][0] = int(
                    team1batscore[teamplayers1[i].get()][1] / team1batscore[teamplayers1[i].get()][2] * 100)
            except:
                continue
        for i in range(k):
            try:
                team2batscore[teamplayers2[i].get()][0] = int(
                    team2batscore[teamplayers2[i].get()][1] / team2batscore[teamplayers2[i].get()][2] * 100)
            except:
                continue
    except:
        pass
    finally:
        sorted_d = dict(sorted(team1batscore.items(), key=operator.itemgetter(1), reverse=True))
        team1batscore = sorted_d
        keysList = list(team1batscore.keys())
        print(team1batscore)
        sorted_d1 = dict(sorted(team2batscore.items(), key=operator.itemgetter(1), reverse=True))
        team2batscore = sorted_d1
        keysList2 = list(team2batscore.keys())
        print(team2batscore)
        sorted_d2 = dict(sorted(team1bowlscore.items(), key=operator.itemgetter(1), reverse=True))
        keysList3 = list(team1bowlscore.keys())
        sorted_d3 = dict(sorted(team2bowlscore.items(), key=operator.itemgetter(1), reverse=True))
        keysList4 = list(team2bowlscore.keys())
        window6 = Tk()
        window6.geometry('1000x1000')
        window6.title('score pannel')
        window6.resizable(0, 0)
        Label(window6, text="MATCH SUMMARY", font="rockwell 17 italic bold").place(x=420, y=0)
        Label(window6, text=team1.get(), font="rockwell 24 bold italic", bg="red", width=30,
              relief="raised", borderwidth=7,
              fg="white", ).place(x=-133, y=50)
        Label(window6, text="Vs", font="roman 40 bold", fg="black").place(x=485, y=75)
        Label(window6, text=team2.get(), font="rockwell 24 bold italic", bg="blue", relief="raised", borderwidth=7,
              fg="white", width=30).place(x=540, y=115)
        Label(window6, text="-------------------------------------------------------------",
              font="roman 10 bold").place(
            x=0, y=115)
        Label(window6, text="-------------------------------------------------------------",
              font="roman 10 bold").place(
            x=532, y=80)
        Label(window6, text="BATSMAN                             R   B   SR ", font="rockwell 15 bold", bg="red",
              fg="white", relief="ridge").place(x=120, y=200)
        j = 30
        for i in range(4):
            Label(window6, text=str(keysList[i]), font="rockwell 13 bold").place(x=120, y=200 + j)
            Label(window6, text=str(team1batscore[keysList[i]][1]), font="rockwell 13 bold").place(x=395, y=200 + j)
            Label(window6, text=str(team1batscore[keysList[i]][2]), font="rockwell 13 bold").place(x=423, y=200 + j)
            Label(window6, text=str(team1batscore[keysList[i]][0]), font="rockwell 13 bold").place(x=458, y=200 + j)
            j += 30
        Label(window6, text="BATSMAN                             R   B   SR ", font="rockwell 15 bold", bg="blue",
              fg="white", relief="ridge").place(x=520, y=200)
        j = 30
        for i in range(4):
            Label(window6, text=str(keysList2[i]), font="rockwell 13 bold").place(x=525, y=200 + j)
            Label(window6, text=str(team2batscore[keysList2[i]][1]), font="rockwell 13 bold").place(x=795, y=200 + j)
            Label(window6, text=str(team2batscore[keysList2[i]][2]), font="rockwell 13 bold").place(x=823, y=200 + j)
            Label(window6, text=str(team2batscore[keysList2[i]][0]), font="rockwell 13 bold").place(x=855, y=200 + j)
            j += 30
        Label(window6, text="BOWLER                       O    B    W   R ", font="rockwell 15 bold", bg="red",
              fg="white", relief="ridge").place(x=120, y=400)
        j = 30
        for i in range(4):
            Label(window6, text=str(teamplayers1[i].get()), font="rockwell 13 bold").place(x=120, y=400 + j)
            Label(window6, text=str(team1bowlscore[teamplayers1[i].get()][0]), font="rockwell 13 bold").place(x=347,
                                                                                                              y=400 + j)
            Label(window6, text=str(team1bowlscore[teamplayers1[i].get()][1]) + "  /", font="rockwell 13 bold").place(
                x=390, y=400 + j)
            Label(window6, text=str(team1bowlscore[teamplayers1[i].get()][2]) + " --", font="rockwell 13 bold").place(
                x=430, y=400 + j)
            Label(window6, text=str(team1bowlscore[teamplayers1[i].get()][3]), font="rockwell 13 bold").place(x=460,
                                                                                                              y=400 + j)
            j += 30
        Label(window6, text="BOWLER                       O    B    W   R ", font="rockwell 15 bold", bg="blue",
              fg="white", relief="ridge").place(x=520, y=400)
        j = 30
        for i in range(4):
            Label(window6, text=str(teamplayers2[i].get()), font="rockwell 13 bold").place(x=525, y=400 + j)
            Label(window6, text=str(team2bowlscore[teamplayers2[i].get()][0]), font="rockwell 13 bold").place(x=750,
                                                                                                              y=400 + j)
            Label(window6, text=str(team2bowlscore[teamplayers2[i].get()][1]) + "  /", font="rockwell 13 bold").place(
                x=790, y=400 + j)
            Label(window6, text=str(team2bowlscore[teamplayers2[i].get()][2]) + " --", font="rockwell 13 bold").place(
                x=830, y=400 + j)
            Label(window6, text=str(team2bowlscore[teamplayers2[i].get()][3]), font="rockwell 13 bold").place(x=860,
                                                                                                              y=400 + j)
            j += 30
        if count == 1:
            Label(window6, text=str(in1score.get()) + "/" + str(wicket1), font="rockwell 16 italic bold",
                  relief="raised", bg="white", borderwidth=3, width=7).place(x=150, y=113)
            Label(window6, text=str(totalscore.get()) + "/" + str(wicket2), font="rockwell 16 italic bold",
                  relief="raised", bg="white", borderwidth=3, width=7).place(x=780, y=79)
            Label(window6, text="EXTRA=                            W:" + str(widerun1) + " NB:" + str(nb1),
                  font="rockwell 15 bold", relief="ridge", width=30).place(x=120, y=355)
            Label(window6, text="EXTRA=                            W:" + str(widerun.get()) + " NB:" + str(nb.get()),
                  font="rockwell 15 bold", relief="ridge", width=30).place(x=520, y=355)
        else:
            Label(window6, text=str(in1score.get()) + "/" + str(wicket1), font="rockwell 16 italic bold",
                  relief="raised", bg="white", borderwidth=3, width=7).place(x=780, y=79)
            Label(window6, text=str(totalscore.get()) + "/" + str(wicket2), font="rockwell 16 italic bold",
                  relief="raised", bg="white", borderwidth=3, width=7).place(x=150, y=113)
            Label(window6, text="EXTRA=                            W:" + str(widerun.get()) + " NB:" + str(nb.get()),
                  font="rockwell 15 bold", relief="ridge", width=30).place(x=520, y=355)
            Label(window6, text="EXTRA=                            W:" + str(widerun1) + " NB:" + str(nb1),
                  font="rockwell 15 bold", relief="ridge", width=30).place(x=120, y=355)
        if in1score.get() == totalscore.get():
            Label(window6, text="MATCH DRAWN", font="rockwell 15 italic bold", relief="flat", bg="black", fg="white",
                  width=40).place(x=250, y=550)
        else:
            if fromchas == 1:
                if count == 1:
                    Label(window6, text=str(totalscore.get()) + " Run's " + str(team2.get()) + " Won by " + str(
                        k - wicket2) + " wickets", font="rockwell 15 italic bold", relief="flat", bg="black",
                          fg="white", width=40).place(x=250, y=550)
                elif count == 0:
                    Label(window6,
                          text=str(in1score.get()) + " Run's " + str(team1.get()) + " Won by " + str(
                              k - wicket1) + " wickets",
                          font="rockwell 15 italic bold", relief="flat", bg="black", fg="white", width=40).place(x=250,
                                                                                                                 y=550)
            if fromdefend == 1:
                if count == 1:
                    Label(window6, text=str(in1score.get()) + " Run's " + str(team1.get()) + " Won by " + str(
                        in1score.get() - totalscore.get()) + " Run's ", font="rockwell 15 italic bold", relief="flat",
                          bg="black", fg="white", width=40).place(x=250,
                                                                  y=550)
                elif count == 0:
                    Label(window6, text=str(in1score.get()) + " Run's " + str(team2.get()) + " Won by " + str(
                        in1score.get() - totalscore.get()) + " Run's ", font="rockwell 15 italic bold", relief="flat",
                          bg="black", fg="white", width=40).place(x=250,
                                                                  y=550)
    Button(window6, text="Close", font="rockwell 15 bold", fg="black", bg="white", command=window6.destroy).place(x=870,
                                                                                                                  y=630)


window.mainloop()
