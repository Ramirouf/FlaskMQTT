from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import os, logging, ssl
from functools import wraps
from werkzeug.middleware.proxy_fix import ProxyFix
import paho.mqtt.publish as publish

logging.basicConfig(format='%(asctime)s - Ej2Flask - %(levelname)s - %(message)s', level=logging.INFO)

app = Flask(__name__)
# Get environment variables:

app.config["SECRET_KEY"] = os.getenv('FLASK_SECRET_KEY')

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
tls_config = {'tls_version': ssl.PROTOCOL_TLS}

MQTT_BROKER = os.getenv('SERVIDOR')
MQTT_PORT = int(os.getenv('PUERTO_MQTTS')) # Porque Paho MQTT espera un int para conectarse
MQTT_USER = os.getenv('MQTT_USR')
MQTT_PASSWORD = os.getenv('MQTT_PASS')

AVAILABLE_NODES = [
    {"id": "6553C66F88E0CD81", "name": "Raspberry Pi Pico 2W - Ramiro"}
]

@app.route('/')
def index():
    return render_template('index.html', nodes= AVAILABLE_NODES)

@app.route('/set_theme', methods=['POST'])
def set_theme(theme):
    if theme in ['light', 'dark']:
        session['theme'] = theme
        return jsonify({'status': 'success', 'message': f'Theme set to {theme}.'})
    return jsonify({'status': 'error', 'message': 'Invalid theme.'}), 400

@app.route('/send_blink', methods=['POST'])
def send_blink():
    try:
        data = request.json
        node_id = data.get('node_id')
        if not node_id:
            return jsonify({'status': 'error', 'message': 'Node ID is required.'}), 400
        
        topic = f"{node_id}/destello"
        payload = "1"  # Assuming '1' is the command to trigger the blink
        logging.info(f"Sending blink command to {node_id} on topic {topic}")
        publish.single(topic, payload, hostname=MQTT_BROKER, port=MQTT_PORT, auth={'username': MQTT_USER, 'password': MQTT_PASSWORD}, tls=tls_config)
        return jsonify({'status': 'success', 'message': f'Blink command sent to {node_id}.'})
    except Exception as e:
        logging.error(f"Error sending blink command: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/send_setpoint', methods=['POST'])
def send_setpoint():
    try:
        data = request.json
        node_id = data.get('node_id')
        setpoint = data.get('setpoint')
        if not node_id or setpoint is None:
            return jsonify({'status': 'error', 'message': 'Node ID and setpoint are required.'}), 400
        
        topic = f"{node_id}/setpoint"
        payload = str(setpoint)
        logging.info(f"Sending setpoint {setpoint} to {node_id} on topic {topic}")
        publish.single(topic, payload, hostname=MQTT_BROKER, port=MQTT_PORT, auth={'username': MQTT_USER, 'password': MQTT_PASSWORD}, tls=tls_config)
        return jsonify({'status': 'success', 'message': f'Setpoint {setpoint} sent to {node_id}.'})
    except Exception as e:
        logging.error(f"Error sending setpoint: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500