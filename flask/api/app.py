from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_mqtt import MQTT

mqtt_client = Mqtt(app)

def create_app():
    app = Flask(__name__)

    app.config['MQTT_BROKER_URL'] = '35.199.162.143'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True
    topic = '/flask/mqtt'

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            mqtt_client.subscribe(topic) # subscribe topic
        else:
            print('Bad connection. Code:', rc)
    
    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            topic=message.topic,
            payload=message.payload.decode()
    )       
    print('Received message on topic: {topic} with payload: {payload}'.format(**data))

    if __name__ == '__main__':
        app.run(host='10.138.0.5', port=5000)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app