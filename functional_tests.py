from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Ouvimos falar sobre uma aplicacao interessante para lista de tarefas e decidimos verificar
    self.browser.get('http://localhost:8000')

    # Percebemos logo de cara o titulo da pagina
    self.assertIn('TODO', self.browser.title)
    self.fail('Finish the test!')

    # Logo somos convidados a inserir um item na lista

    # Digitamos em uma caixa de texto -- Comprar pao

    # Em seguimos, ao enviar, conseguimos perceber o nosso item
    # "1. Comprar pao" em uma lista de tarefas

    # Ainda continua uma caixa de texto, nos convidando a adicionar outro item
    # Entao decidimos incrementar a nossa refeicao, compramdo presento

    # A pagina e atualizada novamente agora "2. Comprar presento" tambem e exibido na lista

    # Podemos notar ao fim que foi gerado uma URL unica, para salvar os item que adicionamos na nossa lista

    # Agora podemos sair

if __name__ == '__main__':
    unittest.main(warnings='ignore')
