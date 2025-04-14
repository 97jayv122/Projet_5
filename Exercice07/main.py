## Écrivez votre code ici !
def square(n):
    """
    Return the square of a number. if n is not a number, return None.

    Args:
        n (int or float): The number

    Returns:
        int or float: The square of n or None if n is not a number
    """
    if isinstance(n, (int, float)):
        return n**2
    else:
        print("Le paramètre doit être un nombre !")
        return None
