def test(num):

    print("in the function %d is saved in %d" %(num, id(num)))

    #1> define a str var

    result = "hello"

    print("The memory address of the function to return data to is %d" %id(result))
    #2> return str var

    return result
a = 10

print("Variable a‘s memory address where data is stored is %d" % id(a))

r = test(a)

print("%s's memory address is %d" %(r, id(r)))