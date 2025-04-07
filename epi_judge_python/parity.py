from test_framework import generic_test


def parity(x: int) -> int:
    result = False
    while x:
        result = not result
        x &= (x-1)
    return 1 if result else 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
