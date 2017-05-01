from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sistema():
	driver.get("http://www.wordreference.com")
	search_box = driver.find_element_by_id("si")
	search_box.send_keys("sistema")
	language_list = driver.find_element_by_id("fSelect")
	language_list.click()
	language = driver.find_element_by_id("esen")
	language.click()
	search_box.send_keys(Keys.RETURN)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "esen:16905")))
	element = driver.find_element_by_css_selector("#esen\:16905 > td:nth-child(3)")
	inner_english_text = driver.execute_script("return arguments[0].innerText", element)
	clean_inner_english_text = inner_english_text[:-2]
	print str(clean_inner_english_text)

	print ("system" == clean_inner_english_text)

def test_diccionario():
	driver.get("http://www.wordreference.com")
	search_box = driver.find_element_by_id("si")
	search_box.send_keys("diccionario")
	language_list = driver.find_element_by_id("fSelect")
	language_list.click()
	language = driver.find_element_by_id("esen")
	language.click()
	search_box.send_keys(Keys.RETURN)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "esen:27977")))
	element = driver.find_element_by_css_selector("#esen\:27977 > td:nth-child(3)")
	inner_english_text = driver.execute_script("return arguments[0].innerText", element)
	clean_inner_english_text = inner_english_text[:-2]
	print str(clean_inner_english_text)

	print ("dictionary" == clean_inner_english_text)

def test_aplicacion():
	driver.get("http://www.wordreference.com")
	search_box = driver.find_element_by_id("si")
	search_box.send_keys("aplicacion")
	language_list = driver.find_element_by_id("fSelect")
	language_list.click()
	language = driver.find_element_by_id("esen")
	language.click()
	search_box.send_keys(Keys.RETURN)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "esen:21729")))
	element = driver.find_element_by_css_selector("#esen\:21729 > td:nth-child(3)")
	inner_english_text = driver.execute_script("return arguments[0].innerText", element)
	clean_inner_english_text = inner_english_text[:-2]
	print str(clean_inner_english_text)

	print ("application" == clean_inner_english_text)

def test_libreria():
	driver.get("http://www.wordreference.com")
	search_box = driver.find_element_by_id("si")
	search_box.send_keys("libreria")
	language_list = driver.find_element_by_id("fSelect")
	language_list.click()
	language = driver.find_element_by_id("esen")
	language.click()
	search_box.send_keys(Keys.RETURN)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "esen:10979")))
	element = driver.find_element_by_css_selector("#esen\:10979 > td:nth-child(3)")
	inner_english_text = driver.execute_script("return arguments[0].innerText", element)
	clean_inner_english_text = inner_english_text[:-2]
	print str(clean_inner_english_text)

	print ("library" == clean_inner_english_text)


if __name__ == "__main__":
	driver = webdriver.Firefox()
	test_sistema()
	test_diccionario()
	test_aplicacion()
	test_libreria()
	driver.close()

