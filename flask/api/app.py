from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_mqtt import Mqtt


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')
        
    @app.route('/1')
    def home2():
        return render_template('index2.html')
    
    @app.route('/esp32')
    def esp32_get():
        return render_template('mqtt_test.html')

    return mqtt(app)

def mqtt(app):
    app.config['MQTT_BROKER_URL'] = '35.199.162.143'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True
    topic = 'esp32/IR'

    mqtt_client = Mqtt(app)

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            mqtt_client.subscribe(topic) # subscribe topic
        else:
            print('Bad connection. Code:', rc)

    tmp="none"
    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            topic=message.topic,
            payload=message.payload.decode()
        )
        tmp = 'Received message on topic: {topic} with payload: {payload}'.format(**data)
        print(tmp)


    @app.route('/publish')
    def publish_message():
        # request_data = request.get_json()
        publish_result = mqtt_client.publish("esp32/IR", "001")
        return "1"
    
    @app.route('/check')
    def check():
        return tmp
    
    return app



