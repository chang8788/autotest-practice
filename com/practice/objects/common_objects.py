# -*- coding: utf-8 -*-

'''
Common page objects
'''
import os 

class Common(object):
    base_url = 'https://automationexercise.com/'
    login_url = base_url + 'login'
    signup_url = base_url + 'signup'
    
  


# class LoginPage(object):
#     username_input = '.login-page__username input'
#     password_input = '.login-page__password input'
#     login_btn = '.login-page__button-wrapper .btn--primary'

#     username_value = ''
#     password_value = ''
class LoginPage(object):
    email_input = '//input[@data-qa="login-email"]'
    password_input = '//input[@data-qa="login-password"]'
    login_btn = '//button[@data-qa="login-button"]'
    logout_btn = '//a[@href="/logout"]'
    email_value = '6969@yopmail.com'
    password_value = 'mm1111'

class HomePage2(object):
    contact_btn = '//a[@href="/contact_us"]'
    testcase_header_btn = '//header//a[@href="/test_cases"]'
    product_btn = '//a[@href="/products"]'
    subscription_input = '//input[@id="susbscribe_email"]'
    subsciption_btn = '//button[@id="subscribe"]'
    subscription_value = '6787@yopmail.com'
    cart_btn = '//a[@href="/view_cart"]'
    viewproduct_btn = '//a[@href="/product_details/1"]'
    signup_login_btn = '//a[@href="/login"]'
    recommended_items_div = '//div[@class="recommended_items"]'
    addcart_recomment_btn = '(//div[@class="recommended_items"]//div[@class="item active"]//a)[1]'
    scrollup_btn = '//a[@id="scrollUp"]'

class PopupTestPage(object):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    popup_base_url = 'file:///' + dir_path + '/../../../mock_pages/index.html'

    popup1_btn = '//button[contains(text(), "Popup 1")]'
    popup2_btn = '//button[contains(text(), "Popup 2")]'
    popup3_btn = '//button[contains(text(), "Popup 3")]'

    popup_title = '//h1[contains(text(), "Đây là cửa sổ popup")]'
    text_input = '#fname'

class RegisterTestPage(object):
    login_btn = '//a[contains(@href, "/login")]'
    name_input = '//input[contains(@name, "name")]'
    email_input = '//input[contains(@name, "email") and contains(@data-qa, "signup-email")]'
    submit_btn = '//*[@id="form"]/div/div/div[3]/div/form/button'
    name_value = 'channg8788'
    email_value = '696990@yopmail.com'

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

class AccountCreatedPage(object):
    continue_btn = '//*[@id="form"]/div/div/div/div/a'

class HomePage(object):
    delete_btn = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a'

class AccountDeletedPage(object):
    continue_btn = '//*[@id="form"]/div/div/div/div/a'

class ContactUsPage(object):
    name_input = '//input[@data-qa="name"]'
    email_input = '//input[@data-qa="email"]'
    subject_input = '//input[@data-qa="subject"]'
    message_input = '//textarea[@data-qa="message"]'
    upload_btn = '//input[@name="upload_file"]'
    name_value = '1000'
    email_value = '1000@yopmail.com'
    subject_value = '1000'
    message_value = '1000'
    submit_btn = '//input[@data-qa="submit-button"]'
    file_input = '//input[@name="upload_file"]'

class ProductsPage(object):
    search_input = '//input[@name="search"]'
    search_btn = '//button[@id="submit_search"]'
    search_value = 'winter'
    product1_hover = '(//div[@class="productinfo text-center"])[1]'
    addproduct1_hover_btn = '(//a[@class="btn btn-default add-to-cart"])[1]'
    product2_hover = '(//div[@class="productinfo text-center"])[2]'
    addproduct2_hover_btn = '(//a[@class="btn btn-default add-to-cart"])[3]'
    women_btn = '//a[@href="#Women"]'
    subwomen_top_btn = '//a[@href="/category_products/2"]'
    men_btn = '//a[@href="#Men"]'
    submen_btn = '//a[@href="/category_products/3"]'
    itembrand1_btn = '//a[@href="/brand_products/Polo"]'
    itembrand2_btn = '//a[@href="/brand_products/H&M"]'
    addproduct3_hover_btn = '//a[@data-product-id="30"]'
   
class CartPage(object):
    subscription_input = '//input[@id="susbscribe_email"]'
    subsciption_btn = '//button[@id="subscribe"]'
    subscription_value = '6787@yopmail.com'
    proceed_btn = '//a[@class="btn btn-default check_out"]'
    delete_btn = '//a[@class="cart_quantity_delete"]'

class PopupAdded(object):
    countinue_btn = '//button[@class="btn btn-success close-modal btn-block"]'
    viewcart_btn = '//u'

class PopupCheckout(object):
    register_textlink = '//u'
class DetailPage(object):
    quantity_input = '//input[@name="quantity"]'
    add_btn = '//button[@class="btn btn-default cart"]'
    quantity_value = '4'
    name_input = '//input[@type="text"]'
    name_value = 'trang'
    email_input = '//input[@id="email"]'
    review_input = '//textarea[@name="review"]'
    submit_btn = '//button[@id="button-review"]'
    email_value = '6969@yopmail.com'
    review_value = 'mmm'


class AddressDetailsPage(object):
    comment_input = '//textarea'
    comment_value = 'jj'
    payment_btn = '//a[@href="/payment"]'

class PaymentPage(object):
    namecard_input = '//input[@name="name_on_card"]'
    numbercard_input = '//input[@name="card_number"]'
    cvc_input = '//input[@name="cvc"]'
    expirymonth_input = '//input[@name="expiry_month"]'
    expiryyear_input = '//input[@name="expiry_year"]'
    pay_btn = '//button[@type="submit"]'
    namecard_value = '0'
    numbercard_value = '0'
    cvc_value = '0'
    expirymonth_value = '0'
    expiryyear_value = '0'
    download_btn = '//a[@href="/download_invoice/1300"]'
    continue_btn = '//div[@class="pull-right"]/a'
    

    
    