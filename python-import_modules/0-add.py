a = 1
b = 2
if __name__ == "__main__" :
    import add_0 as add_module
    result = add_module.add(a, b)
    print("{} + {} = {}".format(a, b, result))