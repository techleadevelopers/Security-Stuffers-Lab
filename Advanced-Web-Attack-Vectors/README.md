🧠 Advanced Web Attack Vectors — Security Stuffers Lab


📜 Visão Geral

Este módulo do Security Stuffers Lab é dedicado exclusivamente ao estudo, prática e simulação de vetores de ataque avançados em ambientes Web.

O objetivo é cobrir de forma prática e realista:
Manipulação avançada de protocolos HTTP.
Abuso de autenticação JWT.
Quebra de lógica de aplicação.
Hijacking de sessões via WebSocket e OAuth.
Exfiltração furtiva de dados.
Subversão de sistemas de cache.

🎯 Meta final: construir um pipeline real de Initial Access ➔ Privilege Escalation ➔ Persistence focado em vulnerabilidades Web modernas.

🛠️ Estrutura do Módulo (Organizada por Vetores de Ataque)

advanced-web-attack-vectors/
├── jwt-attacks/
├── http-request-smuggling/
├── business-logic-flaws/
├── broken-object-authorization/
├── advanced-sqli-oob/
├── cache-deception/
├── websocket-attacks/
├── clickjacking-frame-injection/
└── README.md


🔥 Descrição Detalhada de Cada Pasta (com cenários reais)

1. 📜 jwt-attacks/

Fase: Autenticação/Token Abuse
Manipulação de JWTs mal configurados.
Exploração de falha no algoritmo (alg: "none").
Ataques de confusão de chaves públicas x privadas (Key Confusion).

📂 Inclui:

jwt_tool/ → Ferramenta de manipulação de tokens.
jwt_none_algo_bypass.py → Criação de JWTs inválidos sem assinatura.
jwt_key_confusion_exploit.py → Bypass usando confusão de chaves.

🧠 Impacto real: Escalada de privilégio, acesso de admin, bypass total de autenticação.

2. 📜 http-request-smuggling/
Fase: Exploração de Backend / Caching
Exploração de inconsistências entre proxy (frontend) e servidor de aplicação (backend).
Injeção de requisições secundárias invisíveis.

📂 Inclui:

http-request-smuggler/ → Ferramenta Burp para ataques CL.TE / TE.CL.
smuggler/ → Exploitadores puros de HTTP Smuggling.
turbo-intruder-scripts/ → Scripts para fuzzing massivo.
smuggling-payloads.txt → Payloads prontos e testados.

🧠 Impacto real: Session hijack, bypass de login, cache poisoning.

3. 📜 business-logic-flaws/
Fase: Manipulação de Fluxo de Aplicação
Manipular lógica de preços, descontos, steps de checkout.
Atacar pontos críticos do fluxo de negócios.

📂 Inclui:

price-tampering-checkout.py → Alteração furtiva de preços.
order-manipulation-poison.py → Corrupção de ordens/pedidos.

🧠 Impacto real: Compra de produtos a preço irrisório, abuso de fluxos de pagamento.

4. 📜 broken-object-authorization/
Fase: Escalada Horizontal
Exploração de falhas de autorização (IDOR, BOLA).
Acesso não autorizado a recursos de outros usuários.

📂 Inclui:

bola_fuzzer.py → Fuzzer automático de endpoints.
idor-automation.py → Scripts para varrer APIs públicas.

🧠 Impacto real: Roubo de informações privadas (wallets, pedidos, contas).

5. 📜 advanced-sqli-oob/

Fase: Exfiltração Avançada
Realizar SQL Injection cega (Blind SQLi) usando exfiltração fora de banda (DNS, HTTP).

📂 Inclui:

sqli-dns-exfiltrator.py → Extração de dados via requisições DNS.
blind-sqli-oob-examples.txt → Payloads prontos.

🧠 Impacto real: Vazamento de bancos de dados inteiros mesmo sem erro HTTP.

6. 📜 cache-deception/

Fase: Exploração de Sistemas de Cache
Induzir servidores a armazenar páginas sensíveis e entregar a qualquer visitante.

📂 Inclui:

cache-deception-payloads.txt → Estratégias e URLs manipuladas.
cache-poisoning-example.md → Documentação tática.

🧠 Impacto real: Roubo de sessões de login, exfiltração de dados confidenciais via cache.

7. 📜 websocket-attacks/

Fase: Session Hijacking via WebSocket
Ataques Cross-Site WebSocket Hijacking (CSWSH).

📂 Inclui:

websocket-hijack-exploit.js → Sequestro de sessões WebSocket.
ws-cookie-stealer.js → Roubo furtivo de cookies/sessões.

🧠 Impacto real: Espionagem em chats, sequestro de tokens em tempo real.

8. 📜 clickjacking-frame-injection/

Fase: Engenharia Social via Clickjacking
Enganar o usuário para clicar em áreas invisíveis de outros sites.

📂 Inclui:

clickjacking-template.html → Template stealth.
iframe-poisoner.html → Versão agressiva para automação.

🧠 Impacto real: Transações financeiras falsas, execução remota de ações críticas.

🚀 Pipeline de Ataque Sugerido

Fluxo real de uma operação usando este módulo:

1. jwt_none_algo_bypass.py  --> Bypass de login em painel Web3
2. http-request-smuggler/   --> Hijack de sessão admin
3. bola_fuzzer.py           --> Roubo de carteiras conectadas
4. sqli-dns-exfiltrator.py  --> Exfiltração de senhas e API keys
5. websocket-hijack-exploit.js --> Captura de mensagens em tempo real
6. cache-poisoning-example.md --> Persistência de acesso via cache CDN
7. clickjacking-template.html --> Induzir vítimas a autorizar ações críticas

📚 Fontes e Técnicas Baseadas em:

OWASP Top 10 (A01, A05, A07)
MITRE ATT&CK: T1078, T1110, T1190, T1557
Black Hat USA/DEFCON Advanced Web Hacking tracks
PortSwigger Research Blog
HackTricks methodology (HTTP Smuggling, WebSocket Attacks)

📢 Aviso Legal
Este material foi desenvolvido exclusivamente para fins educacionais e simulações controladas. NUNCA use essas técnicas em sistemas sem autorização explícita. O uso indevido é crime previsto na legislação de segurança cibernética.

🎯 Status do Módulo: EM EXPANSÃO

Próximos passos planejados:

 Automatizar ataques com chain scripts.
 Integrar exploits de SSRF avançado.
 Incluir bypasses de Web Application Firewalls (WAFs).

🧠 Domine ataques Web modernos, domine o campo real.


🛡️ Attack like a researcher. Defend like a hacker.

