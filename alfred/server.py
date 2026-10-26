from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
conversation = []
app = Flask(__name__)
CORS(app)
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message']
    habits = data['habits']
    
    client = anthropic.Anthropic()
    system = f"You are Alfred, a supportive life coach AI. The user's current habits and streaks are: {habits}. Use this to motivate them. Be encouraging and positive!"
    
    conversation.append({"role": "user", "content": message})
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system,
        messages=conversation[-10:]
    )
    
    reply = response.content[0].text
    conversation.append({"role": "assistant", "content": reply})
    return jsonify({'reply': reply})
@app.route('/clear', methods=['POST'])
def clear():
    global conversation
    conversation = []
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(port=5000)
