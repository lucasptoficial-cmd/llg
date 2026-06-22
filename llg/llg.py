import sys
import time

def interpretar(nome_ficheiro):
    variaveis = {}

    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            continue

        if linha == "exit":
            break

        if linha.startswith("say "):
            texto = linha[4:].strip()

            if texto.startswith('"') and texto.endswith('"'):
                texto = texto[1:-1]

            for nome, valor in variaveis.items():
                texto = texto.replace(f"({nome})", str(valor))

            if texto in variaveis:
                texto = str(variaveis[texto])

            print(texto)

        elif linha.startswith("let "):
            resto = linha[4:]

            if "=" in resto:
                nome, valor = resto.split("=", 1)

                nome = nome.strip()
                valor = valor.strip()

                if valor.startswith('"') and valor.endswith('"'):
                    variaveis[nome] = valor[1:-1]
                else:
                    try:
                        variaveis[nome] = int(valor)
                    except:
                        variaveis[nome] = valor

        elif linha.startswith("rcb "):
            nome = linha[4:].strip()
            variaveis[nome] = input("> ")

        elif linha.startswith("wait "):
            try:
                time.sleep(float(linha[5:]))
            except:
                pass


def mostrar_regras():
    print("Uso: python llg.py play ficheiro.llg")
    print("Uso: python llg.py regras")
    print("Comandos LLG:")
    print("  say <texto>           - exibe texto, usando (nome) para variáveis")
    print("  let <nome>=<valor>    - define variável")
    print("  rcb <nome>            - lê entrada do usuário e grava em variável")
    print("  wait <segundos>       - pausa por um tempo")
    print("  exit                  - encerra o programa")
    print("Exemplo de uso:")
    print("  say \"Olá (nome)\"")
    print("  rcb nome")


def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("regras", "help"):
        mostrar_regras()
        return

    if len(sys.argv) != 3:
        print("Uso: python llg.py play ficheiro.llg")
        print("Para ver as regras: python llg.py regras")
        return

    if sys.argv[1] != "play":
        print("Comando desconhecido")
        return

    interpretar(sys.argv[2])


if __name__ == "__main__":
    main()