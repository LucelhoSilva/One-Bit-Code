def count_upper_lower(letter):
    upper = 0
    lower = 0
    for i in letter:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower

print(count_upper_lower('A melhor forma de prever o futuro é Criá-Lo'))