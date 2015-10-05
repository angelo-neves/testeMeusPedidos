Feature: Login

    Scenario: Valid and registered email and password
        Given we are at the login page
        When we input a valid and registered email
        And we input a valid and registered password
        And we click entrar
        Then the system logs in

    Scenario: Valid and not registered email and password
    	Given we are at the login page
    	When we input a valid and not registered email
    	And we input a valid and not registered password
    	And we click entrar
    	Then the system shows a not registered error

	Scenario: Invalid email and valid password
		Given we are at the login page
		When we input an invalid email
        And we input a valid and registered password
        And we click entrar
        Then the browser or the system shows an invalid email error

    Scenario: Blank email and password
    	Given we are at the login page
        When we click entrar
        Then the system shows a blank email error
        And the system shows a blank password error