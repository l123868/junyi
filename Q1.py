def f(word):
    print(word, end = " ")

def main():
    data = input().split()
    for i in range(len(data)):
        f(data[i][::-1])

main()
