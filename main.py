tabela = [[5,8,2,6,9,1,4,7,3],
		  [1,3,7,0,0,8,5,9,6],
		  [6,4,9,3,5,7,8,2,1],
		  [8,9,0,7,6,5,3,0,2],
		  [7,5,3,0,0,0,6,8,9],
		  [2,6,0,8,3,9,0,0,0],
		  [4,7,0,0,8,0,0,3,0],
		  [3,1,0,0,0,0,0,0,0],
		  [9,2,0,5,0,3,0,0,0]
]

def range_1a9():
	lista = []
	for i in range(1,10):
		lista.append(i)
	return lista

def range_0a8():
	lista = []
	for i in range(0,9):
		lista.append(i)
	return lista

def range_0a2():
	lista = []
	for i in range(0,3):
		lista.append(i)
	return lista

def get_linha(l_index,tabela):
	colunas = range_0a8()
	linha = []
	for i in colunas:		
		linha.append(tabela[l_index][i])
	return linha

def get_coluna(c_index,tabela):
	colunas = range_0a8()
	linha = []
	for i in colunas:		
		linha.append(tabela[i][c_index])
	return linha

def get_quadrante(x_index,y_index,tabela):
	x_index = x_index * 3
	y_index = y_index * 3
	quadrante = [] 
	for x_linha in range_0a2():
		for y_linha in range_0a2():
			quadrante.append(tabela[x_linha + x_index][y_linha + y_index])
	return quadrante

def possibilidade_linha(l_index,tabela):
	lista_linha = get_linha(l_index,tabela)
	lista_possibilidade = range_1a9()
	colunas = range_0a8()
	linha_possibilidade = []
	for i in colunas:
		if lista_linha[i] != 0:
			lista_possibilidade.remove(lista_linha[i])
	for i in colunas:
		if lista_linha[i] == 0:
			linha_possibilidade.append(lista_possibilidade)
		else: 
			linha_possibilidade.append(lista_linha[i])
	return linha_possibilidade

def possibilidade_coluna(c_index,tabela):
	lista_coluna = get_coluna(c_index,tabela)
	lista_possibilidade = range_1a9()
	colunas = range_0a8()
	coluna_possibilidade = []
	for i in colunas:
		if lista_coluna[i] != 0:
			lista_possibilidade.remove(lista_coluna[i])
	for i in colunas:
		if lista_coluna[i] == 0:
			coluna_possibilidade.append(lista_possibilidade)
		else: 
			coluna_possibilidade.append(lista_coluna[i])
	return coluna_possibilidade

def possibilidade_quadrante(x_index,y_index,tabela):
	lista_quadrante = get_quadrante(x_index,y_index,tabela)
	lista_possibilidade = range_1a9()
	colunas = range_0a8()
	linha_possibilidade = []
	for i in colunas:
			if lista_quadrante[i] != 0:
				lista_possibilidade.remove(lista_quadrante[i])
	for i in colunas:
		if lista_quadrante[i] == 0:
			linha_possibilidade.append(lista_possibilidade)
		else: 
			linha_possibilidade.append(lista_quadrante[i])
	return linha_possibilidade

def get_possibilidade(y_index,x_index,tabela):
	lista_possibilidade = range_1a9()
	coluna = possibilidade_linha(y_index,tabela)
	linha  = possibilidade_coluna(x_index,tabela)
	num_achados = []
	for c in coluna:
		if isinstance(c, int):
			num_achados.append(c)
	for l in linha:
		if isinstance(l, int):
			num_achados.append(l)
	num_achados = list(dict.fromkeys(num_achados))
	num_achados.sort()
	for numero in num_achados:
		lista_possibilidade.remove(numero)
	return lista_possibilidade

def resposta_destaque(lista):
    if len(lista) == 1:
            return "*"+str(lista)+"*"
    return str(lista)

sudoku = []
for y in range_0a8():
	linha_sudoku = possibilidade_linha(y,tabela)
	novo_sudoku = []
	x = 0
	for lin in linha_sudoku:
		if isinstance(lin,int):
			novo_sudoku.append(lin)
		else:
			novo_sudoku.append(resposta_destaque(get_possibilidade(y,x,tabela)))
		x += 1
	novo_sudoku
