## 🎯 Desafio 1: Substituindo caractere repetido

#### Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere.

**Solução fornecida pela OBC:**

```python
name = 'Fifa 23'

character = name[0].lower()
new = name.replace(character, '#')
new = character +  new[1:]
print(new)
```

## 🎯 Desafio 2: Substituindo caractere repetido

#### Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

**Solução fornecida pela OBC:**

```python
st1 = 'abc'
st2 = 'xyz'

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")
```
