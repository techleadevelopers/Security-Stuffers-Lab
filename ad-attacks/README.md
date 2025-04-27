🛡️ AD-Attacks Framework — Security Stuffers Lab
📜 Visão Geral
O módulo ad-attacks/ do Security Stuffers Lab é focado em simular ataques reais contra Active Directory (AD) — incluindo:

Reconhecimento furtivo

Captura de credenciais

Movimentação lateral

Persistência em ambiente corporativo

Exfiltração furtiva de dados

Aqui você terá as mesmas fases de ataques APTs e Red Teams avançados, com técnicas modernas baseadas no MITRE ATT&CK.

🎯 Objetivo do Módulo
Simular a cadeia completa de comprometimento em Active Directory, desde enumeração inicial até domínio completo (Dominance), com foco real em:

Obtenção de credenciais

Abuso de serviços do Windows

Escalada de privilégios (Domain Admin)

Exfiltração segura de dados críticos

🛠️ Estrutura do Módulo (Organizada por Etapas Reais de Ataque)
bash
Copiar
Editar
ad-attacks/
├── discovery/                 # Fase 1: Reconhecimento inicial furtivo
│   ├── ad-enumeration-tools/
│   │   ├── BloodHound-importer.py
│   │   ├── ldap-enumeration.py
│   │   └── README.md
│   └── README.md

├── credential-access/         # Fase 2: Acesso e roubo de credenciais
│   ├── deathstar/
│   ├── mimikatz-mini-modules/
│   │   ├── lsass-dumper.py
│   │   ├── ticket-dumper.py
│   │   └── README.md
│   └── README.md

├── lateral-movement/          # Fase 3: Movimentação lateral stealth
│   ├── wmiexec-modules/
│   ├── remote-service-abuse/
│   └── README.md

├── persistence/               # Fase 4: Persistência longa no domínio
│   ├── golden-ticket-generator.py
│   ├── asrep-roasting-exploit.py
│   ├── admin-sdholder-backdoor.py
│   └── README.md

├── exfiltration/              # Fase 5: Exfiltração furtiva de dados
│   ├── pyexfil/
│   ├── dns-exfil-ad.py
│   └── README.md

└── README.md                 # Documentação principal do módulo
🔥 Fase 1 — Discovery (Enumeração e Mapeamento)
📂 ad-attacks/discovery/


Técnica	Descrição	Exemplos
Enumeração LDAP	Extrair usuários, grupos, máquinas via LDAP	ldap-enumeration.py
BloodHound Coleta	Dump de objetos de AD para análise gráfica	BloodHound-importer.py
🎯 Foco: Coleta de informações crítica sem levantar alertas.

⚔️ Fase 2 — Credential Access (Dump de Credenciais)
📂 ad-attacks/credential-access/


Técnica	Descrição	Exemplos
Dump de LSASS	Captura de senhas/hashes da memória	lsass-dumper.py
Dump de Tickets	Captura de TGTs e TGSs em memória	ticket-dumper.py
Automatização Total	DeathStar: Automação de movement + cred capture	deathstar/
🎯 Foco: Capturar credenciais para escalar privilégios.

🚀 Fase 3 — Lateral Movement (Movimentação Lateral)
📂 ad-attacks/lateral-movement/


Técnica	Descrição	Exemplos
Execução Remota via WMI	Comando remoto stealth	wmiexec-modules/
Abuse de Serviços	Uso de RPC, RDP, SMB para movimentação	remote-service-abuse/
🎯 Foco: Espalhar-se para outras máquinas sem ser detectado.

🛡️ Fase 4 — Persistence (Persistência)
📂 ad-attacks/persistence/


Técnica	Descrição	Exemplos
Golden Ticket Attack	Criação de tickets de autenticação falsos eternos	golden-ticket-generator.py
AS-REP Roasting	Exploração de contas sem preauth Kerberos	asrep-roasting-exploit.py
AdminSDHolder Backdoor	Persistência por herança de permissões	admin-sdholder-backdoor.py
🎯 Foco: Permanecer invisível dentro do domínio.

📡 Fase 5 — Exfiltration (Roubo de Dados)
📂 ad-attacks/exfiltration/


Técnica	Descrição	Exemplos
Exfiltração HTTP Stealth	Upload furtivo de dados capturados	pyexfil/
Exfiltração DNS Tunneling	Abuso de DNS para extrair dados	dns-exfil-ad.py
🎯 Foco: Enviar dados roubados para servidor C2 sem levantar alerta.

📚 Técnicas Representadas — MITRE ATT&CK Mapping

Tática	Técnica	Código
Discovery	LDAP Enumeration (T1018)	ldap-enumeration.py
Credential Access	LSASS Dumping (T1003.001)	lsass-dumper.py
Credential Access	Kerberos Ticket Extraction (T1558.003)	ticket-dumper.py
Lateral Movement	Remote Services Abuse (T1021)	wmiexec-modules/
Persistence	Golden Ticket (T1558.001)	golden-ticket-generator.py
Exfiltration	Exfiltration over Alternative Protocol (T1048.003)	dns-exfil-ad.py
📈 Pipeline Real de Uso
bash
Copiar
Editar
python ldap-enumeration.py     # Enumeração inicial
python lsass-dumper.py         # Roubo de credenciais da memória
python wmiexec-spray.py        # Movimento lateral para outras máquinas
python golden-ticket-generator.py # Persistência no AD
python dns-exfil-ad.py         # Exfiltração stealth de dados sensíveis
⚡ Futuras Melhorias Planejadas

Melhorias	Prioridade
Integração de Kerberoasting completo	🔥
Script de Exploração de ACLs de objetos AD	⚡
Integração de ZeroLogon exploit (para ambientes de lab)	🔥
DNS stealth + HTTP fallback exfiltration	⚡
📢 Aviso Legal
Este módulo é estritamente educacional e deve ser utilizado apenas:

Em ambientes controlados

Com autorização explícita

Para aprendizado de segurança ofensiva e Red Teaming

⚠️ O uso indevido em redes sem permissão pode ser crime.

🚀 Status Atual
📌 Módulo ad-attacks/ está em desenvolvimento avançado.
📚 Aceitamos Pull Requests de novas técnicas e ferramentas stealth!

🔥 Let's Dominate Active Directory.