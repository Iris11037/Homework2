def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()

#inner_function() - невозможно вызвать эту функцию вне функции test_function(),
#                   так как она только в области test_function.