def get_city():
    city=input("enter a city: ")
    return city.strip()
def check_city(city):
    return city != ""
def raise_city_error():
    raise ValueError("the input must not be empty")
def raise_code_error():
    raise ValueError("code must contains exactly two letters")
def get_country_code():
    country_code=input("enter country code: ")
    return country_code.upper().strip()
def check_cod(country_code):
    return len(country_code) == 2
def check_us(country_code):
    return country_code == "US"
def get_state_code():
    state_code=input("enter state code: ")
    return state_code.upper().strip()
