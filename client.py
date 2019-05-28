#!/usr/bin/env python3

while True:
  tx = input("Insert tx:")
  open('tx', 'a').write(tx)
