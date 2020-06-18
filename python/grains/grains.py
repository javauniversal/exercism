def on_square(n):
    if n < 1 or n > 64:
        raise ValueError("Square must be [1, 64]")
    return 2**(n - 1)

def total_after(n):
    if n < 1 or n > 64:
        raise ValueError("Square must be [1, 64]")
    return sum(on_square(i) for i in range(1, n+1))