
class List:
    def __init__(self):
        self.num = None
        self.next = None


def make_list(n):
    first = None
    for i in range(n):
        s = int(input())
        p = list()
        p.num = s
        p.next = first
        first = p
    return first


def printt(p):
    while p != None:
        print(p.num)
        p = p.next


if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    print("Enter elements:")
    first = make_list(n)
    printt(first)

