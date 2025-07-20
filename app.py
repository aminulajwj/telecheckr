from flask import Flask, request, jsonify
from telethon.sync import TelegramClient
import os

app = Flask(__name__)

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

client = TelegramClient('session', api_id, api_hash)

@app.route('/')
def home():
    return "✅ TeleCheckr API Running!"

@app.route('/check', methods=['POST'])
def check_number():
    number = request.form.get('number')
    if not number:
        return jsonify({'error': 'Phone number is required'}), 400

    try:
        client.connect()
        result = client.is_user_authorized()
        client.disconnect()
        return jsonify({'number': number, 'telegram_registered': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
