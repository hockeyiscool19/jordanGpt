import os
import argparse
from app import create_app
import threading
import time
from werkzeug.serving import make_server
from app.utils.firebase import FIRE

app = create_app()
last_request_time = time.time()
http_server = None

@app.before_request
def update_last_request_time():
    global last_request_time
    last_request_time = time.time()

def monitor_inactivity():
    global last_request_time
    while True:
        time.sleep(180)  # Check every second
        FIRE.load_dict({"last_request_time": last_request_time}, path='/logs')
        current_time = time.time()
        if current_time - last_request_time > 20:  # 10 seconds of inactivity
            FIRE.load_dict({"last_request_time": last_request_time}, path='/logs')
            http_server.shutdown()
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Flask app")

    # Set the default host to '0.0.0.0' to ensure it binds to all network interfaces
    parser.add_argument("--host", type=str, default="0.0.0.0",
                        help="Hostname to run the app on. Default is 0.0.0.0.")
    
    # Default port is taken from the PORT environment variable if set, otherwise 5000
    default_port = int(os.environ.get("PORT", 5000))
    parser.add_argument("--port", type=int, default=default_port,
                        help=f"Port to run the app on. Default is {default_port}.")


    args = parser.parse_args()
    
    t = threading.Thread(target=monitor_inactivity)
    t.start()

    http_server = make_server(args.host, args.port, app)
    http_server.serve_forever()
