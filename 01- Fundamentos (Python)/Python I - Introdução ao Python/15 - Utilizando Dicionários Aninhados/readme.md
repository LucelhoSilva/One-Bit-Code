# 📚 Aula 15: Utilizando Dicionários Aninhados

#### Um dicionário aninhado é um dicionário dentro de outro dicionário. Ele é extremamente útil para representar dados mais complexos e estruturados.

- Ideal para organizar informações hierárquicas.
- Permite acessar dados específicos de maneira direta.
- Suporta múltiplos níveis de aninhamento.
- Facilita a manipulação de dados relacionados.

#### Exemplo e Sintaxe

```python
import pprint

gamesDict = {
    "fifa 23": {
        "yearLaunch": 2022,
        "classification": 8.5,
        "genre": ["esporte", "família"]
    },
    "mario odyssey": {
        "yearLaunch": 2017,
        "classification": 10.0,
        "genre": ["aventura", "3d"]
    },
    "donkey kong country": {
        "yearLaunch": 1996,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscando informação dentro de um dicionário
print(gamesDict["mario odyssey"]["genre"])

# 2 - Adicionando novo item
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict['mario odyssey'])

# 3 - Excluindo um dicionário
del gamesDict["fifa 23"]
pp.pprint(gamesDict)
```

### Explicação Detalhada

#### 1 - **Buscando informação em dicionário aninhado**
Podemos acessar informações específicas navegando pelos níveis do dicionário.  
Exemplo:
```python
print(gamesDict["mario odyssey"]["genre"])
# Saída: ["aventura", "3d"]
```

#### 2 - **Adicionando itens em um dicionário aninhado**
Usamos as chaves do dicionário para identificar onde o novo dado será adicionado.  
Exemplo:
```python
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])
# Saída: {'yearLaunch': 2017, 'classification': 10.0, 'genre': ['aventura', '3d'], 'players': 1}
```

#### 3 - **Excluindo um dicionário inteiro**
Para remover uma entrada inteira, utilizamos a função `del`.  
Exemplo:
```python
del gamesDict["fifa 23"]
pp.pprint(gamesDict)
# Saída:
# {'donkey kong country': {'yearLaunch': 1996, 'classification': 9.5, 'genre': ['aventura', 'plataforma']},
#  'mario odyssey': {'yearLaunch': 2017, 'classification': 10.0, 'genre': ['aventura', '3d'], 'players': 1}}
```

#### **Aplicações**
- Representar jogos, categorias, e classificações.
- Modelar dados estruturados como arquivos JSON.
- Navegar e manipular informações hierárquicas.