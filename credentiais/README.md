🔒 Credential Attack Framework — Security Stuffers Lab
📜 Visão Geral
Este módulo do Security Stuffers Lab é focado em operações de roubo, exfiltração e abuso de credenciais no contexto de simulações de APTs, Red Team Operations e ciberataques avançados.

As técnicas aqui cobrem todo o ciclo de ataque:

Captura furtiva (Dumps de navegadores, memória RAM, arquivos locais).

Ataques de login (Credential stuffing, password spraying, brute-force).

Parsing e validação (Organização e filtragem de grandes dumps).

Exfiltração stealth (Envio oculto para C2s ou servidores de coleta).

Pós-exploração (Uso das credenciais para movimentação lateral e persistência).

🎯 Objetivo do Módulo
Simular de forma prática e brutal as fases de Credential Access e Credential Abuse da matriz MITRE ATT&CK (T1078, T1003, T1110).

Permitir que operadores ofensivos ou pesquisadores:

Aprendam técnicas modernas de extração de credenciais.

Automatizem ataques de credenciais em pipelines reais.

Construam simulações de intrusão completas, em laboratório ou em ambientes controlados.

🛠️ Estrutura do Módulo (Organizada por Etapas de Ataque)
bash
Copiar
Editar
credentials/
├── dumpers/          # Fase 1: Captura furtiva de credenciais
├── stuffers/         # Fase 2: Credential Stuffing / Spraying
├── parsers/          # Fase 3: Parsing e validação dos dados coletados
├── exfiltration/     # Fase 4: Exfiltração stealth
├── postexploitation/ # Fase 5: Abuso pós-comprometimento
└── README.md         # Documentação completa
🔥 Fase 1 — Dumpers (Captura de Credenciais)
📂 credentials/dumpers/

Módulos que realizam coleta inicial de credenciais:


Técnica	Descrição	Exemplos de Ferramentas
Browser Dumpers	Extração de senhas salvas em Chrome, Edge, Brave, Firefox.	browser-dumper.py, chromepass-dumper.py
Memory Dumpers	Dump de processos (LSASS, RAM) para capturar senhas e tokens.	Pymem, LaZagne, Mimikatz
File Dumpers	Coleta de arquivos sensíveis: wallet.dat, .kdbx, .json com secrets.	wallet-dumper.py, keyfile-scraper.py
Vault Extractors	Extração de senhas do Windows Credential Manager.	LaZagne-modules/
🎯 Foco: Captura passiva e stealth, sem levantar alarmes.

⚔️ Fase 2 — Stuffers (Credential Stuffing e Password Spraying)
📂 credentials/stuffers/

Módulos para ataques ativos usando dumps de credenciais:


Técnica	Descrição	Exemplos de Ferramentas
Credential Stuffing	Tentativa automática de logins com leaks/dumps.	credential_stuffer/, chromedriver-credential-stuffing/
Password Spraying	Teste de senhas comuns em massa, minimizando bloqueios.	SprayingToolkit/, password-sprayer.py
Bruteforce Modules	Pequenos bruteforcers de APIs, SSH, RDP, SMB, FTP.	brute-modules/
🎯 Foco: Automatizar takeover de contas com credenciais capturadas.

🛡️ Fase 3 — Parsers (Validação e Organização)
📂 credentials/parsers/

Módulos para organizar e validar as credenciais capturadas:


Técnica	Descrição	Exemplos de Scripts
Parsing de Dumps	Separação de combos válidos/inválidos.	parse-valids.py, combo-cleaner.py
Splitting	Divisão de grandes dumps em pequenos batches para ataque.	combo-splitter.py
🎯 Foco: Preparar os dados para otimizar os ataques de brute-force.

🚀 Fase 4 — Exfiltration (Roubo e Exfiltração Stealth)
📂 credentials/exfiltration/

Módulos para enviar as credenciais capturadas para servidores controlados:


Técnica	Descrição	Exemplos de Scripts
POST Stealth Upload	Envio HTTP stealth para C2.	stealth-uploader.py
DNS Tunneling Exfil	Exfiltração via requests DNS.	dns-exfiltrator.py
C2 Client	Comunicação com backend controlado.	c2-exfil-client.py
🎯 Foco: Evitar detecção durante a movimentação de dados roubados.

⚡ Fase 5 — Post-Exploitation (Abuso de Credenciais)
📂 credentials/postexploitation/

Módulos para usar credenciais capturadas para avançar dentro da rede:


Técnica	Descrição	Exemplos de Scripts
RDP Auto Login	Logins automáticos com senhas roubadas.	rdp-autologin.py
SMB Lateral Movement	Uso de senhas para pivô lateral via SMB.	smb-login-sprayer.py
VPN/Proxy Access	Configurações para acesso persistente via VPN ou proxy reverso.	vpn-hijacker.py
🎯 Foco: Persistência e escalada de privilégios usando credenciais capturadas.

🧠 Técnicas Reais Representadas
Credential Access (T1078)

Valid Accounts (T1078.004)

Unsecured Credentials (T1552)

Password Spraying (T1110.003)

Brute Force (T1110)

Exfiltration Over Alternative Protocol (T1048.003)

Remote Services Abuse (T1021)

📋 Como Usar na Prática
Executar dumpers para coletar credenciais.

Usar stuffers para fazer login com as credenciais roubadas.

Rodar parsers para filtrar as credenciais válidas.

Exfiltrar stealth para servidor seguro.

Usar postexploitation para movimentação lateral ou persistência.

🔥 Exemplo de Pipeline Real:
bash
Copiar
Editar
python browser-dumper.py       # Dump de senhas do navegador
python parse-valids.py         # Filtrar credenciais úteis
python credential_stuffer.py   # Ataque stuffing em portal alvo
python stealth-uploader.py     # Enviar credenciais roubadas para C2
python rdp-autologin.py        # Entrar em máquinas internas
🛠️ Requisitos Básicos
Python 3.9+

Pipenv ou venv para ambientes isolados.

Acesso de operador com privilégios para dumpers avançados (opcional).

📚 Fontes e Referências Técnicas
MITRE ATT&CK Framework

Black Hat & DEFCON talks (Credential Theft & Exfiltration)

Adversary Emulation Plans (APT29, APT41 credential campaigns)

Research papers: "Password Spraying at Scale", "Post-Exploitation Movement".

🚀 Status: Ativamente em expansão!
Novos módulos planejados:

Kerberoasting attack scripts.

Office 365 credential stuffing.

OAUTH Token replay attacks.

📢 Este módulo é apenas para fins educacionais e simulação controlada!
Nunca use em ambientes sem autorização explícita.