from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause
pygame.mixer.init()
button_sounds = {
    Button(2): Sound("sound1.wav"),
    Button(3): Sound("sound2.wav"),

}
for button, sound in button_sounds.items():
    button.when_pressed = sound.play
pause()

# i tried this out but unfortunately there i could get my pi to play audio. I tried bluetooth, through the reomte desktop, and through
# usb but no luck :(
# i think it probably works though

