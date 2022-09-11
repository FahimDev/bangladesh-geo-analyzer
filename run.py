from src.manager import Manager


def main():
    try:
        menuObj = Manager()
        menuObj.menu()
    except Exception as e:
        print("Something went wrong! Error:")
        print(e)
        # If any Error occur in other classes those Exceptions will be also printed here.


if __name__ == '__main__':
    main()
