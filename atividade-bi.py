nome_completo = input("Digite seu nome completo: ")

nomes = nome_completo.split()

for pos, nome in enumerate(nomes, 1):
    print(f"Nome {pos}: {nome}")
    print(f"- Número de caracteres: {len(nome)}")
    print(f"- Posição: {pos}")
    print(f"- Invertido: {nome[::-1]}")
    print()
