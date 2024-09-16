from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BOARD)

red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

win = Tk()
win.title("RGB GUI")
win.geometry('800x480')
myFont = tkinter.font.Font(family ='Helvetica', size = 20, weight = "bold")

def ledToggle(chk):
	if chk == 1:
		if red_led.is_lit:
			red_led.off()
			redledButton["text"] = "Turn LED on"
		else:
			red_led.on()
			green_led.off()
			blue_led.off()
			redledButton["text"] = "Turn LED off"
	if chk == 2:
		if green_led.is_lit:
			green_led.off()
			greenledButton["text"] = "Turn LED on"
		else:
			green_led.on()
			red_led.off()
			blue_led.off()
			greenledButton["text"] = "Turn LED off"
	if chk == 3:
		if blue_led.is_lit:
			blue_led.off()
			blueledButton["text"] = "Turn LED on"
		else:
			blue_led.on()
			green_led.off()
			red_led.off()
			redledButton["text"] = "Turn LED off"

def close():
	RPi.GPIO.cleanup()
	win.destroy()

redledButton = Radiobutton(win, text = 'RED', font = myFont, command = lambda: ledToggle(1), bg='red', height = 1, width = 24)
redledButton.grid(row = 0, column = 1)

greenledButton = Radiobutton(win, text = 'GREEN', font = myFont, command = lambda: ledToggle(2), bg='green', height = 1, width = 24)
greenledButton.grid(row = 0, column = 2)

blueledButton = Radiobutton(win, text = 'BLUE', font = myFont, command = lambda: ledToggle(3), bg='blue', height = 1, width = 24)
blueledButton.grid(row = 0, column = 3)

exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'yellow', height = 1, width = 24)
exitButton.grid(row = 1, column = 1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
