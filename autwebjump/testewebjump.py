# - Configura
# - linguagem Python 3...
# - PyCharm 2021.3.3
# - Pytest para teste em Python
# - Seleniumwebdriver como ferramenta/motor da automatizacao
# _ webdrivermanager gerenciador do broswer/navegadores que deseja automatizar
# - Usei pip como gerenciador dos pacotes, no promp/terminal do Pycham
# - chromedriver no caso de usar o chrome

# - Biblioteca / Imports
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testes:
    # -  Inicío
     def setup_method(self):
    # - Instancia do driver com o chrome, (Neste caso aqui esta no venv/scripts)
    # - webdrivermanager versao/chromedriver
       self.driver = webdriver.Chrome('C:\\Users\\ademarfr\\PycharmProjects\\WebJump'
                                      '\\venv\\Scripts\\chromedriver.exe'
                                      )

    # - Fim quando o teste acabar
     def teardown_method(self):

    # - Destruir o objeto da biblioteca utilizado (fechar navegador)
        self.driver.quit()

     def teste_automacao_webjump(self):

    # Rota da pagina/ que vai ser aberta pelo Google
        self.driver.get("https://wj-qa-automation-test.github.io/qa-test/")
        self.driver.maximize_window()  # maximizando a a tela
        
        self.driver.find_element(By.ID, "btn_one").click()
        self.driver.find_element(By.ID, "btn_two").click()
        self.driver.find_element(By.ID, "btn_link").click()

    # verificando se esse elemento está ou não na pagina.
        elements = self.driver.find_elements(By.ID, "btn_one")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "btn_two")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "btn_link")
        assert len(elements) > 0

        self.driver.switch_to.frame(0)

        self.driver.find_element(By.ID, "btn_one").click()
        self.driver.find_element(By.ID, "btn_two").click()
        self.driver.find_element(By.ID, "btn_link").click()
    # Valindando que o elemento não esta na pagina.
        assert self.driver.find_element(By.ID, "btn_one").is_enabled() is True
        assert self.driver.find_element(By.ID, "btn_two").is_enabled() is True
        assert self.driver.find_element(By.ID, "btn_link").is_enabled() is True
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "first_name").click()
        self.driver.find_element(By.ID, "first_name").send_keys("Ademar")
        self.driver.find_element(By.CSS_SELECTOR, "input#mid_name").send_keys("Ferreira")
        self.driver.find_element(By.CSS_SELECTOR, "input#last_name").send_keys("Rodrigues")
        self.driver.find_element(By.ID, "age").send_keys("24/01/1977")
        self.driver.find_element(By.ID, "email").send_keys("admademar@yahoo.com.br")
        self.driver.find_element(By.CSS_SELECTOR, "input#job").send_keys("Analista de Testes/QA")
        self.driver.find_element(By.ID, "gender").send_keys("Masculino")
        self.driver.find_element(By.ID, "reset_buttons").click()
        self.driver.find_element(By.ID, "btn_one").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#opt_three").click()
        self.driver.find_element(By.CSS_SELECTOR, "#select_box > option:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".img-responsive-center-block:nth-child(4)").is_displayed()






