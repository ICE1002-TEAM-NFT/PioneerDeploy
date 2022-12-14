from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_mqtt import Mqtt
import csv
import json
import pandas as pd
from fun import csv_make,csv_add


def create_app():

    global tmp_data
    tmp_data = {
        'class_room': 0,
        'info': "0",
        'used_time': 0,
    }
    
    csv_make()
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')
        
    @app.route('/building_1')
    def home2():
        return render_template('index2.html')
    
    @app.route('/building_1/307', methods=['GET', 'POST'])
    def get_307():
        f = open("data.csv", "r")
        rdr = csv.reader(f)
        lines = []
        for line in rdr:
            
            if line[1] == "435":
                tmp_data['info'] = line[2]
                tmp_data['used_time'] = line[3]

        json_data = json.dumps(tmp_data)
        f.close()
        return jsonify(json_data)

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
        tmp = message.payload.decode()
        csv_add(tmp)

    @app.route('/publish')
    def publish_message():
        publish_result = mqtt_client.publish("esp32/IR", "001")
        return "1"

    return app



