import hashlib

user_hash = input("Enter md5 hash: ")
wordlist = input("File name: ")
found = False

try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:
    encoded_word = word.encode('utf-8')
    digest = hashlib.md5(encoded_word.strip()).hexdigest()

    if digest == user_hash:
        print("Password Found")
        print("Password is " + word)
        found = True
        break

if not found:
    print("Password is not in the list")
