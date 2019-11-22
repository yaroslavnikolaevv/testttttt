import time
import paho.mqtt.client as mqtt
from s7_pars import *
#Callbacks
def on_connect(client,userdata,flags,rc):
    print('Connected with code'+str(rc))
    #Sub
    client.subscribe("Inform/#")
def on_message(client,userdata,msg):
    line=msg.payload.decode("UTF-8")
    print(line)
    a=line.split(":")
    fromInput1=a[0]
    fromOutput1=a[1]
    date1=a[2]
    print(fromInput1)
    print(fromOutput1)
    print(date1)
    client.publish("toglobal2",S7('владивосток', 'москва', '12.09.2020').poisk())
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect("m16.cloudmqtt.com",11729,60)
client.username_pw_set("tizzoqtl", "sqCYE8vpFV1P")

time.sleep(1)
client.loop_start()
while True:
    client.publish("Tutorial/","Getting started with MQTT")
    time.sleep(15)

client.loop_stop()
client.disconnect()
