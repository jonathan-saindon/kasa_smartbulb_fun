import asyncio
import os
from dotenv import load_dotenv
from enum import Enum
from kasa import iot
from controller import BulbController

load_dotenv()
ip_addresses = os.getenv("IP_ADDRESSES").split(',')
start_hue = os.getenv("START_HUE")

class Speed(Enum):
  VerySlow = 5000 # Useful to see the colors change
  Slow = 3000
  Medium = 1000
  Fast = 500

async def get_bulb(ip) -> iot.IotBulb:
  bulb = iot.IotBulb(ip)
  await bulb.update() # Load bulb information

  print(f"[{bulb.alias}] {bulb.device_type.name} found")
  print(f"[{bulb.alias}] Status: {'On' if bulb.is_on else 'Off'}")

  return bulb

async def __main__():
  tasks = []
  for ip in ip_addresses:
    bulb = await get_bulb(ip)

    if not bulb.is_on:
      print(f"[{bulb.alias}] Turning on")
      await bulb.turn_on()

    ctrl = BulbController(bulb, start_hue)
    task = asyncio.create_task(ctrl.start_rainbow_cycle(Speed.Fast.value))
    tasks.append(task)

  # Run all tasks concurrently
  await asyncio.gather(*tasks)

# Run script
asyncio.run(__main__())