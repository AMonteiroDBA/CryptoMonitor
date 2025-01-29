# CryptoMonitor

CryptoMonitor é um projeto Python para monitorar o mercado de criptomoedas em busca de oportunidades de compra ou venda. O projeto utiliza um arquivo de configuração (`config.conf`) para especificar os ativos a serem monitorados e verifica o mercado a cada 60 segundos.

## Estrutura do Projeto

1. **Diretórios e Arquivos:**

   - `CryptoMonitor/`
     - `main.py`
     - `config.conf`
     - `requirements.txt`
     - `crypto_monitor.py`
     - `README.md`

2. **Bibliotecas necessárias:**
   - `requests`
   - `pandas`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/AMonteiroDBA/CryptoMonitor.git
   cd CryptoMonitor
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Atualize o arquivo `config.conf` com os ativos que deseja monitorar.
2. Execute o script principal:
   ```bash
   python main.py
   ```

O monitoramento será realizado a cada 60 segundos, exibindo os preços atuais dos ativos especificados no arquivo de configuração.

## Melhorias Possíveis

1. **Alertas de Preço:** Adicionar lógica para enviar notificações (por e-mail, SMS, etc.) quando um ativo atingir um determinado preço.
2. **Histórico de Preços:** Salvar os preços em um banco de dados ou arquivo para análise posterior.
3. **Análise Técnica:** Implementar indicadores técnicos para identificar oportunidades de compra e venda com maior precisão.
4. **Interface Gráfica:** Criar uma interface gráfica para visualizar os dados em tempo real.
