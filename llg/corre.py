# corre.py - Motor da linguagem LLG
import sys

def interpretar():
    # Tenta abrir o ficheiro que foi passado como argumento ou o padrão
    try:
        nome_ficheiro = sys.argv[1] if len(sys.argv) > 1 else "programa.llg"
        with open(nome_ficheiro, "r") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{nome_ficheiro}' não foi encontrado.")
        return

    for linha in linhas:
        linha = linha.strip()
        if not linha or linha.startswith("//"): continue # Ignora vazios e comentários

        # Divide o comando do conteúdo
        if " " in linha:
            partes = linha.split(" ", 1)
            comando = partes[0]
            conteudo = partes[1].replace('"', '')
        else:
            comando = linha
            conteudo = ""
        
        if comando == "say":
            if "=" in conteudo:
                # Divide no primeiro sinal de igual para separar texto da conta
                partes_conta = conteudo.split("=", 1)
                texto = partes_conta[0].strip()
                expressao = partes_conta[1].strip()
                try:
                    # Executa a operação matemática
                    resultado = eval(expressao)
                    print(f"{texto} {resultado}")
                except Exception as e:
                    print(f"{texto} Erro no cálculo: {e}")
            else:
                # Apenas exibe o texto
                print(conteudo)
                
        elif comando == "help":
            print("Comandos LLG: say [texto/conta], help")

if __name__ == "__main__":
    interpretar()