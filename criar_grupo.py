pontuacao = [9,17,12,10,2,7,2,11,20,8,3,4]
tamanho_do_time = 3
k = 4    

def CriarTime(pontucao, tamanho_do_time, k):
    pessoas_selecionadas = []
    for i in range(tamanho_do_time): 
        
        if len(pontuacao) <= k:
            pessoas_selecionadas.append(max(pontuacao))
            pontuacao.remove(max(pontuacao))
            
        else:
            s1 = pontuacao[0:k-1] 
            s1.sort()
            x = s1[-1]

            s2 = pontuacao[len(pontuacao)-4:len(pontuacao)]
            s2.sort()
            y = s2[-1]
                  
            if x == y:
                x = s1[0]
                y = s2[0]
                menor = min(x,y) 
                menor_index = pontuacao.index(min(pontuacao[len(pontuacao)-4:len(pontuacao)]))
                pessoas_selecionadas.append(menor)
                if menor == x:
                    pontuacao.remove(menor)
                else:
                    pontuacao.remove(pontuacao[menor_index])
            
            else:
                maior = max(x,y)
                maior_index = pontuacao.index(max(pontuacao[len(pontuacao)-4:len(pontuacao)]))
                pessoas_selecionadas.append(maior)
                if maior == x:
                    pontuacao.remove(maior)
                else:
                    pontuacao.remove(pontuacao[maior_index])

    soma = 0   
    z = 0           
    for z in pessoas_selecionadas:
        soma += z  

    return soma      