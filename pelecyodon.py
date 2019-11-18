# -*- coding: utf-8 -*-

# Copyright (c) Evgenii Kliuchnikov 2019
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Pelecyodon is an extinct genus of ground sloths from the Early Miocene.

This small and simple utility allows throttling applications working in a
"busy loop" mode.
"""

import os
import signal
import sys
import time
from subprocess import Popen, PIPE

def send_signal_and_sleep(pid, sig, milliseconds):
 '''Pause / resume process and wait.'''
 # If target process has not been found - do nothing.
 if pid >= 0:
  try:
   # "kill" is a weird name of method for sending a signal...
   os.kill(pid, sig)
  except OSError:
   # If process has already gone, do not worry.
   pass
 # Do noting. In the meanwhile, target process is either paused, or running.
 time.sleep(milliseconds / 1000)

def main():
 '''Scan process list and throttle secified process, until terminated.'''
 # Default ratio
 target_ratio = 0.2
 # Script's own process ID
 self_pid = os.getpid()
 num_args = len(sys.argv)
 # Check arguments.
 if num_args < 2 or num_args > 3:
  print("Usage: pelecyodon TARGET [PERCENT]")
  sys.exit()
 target = sys.argv[1]
 if num_args == 3:
  target_ratio = int(sys.argv[2])
  if target_ratio < 1 or target_ratio > 99:
   print("Invalid argument: PERCENT shall be in the in the range 1..99")
   target_ratio = target_ratio / 100.0
   sys.exit()

 # Repeat until terminated...
 while True:
  # Negative value is used to denote that target process is not found
  target_pid = -1
  # List runining processes, equivalent to 'ps -eo pid,command` in terminal.
  process = Popen(['ps', '-eo', 'pid,command'], stdout=PIPE, stderr=PIPE)
  # Run command, take 'console' output.
  stdout, _ = process.communicate()
  # Iterate through the found processses.
  for line in stdout.splitlines():
   pid, cmdline = line.split(' ', 1)
   # If the process name (command line) contains what we want...
   if cmdline.find(target) >= 0:
    # ...we guess it is a target process...
    pid = int(pid)
    if pid != self_pid:
     target_pid = int(pid)
  # Repeat 1000 times. Each iteration should last 1ms.
  # Consequently we scan process list just once in a second
  for _ in range(1000):
   send_signal_and_sleep(target_pid, signal.SIGSTOP, 1 - target_ratio)
   send_signal_and_sleep(target_pid, signal.SIGCONT, target_ratio)

if __name__ == "__main__":
 main()
