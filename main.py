from ss import ss
from pynput import keyboard

def on_press(key): # im declaring global variables because i dont know how to pass it in this damn function
    global num
    try:
        if key == keyboard.KeyCode(char='p'):
            picture = ss(num, path)
            picture.takeSS()
            print("Your screenshot has been saved: " + picture.showPath())
            num += 1
        elif (key == keyboard.KeyCode(char='q')) or (key == keyboard.Key.esc):
            print("Exiting program...")
            return False
    except AttributeError:
        print('This key is not used')

def main():
    global path
    global num
    num = 0
    path = input("Type the PATH to save: ")
    print("How to use:\n1.Press P to take a screenshot\n2.Press ESC or Q to quit the program")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()