from autor import Autor
from livro import Livro

def main():
    a1 = Autor('Antonio Leaes', 1982, 'a@a.com')
    a2 = Autor('Luiz Silva', 1990, 'l@l.com')
    l1 = Livro('Senhor dos Aneis', 'Aventura', 8000, a1)
    
if __name__ == "__name__":
    main