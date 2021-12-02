VICTIM_IP = ""  # 10.0.0.5
VICTIM_NETWORK = ""  # 10.0.0.0/24
START_LINK = f"http://{VICTIM_IP}"
LOGIN_LINK = f"{START_LINK}/login.php"
LINK_AFTER_LOGIN = f"http://{VICTIM_IP}/index.php"
PASSWORDS_FILE = "short.txt"
USERS_FILE = "users.txt"

POSSIBLE_LINKS = [f"{START_LINK}/vulnerabilities/javascript/", f"{START_LINK}/about.php", f"{START_LINK}/phpinfo.php",
                  f"{START_LINK}/security.php", f"{START_LINK}/vulnerabilities/csp/",
                  f"{START_LINK}/vulnerabilities/xss_s/", f"{START_LINK}", f"{START_LINK}/vulnerabilities/xss_r/",
                  f"{START_LINK}/vulnerabilities/xss_d/", f"{START_LINK}/vulnerabilities/weak_id/",
                  f"{START_LINK}/vulnerabilities/sqli_blind/", f"{START_LINK}/vulnerabilities/sqli/",
                  f"{START_LINK}/vulnerabilities/captcha/", f"{START_LINK}/vulnerabilities/upload/",
                  f"{START_LINK}/vulnerabilities/fi/?page=include.php", f"{START_LINK}/vulnerabilities/csrf/",
                  f"{START_LINK}/vulnerabilities/exec/", f"{START_LINK}/vulnerabilities/brute/"]

LOGOUT_LINK = f"{START_LINK}/logout.php"
