# Lucas Scommegna

# 1
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k
    
print(soma) #soma == 91

# 2

# A complexidade de tempo é de O(n), pois executará a operação de consulta em aproximadamente n vezes, sendo n o valor fornecido. Para otimização de tempo, caso seja passado outro valor
# o programa pode ser otimizado com o conceito de memoization de programação dinâmica, salvando os valores anteriores a uma outra lista, sendo feito recursivamente
def is_in_fib(n):
    fib_init = [0,1]
    index = 1
    
    if n == 0 or n == 1:
        return True
    else:
        while fib_init[index] <= n:
            next_value = fib_init[-1] + fib_init[-2]
            
            if next_value == n:
                return True
            
            index += 1
            
            fib_init.append(next_value)
            
    return False

"""
3:

a) 9

b) 128

c) 49

d) 100

e) 13

f) A sequencia foi composta pelos seguintes acrésimos a partir do primeiro valor: 8,2,4,1,1,1... logo não parece ter uma lógica definida para descobrir o próximo valor
"""

"""
4:

Passo a passo:
    Sala dos interruptores:
        Ligue o primeiro interruptor e aguarde alguns minutos antes de desligar ele.
        Ligue o segundo e vá até a sala das lâmpadas.
        
    Sala das lâmpadas:
        A lâmpada que estiver acesa é controlada pelo segundo interruptor.
        A lâmpada que estiver apagada, mas estiver quente é controlada pelo primeiro.
        A lâmpada que estiver apagada e fria ao toque é controlada pelo terceiro.
"""
        
        
# 5
# Esse algoritmo tem complexidade de tempo de O(n), pois percorre cada caractere da string word
def string_reverse(word):
    reversed_word = ""
    
    for i in range(-1, -len(word) - 1, -1):
        reversed_word += word[i]
        
    return reversed_word