import requests


def verificar_cabecalhos(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    cabecalhos_seguranca = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    print(f"Analisando: {url}\n")

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        resposta = requests.get(url, headers=headers, timeout=10)

        cabecalhos_site = {k.lower(): v for k, v in resposta.headers.items()}

        for cabecalho in cabecalhos_seguranca:
            cabecalho_lower = cabecalho.lower()

            if cabecalho_lower in cabecalhos_site:
                print(f"✅ {cabecalho}: ATIVADO")
                print(f"   ↳ Valor: {cabecalhos_site[cabecalho_lower]}\n")
            else:
                print(f"❌ {cabecalho}: FALTANDO (Risco de Segurança)\n")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")


if __name__ == "__main__":
    while True:
        url_usuario = input("Digite a URL do site (ou 'sair' para encerrar): ").strip()

        if url_usuario.lower() in ['sair']:
            print("Encerrando o analisador. Até logo!")
            break

        elif url_usuario:
            verificar_cabecalhos(url_usuario)
            print("-" * 50)

        else:
            print("Nenhuma URL foi informada.\n")