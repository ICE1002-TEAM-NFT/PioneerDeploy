from flask import Flask, jsonify, redirect, render_template, request, session, url_for


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return render_template('index.html')

    return app