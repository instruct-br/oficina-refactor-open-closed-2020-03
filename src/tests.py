import unittest

from main import main, VALIDATORS


class TestMain(unittest.TestCase):
    def test_sucess(self):
        """
        Testa a função main, ela recebe uma lista de e-mail,
        busca nos currículos telefone e a palavra chave python
        e retorna a lista de curriculos válidos
        """
        output = main(['ddignan1', 'ngillard3'], VALIDATORS['python'])
        self.assertIn('ddignan1', output)
        self.assertIn('ngillard3', output)

    def test_fail_phone(self):
        """
        Teste se a função main rejeita currículos sem telefone
        """
        output = main(['clilbourne0'], VALIDATORS['python'])
        self.assertNotIn('clilbourne0', output)

    def test_fail_python(self):
        """
        Teste se a função main rejeita currículos sem telefone
        """
        output = main(['ckneesha2', 'gsatterly4'], VALIDATORS['python'])
        self.assertNotIn('ckneesha2', output)
        self.assertNotIn('gsatterly4', output)


if __name__ == '__main__':
    unittest.main()
