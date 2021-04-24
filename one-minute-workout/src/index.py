from application import Application
from timer import Timer

def main():

    app = Application()
    app.initialize_json()
    app.initialize_ui()
    
if __name__ == "__main__":
    main()
