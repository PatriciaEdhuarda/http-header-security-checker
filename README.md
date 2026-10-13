# HTTP Header Security Checker

Um script simples desenvolvido em Python para análise rápida de cabeçalhos HTTP de segurança em aplicações web. O objetivo desta ferramenta é verificar se os principais cabeçalhos defensivos estão ativos ou ausentes em um determinado site.

## Funcionalidades:
- Verifica a presença de cabeçalhos críticos de segurança:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
- Interface interativa via terminal com opção de repetição contínua e encerramento limpo (`sair`).
- Tratamento de exceções para conexões inválidas ou inalcançáveis.

## Pré-requisitos:
Certifique-se de que tenha o Python instalado e a biblioteca necessária:
```bash
pip install requests
