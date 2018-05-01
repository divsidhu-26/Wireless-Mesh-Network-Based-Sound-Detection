# WIRELESS MESH NETWORK BASED SOUND DETECTION
To run the website on your laptop,
1. Download/Clone and unzip the file 
2. cd website/
3. pip install -r requirements.txt
(In case, this does not work - pip freeze > requirements.txt and rerun)
4. python manage.py runserver <port-number>
Voila! Website gets deployed at http://127.0.0.1:<port-number>

The Arduino folder contains the codes for the arduinos
1. r1ino: Arduino code for a node not on the edge of the mesh. It transmits value received both from a sound sensor and from        </t>another sensor node
2. r2.ino : Arduino code for reading value from a sound sensor on an edge node and transmitting it through XBee

To get it to work install this on Arduino:-
1. Install [Arduino Software](https://www.arduino.cc/en/Guide/Linux) software.
2. Import codes from the ino files for the respective arduinos.


RPI/script_py is the python script to be run on the RPI. 


[XCTU software](https://www.digi.com/products/xbee-rf-solutions/xctu-software/xctu) has been used for the working of the xbee.
XCTU_Configuration files are the configuration files for the xbee. 
Import these are you are good to go.
