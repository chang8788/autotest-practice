# -*- coding: utf-8 -*-

'''
Common page objects
'''
import os 

class Common(object):
    base_url = 'https://automationexercise.com/'
    login_url = base_url + 'login'
    signup_url = base_url + 'signup'


class LoginPage(object):
    username_input = '.login-page__username input'
    password_input = '.login-page__password input'
    login_btn = '.login-page__button-wrapper .btn--primary'

    username_value = ''
    password_value = ''

class PopupTestPage(object):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    popup_base_url = 'file:///' + dir_path + '/../../../mock_pages/index.html'

    popup1_btn = '//button[contains(text(), "Popup 1")]'
    popup2_btn = '//button[contains(text(), "Popup 2")]'
    popup3_btn = '//button[contains(text(), "Popup 3")]'

    popup_title = '//h1[contains(text(), "Đây là cửa sổ popup")]'
    text_input = '#fname'

class RegisterTestPage(object):
    signup_btn = '//a[contains(@href, "/login")]'
    name_input = '//input[contains(@name, "name")]'
    email_input = '//input[contains(@name, "email") and contains(@data-qa, "signup-email")]'
    submit_btn = '//*[@id="form"]/div/div/div[3]/div/form/button'
    name_value = 'channg8788'
    email_value = 'Mm3878933@yopmail.com'

class EnterAccountInforPage(object):
    mrs_radio = '//*[@id="id_gender2"]' 
    name_input = '//*[@id="name"]'  
    email_input = '//*[@id="email"]'
    password_input = '//*[@id="password"]'
    day_select = '//*[@id="days"]'
    month_select = '//*[@id="months"]'
    year_select = '//*[@id="years"]'
    signup_checkbox = '//*[@id="newsletter"]'
    receive_checkbox = '//*[@id="optin"]'
    firstname_input = '//*[@id="first_name"]'
    lastname_input = '//*[@id="last_name"]'
    company_input = '//*[@id="company"]'
    address1_input = '//*[@id="address1"]'
    address2_input = '//*[@id="address2"]'
    country_select = '//*[@id="country"]'
    state_input = '//*[@id="state"]'
    city_input = '//*[@id="city"]'
    zipcode_input = '//*[@id="zipcode"]'
    mobile_input = '//*[@id="mobile_number"]'
    create_submit = '//*[@id="form"]/div/div/div/div[1]/form/button'
    day_value = '25'
    month_value = 'May'
    year_value = '1988'
    password_value = '2510Mtccx'
    firstname_value = 'Trang'
    lastname_value = 'Luong Thi Thu'
    company_value = 'ABC'
    address1_value = 'CDE'
    address2_value = 'DFJ'
    state_value = '10000'
    city_value = '10000'
    zipcode_value = '10000'
    mobile_value = '10000'
    country_value = 'Canada'


