import time
from crypto_monitor import CryptoMonitor

def main():
    monitor = CryptoMonitor('config.conf')
    while True:
        monitor.check_market()
        time.sleep(60)  # Checa o mercado a cada 60 segundos

if __name__ == "__main__":
    main()
