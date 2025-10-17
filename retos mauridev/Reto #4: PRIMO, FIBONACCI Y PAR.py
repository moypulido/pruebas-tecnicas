# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def is_prime(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if is_even(n):
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
        
    return True

    



def is_cuadrado_perfect(n):
    sqrt = int(n**.5)
    return sqrt*sqrt == n

def is_fibonacci(n):
    return is_cuadrado_perfect(5 * (2*n) +4) or is_cuadrado_perfect(5 * (2*n) -4)
    





def is_even(n):
    return n % 2 == 0


def check_properties(num):
    prime_status = "es primo" if is_prime(num) else "no es primo"
    fibonacci_status = "es fibonacci" if is_fibonacci(num) else "no es fibonacci"
    even_status = "es par" if is_even(num) else "es impar"
    
    return f"{num} {prime_status}, {fibonacci_status} y {even_status}"


num = 2
print(check_properties(num))

