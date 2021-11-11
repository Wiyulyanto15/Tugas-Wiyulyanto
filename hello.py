from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_Sirah():
    return 'Hello, Wiyulyanto! Ini pertama kali saya melakukannya '+__name__
