#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Class in Python 2.7 for testing two RFID readers with Raspberry Pi.

Use: 
$ cd TwoRC522RPi/
$ sudo python run_main_test.py 
Press Ctrl + C to finish.

"""

import sys
from module.leitor_cartao import LeitorCartao


def main(self):
    
    reader_card = LeitorCartao()
    try:
        while True:
            if not reader_card.isAlive():
               reader_card.start()
    except KeyboardInterrupt:
        print "trl+C received! Sending kill to " + reader_card.getName()
        if reader_card.isAlive():
            reader_card._stopevent.set()
            
if __name__ == '__main__':
    main(sys.argv)
  
    
