#demonstrate example of arbitrary function

def greet(*names):
    for name in names:
        print(f"Hello, {name}")
        
greet("Alice", "Bob", "Charlie")