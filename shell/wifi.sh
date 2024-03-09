#!/bin/bash

ip link set wlo1 up
wpa_supplicant -B -i wlo1 -c /etc/wpa_supplicant/WIFI_NAME.conf
dhclient -v wlo1
