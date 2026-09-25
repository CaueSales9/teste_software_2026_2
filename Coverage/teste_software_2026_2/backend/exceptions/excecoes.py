class NomeInvalidoError(Exception):
    """Lançada quando o nome do produto está vazio ou inválido."""

    def __init__(self,msg):
        """Armazena a mensagem de erro."""
        self.msg = msg

    def __str__(self):
        """Retorna a mensagem de erro como texto."""
        return self.msg

class PrecoError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
class QntEstoqueError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
class ValidadeError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
class CodigoDeBarrasError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
class CategoriaError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class PesoError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
