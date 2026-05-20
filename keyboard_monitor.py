from pynput import keyboard

def on_press(key):

    print("Key Pressed:", key)

    if key == keyboard.Key.esc:
        print("Program Stopped")
        return False

with keyboard.Listener(
    on_press=on_press
) as listener:

    print("Press ESC to stop")

    listener.join()
