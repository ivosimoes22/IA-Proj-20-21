from solution import MDProblem
import sys


def main():

    file_name = sys.argv[1]
    f = open(file_name, "r")

    a = MDProblem(f)
    a.printDisease()
    print("\n")
    a.printExam()
    print("\n")
    a.printMeas()



if __name__ == "__main__":
    main()