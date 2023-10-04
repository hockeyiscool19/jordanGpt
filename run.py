# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)


import argparse
from app import create_app

app = create_app()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Flask app")
    parser.add_argument("--host", type=str, default="127.0.0.1",
                        help="Hostname to run the app on. Default is 127.0.0.1.")
    parser.add_argument("--port", type=int, default=5000,
                        help="Port to run the app on. Default is 5000.")

    args = parser.parse_args()

    app.run(debug=True, host=args.host, port=args.port)
