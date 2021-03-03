from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import sys
import smtplib
import webbrowser

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot",
 storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[  {
                        'import_path': 'chatterbot.logic.BestMatch'
                    },
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
            'threshold': 0.65,
            'default_response': 'sorry did not understand'
                    },],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    database="db.sqlite3")

convo = [
    'hello',
    'hi there ! how can i help you',
    'what is your name',
    'My name is Bot',
    'how are you',
    'I am doing great these days',
    'what is your age',
    'i am 15 days old',
    'diagnose',
    'tell me about some of your symptoms',
    'in which city you live',
    'I live in lucknow',
    'in which language you talk',
    ' I mostly talk in english',
    'fever , cough',
    'viral infection',
    "cough , cold , fever, loss of taste , loss of smell",
    'covid 19',
    "aches stiffness,muscle aches,low-grade fever,lack of appetite,loss of energy,joints swollen,reddened,painful",
    "rheumatoid arthiritis",
    "fatigue,loss of appetite,nausea,jaundice,pain in the upper right abdomen",
    'heapatatis B',
    "fever,exhaustion,severe joint pain,swollen lymph nodes,itchy rash",
    "dengue",
    "fever,headache,vomiting,weakness,body aches",
    "malaria",
    "general weakness,chills,fever up to 102 F,red spots,headache",
    "chicken pox",
    "yellow discoloration of skin,mucous membranes,sleepiness,lethargy,excessive changes in muscle tone",
    "jaundice",
    "bowel movements are frequent watery,no signs of inflammation,cramping abdominal pain",
    "diarrhea",
    "decrease in clarity of vision,not fully correctable with glasses,loss of contrast sensitivity,disturbing glare in light,incorrect vision",
    "cataract",
    "fever,chills,cough,shortness of breath,fatigue",
    "pneumonia",
    "sleepiness,fatigue,anxiety,lack of energy,increased errors",
    "insomnia",
    "lethargy,enlarged thyroid,sexual dysfunction,irregular uterine bleeding,sluggishness",
    "thyroid",
    "swelling of bone, redness in bone, lump over a bone, persistent bone pain,fractures",
    "bone cancer",
    "Diarrhoea,Abdominal Pain,Fatigue (extreme tiredness)Blood and Mucus in faeces(stools),Weight Loss",
    "Crohns_Disease",
    "Rashes, Itching and Stinging, Diarrhoea, Red raised Patches with blisters,Bloating",
    "Dermatitis_Herpetiformis",
    "decrease in clarity of vision,not fully correctable with glasses,loss of contrast sensitivity,Disturbing glare in light",
    "cataract",
    "Mild Fever,Vomiting,Watery Diarrhoea,Upset Stomach,aching limbs",
]

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
   "./conversations.yml"
)


cities=["indore","bhopal","jabalpur","gwalior","ujjain","dewas","ratlam","khandwa","madhya pradesh"]
main = Tk()

main.geometry("500x700")

main.title("Healthcare chatbot")
img = PhotoImage(file="bot1.jpeg")

photoL = Label(main, image=img)

photoL.pack(pady=5)


myLabel1=Label(main,text="Use microphone to give input in form of audio")
myLabel1.pack(pady=6)

myLabel1=Label(main,text="Enter diagnose to get yourself diagnosed or say diagnose")
myLabel1.pack(pady=7)

myLabel1=Label(main,text="Enter your mail-id and then your disease to get proper medication reference related to your disease")
myLabel1.pack(pady=8)

myLabel1=Label(main,text="Please enter your city to get details regarding hospitals and clinic in your city")
myLabel1.pack(pady=9)

# takey query : it takes audio as input from user and convert it to string..
reciever_email=[]
def takeQuery():
    sr = s.Recognizer()
    with s.Microphone() as source:
        print("your bot is listening try to speak")
        sr.pause_threshold=0.5
        audio = sr.listen(source)
        try:
            query = sr.recognize_google(audio)
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    l=[]
    l=list(query)
    query=query.lower()
    if query in cities:
        if "ujjain"==query:
            webbrowser.open("https://www.justdial.com/Ujjain/Hospitals/nct-10253670")
        elif "indore"==query:
            webbrowser.open("https://www.medifee.com/hospitals-in-indore")
        elif query=="bhopal":
            webbrowser.open("https://www.justdial.com/Bhopal/Private-Hospitals/nct-10390288")
        elif query=="ratlam":
            webbrowser.open("https://www.justdial.com/Ratlam/Hospitals/nct-10253670")    
        elif query=="dewas":
            webbrowser.open("https://www.justdial.com/Dewas/Hospitals/nct-10253670")        
        elif query=="jabalpur":
            webbrowser.open("https://www.justdial.com/Jabalpur/Hospitals/nct-10253670")    
        elif query=="madhya pradesh":
            webbrowser.open("https://www.medicineindia.org/hospitals-in-state/madhya-pradesh") 
    else:                 
        if "@" not in l:
            if query=="malaria":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference for malaria: \n{}\n{}\n{}\n".format("Chloroquine","Mefloquine","Quinine sulfate (Qualaquin) with doxycycline (Vibramycin, Monodox, others)")
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            elif query=="dengue":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference for dengue: \n{}\n{}\n{}\n".format("Acetaminophen (Tylenol, others) can alleviate pain and reduce fever.","aspirin, ibuprofen"," naproxen sodium (Aleve, others).")
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            elif query=="insomnia":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference for insomnia: \n{}\n{}\n{}\n".format("Benzodiazepine sedatives such as triazolam (Halcion)","non-benzodiazepine sedatives such as zolpidem (Ambien, Intermezzo), eszopiclone (Lunesta), and zaleplon (Sonata) are drugs that can help induce sleep")
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            elif query=="covid":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference for covid: \n{}\n{}\n{}\n".format("Tell others you're sick so they keep their distance.","Cover your coughs and sneezes with a tissue or your elbow.","Wear a mask over your nose and mouth if you can.Wash regularly, especially your hands.")
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            elif query=="thyroid":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference for thyroid: \n{}\n{}\n".format("Standard treatment for hypothyroidism involves daily use of the synthetic thyroid hormone levothyroxine,","(Levo-T, Synthroid, others)")
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            elif query=="chicken pox":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference for chicken pox :\n{}\n{}".format("acyclovir (Zovirax, Sitavig)","another drug called immune globulin intravenous (Privigen).")
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            elif query=="jaundice":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference for jaundice: \n{}\n{}".format("Hepatitis-induced jaundice requires antiviral or steroid medications.","Crigler-Najjar syndrome type 2.")
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            elif query=="diarrhea":
                sender_email="poalatharva@gmail.com"
                password="#@atharva1@#"
                message="medication reference"
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(sender_email,password)
                print("Login success")
                server.sendmail(sender_email,reciever_email[0],message)
                print("email sent!")
                speak("Your medication reference has been sent successfully to your mail-id")
                textF.delete(0, END)
            else:
                answer_from_bot = bot.get_response(query)
                msgs.insert(END, "you : " + query)
                print(type(answer_from_bot))
                msgs.insert(END, "bot : " + str(answer_from_bot))
                speak(answer_from_bot)
                textF.delete(0, END)
                msgs.yview(END)    
        else:
            reciever_email.insert(0,query)       
            print(reciever_email[0])     


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)


btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)



def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()