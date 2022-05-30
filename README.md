# Turn receiver on when chromecast is connected
With this python script you can control an audio receiver based on whether a connected chromecast audio is connected to or not. 

## Description
This work can be used, if you have a good old hifi receiver, and stream music to the receiver with a Chromecast Audio. Unfortunately, Chromecast Audio is discontinued, but I'm sure many Chromecast Audios are still used. The idea is to turn the receiver on/off with a smart plug based on whether the Chromecast is connected to or not. This obviously requires that the receiver can be turned on directly by turning on the power outlet. Some receivers will, however, start on standby mode. If your receiver supports HDMI-CEC, this is unnecessary, and you can just use a HDMI-Chromecast. 

## What do you need?
* An audio receiver
* A Chromecast Audio
* A smart plug, e.g. TP Link HS110
* A Raspbery Pi or another place to run the script

## Read chromecast status
The chromecast status can be read from the [`pychromecast` library](https://pypi.org/project/PyChromecast/). First, you list the chromecast device by
```python
cast, browser = pychromecast.get_listed_chromecasts(friendly_names=CHROMECAST_NAME)
```
where `CHROMECAST_NAME` is the name of the chromecast. If the chromecast is part of any speaker group(s), you can insert a list with both the chromecast name and the speaker group name(s). The script supports this. The chromecast status is then obtained by 
```python
cast.wait()
status = cast.status
```
You need to be connected to the same wifi as the chromecast.

## Control smart plug
To control the smart plug, the [`python-kasa` library](https://python-kasa.readthedocs.io/) is used. I use a TP Link HS110, but this should work with other TP Link smart plugs as well. The plug can be turned on/off from the command line by
```bash
kasa --type plug --host "INSERT_IP_ADDRESS_OF_PLUG" on
kasa --type plug --host "INSERT_IP_ADDRESS_OF_PLUG" off
```

## Deploy script as a linux service
Finally, you need somewhere to deploy the script. I used my Raspberry Pi, but you can obviously also use a server, if you have that. I have deployed the script as a linux service. You can see how it can be done on [this link](https://websofttechs.com/tutorials/how-to-setup-python-script-autorun-in-ubuntu-18-04/) for example.
