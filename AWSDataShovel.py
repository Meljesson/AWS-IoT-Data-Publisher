from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import paho.mqtt.client as mqtt
import json
#aws configuration
awsClient = AWSIoTMQTTClient("...") #Gateway 
awsClient.configureEndpoint("AWSIOTEndpoint", 8883) #
awsClient.configureCredentials("/home/admin/aws/root-CA.crt", "/home/admin/aws/awsthing.private.key", "/home/admin/aws/awsthing.cert.pem") 
awsClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
awsClient.configureDrainingFrequency(2) # Draining: 2 Hz
awsClient.configureConnectDisconnectTimeout(10) # 10 sec
awsClient.configureMQTTOperationTimeout(5) # 5 sec
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    #push message to aws
    #create a new message which includes the topic and a the payload
    message = {
        'payload': msg.payload,
        'topic': msg.topic
    }
	awsClient.publish(msg.topic, json.dumps(message), 0)
subscribed = False
def on_connect(localClient, userdata, flags, rc):
    print("Connected to local mqtt server")
    if subscribed == False:
        localClient.subscribe("#")
        awsClient.connect()
        localClient.on_message = on_message
localClient = mqtt.Client()
localClient.on_connect = on_connect
localClient.connect("localhost", 1883, 60)
localClient.loop_forever()