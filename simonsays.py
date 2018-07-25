import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
from getpass import getpass

colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

frequencies = [220, 420, 880, 1760]

def validate_guess(color_sequence_string, guess):
	if guess == color_sequence_string:
		print 'Correct! Here is the next sequence' 
		
	else:
		print 'Wrong!'
		print ('the correct sequence is', color_sequence_string)
		print ('your guess was', guess)
		Buzz.ChangeFrequency (55) 
		Buzz.start(50)
		LED.setColor(colors[0])
		time.sleep(0.5)
		LED.setColor(colors[1])
		time.sleep(0.5)
		LED.setColor(colors[2])
		time.sleep(0.5)
		LED.setColor(colors[3])
		time.sleep(0.5)
		Buzz.stop()
		LED.destroy()
		exit()

def loop():
	n = random.randint(0,3)
	color_sequence = [colors[n]]
	frequency_sequence = [frequencies[n]]
	while True:
		for i in range (0, len(color_sequence)):
			LED.setColor(color_sequence[i])
			Buzz.ChangeFrequency(frequency_sequence[i])
			Buzz.start(50)
			time.sleep(0.5)
			Buzz.stop()
			time.sleep(0.5)
			LED.noColor()
			time.sleep(0.5)
		guess = getpass("Guess the color sequence")
		color_sequence_string = '' .join(color_sequence)
		validate_guess(color_sequence_string, guess.upper())
		n = random.randint(0,3)
		color_sequence.append(colors[n])
		frequency_sequence.append(frequencies[n])
		time.sleep(0.5)

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Good bye'
		LED.destroy()
