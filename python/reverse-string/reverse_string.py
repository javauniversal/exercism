def reverse(input=''):
    if input is None or type(input) != str:
        raise Exception('Input must be string')

    reversal = ''

    index = len(input) - 1
    while index >= 0:
        reversal += input[index]
        index -= 1

    return reversal
