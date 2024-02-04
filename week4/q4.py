def print_stats_decorator(func):
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        
        if numbers:
            print("Numbers read:", numbers)
            print("Count of numbers:", len(numbers))
            print("Average of numbers:", sum(numbers) / len(numbers))
            print("Maximum of numbers:", max(numbers))
        else:
            print("No numbers to display.")

    return wrapper

@print_stats_decorator
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        numbers = [float(num) for line in lines for num in line.split()]

    return numbers

