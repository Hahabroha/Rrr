from flask import Flask, request
from pyshorteners import Shortener
import os
import time

app = Flask(__name)

# Dictionary to store verification tokens and their creation times
verification_tokens = {}

# Get the API key from the environment variable
SHORTENER_API_KEY = os.environ.get("SHORTENER_API_KEY")

# Initialize the Shortener with your API key
shortener = Shortener(api_key=SHORTENER_API_KEY)

@app.route('/generate_verification_token', methods=['POST'])
def generate_verification_token():
    # Generate a unique verification token and store it
    verification_token = "your_unique_token_here"
    verification_tokens[verification_token] = time.time()

    # Shorten the verification token URL
    shortened_url = shortener.zxlink.in.short("https://zxlink.in/verify?token=" + verification_token)

    # Return the shortened URL to the user
    return shortened_url

@app.route('/verify_token', methods=['POST'])
def verify_token():
    received_token = request.form.get('token')  # Adjust this based on how the token is sent (e.g., via a form)

    if received_token in verification_tokens:
        token_creation_time = verification_tokens[received_token]
        current_time = time.time()

        if current_time - token_creation_time <= 12 * 3600:  # 12 hours in seconds
            # Token is valid and within the 12-hour window, mark the user as verified
            del verification_tokens[received_token]
            return "Verification successful"
        else:
            return "Token has expired"
    else:
        return "Invalid token"

if __name__ == "__main__":
    app.run()
