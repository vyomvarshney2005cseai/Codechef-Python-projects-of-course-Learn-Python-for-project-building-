from cryptography.fernet import Fernet

def userChoice(choice):

    if choice == 1:
        generate_key()

    elif choice == 2:
        input_file = input("Enter the file to encrypt: ")
        output_file = input("Enter the output file name: ")
        encrypt_file(input_file, output_file)

    elif choice == 3:
        input_file = input("Enter the file to decrypt: ")
        output_file = input("Enter the output file name: ")
        decrypt_file(input_file, output_file)

    elif choice == 4:
        return "Exiting application... Goodbye!"

    else:
        print("Invalid choice!\n")


# Update the code below to solve the problem
#--------------------------------------------------------
def generate_key():
    key=Fernet.generate_key()
    with open("/Users/vyomvarshney2005/Desktop/codechef python projects/Intermediate-level projects/File Encryption Tool/secret.key",'wb') as keyfile:
        keyfile.write(key)
    print("Key generated and saved in \"secret.key\" file .Keep it safe!")










#--------------------------------------------------------

def encrypt_file(input_file, output_file):
    """Function to encrypt a file using the secret key."""

def decrypt_file(input_file, output_file):
    """Function to decrypt a file using the secret key."""


if __name__ == "__main__":
    print("Welcome to the File Encryption Tool!")

    while True:
        print("\nChoose one operation:")
        print("1. Generate Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        value = userChoice(choice)
        if value == "Exiting application... Goodbye!":
            print(value)
            break
