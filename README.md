### Social Engineering Chatbot for Red Team Training

#### Introduction
This Social Engineering Chatbot is designed to simulate common social engineering tactics, focusing on red team scenarios for training employees. It can be used to help employees recognize social engineering attempts and practice responding appropriately to potentially malicious interactions.

#### Features
- **Social Engineering Simulations**: Uses common tactics such as impersonation, authority pressure, urgency, or creating a sense of trust to gather sensitive information.
- **Employee Response Training**: The chatbot provides model responses to demonstrate how to properly refuse social engineering attempts.
- **Red Team Scenario Simulation**: Runs simulated red team scenarios that log attempts and employee responses for review.

#### Usage Instructions
1. **Setup Dependencies**: Install necessary Python packages using `pip`.
    ```sh
    pip install Flask
    ```
2. **Run the Chatbot**: Start the chatbot using the following command.
    ```sh
    python social_engineering_chatbot.py
    ```
3. **API Usage**: The chatbot runs on port 5000 by default. You can use the `/chat` endpoint to interact with the chatbot.
   - **Endpoint**: `POST /chat`
   - **Request Body**: `{ "user_input": "<user message>" }`
   - **Response**: `{ "response": "<chatbot reply>" }`

4. **Red Team Simulation**: Uncomment `run_red_team_simulation()` to run a red team simulation instead of starting the chatbot as a web server.

#### Example Usage
- **Chat Request**:
  ```json
  {
    "user_input": "I'm conducting a training exercise."
  }
  ```
- **Chat Response**:
  ```json
  {
    "response": "Your account seems to have some suspicious activities. Can you provide me with your employee ID and email for verification?"
  }
  ```

#### Prerequisites
- **Python 3.6 or above**: Ensure you have Python installed in your system.
- **Flask**: Used to create the chatbot's web interface.

#### How It Works
1. **Flask Web Server**: Runs a simple Flask web server to allow interactions with the chatbot.
2. **Social Engineering Scenarios**: When prompted, the chatbot uses common social engineering phrases to simulate a threat.
3. **Response Demonstration**: The chatbot also provides model responses, guiding employees on how to react to potential social engineering attempts.
4. **Logging**: Logs all interactions to `social_engineering_chatbot.log` for later analysis.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Use `pip install -r requirements.txt` to install all necessary dependencies.
3. **Run the Tool**: Use `python social_engineering_chatbot.py` to start the chatbot or run a red team simulation.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This chatbot is intended for educational purposes and internal organizational training. Users are responsible for ensuring they comply with applicable laws and regulations before using or modifying the chatbot for training purposes.
