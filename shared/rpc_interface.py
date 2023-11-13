# rpc_interface.py
import rpyc

class ControladorService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_enviar_status(self, status):
        print(f"Enviando status: {status}")
        # Adicione aqui a lógica para enviar o status para o atuador
        # Por exemplo, você pode publicar o status em um tópico MQTT
        # ou chamar uma função que controle o atuador
        # Substitua esta mensagem de exemplo pela lógica real.

    def exposed_obter_status(self):
        # Adicione aqui a lógica para obter o status, se necessário
        # Por exemplo, você pode retornar o status atual do atuador
        # ou outras informações relevantes.
        return "Status atual: OK"
