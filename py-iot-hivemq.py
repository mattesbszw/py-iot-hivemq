import paho.mqtt.client as mqtt 
import json

MQTT_SERVER = "broker.hivemq.com"
MQTT_PORT = 1883

MQTT_CLIENT_ID = "bszwbszw" # erfinden Sie eine beliebige Client-ID


def on_connect(client, userdata, flags, reason_code, properties):  # The callback for when the client connects to the broker
    print("Connected: {0}".format(reason_code))  # Print result of connection attempt
    client.subscribe("bszw/#")  # Subscribe to the topic 
## end on_connect function


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.

    print("Message received-> " + msg.topic)
    print("Payload: " + str(msg.payload.decode("utf-8")))
    
    # Anmerkung: 
    #   - msg.topic enthält das Topic, auf dem eine Nachricht erhalten wurde
    #   - msg.payload enthält den Inhalt der Nachricht, binär codiert
    
## end on_message function



## main routine

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, MQTT_CLIENT_ID) #create new instance

client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message

client.connect(MQTT_SERVER, MQTT_PORT)
client.loop_forever()  # Start networking daemon

