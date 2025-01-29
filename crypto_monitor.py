import requests
import pandas as pd
from datetime import datetime

class CryptoMonitor:
    def __init__(self, config_path):
        self.config_path = config_path
        self.assets = self.load_assets()

    def load_assets(self):
        with open(self.config_path, 'r') as f:
            assets = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return assets

    def fetch_prices(self):
        prices = {}
        for asset in self.assets:
            response = requests.get(f'https://api.coinbase.com/v2/prices/{asset}/spot')
            data = response.json()
            prices[asset] = float(data['data']['amount'])
        return prices

    def check_market(self):
        prices = self.fetch_prices()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for asset, price in prices.items():
            print(f"[{now}] {asset}: ${price:.2f}")

        # Aqui você pode adicionar lógica para detectar oportunidades de compra e venda
        # e, se necessário, executar ordens.

