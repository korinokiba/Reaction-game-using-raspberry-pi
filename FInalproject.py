import pygame
from gpiozero import Button,LED
import time
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Downloads/pre-drop-3-2-1-go-vocal-spoken_128bpm_F_major.wav")

btn1 = Button(17)
btn2 = Button(16)
led1= LED(21)
led2 = LED(20)
highScore = 99999 #default
# first time playing

#test your reaction time.
def single_player():
    print("press button to start")
    btn1.wait_for_press()
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    led1.on()
    print("GO!")
    startTime = time.time()
    btn1.wait_for_press()
    led1.off()
    endTime = time.time()
    resultTime = endTime - startTime
    print("Result: " + str(resultTime))
    if resultTime < highScore:
        firstTry = False
        print("NEW HIGHSCORE")
        highscore = resultTime

# whoever press the button first wins
def multi_Player():
    winner = False
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    print("GO!")
    while not winner:
        if btn1.is_pressed:
            led1.on()
            print("PLAYER 1 WINNER")
            time.sleep(1)
            led1.off()
            winner = True
        elif btn2.is_pressed:
            led1.off()
            led2.on()
            print("PLAYER 2 WINNER")
            time.sleep(2)
            led2.off()
            winner = True
    

# How to start the game
while True:
    players = input("1 or 2 player?")
    if players == "1":
       single_player()
    elif players == "2":
        multi_Player()
