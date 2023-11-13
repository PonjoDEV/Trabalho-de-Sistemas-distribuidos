import paho.mqtt.client as mqtt
from trabalhoSD.shared.globalVar import enviado

mqtt_broker = "localhost"
mqtt_topic_sub = "sensor"
mqtt_topic_pub = "atuador"
mqtt_topic_status = "status"

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883, 60)
enviado = True
def on_publish(client, userdata, result):
    print("Dados Publicados.")

def on_message(client, userdata, msg):

    intensidade = int(msg.payload.decode())

    if intensidade > 50:
        status = "Ligado 1 "
        resultado = mqtt_client.publish(mqtt_topic_pub, status)
        mqtt_client.on_publish = on_publish                
    
    elif intensidade <= 50 :
        status = "Desligado 1 "
        resultado = mqtt_client.publish(mqtt_topic_pub, status)
        mqtt_client.on_publish = on_publish 
    enviado = "enviado"
    mqtt_client.publish(mqtt_topic_status, enviado)
        
mqtt_client.subscribe(mqtt_topic_sub)
mqtt_client.on_message = on_message
mqtt_client.loop_forever()