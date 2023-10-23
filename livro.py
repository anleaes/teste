class Livro:

    def __init__(self, titulo, snopse, pagina, autor):
        self._titulo = titulo 
        self._snopse = snopse
        self._pagina = pagina 
        self._autor = autor

    def imprime_dados(self):
        print('%s %s %s %s' % (self._titulo, self._snopse, self._pagina, self._autor)) 
        

    