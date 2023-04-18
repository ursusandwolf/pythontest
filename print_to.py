def print_to(n: int) -> None:
    if n > 1:
        n -=1
        print_to(n)
        print(n)

print_to(5)
