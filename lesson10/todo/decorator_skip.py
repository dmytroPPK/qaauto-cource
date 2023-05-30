def skip(condition=True, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(reason)
            else:
                print(func(*args, **kwargs))
        return wrapper
    return decorator


@skip(condition=False, reason='Skipped because of JIRA-123 bug')
def two_plus_two():
    return 2 + 2 == 4

two_plus_two()
