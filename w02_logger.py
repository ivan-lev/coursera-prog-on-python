def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filenamet', 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

num_list = [1, 2, 3, 4, 5]

@logger('log_file.txt')
def summator(num_list):
    return sum(num_list)

summator(num_list)
