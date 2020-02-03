from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr

# Create your views here.
def index(request) :
    if 'speak' in request.POST :
        r=sr.Recognizer()
        with sr.Microphone() as source :
            print("Speak Anything : ")
            audio=r.listen(source)
        try :
            text=r.recognize_google(audio, language="gu-IN")
            print("You Said : ",format(text))
        except :
            print("Sorry could not recognize your voice")
            text="Sorry could not recognize your voice"
        return render(request, 'homepage/homepage.html',{'s':text})
    elif request.method == "POST" and len(request.FILES)!=0 :
        uploaded_file = request.FILES["document"]
        r = sr.Recognizer()
        with sr.AudioFile(uploaded_file) as source :
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.record(source)
        try :
            s=r.recognize_google(audio, language="gu-IN")
            print(s)
            return render(request, 'homepage/homepage.html',{'s':s})
        except :
            print("Something Went Wrong")
    return render(request, 'homepage/homepage.html')
        