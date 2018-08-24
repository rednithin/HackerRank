"""https://www.hackerrank.com/challenges/30-review-loop/problem"""

def main():
    """Main function."""
    counter = int(input())
    while counter != 0:
        my_str = input()
        for i in range(0, len(my_str), 2):
            print(my_str[i], end='')
        print(' ', end='')
        for i in range(1, len(my_str), 2):
            print(my_str[i], end='')
        print()
        counter -= 1

if __name__ == '__main__':
    main()
    
