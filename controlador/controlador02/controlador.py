import paho.mqtt.client as mqtt
from trabalhoSD.shared.globalVar import enviado

mqtt_broker = "localhost"
mqtt_topic_sub = "sensor"
mqtt_topic_pub = "atuador"
mqtt_topic_status = "status"

mqtt_client = mqtt.Client()
mqtt_controlador = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883, 60)

intensidade = 0
enviado = False

def on_publish(client, userdata, result):
    print("Dados Publicados.")

def on_message(client, userdata, msg):
    intensidade = int(msg.payload.decode())
    
def on_status(client, userdata, msg):
    enviado = msg.payload.decode()

def on_receive(client, userdata,msg):
    print("C")
    if(enviado!="enviado"):
        if intensidade > 50 :
            status = "Ligar 2 "
            resultado = mqtt_client.publish(mqtt_topic_pub, status)
            mqtt_client.on_publish = on_publish
        
        elif intensidade <= 50:
            status = "Desligar 2 "
            resultado = mqtt_client.publish(mqtt_topic_pub, status)
            mqtt_client.on_publish = on_publish            
    enviado = False
while True:
    mqtt_controlador.subscribe(mqtt_topic_status)
    mqtt_client.subscribe(mqtt_topic_sub)

    mqtt_controlador.on_message = on_message
    mqtt_client.on_message = on_message

   