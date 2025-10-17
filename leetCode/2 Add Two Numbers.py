# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def addTwoNumbers(l1: list[int], l2: list[int]) -> list[int]:
    resul = []
    n1 = n2 = ""
    for n in l1[::-1] if len(l1) >= len(l2) else l2[::-1]:
        n1 += str(n)
        n2 += str(n)

    # print(n1,n2)
    result = int(n1) + int(n2)

    return [int(d) for d in str(result)]

print(addTwoNumbers([3,3,3], [2,2,2]))