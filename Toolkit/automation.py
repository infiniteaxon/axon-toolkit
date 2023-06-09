import time
import os


def munge():
    os.system("ls")
    print("-------------------------------")
    source = input("Select a file above to Munge...")
    output = input("Please input the name of your desired output file (no extension needed)...")
    os.system("python mungeit.py -l 9 -i " + source + " -o " + output + ".dict")
    return


def hashcat():
    global hashoutput
    print("We're gonna need some more info to start cracking. Please input that as it is requested. \n")
    hashoutput = input("Please input the name of your desired output file (no extension needed)...")
    target = input("Please input the filename of your target hashes (no extension needed)...")
    dictionary = input("Please input the path to your dictionary or just the filename if it shares this directory (no "
                       "extension needed)...")
    rule = input("Please input any rules you'd like to include... (NULL is required if no rules desired)... ")
    if rule == "NULL":
        os.system("hashcat -m 0 -a 0 -o " + hashoutput + ".pot " + target + ".hash " + dictionary + ".dict --show")
    else:
        os.system("hashcat -m 0 -a 0 -o " + hashoutput + ".pot " + target + ".hash " + dictionary + ".dict -r" + rule + " --show")

    time.sleep(3)
    return
    
    
def password():
    print("[-----Cracked Hashes-----]")
    print("\n")
    os.system("cat " + hashoutput + ".pot")
    print("\n")
    exit = input("Press ENTER to goto menu...")
    if exit == "":
    	return

def loop():
    print("\n")
    print("Task Attempted")
    time.sleep(3)
    os.system("clear")
    return


logo = "         _           _      _              _            _           \n" \
       "        / /\       /_/\    /\ \           /\ \         /\ \     _   \n" \
       "       / /  \      \ \ \   \ \_\         /  \ \       /  \ \   /\_\ \n" \
       "      / / /\ \      \ \ \__/ / /        / /\ \ \     / /\ \ \_/ / / \n" \
       "     / / /\ \ \      \ \__ \/_/        / / /\ \ \   / / /\ \___/ /  \n" \
       "    / / /  \ \ \      \/_/\__/\       / / /  \ \_\ / / /  \/____/   \n" \
       "   / / /___/ /\ \      _/\/__\ \     / / /   / / // / /    / / /    \n" \
       "  / / /_____/ /\ \    / _/_/\ \ \   / / /____\/ // / /    / / /     \n" \
       " / /_________/\ \ \  / / /   \ \ \  \/_________/ \/_/     \/_/      \n" \
       "/ / /_       __\ \_\/ / /    /_/ / --.--               |  | o|      \n" \
       "\ \  \     /     / \/_ /_\  /_ \/    |  ,---.,---.|    |__/ .|---   \n" \
       " \_\__\   /_/_/_/_ /\__\_/  \__/     |  |   ||   ||    |  \ ||      \n" \
       "=================================    `  `---'`---'`---'`   ```---'  \n" \
       "\n" \
       "Mungeit Main Algorithms by iq-thegoat\n" \
       "Automation by Axon\n" \
       "Not Intended for Malicious Use\n"

options = "------------------------------------------------------------------\n" \
          "Menu\n" \
          "1. Munge a Dictionary\n" \
          "2. Crack the Hash\n" \
          "3. Show Cracked Passwords\n" \
          "4. Exit\n"

while True:
    print(logo, options)
    decision = input("Select a Number (1-4):")
    print("\n")

    match decision:
        case "1":
            munge()
            loop()
        case "2":
            hashcat()
            loop()
            password()
        case "3":
            password()
        case "4":
            break
        case _:
            continue

print("Thanks for trying the program! Goodbye.  \n")
print("Github:                                  \n"
      "https://github.com/iq-thegoat            \n"
      "https://github.com/infiniteaxon          \n")
time.sleep(10)
