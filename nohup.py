import os
import sys

def nohup(func):
  try: 
    pid = os.fork() 
    if pid > 0:
      return
  except OSError, e:
    print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
    sys.exit(1)

  os.setsid()

  try: 
    pid = os.fork() 
    if pid > 0:
      sys.exit(0) 
  except OSError, e: 
    print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
    sys.exit(1)

  func()

  os._exit(os.EX_OK)
