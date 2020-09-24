def opt (x):
    try:
        return 42/x
    except ZeroDivisionError:
        print('cant divide by 0')
opt(0)
