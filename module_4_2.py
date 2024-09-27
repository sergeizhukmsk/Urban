def test_function():
    def inner_function():
        print ( "Я в области видимости функции test_function" )

    inner_function ()


# Вызовем функцию test_function
test_function ()

# Попробуем вызвать inner_function вне функции test_function
inner_function ()

# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# При вызове innerfunction вне функции testfunction возникнет ошибка, так как innerfunction доступна только в области видимости testfunction.
