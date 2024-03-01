import string
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password: str) -> int:
    score = 0
    # Check if the password contains at least one character from each required character class
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    # Check if the password is long enough
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1
  
    return score

def check_password(password: str, common_passwords: set) -> str:
    # Check if the password is too common
    if password in common_passwords:
        return "Password is too common. Your password strength is 0."

    # Check the password strength
    score = check_password_strength(password)
    if score == 0:
        return "Password is too weak."
    elif score <= 2:
        return "Password is not strong enough."
    else:
        return "Password is strong."

def get_common_passwords(file_path: str) -> set:
    """Reads the list of common passwords from a file and returns a set."""
    try:
        with open(r"C:\Users\vicky\Downloads\Python-Password-Strength-Checker-main\Python-Password-Strength-Checker-main\templates\common.txt", "r") as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        print(f"Common password file not found at {file_path}. Returning an empty set.")
        return set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password_route():
    password = request.form['password']
    common_passwords = get_common_passwords("path/to/common.txt")
    result = check_password(password, common_passwords)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
