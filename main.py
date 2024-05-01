import requests
import keyboard
from time import sleep

downloadUrl = "https://newgrounds.com/audio/download/"

GDFolder = ""
try:
    exec(open("settings.txt", "r").read())
except:
    print("Oops! There is a problem with the 'settings.txt' file.")
    print("Close this program and go check if such file does not exist or has problems.")
    while True:
        pass

songalias = { # around 40 lines of code (what)
    "Back On Track":"BackOnTrack.mp3", 
    "Base After Base":"BaseAfterBase.mp3", 
    "Blast Processing":"BlastProcessing.mp3",
    "Cant Let Go":"CantLetGo.mp3",
    "Clubstep":"Clubstep.mp3",
    "Clutterfunk":"ClutterFunk.mp3",
    "Cycles":"Cycles.mp3",
    "Dash":"Dash.mp3",
    "Deadlocked":"Deadlocked.mp3",
    "Dry Out":"DryOut.mp3",
    "Electrodynamix":"Electrodynamix.mp3",
    "Electroman Adventures":"Electroman.mp3",
    "Fingerb*ng (name too vulgar) (Fingerdash song)":"Fingerdash.mp3",
    "Geometrical Dominator":"GeometricalDominator.mp3",
    "Hexagon Force":"HexagonForce.mp3",
    "Jumper":"Jumper.mp3",
    "Polargeist":"Polargeist.mp3",
    "Stereo Madness":"StereoMadness.mp3",
    "Theory Of Everything":"TheoryOfEverything.mp3",
    "Theory Of Everything 2":"TheoryOfEverything2.mp3",
    "Time Machine":"TimeMachine.mp3",
    "xStep":"xStep.mp3",
    "Stay Inside Me (Practice music)":"StayInsideMe.mp3",
    "DJ RubRub (The Challenge song)":"DJRubRub.mp3",
    "The Treasure Room music":"secretLoop.mp3",
    "Vault of Secrets music":"secretLoop02.mp3",
    "Chamber of Time music":"secretLoop03.mp3",
    "Shop":"shop.mp3",
    "Secret shop music (Scratch's shop)":"secretshop.mp3",
    "Community shop":"shop3.mp3",
    "The Mechanic's shop":"shop4.mp3",
    "Diamond shop":"shop5.mp3",
    "danger loop":"dangerloop.mp3",
    "Menu loop":"menuLoop.mp3",
    "The tower menu loop":"tower01.mp3",
    "Power Trip (Why is it in the game files?)":"PowerTrip.mp3"
}

songtitles = list(songalias.keys())

done = False

def clear_con():
    from os import system, name
    if name == "nt":
        system("cls")
    else:
        system("clear")

def choose_a_song():
    err = True
    while err:
        curs = 0
        print("Choose a song:")
        print("["+str(curs+1)+" - "+songtitles[curs]+"]")
        print("(Navigate with the arrow keys)")
        print("(press [SHIFT] once you selected the desired song)")
        while True:
            if keyboard.is_pressed("up") and curs > 0:
                curs -= 1
                clear_con()
                print("Choose a song:")
                print("["+str(curs+1)+" - "+songtitles[curs]+"]")
                print("(press [SHIFT] once you selected the desired song)")
                while keyboard.is_pressed("up"):
                    pass
                
            elif keyboard.is_pressed("down") and curs < len(songtitles)-1:
                curs += 1
                clear_con()
                print("Choose a song:")
                print("["+str(curs+1)+" - "+songtitles[curs]+"]")
                print("(press [SHIFT] once you selected the desired song)")
                while keyboard.is_pressed("down"):
                    pass
                
            elif keyboard.is_pressed("shift"):
                while keyboard.is_pressed("shift"):
                    pass
                return curs

            while not keyboard.is_pressed("up") and not keyboard.is_pressed("down") and not keyboard.is_pressed("shift"):
                pass
            done = False

def edit_song(snum):
    choosen = songtitles[snum]
    file_ = songalias[choosen]
    print("Selected song:", choosen)
    print("WARNING: this program cannot distinguish (yet) 404 pages by real sounds files.\nAlways use existing newgrounds song IDs.")
    print("Put the song ID down below, or leave everything blank to restore the original song.")
    err = True
    while err:
        song_ID = input("Song ID: ")
        clear_con()
        err = False
    
        if song_ID == "":
            print("No ID given! Restoring original song...", end="")
            open(GDFolder+"/Resources/"+file_, "wb").write(open("Original/"+file_, "rb").read())
        else:
            try:
                print("Downloading song to RAM...", end="")
                newsong = requests.get(downloadUrl+song_ID)
                print("[DONE]")
            except:
                print("Oops! There was a problem while downloading the song.")
                print("Please check your internet connection.")
                err = True
            
            try:
                print("Overwriting current song...", end="")
                open(GDFolder+"/Resources/"+file_, "wb").write(newsong.content)
            except:
                print("\nOops! there was a problem while overwriting the song.")

    done = True

while True:
    if done:
        print("[DONE]")
        sleep(1)
    clear_con()
    songnum = choose_a_song()
    sleep(1)
    clear_con()
    edit_song(songnum)
    done = True