from db_manager import add_password, get_passwords, delete_password
from encryption import encrypt_password, decrypt_password

def menu():
    while True:
        print("\nPassword Manager")
        print("1. Add a password")
        print("2. View saved passwords")
        print("3. Delete a password")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            encrypted_password = encrypt_password(password)
            add_password(website, username, encrypted_password)
            print("Password saved successfully!")

        elif choice == "2":
            passwords = get_passwords()
            if passwords:
                print("\nSaved Passwords:")
                for row in passwords:
                    decrypted_password = decrypt_password(row[3])
                    print(f"ID: {row[0]}, Website: {row[1]}, Username: {row[2]}, Password: {decrypted_password}")
            else:
                print("No passwords saved.")

        elif choice == "3":
            password_id = input("Enter password ID to delete: ")
            delete_password(password_id)
            print("Password deleted successfully!")

        elif choice == "4":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
