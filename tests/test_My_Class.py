from classes.My_Class import My_Class

my_class = My_Class(string="My_String", number=1)

def test_get_string():
    assert my_class.get_string() == my_class.string

def test_get_number():
    assert my_class.get_number() == my_class.number
