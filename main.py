# # convert text to speech
# import pyttsx3
# assistant = pyttsx3.init()
# assistant.say("Hii I am here to assist you")
# assistant.runAndWait()

#convert speech to text
import  datetime
import speech_recognition as sr
import pyttsx3
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        audio = r.listen(source)
        try:
            print("I heard: \n" + r.recognize_google(audio))
            # assistant = pyttsx3.init()
            # assistant.say(r.recognize_google(audio))
            # assistant.runAndWait()
            f = open("myfile.txt", "a")
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(current_time + "\n" + r.recognize_google(audio) + "\n\n")
            f.close()
        except Exception as e:
            print("Error: " +str(e))

if __name__ == "__main__":
    main()        