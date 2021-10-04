from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = str(input('Digite a pesquisa: '))

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com/')

campo = driver.find_element_by_xpath('//input[@aria-label="Pesquisar"]')
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element_by_id('result-stats').text
print(resultados)
numeroResultados = int(resultados.split('Aproximadamente')[1].split('resultados')[0].replace('.', ''))
maxPags = numeroResultados / 10
paginaAlvo = input(f'{maxPags} Páginas encontradas, até qual quer ir? ')

urlPag = driver.find_element_by_xpath('//a[@aria-label="Page 2"]').get_attribute('href')

pagAtual = 0
start = 10
listaResultados = []

while pagAtual <= int(paginaAlvo) - 1:
    if pagAtual > 1:
        urlPag = urlPag.replace("start=%s" % start, "start=%s" % (start+10))
        start += 10
        driver.get(urlPag)
    elif pagAtual == 1:
        driver.get(urlPag)
    pagAtual += 1

    divs = driver.find_elements_by_xpath('//div[@class="g"]')
    for div in divs:
        nome = div.find_element_by_tag_name('span')
        link = div.find_element_by_tag_name('a')
        resultado = f'{nome.text, link.get_attribute("href")}'
        print(resultado)
        listaResultados.append(resultado)

with open('resultados.txt', 'w') as arquivo:
    for resultado in listaResultados:
        arquivo.write(f'\n {resultado}')
    arquivo.close()
print(f'Resultados encontrados do google e salvos no arquivo resultados.text', len(listaResultados))



