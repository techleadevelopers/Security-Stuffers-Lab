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

## 📚 Como Contribuir

1. **Fork** o repositório
2. **Branch** com sua feature (`git checkout -b feature/x`)
3. **Commit** e **Push** (`git commit -m "feat: descrição" && git push origin feature/x`)
4. **Pull Request** detalhando mudanças

---

## 📜 Licença

MIT License

> **Disclaimer:** Ferramentas para uso em ambientes autorizados e fins educacionais. Seja responsável e ético.

