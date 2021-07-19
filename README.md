# Two RFID with Raspberry PI 
Two RFID MFRC522 readers with Raspberry Pi 3 b

Assuming the python-dev and SPI-Py libraries are already correctly installed, configured, and tested on Raspberry Pi.

Otherwise, here is a brief help:
```{r, engine='bash', count_lines}
$ sudo apt-get install python-dev
$ git clone https://github.com/lthiery/SPI-Py.git
$ cd SPI-Py
$ sudo python setup.py install
```

Use: 
```{r, engine='bash', count_lines}
$ git clone https://github.com/AriBram/TwoRFIDsystem.git
$ cd TwoRC522RPi/
$ sudo python run_main_test.py 
```
Press Ctrl + C to finish.

![alt tag](https://www.raspberrypi.org/forums/download/file.php?id=16527)
