Feature: Login Features

  Background:
    Given I launched the website
    When I click "loginbutton" button
    Then User should be redirected to "loginpage" page

  Scenario: Positive Scenario: UI element checks
    Then I checked that element "permission_logo" is displayed
    And I checked that element "center_image" is displayed
    And I checked that text "header_text" is displayed as "Log in to your account"
    And I checked that text "subtitle_text" is displayed as "Welcome back! Please enter your details."
    And I checked that element "email_textbox" is displayed
    And I checked that element "password_textbox" is displayed
    And I checked that element "recaptcha" is displayed
    And I checked that element "user_login_button" is displayed

  Scenario Outline: Positive Scenario: Successfull login
  #Prerequisite user is already created
    When I entered "<valid_email>" in the "email_textbox" textbox field
    And I entered "<valid_password>" in the "password_textbox" textbox field
    And I attempt to click "recaptcha"
    #automated I'm not a robot check but need manual intervention for image captcha
    And I click "user_login_button" button
    Then User should be redirected to "earnpage" page

  Examples:
    | valid_email             | valid_password |
    | onehazeltest@gmail.com  | QApassword1!   |

  Scenario Outline: Negative Scenario: Un-successfull login with error message
    When I entered "<invalid_email>" in the "email_textbox" textbox field
    And I entered "<invalid_password>" in the "password_textbox" textbox field
    And I attempt to click "recaptcha"
    #automated I'm not a robot check but need manual intervention for image captcha
    And I click "user_login_button" button
    Then verify "error" is displayed as "<error_message>"

  Examples:
    | invalid_email          | invalid_password | error_message |
    | invalid@gmail.com      | invalid          | Email or Password is incorrect. |
    | onehazeltest@gmail.com | invalid          | Email or Password is incorrect. |
   
  Scenario Outline: Negative Scenario: Un-successfull login recaptcha error
    When I entered "<invalid_email>" in the "email_textbox" textbox field
    And I entered "<invalid_password>" in the "password_textbox" textbox field
    And I click "user_login_button" button
    Then verify "recaptcha_error" is displayed as "<error_message>"

  Examples:
    | invalid_email          | invalid_password | error_message     |
    | onehazeltest@gmail.com | QApassword1!     | Invalid Recaptcha |
    | invalid@gmail.com      | invalid          | Invalid Recaptcha |
