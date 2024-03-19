import boto3
from flask import Flask, request, render_template, jsonify

# Configure AWS credentials
AWS_ACCESS_KEY_ID = 'AKIA2RLQ5PAUZYNSGSZC'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = ''

# Initialize Flask app
app = Flask(__name__)

# Initialize Amazon Lex client
client = boto3.client('lex-runtime',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION)

# Route for handling chatbot requests
@app.route('/')
def index():
    return render_template('index.html', message=None)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user input from request
    user_input = request.form['user_input']

    # Call Amazon Lex
    response = client.post_text(
        botName='HotelBookingBot',
        botAlias='TestBotAlias',
        userId='TSTALIASID',
        inputText=user_input
    )

    # Extract bot's response
    bot_response = response['message']

    return render_template('index.html', message=bot_response)

if __name__ == '__main__':
    # Run Flask app on localhost:5000
    app.run(debug=True, port=5000)
