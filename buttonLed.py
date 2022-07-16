import RPi.GPIO as GPIO
import time

button=4
LED=18


def main():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED, GPIO.OUT)
  GPIO.setup(button, GPIO.IN)

  while True:
    if GPIO.input(button) == 0 :
      GPIO.output(LED, False)
    else:
      GPIO.output(LED, True)

if __name__ == '__main__':

 try:
   main()
 except KeyboardInterrupt:
   pass
 finally:
   GPIO.cleanup()
