import asyncio;
import random;
from kasa import iot

class BulbController:
  _max_hue = 360
  _max_saturation = 100
  _max_brightness = 100
  _step = 10 # How much to change the hue by

  def __init__(self, bulb: iot.IotBulb, hue: str = None):
    self.bulb = bulb
    self.hue = int(hue) if hue else (30 * (int(random.random() * 12))) % self._max_hue # Random hue between 0 and 330

  async def start_rainbow_cycle(self, change_interval=1000):
    print(f"[{self.bulb.alias}] Starting rainbow cycle 🌈")
    print(f"[{self.bulb.alias}] Cycling through colors every", change_interval, "ms")
    while True:
      await self._set_next_hue()
      await asyncio.sleep(change_interval / 1000)

  async def _set_next_hue(self):
    self.hue = (self.hue + self._step) % self._max_hue # Ensure hue stays within the range of 0-359
    print(f"[{self.bulb.alias}] Updating hue to", self.hue)
    await self.bulb.set_hsv(self.hue, self._max_saturation, self._max_brightness)
    await self.bulb.update()
