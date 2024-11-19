from behave import given, when, then
from features.locators.environment_locators import urlLocators
from features.locators.loginpage_locators import loginpageLocators
from features.utils.locator_helper import get_locator

#------------------Define Locator Modules -----------------------#
locator_modules = [
    loginpageLocators,
    urlLocators
   ]

#--------------------- For Preconditions -------------------------#
@given('I launched the website')
def launch_website(context):
    context.page.goto(urlLocators.homepage)


#------------------- basic command steps ------------------------#
@when('I click "{button_name}" button')
def click_button(context, button_name):
    locator = get_locator(context, button_name, locator_modules)
    button =  context.page.locator(locator)
    button.wait_for(state="visible", timeout=5000)
    button.click()

@when('I entered "{text_value}" in the "{text_field}" textbox field')
def user_input_value(context, text_value, text_field):
    locator =  get_locator(context, text_field, locator_modules)
    text_box = context.page.locator(locator)
    text_box.click()
    if text_value == "":
        text_box.fill("")
    else:
        text_box.fill(text_value)

@then('I checked that element "{image_name}" is displayed')
def verify_element_is_displayed(context, image_name):
    locator = get_locator(context, image_name, locator_modules)
    image = context.page.locator(locator)
    assert image.is_visible(), \
        f"The image '{image_name}' is not displayed"

@then('I checked that text "{text_message}" is displayed as "{expected_text}"')
def verify_element_is_displayed(context, text_message,expected_text):
    locator = get_locator(context, text_message, locator_modules)
    text = context.page.locator(locator)
    assert text.is_visible(), f"The text '{text_message}' is not displayed"
    actual_text = text.inner_text().strip()
    expected_text = expected_text.strip()
    assert actual_text == expected_text, \
        f"the '{actual_text}' is not equals to '{expected_text}'"

@then('verify "{error}" is displayed as "{error_message}"')
def verify_error_message_displayed(context, error, error_message):
    locator = get_locator(context, error, locator_modules)
    error_locator = context.page.locator(locator)
    assert error_locator.is_visible(), f"The error '{error}' is not displayed"
    actual_error= error_locator.inner_text().strip()
    error_message = error_message.strip()
    assert actual_error == error_message, \
        f"the '{actual_error}' is not equals to '{error_message}'"

#@then('User should be redirected to Login to your account page')
#def redirected_to_login_page(context):
#    expected_url = urlLocators.loginpage
    #context.page.wait_for_url(expected_url,timeout=10000)
#    current_url = context.page.url
#    assert current_url.startswith(expected_url), \
#        f"Expected URL to start with {expected_url}, but got {current_url}"

@then('User should be redirected to "{page_name}" page')
def redirected_to_login_page(context, page_name):
    expected_url = get_locator(context, page_name, locator_modules)
    current_url = context.page.url
    assert current_url.startswith(expected_url), \
        f"Expected URL to start with {expected_url}, but got {current_url}"

#------------- Recaptcha ----------------------------------------#
@when('I attempt to click "{recaptcha}"')
def solve_recaptcha(context, recaptcha):
    locator = getattr(loginpageLocators, recaptcha)
    context.page.wait_for_selector(locator)

    captcha_iframe = context.page.locator(locator)

    # Switch to the CAPTCHA iframe
    iframe_element = captcha_iframe.element_handle()
    captcha_frame = iframe_element.content_frame()

    try:
        # Locate the reCAPTCHA checkbox
        captcha_checkbox = captcha_frame.locator('#recaptcha-anchor')

        # Check if the checkbox is visible and clickable
        if captcha_checkbox.is_visible():
            captcha_checkbox.click()

        else:
            # Wait for the user to manually solve the CAPTCHA
            context.page.wait_for_selector('#recaptcha-verify-button', state='visible')

    except Exception as e:
        print(f"Failed to interact with CAPTCHA: {str(e)}")
