def intercept(interceptor):
    """Python decorator that allows modification of the arguments and
       results."""
    def interceptor_generator(original_function):
        def intercept_hook(*args, **kwargs):
            return interceptor(original_function, *args, **kwargs)

        return intercept_hook
    return interceptor_generator
