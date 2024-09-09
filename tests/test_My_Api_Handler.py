from classes.My_Api_Handler import My_Api_Handler

my_api = My_Api_Handler()

def test_cat_fact():
    cat_fact = my_api.get_cat_fact()
    assert cat_fact != ""

def test_get_user():
    user = my_api.get_user()
    assert user.get('gender') is not None

def test_yes_no():
    answers = [
        'yes',
        'no'
    ]
    answer = my_api.yes_no()
    assert answer in answers 