# 📚 Aula 4: Aprenda a Concatenar Valores

### Objetivos de Aprendizagem:

- Entender diferentes formas de concatenar strings e valores em Python
- Aprender a usar f-strings para formatação moderna de strings
- Compreender como organizar a saída de dados de forma legível
- Explorar diferentes técnicas de formatação de texto

### Código da Aula:

```python
# Recebendo dados do usuário
name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrice = float(input("Digite o preço do jogo\n"))
planIncluded = input("Está incluso no serviço mensal?\n")

# Criando um cabeçalho para os dados
print("###Dados do Jogo####")
print("====================")

# Alternativa 1: Concatenação usando vírgula
# print("Nome do Jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrice)
# print("Está incluído no plano?", planIncluded)

# Alternativa 2: Concatenação em linha única com \n
# print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
#       "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)

# Alternativa 3: Usando f-string (forma mais moderna e recomendada)
print(f"Nome do Jogo: {name} \nAno Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluso no serviço? {planIncluded}")
```

### Conceitos Importantes

- F-strings (formatação de strings):

  - Introduzidas no Python 3.6+
  - Permitem inserir variáveis diretamente na string usando {variavel}
  - Mais legível e manutenível que outras formas de concatenação

- Diferentes métodos de concatenação:

  1. Usando vírgula: print("texto", variavel)
  2. Concatenação em linha única com \n para quebras de linha
  3. F-strings: print(f"texto {variavel}")

- Caracteres especiais:
  - \n: Quebra de linha
  - ###: Usado para criar destaque visual
  - =: Usado para criar linhas decorativas

### Exemplo de Saída:

```
Digite o nome do jogo
God of War Ragnarök
Digite o ano de lançamento do jogo
2022
Digite o preço do jogo
349.90
Está incluso no serviço mensal?
Sim

###Dados do Jogo####
====================
Nome do Jogo: God of War Ragnarök
Ano Lançamento: 2022
Preço do Jogo: 349.9
Está incluso no serviço? Sim
```

### Observações Importantes:

1. F-strings (Alternativa 3) são consideradas a forma mais moderna e recomendada de formatação em Python
2. A escolha do método de concatenação pode afetar a legibilidade do código
3. É importante manter a consistência no estilo de formatação em todo o projeto
4. A organização visual dos dados (cabeçalho, separadores) ajuda na legibilidade da saída
