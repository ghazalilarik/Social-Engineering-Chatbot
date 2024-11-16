import random
import logging
import time
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(filename='social_engineering_chatbot.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Define typical social engineering tactics
SOCIAL_ENGINEERING_TACTICS = [
    "Your account seems to have some suspicious activities. Can you provide me with your employee ID and email for verification?",
    "This is IT support, and we're experiencing a security threat. Please confirm your password to keep your account secure.",
    "I'm conducting a survey on employee satisfaction. Could you give me some information about your department and your colleagues?",
    "Hello, I'm from HR, and we're updating employee records. Could you share your full name, contact number, and role to verify your details?",
    "We detected unusual login attempts. Can you please provide the latest 6-digit code sent to your email?",
    "Congratulations, you've been selected for a reward! To confirm, we just need your official company email address and contact details."
]

# Define typical responses to social engineering attempts
RESPONSES_TO_SOCIAL_ENGINEERING = [
    "I am sorry, but I cannot provide that information without verifying your credentials.",
    "For security purposes, I don't share personal or sensitive information over chat.",
    "Could you please send an official communication regarding this request?",
    "I do not recognize this request. I will report it to the relevant authority.",
    "I cannot give any information without checking with my supervisor."
]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("user_input")
    if not user_input:
        return jsonify({"error": "No user input provided."}), 400

    # Simulate social engineering tactic based on user input (for training purposes)
    response = generate_social_engineering_response(user_input)
    logging.info(f"User: {user_input}")
    logging.info(f"Chatbot: {response}")
    return jsonify({"response": response})

# Function to generate social engineering response
def generate_social_engineering_response(user_input):
    # Randomly choose between providing a social engineering tactic or a good response
    if "training" in user_input.lower():
        return random.choice(SOCIAL_ENGINEERING_TACTICS)
    else:
        return random.choice(RESPONSES_TO_SOCIAL_ENGINEERING)

# Function to simulate a full red team scenario
def run_red_team_simulation():
    logging.info("Starting Red Team Simulation")
    for i in range(5):
        tactic = random.choice(SOCIAL_ENGINEERING_TACTICS)
        logging.info(f"Social Engineering Attempt {i+1}: {tactic}")
        time.sleep(2)
        response = random.choice(RESPONSES_TO_SOCIAL_ENGINEERING)
        logging.info(f"Employee Response {i+1}: {response}")
    logging.info("Red Team Simulation Complete")

if __name__ == "__main__":
    print("Social Engineering Chatbot is running...")
    # Run as Flask app
    app.run(debug=True, port=5000)
    # Uncomment to run a simulation instead
    # run_red_team_simulation()
