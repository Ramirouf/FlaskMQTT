# MQTT Web Controller

Simple web interface built with Flask for sending commands to MQTT-enabled devices.
It allows a user to select a target device (node) and send predefined commands, such as blinking an LED or setting a numerical setpoint.

## Live Demo

You can access a live version of this application here:

[https://ramirouf.duckdns.org:23416/ej2flask/](https://ramirouf.duckdns.org:23416/ej2flask/)

## Features

- **Send a "blink" command** to a device.
- **Send a numerical setpoint** value.
- Switch between **light and dark themes**.
- Responsive interface built with Bootstrap.
- Secure communication with an MQTT broker using TLS and authentication.

## How to Use

The interface is designed to be straightforward:

1.  **Select a Node:** Choose the target device from the "Elegir nodo" dropdown menu. _Currently, the list of nodes is hardcoded in the application._
2.  **Send Commands:**
    - **Enviar destello:** Click this button to send a blink command to the selected node. The topic used is `<node_id>/destello`.
    - **Enviar setpoint:** Enter a number in the "Setpoint" field and click this button to send the value. The topic used is `<node_id>/setpoint`.
3.  **Change Theme:** Use the "Tema" dropdown in the navigation bar to switch between light and dark modes.

## Technology Stack

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **UI Framework:** Bootstrap 5 (using the Flatly theme from Bootswatch)
- **MQTT Client:** Paho-MQTT
- **Deployment:** Docker, Gunicorn, Nginx (as a reverse proxy)

## Configuration

The application is configured using environment variables. To run it yourself, you will need to provide the following:

```
# Flask session security
FLASK_SECRET_KEY=your_super_secret_key

# MQTT Broker Connection Details
SERVIDOR=your_mqtt_broker_address
PUERTO_MQTTS=8883
MQTT_USR=your_mqtt_username
MQTT_PASS=your_mqtt_password
```
