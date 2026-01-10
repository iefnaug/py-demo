import func
from func import is_prime

if __name__ == '__main__':
    for _ in range(5):
        code = func.generate_code(code_len=6)
        print(code)

    print(is_prime(11))
