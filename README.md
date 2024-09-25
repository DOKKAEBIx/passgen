# Password Generator Script

This Python script is here to help you create secure and customizable passwords tailored to your needs. It follows the best practices for password security by letting you choose whether to include uppercase letters, special characters, and numbers. Plus, it ensures your password meets certain length requirements, making it strong and reliable.

 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)  
          `-    \`_`"'- 

## Features

- **User Interaction**: The script interacts with the user through the command line, asking a series of questions to tailor the password generation process to individual preferences.

- **Customizable Length**:
  - Users can choose to specify a password length between **8 and 100 characters**. If the user opts not to specify a length, the script defaults to **12 characters**.
  - The script includes validation to ensure the input length is within the allowed range.

- **Character Set Options**:
  - Users can select whether to include:
    - **Uppercase Letters**: A–Z
    - **Special Characters**: Common symbols like `!@#$%^&*()_+-=[]{}|;':",.<>?`
    - **Numbers**: Digits from 0 to 9

- **Secure Password Generation**: The password is generated by randomly selecting characters from a combined set based on user preferences, ensuring that each password is unique and difficult to guess.

- **Debugging Output**: The script includes a print statement to display the character set used for generating the password. This feature is helpful for verifying the contents and understanding how the final password is constructed.

## Example Usage

When run, the script will ask:
- If the user wants to specify a length.
- If the user wants to include uppercase letters.
- If the user wants to include special characters.
- If the user wants to include numbers.

Based on these inputs, the script generates a secure password and displays it.

## Implementation

The script leverages Python's `random` and `string` modules to facilitate password generation, ensuring a well-randomized selection process from the specified character set.
