from Crypto.Cipher import AES

from encryption_key import encryption_key
from login_data import login_data

if __name__ == "__main__":
    decrypted_login_data = []

    for login in login_data:
        initialisation_vector = login["ciphertext"][3:15]
        encrypted_password = login["ciphertext"][15:-16]
        
        cipher = AES.new(encryption_key, AES.MODE_GCM, initialisation_vector)
        decrypted_password = cipher.decrypt(encrypted_password)
        decrypted_password = decrypted_password.decode()

        decrypted_login_data.append({
            "url": login["url"],
            "username": login["username"],
            "password": decrypted_password
        })

    print("Decrypted Google Chrome saved passwords:\n")

    for i, login in enumerate(decrypted_login_data):
        print(f"Login ID {i}")
        print("URL:         " + login["url"])
        print("Username:    " + login["username"])
        print("Password:    " + login["password"])
        print("")