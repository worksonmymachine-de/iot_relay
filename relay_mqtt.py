from gpiozero import OutputDevice
from paho.mqtt import subscribe
import asyncio

class RemoteRelay:
    def __init__(self, pin, mqtt_server, topic):
        self.relay = OutputDevice(pin)
        subscribe.callback(callback=self.callback, topics=topic, hostname=mqtt_server)

    def callback(self, client, userdata, message):
        self._switch(int(message.payload))
        

    def _switch(self, status):
        print(f"switch called with {status} - current status: {self.relay.value}")
        if status is not self.relay.value:
            print(f"switching to: {status}")
            self.relay.toggle()
            
if __name__ == '__main__':
    asyncio.run(RemoteRelay(4, "192.168.188.37", "/setting/picenter/relay/"))
