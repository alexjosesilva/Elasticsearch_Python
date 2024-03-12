import unittest
from adicionar import clean_text

class TestCleanText(unittest.TestCase):

    def test_clean_text(self):
        # Texto com quebras de linha e espaços extras
        text_with_extra_spaces = "Capitalismo:\nBenefícios\ne\nLimitações"

        # Texto esperado após a limpeza
        expected_cleaned_text = "Capitalismo: Benefícios e Limitações"

        # Chama a função clean_text para limpar o texto
        cleaned_text = clean_text(text_with_extra_spaces)

        # Verifica se o texto limpo é igual ao texto esperado
        self.assertEqual(cleaned_text, expected_cleaned_text)

if __name__ == '__main__':
    unittest.main()
