from os import path
from pywebio.platform import path_deploy

HOST = "0.0.0.0"
PORT = 8080

if __name__ == "__main__":

    here_dir = path.dirname(path.abspath(__file__))
    try:
        path_deploy(f"{here_dir}", port=PORT, host=HOST, debug=True)
    except Exception as e:
        pass