# wgmanager
Django driven "keylocker" for wireguard. Add peers to groups, generate keys and configs. 
Uses the django-admin interface directly. 

### Requirements
* Python 3
* Wireguard
* wgconfig (pip3 install wgconfig)

### Installation
* Clone the repo to where you would like your installation
* Create a venv
* Run pip install -r requirements.txt to install depencies 
* Get it up and running with your choice of WSGI handler
* Turn off debug-mode in settings.py
* Fill in a new secret-key in settings.py
* Update allowed hosts in settings.py

### How it works
* Add a group
	* The group contains information about IP networks, ports and endpoint that the peers connects to
* Add a peer
	* First add your master peer. This is needed when generating the keypair for the master. 
* Add a key for your master
	* When adding a key to a group with a peer, a keypair will be generated automagically. 
	* Tick the master checkbox for your master
* Add more peers (clients)
* Add keypairs to the clients
	* When adding a key, a keypair will be suggested automagically. 
	* Choose an available IP address for both IPv4 and IPv6
	* If you click "Save and continue editing", the configfile will appear for the newly created peer. 
* When new peers are added, the config for master is updated dynamically and can be copy&pasted right into the server

### Wishlist
* Auto update wireguard config
* Status of the peers (host up/down, latest handshake)
