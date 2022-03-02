import signal
import time
def handler(signum, frame):
  raise Exception("end of time")
signal.signal(signal.SIGALRM, handler)
signal.alarm(2)
try:
  time.sleep(6)
except Exception:
  print("Can't run")
print("Ended")