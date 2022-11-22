from flask import Flask, jsonify, redirect, render_template, request, session, url_for


def create_app():
    app = Flask(__name__)

    @app.route('/hi', methods=['POST'])
    def hello():
        return jsonify({'reply' : "welcome"}), 200
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/classRoom')
    def classroom():
        return render_template('classRoom.html')
    
    @app.route('/analysis')
    def analysis():
        return render_template('analysis.html')
    
    @app.route('/about')
    def about():
        return render_template('readme.html')

    return app