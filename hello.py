from flask import Flask
app = Flask(__name__)

@app.route('/')
def innopolis():
    return 'Sorry, I did not  have enough time to figure it out'

if __name__ == '__main__':
    app.run()