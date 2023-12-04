# Discord-RPC
# Discord Rich Presence Python Script

## Description

This Python script utilizes the `pypresence` library to set up and update Discord Rich Presence. It allows you to showcase details, state, images, and buttons on your Discord profile.

## Features

- Display custom details and state
- Show large and small images with accompanying text
- Add clickable buttons with custom labels and URLs

## Requirements

- Python 3.x
- [pypresence](https://github.com/qwertyquerty/pypresence) library
- [requests](https://docs.python-requests.org/en/latest/) library

## Usage

1. Install the required libraries using the following command:

   ```bash
   cd [parent_directory_of_project]/Discord-RPC-main/Discord-RPC-main
   pip install -r requirements.txt
   python Discord_Rpc.py
Run the script and follow the prompts to input your Discord client ID, details, state, images, text, and buttons.

The script will continuously update your Discord Rich Presence every 15 seconds.

Configuration
client_id: Your Discord application's client ID.

details: The main text displayed on your profile.

state: Additional information displayed below details.

large_image: URL of the large image to be displayed.

small_image: URL of the small image to be displayed.

large_text: Tooltip text for the large image.

small_text: Tooltip text for the small image.

button1 and button2: Names for the clickable buttons.

button1_url and button2_url: URLs for the clickable buttons.
Note
Ensure that the image URLs provided are valid and accessible.

The script will continuously run and update your presence every 15 seconds.
License

This project is licensed under the MIT License.

Acknowledgments
pypresence library developers
Contribution
Feel free to contribute to the project by opening issues or submitting pull requests.
