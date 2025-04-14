# Fonction calculate_average
def calculate_average(numbers):
    """
    Returns the average of a list of numbers.

    Args:
        numbers (list of int or float): The list of numbers"
    """
    return sum(numbers) / len(numbers)
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
