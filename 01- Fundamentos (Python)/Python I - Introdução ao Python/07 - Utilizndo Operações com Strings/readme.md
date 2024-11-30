# 📚 Aula 7: Utilizando Operações com Strings

### Objetivos de Aprendizagem:

- Entender as operações básicas com strings em Python
- Aprender a concatenar strings de diferentes formas
- Compreender a multiplicação de strings
- Explorar a verificação de substrings usando o operador 'in'

### Código da Aula:

```python
# Criando uma string multilinha com a descrição do jogo
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar
localmente ou online.
                '''

# Definindo caractere para criar linha decorativa
line = '='

# Criando strings separadas para nome e versão do jogo
gameName = 'Fifa'
gameVersion = '24'

# Concatenando strings para criar o nome completo do jogo
gameFullName = gameName + gameVersion  # Concatenação simples unindo duas strings

# Criando uma apresentação formatada
print(line * 30)  # Multiplica o caractere '=' por 30 para criar uma linha decorativa
print(gameFullName)  # Exibe o nome completo do jogo
print(gameDescription)  # Exibe a descrição completa

# Verificando se determinadas palavras existem na descrição
print("Fifa" in gameDescription)    # Verifica se "Fifa" está presente na descrição
print("futebol" in gameDescription) # Verifica se "futebol" está presente na descrição
print(line * 30)  # Cria outra linha decorativa para finalizar
```

### Exemplo de Saída:

```
==============================
Fifa24

Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar
localmente ou online.

True
True
==============================
```

### Conceitos Importantes:

1. Concatenação de Strings:

   - Usando o operador '+' para juntar strings
   - Uma forma simples de combinar textos
   - Exemplo: 'Fifa' + '24' resulta em 'Fifa24'

2. Multiplicação de Strings:

   - Usando o operador '\*' com um número
   - Repete a string o número especificado de vezes
   - Útil para criar elementos decorativos ou padrões
   - Exemplo: '=' \* 30 cria uma linha com 30 sinais de igual

3. Operador 'in':
   - Verifica se uma string está contida em outra
   - Retorna True se encontrar, False se não encontrar
   - Diferencia maiúsculas de minúsculas
   - Útil para buscar palavras em textos longos
