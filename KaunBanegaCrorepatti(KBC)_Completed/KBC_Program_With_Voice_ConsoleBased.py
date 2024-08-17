import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

def say(audio):
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()

def KBC():
    Answers = ["a","b","a","a","d","c","b","d","a","b"]
    Questions = ["How Many Elements are there in Periodic Table?","What is inertia?","The Holy Quran have  surah's:","The Capital of Palestine is:","Russia has  Timezones.","How Many Muslims Countries are there?","According to USA, Number of Countries in World is:","Country with world Largest Population is:","Are you playing KBC","Are Feastables better than Hershey's Chocolate bars?"]
    Options = ["A. 118\t\tB. 120\t\tC. 100\t\tD. 150","A. Force\t\tB. Property\t\tC. P = mv\t\tD. Mass","A. 114\t\tB. 115\t\tC. 116\t\tD. 124","A. Jerusalem\t\tB. Hamas\t\tC. Gaza\t\tD. Israel","A. 10\t\tB. 5\t\tC. 77\t\tD. 11","A. 40\t\tB. 50\t\tC. 57\t\tD. 77","A. 180\t\tB. 195\t\tC. 100\t\tD. 265","A. Pakistan\t\tB. China\t\tC. Russia\t\tD. India","A. Nope\t\tB. Absolutely Not\t\tC. No of course\t\tD. No","A. Nope\t\tB. Absolutely Candyland\t\tC. No of course\t\tD. No"]
    Expected = ["a","b","c","d"]
    # print(len(Questions))
    say("Enter your Balance:")
    Balance = int(input())
    if Balance <= 5000:
        say(f"Your Balance is Rupees {Balance}")
    else:
        Balance = 5000
        say(f"Your Balance is Rupees {Balance}")
    temp = Balance
    i = 0
    for Answer in Answers:
        say(Questions[i])
        say(Options[i])
        Chosen = input()
        if Chosen in Expected:
            if Chosen == Answer:
                Balance = Balance + Balance
                Won = ["And we have a winner! Congratulations to our champion!","Victory is sweet, and our winner today knows it well!","The crown of victory goes to the skilled player among us.","A round of applause for the triumphant player!","Our game's conqueror, bask in the glory of your win!","Success smiles upon one lucky player today!"]
                say(random.choice(Won))
                say(f"Your Balance is now {Balance}")
            elif Chosen != Answer:
                Lose = ["You win some, you lose some. Keep that competitive spirit alive!","It's not always about winning; it's about having a great time together.","Commiserations! But remember, it's all in good fun.","I feel so sorry to say that you have lost it.","That's was close but you have lose","Good Job Better Luck next time."]
                say(random.choice(Lose))
                Balance = 0
                say(f"You won nothing except {Balance}")
                break
        else:
            say(f"There is no such Option {Chosen}")
            say("Congrats! You have lost one of your chances.")
        i = i+1
        if Balance > 0:
            say(f"Congratulations! You have won {Balance} Rupees from Rupees {temp}")

if __name__ == '__main__':
    KBC()