from microbit import *
import speech
import music
import math
import radio

def mapInteger(anInteger, from1, to1, from2, to2):
    span1 = to1 - from1
    span2 = to2 - from2
    scaling_factor = span1 / span2
    return math.floor(anInteger / scaling_factor)

def selectLetter(alphabet):
    letter_index = mapInteger(pin2.read_analog(),0,1023,0,len(min_alphabet))
    letter = alphabet[letter_index]
    return letter

def send_message(message):
    display.show(Image.HAPPY)
    radio.send(message)
    sleep(1000)
    
def show_and_pronounce(word):
    string = speech.translate(word)
    speech.pronounce(string,speed=120, pitch=100, throat=100, mouth=200)
    display.scroll(word)    

radio.on()
special_characters = "_?!"
min_alphabet = "abcdefghijklmnopqrstuvwxyz" + special_characters
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + special_characters
outgoing = ""

while True:
    if button_b.is_pressed():
        letter = selectLetter(cap_alphabet)
    else:
        letter = selectLetter(min_alphabet)
        
    display.show(letter)
    incoming = radio.receive()
    if incoming != None:
        display.scroll("*** ") 
        show_and_pronounce(incoming)
        display.scroll("*** ") 
    
    if accelerometer.was_gesture("shake"):
        show_and_pronounce(outgoing)
    
    i = 0
    while button_a.is_pressed():
        if i == 0:
            outgoing += letter
            i += 1
        elif i > 5:
            outgoing = outgoing[:-1]
            send_message(outgoing)
            break
        else:
            i += 1
        sleep(250)



    
    