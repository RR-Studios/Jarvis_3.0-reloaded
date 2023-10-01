import smtplib
import pyttsx3

#speak function
engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to send an email (you need to provide your email and password)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('raman5ransubhe@gmail.com', 'Fortnite@1')
    server.sendmail('raman5ransubhe@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    if sendEmail():
        print("Sir, the mail was sent successfully.")
        speak("Sir, the mail was sent successfully.")
    else:
        print("Sir, the mail was not sent successfully.")
        speak("Sir, the mail was not sent successfully.")