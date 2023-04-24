from django.test import TestCase
from myapp.models import Produto

class ProdutoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(nome="Produto 1", preco=10, descricao="Descrição do produto 1.")
        Produto.objects.create(nome="Produto 2", preco=20, descricao="Descrição do produto 2.")

    def test_produtos_criados_corretamente(self):
        produto_1 = Produto.objects.get(nome="Produto 1")
        produto_2 = Produto.objects.get(nome="Produto 2")
        self.assertEqual(produto_1.nome, "Produto 1")
        self.assertEqual(produto_1.descricao, "Descrição do produto 1.")
        self.assertEqual(produto_2.nome, "Produto 2")
        self.assertEqual(produto_2.descricao, "Descrição do produto 2.")
        self.assertEqual(produto_1.preco, 10)
        self.assertEqual(produto_2.preco, 20)

    def test_atualizacao_preco(self):
        produto_2_atualizado = Produto.objects.get(nome="Produto 2")
        produto_2_atualizado.preco = 60
        produto_2_atualizado.save()
        produto_2_atualizado = Produto.objects.get(nome="Produto 2")
        self.assertEqual(produto_2_atualizado.preco, 60)
