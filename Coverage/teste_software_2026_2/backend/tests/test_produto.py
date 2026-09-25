from backend.entity.produto import Produto
import pytest
from backend.exceptions.excecoes import (
    NomeInvalidoError,
    PrecoError,
    QntEstoqueError,
    PesoError,
    ValidadeError,
    CategoriaError,
    CodigoDeBarrasError,
)

def test_criar_produto_com_sucesso():
    cafe = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert cafe.nome == "cafe"
    assert cafe.preco == 18
    assert cafe.quant_estoque == 50
    assert cafe.validade == 3
    assert cafe.codigo_barras == 1234567890
    assert cafe.categoria == "alimenticio"
    assert cafe.peso == 250

def test_criar_produto_sem_nome():
    with pytest.raises(NomeInvalidoError) as exc_info:
        Produto("", 18, 50, 3, 1234567890, "alimentos", 250)
    assert str(exc_info.value) != ""

def test_validar_preco():
    with pytest.raises(PrecoError) as exc_info:
        Produto('nome', None, 2, 4, 1234567890, 'Alimentos', 230)
    assert str(exc_info.value) != ""

def test_qtd_de_estoque():
    with pytest.raises(QntEstoqueError) as exc_info:
        Produto('nome', 22, None, 22, 1234567890, 'Alimentos', 22)
    assert str(exc_info.value) != ""

def test_validar_validade():
    with pytest.raises(ValidadeError) as exc_info:
        Produto('nome', 12, 23, None, 1234567890, 'Alimentos', 22)
    assert str(exc_info.value) != ""

def test_codigo_de_barras():
    with pytest.raises(CodigoDeBarrasError) as exc_info:
        Produto('nome', 12, 23, 333, None, 'Alimentos', 22)
    assert str(exc_info.value) != ""

def test_categoria():
    with pytest.raises(CategoriaError) as exc_info:
        Produto('nome', 12, 23, 333, 1234567890, None, 22)
    assert str(exc_info.value) != ""

def test_peso():
    with pytest.raises(PesoError) as exc_info:
        Produto('nome', 12, 23, 333, 1234567890, 'Alimentos', None)
    assert str(exc_info.value) != ""

def test_getter_produto_nome():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    assert p.nome == 'Biscoito'

def test_setter_produto_nome():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    p.nome = 'Chocolate'
    assert p.nome == 'Chocolate'

def test_getter_produto_preco():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    assert p.preco == 22

def test_setter_produto_preco():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    p.preco = 30
    assert p.preco == 30

def test_getter_produto_qtd_estoque():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    assert p.quant_estoque == 23

def test_setter_produto_qtd_estoque():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    p.quant_estoque = 100
    assert p.quant_estoque == 100

def test_getter_produto_validade():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    assert p.validade == 11

def test_setter_produto_validade():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    p.validade = 30
    assert p.validade == 30

def test_getter_produto_codigo():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    assert p.codigo_barras == 1234567890

def test_setter_produto_codigo():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    p.codigo_barras = 9876543210
    assert p.codigo_barras == 9876543210

def test_getter_produto_categoria():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    assert p.categoria == 'Alimentos'

def test_setter_produto_categoria():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    p.categoria = 'Doces'
    assert p.categoria == 'Doces'

def test_getter_produto_peso():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    assert p.peso == 11

def test_setter_produto_peso():
    p = Produto('Biscoito', 22, 23, 11, 1234567890, 'Alimentos', 11)
    p.peso = 500
    assert p.peso == 500