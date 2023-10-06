# import argparse
# from app import create_app

# app = create_app()


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Run the Flask app")
    
#     # Only one --host argument is needed
#     parser.add_argument("--host", type=str, default="127.0.0.1",
#                         help="Hostname to run the app on. Default is 127.0.0.1.")
    
#     parser.add_argument("--port", type=int, default=5000,
#                         help="Port to run the app on. Default is 5000.")

#     args = parser.parse_args()

#     app.run(debug=True, host=args.host, port=args.port)



import os
import argparse
from app import create_app

app = create_app()

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

    app.run(debug=True, host=args.host, port=args.port)
