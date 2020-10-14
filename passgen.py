import random
import time
print("    * Welcome to Random Password Generator v1.0 * ")
print("   ***********************************************")
print("     *    Developed by: Tanmay Phalke 2020     *  ")
print("     *      Visit github.com/TanmayPhalke      *  ")
print("   ***********************************************")
print("Hope this program helps you choose better passwords :p\n")
print("******************************************************")

pass_len = int(input("     ENTER THE DESIRED LENGTH OF THE PASSWORD: "))
pass_chars = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X',
    'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x',
    'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '+', ';', '<',
    '>',
    '/', '?')
print("       Generating your password...")
time.sleep(1.5)
print("            Almost there...")
pass_gen = random.choice(pass_chars)
for i in range(0, pass_len-1):
    current_char = random.choice(pass_chars)
    pass_gen = pass_gen + current_char
time.sleep(1.5)
print("******************************************************")
print("*               Your password is ready!              *")
time.sleep(1.5)
print("******************************************************")
print("*           Your new password is:", pass_gen)
time.sleep(0.5)
print("-------------------------------------------------------")
print("Thank you for using Random Password Generator v1.0\n:')")
