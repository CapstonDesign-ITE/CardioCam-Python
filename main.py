import json

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print('connected to the mqtt server')

def on_subscribe(client, userdata, mid, granted_qos):
    print('subscribing', str(mid))

def on_message(client, userdata, msg):
    a = str(msg.payload.decode('utf-8'))
    print(a)
    data = json.loads(a)
    print(type(data))
    print(data['data'])

client = mqtt.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect('117.16.243.99', 5503)
client.subscribe('app/request', 1)
client.loop_forever()
