lista = ["rossi", "leo pereira", "fabricio bruno", "varela", "vina", "pulgar", "de la cruz", "arrascaeta", "cebolinha", "gabigol", "pedro"]
letra = input("Digite uma letra para filtrar as palavras: ").lower()

filtradas = [palavra for palavra in lista if palavra.startswith(letra)]

if filtradas:
    print(f"Palavras que começam com {letra}:")
    for palavra in filtradas:
        print(palavra)
else:
    print(f"Nenhuma palavra encontrada que comece com '{letra}'.")