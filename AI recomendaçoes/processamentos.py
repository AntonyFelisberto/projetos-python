from math import sqrt

def euclidiana_calculo(base,dado_base_um,dado_base_dois):
    si = {}
    for item in base[dado_base_um]:
        if item in base[dado_base_dois]:  si[item]=1

    if len(si)==0: return 0

    soma = sum([pow(base[dado_base_um][item] - base[dado_base_dois][item],2) 
                for item in base[dado_base_um] if item in base[dado_base_dois]])
    
    return 1/(1 + sqrt(soma))

def get_similares(base,dado_base):
    similaridade = [(euclidiana_calculo(base,dado_base,outro),outro)
                    for outro in base if outro != dado_base]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]

def get_recomendacoes(base,dado_base):
    totais = {}
    soma_similaridades = {}
    for outros in base:
        if outros == dado_base: continue
        similaridade = euclidiana_calculo(base,dado_base,outros)

        if similaridade <= 0: continue
        for item in base[outros]:
            if item not in base[dado_base]:
                totais.setdefault(item,0)
                totais[item]+=base[outros][item]*similaridade
                soma_similaridades.setdefault(item,0)
                soma_similaridades[item]+=similaridade
    
    rankings=[(total / soma_similaridades[item],item) for item,total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]

def calcula_items_similares(base):
    result = {}
    for item in base:
        notas = get_similares(base,item)
        result[item] = notas
    return result