from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic rule-based responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! It's nice to see you. How are you feeling?",
    "anxiety": "I'm sorry to hear that you're feeling anxious. Can you share what's causing your anxiety?",
    "stress": "I understand that you're feeling stressed. Can you tell me more about what’s making you feel this way?",
    "sad": "It’s okay to feel sad sometimes. Can you share what's making you feel this way?",
    "happy": "I'm glad to hear that you're feeling happy! What’s bringing you joy today?",
    "help": "I'm here to help you. Can you share more about what you need assistance with?",
    "overwhelmed": "It sounds like you’re feeling overwhelmed. What parts of your life are weighing heavily on you?",
    "bored": "I see you're feeling bored. What activities do you enjoy that you haven’t done recently?",
    "excited": "That’s wonderful! What’s got you feeling so excited today?",
    "lonely": "I'm sorry to hear that you're feeling lonely. Can you tell me more about how you're feeling?",
    "angry": "It's okay to feel angry. Can you share what’s making you feel this way?",
    "nervous": "Feeling nervous is normal. What’s on your mind that’s making you feel this way?",
    "hopeful": "It’s great to feel hopeful! What are you looking forward to right now?",
    "frustrated": "I understand that you’re feeling frustrated. Can you tell me what’s bothering you?",
    "confused": "It’s normal to feel confused sometimes. Can you share what’s confusing you?",
    "grateful": "Feeling grateful is wonderful. What are you feeling thankful for right now?",
    "motivated": "That's fantastic! What’s inspiring your motivation today?",
    "jealous": "Feeling jealous can be tough. Can you share what triggered this feeling?",
    "tired": "I hear you. Being tired can really affect your mood. Are you getting enough rest?",
    "afraid": "It’s okay to feel afraid. Can you tell me more about what you’re afraid of?",
    "hope": "Hope is a powerful feeling. What gives you hope today?",
    "ashamed": "It’s important to talk about feelings of shame. Can you share what you’re feeling ashamed of?",
    "curious": "Curiosity is a great trait! What are you curious about right now?",
    "inspired": "I’m glad to hear you’re feeling inspired! What’s motivating you?",
    "regret": "Regret can be heavy. Can you share what you wish you could change?",
    "satisfied": "It’s great to feel satisfied! What’s contributing to this feeling for you?",
    "anxious": "I understand that you're feeling anxious. Can you tell me what's on your mind?",
    "empty": "Feeling empty can be unsettling. Can you describe what you're feeling right now?",
    "lost": "It’s okay to feel lost sometimes. What aspects of your life feel uncertain to you?",
    "content": "I'm glad you're feeling content. What’s making you feel this way right now?",
    "disappointed": "Disappointment can be hard to deal with. Can you tell me what has led to this feeling?",
    "embarrassed": "Embarrassment is common. What happened that made you feel this way?",
    "worried": "I understand that you're feeling worried. What’s on your mind that’s causing you to worry?",
    "calm": "I’m glad to hear you’re feeling calm! What practices help you maintain this feeling?",
    "excited": "It sounds like you're really excited! What’s making you feel this way?",
    "appreciative": "Feeling appreciative is great! What are you feeling thankful for right now?",
    "overjoyed": "That’s wonderful! What has brought you so much joy recently?",
    "enthusiastic": "Your enthusiasm is infectious! What’s making you feel so enthusiastic?",
    "unmotivated": "Lack of motivation can be frustrating. Can you identify what’s causing it?",
    "determined": "Determination is a powerful feeling! What are you determined to achieve?",
    "isolated": "Feeling isolated can be challenging. Can you share more about your feelings?",
    "nostalgic": "Nostalgia can bring both joy and sadness. What memories are you reflecting on?",
    "encouraged": "I’m glad you’re feeling encouraged! What’s giving you this encouragement?",
    "apprehensive": "Feeling apprehensive is normal. What’s causing you to feel this way?",
    "indifferent": "Indifference can feel strange. Can you share what’s making you feel this way?",
    "curious": "Curiosity is a wonderful trait! What are you curious about right now?",
    "unsettled": "Feeling unsettled can be tough. Can you tell me more about what you’re experiencing?",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message', '')
    # Simple response logic
    response = responses.get(user_input.lower(), "I'm not sure how to respond to that. Can you tell me more?")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
