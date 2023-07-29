from processamentos import get_similares,get_recomendacoes,calcula_items_similares
from avaliacoes import avaliacoes_filmes,avaliacoes_usuario, carregar_movie_lens

base = carregar_movie_lens()
print(get_similares(base,'1'))

#usuarios similares
#print(get_similares(avaliacoes_usuario,'Ana'))

#possivel recomendacao para filme não visto
print(get_recomendacoes(base,'212'))

itens_similares = calcula_items_similares(avaliacoes_filmes)
print(itens_similares)