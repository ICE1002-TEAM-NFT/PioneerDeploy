from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_mqtt import Mqtt
import datetime
import pandas as pd
from fun import csv_make, csv_add


def create_app():

    csv_make()
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')
        
    @app.route('/1')
    def home2():
        return render_template('index2.html')
    
    @app.route('/esp32', methods=['GET'])
    def esp32_data_get():

        return render_template('mqtt_test.html')

    return mqtt(app)

def mqtt(app):
    app.config['MQTT_BROKER_URL'] = ''
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

        ### This is for test
        # print(tmp)
        # f = open("data.txt", 'a')
        # f.writelines(tmp+"\n")
        # f.close()

        csv_add(tmp)



    @app.route('/publish')
    def publish_message():
        # request_data = request.get_json()
        publish_result = mqtt_client.publish("esp32/IR", "001")
        return "1"
    
    ### This is for debuging
    # @app.route('/check')
    # def check():

    #     f = open("data.txt", 'r')
    #     ans = f.read()
    #     return ans
    
    return app



