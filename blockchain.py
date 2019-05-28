#!/usr/bin/env python3

import time

##########
# CONSTS #
##########
delay = 2

time_begin = int(time.time())

while True:
  time_end = int(time.time())
  if time_begin < time_end - delay:
    time_begin = int(time.time())
    print('Waiting for new block')
