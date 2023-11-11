import paho.mqtt.client as mqtt
from controlador01 import controlador as controlador1

mqtt_broker = "localhost"  
mqtt_topic_sub = "sensor"
mqtt_topic_pub = "atuador"

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883, 60)

resposta = False

def protocolo():
    resposta = controlador1.resposta2
    
def resposta() Boolean:
    
return True

def on_publish(client, userdata, result):
    print("Dados Publicados.")
    
def on_message(client, userdata, msg):
    
    intensidade = msg.payload.decode()
        
    if intensidade > "50" and controlador1.enviado == False:
        status = "Ligar"
        resultado = mqtt_client.publish(mqtt_topic_pub, status)
        mqtt_client.on_publish = on_publish
    
    elif intensidade <= "50" and controlador1.enviado == False:
        status = "Desligar"
        resultado = mqtt_client.publish(mqtt_topic_pub, status)
        mqtt_client.on_publish = on_publish
    
mqtt_client.subscribe(mqtt_topic_sub)
mqtt_client.on_message = on_message
globalVar.enviado = False
mqtt_client.loop_forever()