from behave import *

@given('we are at the login page')
def step_impl(context):
	context.browser.get("http://sandbox.meuspedidos.com.br:8080/login")