from functions.run_python_file import run_python_file

def tests():

    results = run_python_file("calculator", "main.py")
    print(results)
    print("")

    results = run_python_file("calculator", "tests.py")
    print(results)
    print("")


    results = run_python_file("calculator", "../main.py")
    print(results)
    print("")

    results = run_python_file("calculator", "nonexistent.py")
    print(results)
    print("")


    
if __name__ == "__main__":
    tests()