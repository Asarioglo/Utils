import pyautogui
import threading 
import datetime
import random

screenSize = pyautogui.size()
random.seed()
ended = threading.Event()

move_duration = 1
delay = 3

def moveMouse():
	while not ended.is_set():
		randx = random.randint(0, screenSize[0])
		randy = random.randint(0, screenSize[1])
		pyautogui.moveTo(randx, randy, duration = move_duration)

def main():
	new_thread = threading.Thread(target=moveMouse)
	new_thread.start()

	try:
		while not ended.is_set():
			# threading.Timer(delay, moveMouse).start()
			ended.wait(delay)
	except (KeyboardInterrupt, SystemExit):
		print("Stopping Mouse Jiggler")
		ended.set()

main()
