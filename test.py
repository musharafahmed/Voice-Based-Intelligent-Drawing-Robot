import speech_recognition as sr
#import webbrowser as wb

def voice():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("say anything " )
        audio = r.listen(source)

    try:
        get = r.recognize_google(audio)
    #url = 'https://www.google.com/search?q='
    #wb.open_new(url+get)
        return get
        print(get)
    except UnknownValueError :
        print("error")

voice()
