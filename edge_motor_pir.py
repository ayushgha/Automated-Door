import RPi.GPIO as GPIO
from time import sleep

pir = 29
motor1A = 16
motor1B = 18
motor1E = 22


GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor1E, GPIO.OUT)
GPIO.setup(pir, GPIO.IN)


pwm = GPIO.PWM(motor1E, 500)
incr = 100
pwm.start(100)
while incr>0:
#while True:
	try:

	if (GPIO.input(pir)):
		GPIO.output(motor1A, GPIO.HIGH)
		GPIO.output(motor1B, GPIO.LOW)
		GPIO.output(motor1E, GPIO.HIGH)
		pwm.start(incr)
		incr = incr - 5
		sleep(10)
	else:
		print("NOT Detected, No Motor")

GPIO.output(motor1A, GPIO.LOW)
GPIO.output(motor1B, GPIO.HIGH)
GPIO.output(motor1E, GPIO.HIGH)

sleep(1)
	except:
		GPIO.output(motor1E, GPIO.LOW)
		GPIO.cleanup()


