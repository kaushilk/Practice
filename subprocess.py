import os
import subprocess

def basic_commands():
    # Function takes user input and executes on command line
    u_in = input(">>")
    subprocess.call(u_in)
    return "Success!"
test
def multiple():
    print("Under constructiongit")
    return "Success!"

def execute_file():
    # function changes directory and then executes a python file
    os.chdir("/Users/kaushil.katakam@ibm.com/Desktop/Practice code/Practice/system_manipulation/sample_folder")
    subprocess.call('python3 num_list.py', shell=True)
    return "Success!"


def dice():
    user_choice = int(input("Select a number 1-5: "))
    outcomes = {
    1: basic_commands,
    2: multiple,
    3: execute_file,

    }
    answer = outcomes.get(user_choice, lambda: "Not a valid input")

    return answer()


print(dice())
