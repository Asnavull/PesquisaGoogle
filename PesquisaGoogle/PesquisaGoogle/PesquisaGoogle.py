import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()

with open("entrada.json", "r") as f:
	pesquisa = json.load(f)

respostas = []

for x in pesquisa["google-me"]:
	chrome.get("https://www.google.com.br")
	chrome.find_element_by_name("q").send_keys(x + Keys.ENTER)
	resultados = chrome.find_elements_by_class_name("g")[:3]
	resposta = []
	for y in resultados:
		r = y.find_elements_by_class_name("r")[0]
		resposta.append(r.find_element_by_tag_name("h3").text + "|" + r.find_element_by_tag_name("cite").text)
	respostas.append(resposta)

retorno = json.dumps(respostas, indent=4, sort_keys=True)

with open("output.json", "w") as f:
	f.write(retorno)

chrome.quit()