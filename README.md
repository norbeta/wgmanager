# wgmanager
Django driven "keylocker" for wireguard. Add peers to groups, generate keys and configs. 

# Requirements
* Python 3
* Wireguard
* wgconfig (pip3 install wgconfig)

# How it works
* Add your group. Here you set your network options and endpoint-address (server-address)
* Add a peer. 
* Add a key for your master (first peer). 
* Add more peers. Config for master is updated everytime a new peer is added. 

# Wishlist
* Auto update wireguard config
