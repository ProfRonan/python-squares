"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="3")
    def test_squares_3(self, _mock_input):
        """Testa se o programa imprime 1 quando a entrada é 3"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("1", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="10")
    def test_squares_10(self, _mock_input):
        """Testa se o programa imprime 1, 4, 9 quando a entrada é 10"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("1\n4\n9", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="39")
    def test_squares_39(self, _mock_input):
        """Testa se o programa imprime 1, 4, 9, 16, 25, 36 quando a entrada é 39"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("1\n4\n9\n16\n25\n36", captured_output.getvalue().strip())
