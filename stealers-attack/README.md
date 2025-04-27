🛡️ Stealers Attack Framework — Security Stuffers Lab
📜 Visão Geral
O módulo Stealers Attack do Security Stuffers Lab é dedicado a explorar, testar e simular roubo furtivo de dados em ambientes Web, Mobile e APIs.

Aqui reunimos técnicas práticas que cobrem todo o fluxo de:

Skimming de dados confidenciais via Web (cartões de crédito, formulários sensíveis).

Request Smuggling para evasão e exfiltração furtiva.

Roubo de dados em dispositivos móveis (clipboard hijack, keylogging).

Fuzzing e exploração de vulnerabilidades para aumentar a superfície de ataque.

🎯 O objetivo é emular cenários realistas de Data Theft, Initial Access e Credential Access usados por grupos APTs e cibercriminosos avançados.

🎯 Objetivo do Módulo
Simular vetores modernos de roubo de informações baseados nos seguintes TTPs da matriz MITRE ATT&CK:

Input Capture (T1056)

Exfiltration Over Alternative Protocol (T1048)

Valid Accounts - Web Applications (T1078.004)

Resource Hijacking (T1496)

Application Layer Protocol: Web Protocols (T1071.001)

🛠️ Estrutura do Módulo (Organizada por Etapas Reais de Ataque)
bash
Copiar
Editar
stealers-attack/
├── web-skimmers/            # Fase 1: Roubo furtivo em aplicações web
│    ├── formjacker/
│    ├── magcartskimmerPOC/
│    ├── skcc_skimmer/
│    ├── skimmer_webapp/
│    ├── delivery-methods/       # Métodos para injetar os skimmers
│    ├── exfiltration/            # Scripts stealth para roubar dados
│    ├── obfuscators/             # Obfuscadores para payloads maliciosos
│    └── README.md
│
├── request-smuggling/       # Fase 2: Smuggling de requisições HTTP
│    ├── smuggler/
│    ├── advanced-payloads/
│    └── README.md
│
├── mobile-stealers/         # Fase 3: Ataques furtivos a dispositivos móveis
│    ├── Storm-Breaker/
│    ├── android-clipboard-monitor/
│    ├── keylogger-stealth-android/
│    └── README.md
│
├── fuzzers-exploiters/       # Fase 4: Ferramentas auxiliares de exploração
│    ├── XSStrike/
│    ├── dalfox/
│    ├── xsscrapy/
│    └── README.md
│
├── automation/              # Runner Scripts (Execução rápida de módulos)
│    ├── script_lab_runner.py
│    └── README.md
│
└── README.md                # Descrição geral do módulo
🔥 Fase 1 — Web Skimmers
📂 web-skimmers/

Missão:
Capturar furtivamente informações sensíveis (cartões de crédito, CPF, senhas, etc) em sites web através da injeção de scripts maliciosos.

Técnicas Abordadas:


Técnica	Descrição	Exemplos/Tools
Formjacking	Captura de dados de formulários HTML	formjacker/, skcc_skimmer/
Magecart-style attacks	Skimming avançado de ecommerce checkout	magcartskimmerPOC/
Dynamic Skimmer Injection	Injeção dinâmica de payloads stealth	delivery-methods/, dynamic-loader.js
Exfiltration Stealth	Envio oculto dos dados roubados	stealth-uploader.py, dns-exfiltrator.py
Obfuscation	Camuflagem de skimmers para AV/WAF evasion	payload-obfuscator.py
🎯 Foco: Roubos furtivos altamente eficazes com baixa detecção.

🔥 Fase 2 — Request Smuggling
📂 request-smuggling/

Missão:
Explorar inconsistências entre proxies e servidores para:

Desviar requisições.

Bypassar autenticação.

Roubar sessões.

Injetar skimmers furtivamente.

Técnicas Abordadas:


Técnica	Descrição	Exemplos/Tools
HTTP Smuggling (TE.CL, TE.TE)	Injetar requisições escondidas no pipeline HTTP	smuggler/, te-cl-smuggle.py
Cache Poisoning	Envenenar caches para propagar payloads	advanced-payloads/
Session Hijacking via Smuggling	Roubar sessão admin sem precisar credenciais	smuggler-examples/
🎯 Foco: Controle furtivo do tráfego HTTP de sites vulneráveis.

🔥 Fase 3 — Mobile Stealers
📂 mobile-stealers/

Missão:
Roubar informações sensíveis diretamente de dispositivos móveis.

Técnicas Abordadas:


Técnica	Descrição	Exemplos/Tools
RAT para Mobile	Controle remoto total de dispositivos	Storm-Breaker/
Clipboard Hijacking	Roubo de textos copiados (seeds, endereços, senhas)	android-clipboard-monitor/
Keylogger Stealth	Captura de teclas em background	keylogger-stealth-android/
🎯 Foco: Comprometer dispositivos móveis de forma invisível.

🔥 Fase 4 — Fuzzers e Explorers
📂 fuzzers-exploiters/

Missão:
Encontrar falhas (XSS, IDOR, smuggling vectors) para apoiar os ataques anteriores.

Técnicas Abordadas:


Técnica	Descrição	Exemplos/Tools
XSS Fuzzing (Reflection/Stored)	Identificar vulnerabilidades XSS	XSStrike/, dalfox/
Smuggling Payload Testing	Testar vulnerabilidades de backend	advanced-smuggler/
Reconnaissance Crawling	Mapear superfícies para futuros ataques	xsscrapy/
🎯 Foco: Expandir as superfícies de ataque web.

🚀 Automação — Runner Scripts
📂 automation/

Facilita a execução automática de vários módulos via:

bash
Copiar
Editar
python script_lab_runner.py --module web-skimmers
python script_lab_runner.py --module mobile-stealers
python script_lab_runner.py --module fuzzers-exploiters
🎯 Foco: Dinamizar a operação ofensiva em ambientes de laboratório.

🧠 Técnicas Reais Representadas
Credential Access (T1078)

Input Capture (T1056)

Exfiltration Over Alternative Protocol (T1048)

Valid Accounts — Web Apps (T1078.004)

Abuse of Web Services (T1102)

Application Layer Protocol: Web Protocols (T1071.001)

📋 Como Usar na Prática
Injetar skimmers stealth em sites/webapps.

Roubar dados sensíveis sem alertar antivírus ou WAF.

Exfiltrar furtivamente os dados para C2s controlados.

Explorar dispositivos mobile capturados.

Usar fuzzers para descobrir novas superfícies de ataque.

📚 Fontes e Referências Técnicas
MITRE ATT&CK Framework (Enterprise)

Magecart Campaign Analyses

OWASP Web Security Testing Guide

Research: "HTTP Request Smuggling in 2024+", "Magecart Evolution 2025"

DEFCON, Black Hat, Hack In The Box Papers

APT Case Studies (ex: APT41 Magecart variant, FIN7 skimming ops)

📢 Importante
Este material é exclusivamente educacional e para ambientes de laboratório controlados.

⚠️ Nunca execute qualquer técnica aqui descrita sem permissão explícita do alvo.

🚀 Status
✅ Módulo inicial completo.

🔜 Futuras expansões planejadas:

WebRTC leak exfiltration.

Browser extensions stealing (Brave, Chrome, Firefox).

In-browser memory scraping.