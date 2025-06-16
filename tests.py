from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def tests():

    #results = get_files_info("calculator", ".")
    results = get_file_content("calculator", "main.py")
    print(results)
    print("")

    #results = get_files_info("calculator", "pkg")
    results = get_file_content("calculator", "pkg/calculator.py")
    print(results)
    print("")

    #results = get_files_info("calculator", "/bin")
    results = get_file_content("calculator", "/bin/cat")
    print(results)
    print("")

    # results = get_files_info("calculator", "../")
    # print(results)
    # print("")


    
if __name__ == "__main__":
    tests()