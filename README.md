# GPT Chat Interface

The Friendly Chat Interface is a Python application that provides a graphical user interface (GUI) for interacting with multiple AI chat providers. It allows users to send messages and receive responses from various chatbots. The application is built using PySide6 and incorporates features like translation to Persian using the Google Translate API and a dark theme for the interface.

## Features

- Select from various AI chat providers, including GPTalk, Hashnode, GeekGpt, and more.
- Translate responses to Persian using the Google Translate API.
- Apply a dark theme to enhance the user interface.
- Easily switch between different chat providers during the conversation.
- Intuitive GUI with input field, conversation box, and options for customization.

## Requirements

- Python 3.8+
- PySide6
- googletrans
- g4f

## Usage

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python your_script_name.py
   ```

3. Select a chat provider from the dropdown.
4. Type a message in the input field and press Enter or click "Send Message."
5. View the responses from the selected providers in the conversation box.
6. Check "Answer Persian" to translate the responses to Persian.
7. Change the chat provider at any time to interact with different bots.

## Code Structure and Improvements

The code is organized into a `GptChat` class, which manages the GUI components and communication with chat providers. Some potential improvements include:

- Loading the list of providers from a config file.
- Lazy instantiation of the Translator when translation is selected.
- Taking the jailbreak value from user input for flexibility.
- Proper asynchronous handling and awaiting tasks for better performance.
- GUI enhancements, such as language selection, font options, etc.
- Error handling to prevent crashes from invalid bot responses.
- Unit and integration tests to ensure robustness.
- Adding more comments for code clarity and using descriptive method and variable names.

## License

This project is licensed under the MIT License.
