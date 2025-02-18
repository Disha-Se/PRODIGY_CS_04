# PRODIGY_CS_04
# Keylogger in Python

This is a simple Python keylogger that records keystrokes and saves them to a text file (`keylog.txt`).

## Features
- Logs all keyboard inputs.
- Saves keystrokes to a file (`keylog.txt`).
- Stops recording when the `Esc` key is pressed.

## Requirements
Ensure you have Python installed. Additionally, install the required package:

```sh
pip install keyboard
```

## Usage

1. Clone this repository or download the script.
2. Run the script using:
   ```sh
   python keylogger.py
   ```
3. The script will record all keystrokes and save them in `keylog.txt`.
4. Press `Esc` to stop the keylogger.

## File Structure
```
├── keylogger.py    # Keylogger script
├── keylog.txt      # Output file containing logged keys
├── README.md       # Documentation
```

## How It Works
- Uses the `keyboard` module to listen for key presses.
- Each key press is recorded in `keylog.txt`.
- The script runs until `Esc` is pressed.
- If you don't see the textfile on your pc search for it in the file explorer and then click on it to see which keys you used while this code was running.

## Disclaimer ⚠️
This script is for **educational purposes only**. Unauthorized use of keyloggers can violate privacy laws. Ensure you have **explicit permission** before using this software.

## Author
Disha Sejpal

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

