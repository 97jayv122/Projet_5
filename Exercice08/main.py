def log_decorator(func):
    def wrapper():
        print(f"Nom de la fonction: {func.__name__}")
        result = func()
        print("Fin de l'exécution de la fonction.")
        return result
    return wrapper


 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
