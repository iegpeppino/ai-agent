from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def tests():

    #results = get_files_info("calculator", ".")
    #results = get_file_content("calculator", "main.py")
    results = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(results)
    print("")

    #results = get_files_info("calculator", "pkg")
    #results = get_file_content("calculator", "pkg/calculator.py")
    results = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(results)
    print("")

    #results = get_files_info("calculator", "/bin") 
    #results = get_file_content("calculator", "/bin/cat")
    results = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(results)
    print("")

    # results = get_files_info("calculator", "../")
    # print(results)
    # print("")


    
if __name__ == "__main__":
    tests()