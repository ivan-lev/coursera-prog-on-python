def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('file.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped

num_list = [1, 2, 3, 4 , 5]

@logger
def summator(num_list):
    return sum(num_list)

summator(num_list)
