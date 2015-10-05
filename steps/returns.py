# -*- coding: utf-8 -*-

from behave import *

@then('the system logs in')
def step_impl(context):
	assert "Empresa de" in context.browser.title

@then('the system shows a not registered error')
def step_impl(context):
	errorList = context.browser.find_element_by_xpath('//div[@class="form-group"][1]/ul[@class="errorlist"]')
	assert 'não possui cadastro' in errorList.get_attribute('innerHTML').encode('utf8')

# Some HTML5 capable browsers will block incomplete email addresses, when testing for those cases you should expect an error from the browser, not the system.

@then('the browser or the system shows an invalid email error')
def step_impl(context):
	try:
		invalidInput = context.browser.find_element_by_css_selector('input:invalid')
	except:
		errorList = context.browser.find_element_by_xpath('//div[@class="form-group"][1]/ul[@class="errorlist"]')
		assert 'Informe um endereço de email válido' in errorList.get_attribute('innerHTML').encode('utf8')
	else:
		assert 'id_usuario' == invalidInput.get_attribute('id')

@then('the system shows a blank password error')
def step_impl(context):
	errorList = context.browser.find_element_by_xpath('//div[@class="form-group"][2]/ul[@class="errorlist"]')
	assert 'Informe sua senha' in errorList.get_attribute('innerHTML').encode('utf8')

@then('the system shows a blank email error')
def step_impl(context):
	errorList = context.browser.find_element_by_xpath('//div[@class="form-group"][1]/ul[@class="errorlist"]')
	assert 'Informe seu e-mail' in errorList.get_attribute('innerHTML').encode('utf8')