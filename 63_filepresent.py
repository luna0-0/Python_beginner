def file(name):
    try:
        with open(name) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {name} not found.")
file('1.txt')
file('2.txt')
file('3.txt')