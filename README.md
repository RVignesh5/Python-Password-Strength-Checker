# Python-Password-Strength-Checker
This Python script assesses the strength of user passwords, providing insights into their security level. The script evaluates passwords based on criteria such as length, character variety, and the inclusion of common passwords.

<img src="https://cioafrica.co/wp-content/uploads/2024/01/cyber-security-1536x864.jpeg">   

## Features

1. Utilizes Flask for a web-based interface.
2. Checks for the presence of uppercase, lowercase, numeric, and special characters in the password.
3. Assesses password strength based on a scoring system.
4. Flags passwords that are too common.
5. Includes a simple HTML interface for user interaction.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/RVignesh5/password-strength-checker.git
    ```

2. Install dependencies:

    ```bash
    pip install flask
    ```

3. Run the script:

    ```bash
    python app.py
    ```

4. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the password strength checker.

## Customization

- **Common Passwords:** You can customize the list of common passwords by modifying the `common.txt` file.
- **Password Strength Criteria:** Adjust the scoring system in the `check_password_strength` function to fit your security requirements.

## Contributing

Contributions are welcome! If you find issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

**Note:** Avoid sharing or storing sensitive information, such as actual passwords or personal data, in the repository.
