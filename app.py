om flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 AutoDeployX is Live on AWS via Jenkins!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

