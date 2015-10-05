from behave import *

@when('we input a valid and registered email')
def step_impl(context):
	inputEmail = context.browser.find_element_by_id("id_usuario")
	inputEmail.send_keys('angelo_ribeiro@me.com')

@when('we input a valid and not registered email')
def step_impl(context):
	inputEmail = context.browser.find_element_by_id("id_usuario")
	inputEmail.send_keys('abcdloren@me.com')

@when('we input an invalid email')
def step_impl(context):
	inputEmail = context.browser.find_element_by_id("id_usuario")
	inputEmail.send_keys('abcd@terra')

@when('we input a valid and registered password')
def step_impl(context):
	inputPassword = context.browser.find_element_by_id("id_senha")
	inputPassword.send_keys('1610')

@when('we input a valid and not registered password')
def step_impl(context):
	inputPassword = context.browser.find_element_by_id("id_senha")
	inputPassword.send_keys('abc123')	

@when('we click entrar')
def step_impl(context):
	buttonEntrar = context.browser.find_element_by_xpath("//form[@class='form-login']/button[@type='submit']")
	buttonEntrar.click()