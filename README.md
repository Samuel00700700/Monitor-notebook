# 🔔 Monitor de Preço - Notebook Asus

> Script Python que monitora o preço de um produto no Mercado Livre e alerta via notificação no Android quando o preço cai abaixo de um valor base.

---

## 📱 Sobre o projeto

O projeto roda no **Termux** (emulador de terminal para Android) e é executado automaticamente a cada **1 hora**, alertando o usuário com uma **notificação push** e um **som de alarme** sempre que o preço do produto monitorado cair.

## ⚙️ O que ele faz

- 🌐 Realiza uma requisição HTTP na página do produto no Mercado Livre
- 🔍 Extrai o preço atual via **web scraping** com BeautifulSoup
- 📊 Compara com um preço base definido no script
- 🔔 Caso o preço seja menor, dispara uma **notificação** e toca um **alarme**
- ❌ Em caso de falha na requisição ou mudança no HTML do site, envia uma notificação de erro

## 🛠️ Tecnologias utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3 | Linguagem principal |
| Requests | Requisições HTTP |
| BeautifulSoup4 | Web scraping |
| Termux:API | Notificações e media player no Android |
| Cron (Termux) | Agendamento automático de execução |

## 🔧 Configuração

As principais variáveis do script para personalizar o monitoramento:

| Variável | Descrição |
|---|---|
| `url` | Link do produto no Mercado Livre |
| `preco_normal` | Preço base para comparação (em R$) |

## ⚠️ Observações

- O script depende da estrutura HTML atual do Mercado Livre. Caso o site seja atualizado, pode ser necessário ajustar o seletor CSS usado no scraping.
- O arquivo de áudio do alarme deve estar em `/storage/emulated/0/Notifications/alarm.mp3`.
