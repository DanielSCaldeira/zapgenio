import subprocess
import shutil
import time
import threading

lt_port = "8000"
subdominio = "daniel-dsaddah827"

lt_path = shutil.which("lt")

def get_tunnel_password():
    try:
        result = subprocess.run(
            ["curl", "-s", "https://loca.lt/mytunnelpassword"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print("Erro ao obter a senha do túnel:", e)
        return None

if lt_path is None:
    print("LocalTunnel (lt) não encontrado no PATH. Verifique a instalação.")
else:
    print(f"Iniciando LocalTunnel com subdomínio: {subdominio}.loca.lt")

    # Rodar túnel em background
    proc = subprocess.Popen([lt_path, "--port", lt_port, "--subdomain", subdominio])

    # Espera alguns segundos para o túnel abrir e senha ficar disponível
    time.sleep(5)

    senha = get_tunnel_password()
    if senha:
        print(f"Senha para acesso: {senha}")
        print("Informe essa senha na página de aviso do LocalTunnel para acessar o link:")
        print(f"https://{subdominio}.loca.lt")
    else:
        print("Não foi possível obter a senha do túnel.")

    # Opcional: esperar o túnel encerrar (Ctrl+C)
    proc.wait()
