# Resolução do desafio yes she code da nubank 2021

#Descrição do problema:
Uma função que recebe uma lista "pontucao" que contem a pontuação de algums usuarios. A partir dela tem que ser criado um time de tamanho contido na variavel "tamanho_do_time", e retornar a soma das pontuções do time.

Para isso, deve-se criar sub-listas do vetor de pontuação, onde cada sublista deve ter o tamanho "k" de posições sendo uma sublista retirada do inicio do vetor de pontuação e a segunda retirada do final do vetor.

Em cada sub-lista tem que retirar a maior pontuação, que se refere a pessoa que irá compor o time, caso o numero de maior pontuação de uma sub-lista esteja repetido, então será considerado o menor valor.

A cada pessoa selecionada, sua pontuação deve ser retirada do vetor.

Se o tamanho do vetor de pontuações for menor ou igual a "k", não é necessario criar as sub-listas.
