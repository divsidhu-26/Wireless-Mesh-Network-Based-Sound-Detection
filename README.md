# WIRELESS MESH NETWORK BASED SOUND DETECTION
### Website
To run the website on your laptop,
1. Download/Clone and unzip the file 
2. cd website/
3. pip install -r requirements.txt
(In case, this does not work - pip freeze > requirements.txt and rerun)
4. python manage.py runserver <port-number>
Voila! Website gets deployed at http://127.0.0.1:<port-number>

### Arduino
The Arduino folder contains the codes for the arduinos
1. r1ino: Arduino code for a node not on the edge of the mesh. It transmits value received both from a sound sensor and from      </t> another sensor node
2. r2.ino : Arduino code for reading value from a sound sensor on an edge node and transmitting it through XBee

To replicate our settings, do the following:-
1. Install [Arduino Software](https://www.arduino.cc/en/Guide/Linux).
2. Connect arduino-uno to your laptop.
3. Import codes from the ino files for the respective arduinos.

###### PIN DIAGRAM
![Pin Diagram](https://github.com/divsidhu-26/cop315/blob/master/Arduino/pin_diagram.png)
<br>The arduino module is connected to a sound sensor (KY037) which detects the sound, a battery which powers the arduino and 
an xbee which takes care of communication to others.

### RPI
RPI/rpi_script.py is the python script to be run on the RPI.
Just run this on the RPI terminal.

### Xbee Modules
[XCTU software](https://www.digi.com/products/xbee-rf-solutions/xctu-software/xctu) has been used for the working of the xbee.
<br>XCTU_Configuration files are the configuration files for the xbee. <br>
Import these and you are good to go.

Other details of the project can be found [here](https://cop315.wordpress.com).
