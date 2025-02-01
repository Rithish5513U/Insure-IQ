from flask import Flask, render_template
from upload import upload
from predict import predict
from train import train

app = Flask(__name__)

# Register routes using add_url_rule
app.add_url_rule('/', 'index', lambda: render_template('index.html'), methods=['GET'])
app.add_url_rule('/upload', 'upload', upload, methods=['POST'])
app.add_url_rule('/train', 'train', train, methods=['GET'])
app.add_url_rule('/predict', 'predict', predict, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)