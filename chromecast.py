import pychromecast
import os
import time 
import kasa

IP_ADDRESS_PLUG = 'INSERT_IP_ADDRESS'
CHROMECAST_NAME = ['INSERT_CHROMECAST_NAMES'] # If the relevant chromecast is part of speaker groups, you should list both the name of the chromecast and the name(s) of the group(s).

def get_chromecasts(friendly_names):
  """
  Searches the network for chromecast devices matching a list of friendly
  names or a list of UUIDs.
  """
  chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=friendly_names)
  return chromecasts

def is_chromecast_connected(cast):
  """
  Checks if the inputted chromecast is connected to or not
  """
  cast.wait()
  status = cast.status
  return status.app_id != None
  
def is_any_cast_connected(casts): 
  """
  Checks if any of the inputted chromecasts are connected to or not.
  """
  if casts == []:
    raise Exception("No chromecasts are found")
    
  y = [is_chromecast_connected(x) for x in casts]
  return any(y)
  
def turn_plug_on(ip_address_plug):
  """
  Turns the smart plug on
  """
  status = os.system(f'kasa --type plug --host "{ip_address_plug}" on')
  if status != 0:
    raise Exception("Can't turn plug on")

def turn_plug_off(ip_address_plug):
  """
  Turns the smart plug off
  """
  status = os.system(f'kasa --type plug --host "{ip_address_plug}" off')
  if status != 0:
    raise Exception("Can't turn plug off")
  
def update_plug_state(state, ip_address_plug):
  """
  Updates the smart plug state
  """
  if state == True:
    turn_plug_on(ip_address_plug)
  else:
    turn_plug_off(ip_address_plug)

if __name__ == "__main__":
  casts = get_chromecasts(friendly_names=CHROMECAST_NAME)
  cast_state = None
      
  while(True):
    try:
      time.sleep(1)
      new_cast_state = is_any_cast_connected(casts)
      if cast_state != new_cast_state:
        update_plug_state(new_cast_state, IP_ADDRESS_PLUG)
        cast_state = new_cast_state
    except Exception as e:
      print(f'Step failed: {e}')
      time.sleep(10)
      continue
