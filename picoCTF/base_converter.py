import string 

""" 
Convert a number from base 16 to base 10
"""

def convert_base(input_value: string, from_base: int, to_base: int) -> string: 
    """
    Base 16 uses 16 values: the numbers 0-9 and the letters A-F.
    Base 10 uses 10 values: the numbers 0-9.

    Here is a mapping for reference: 
        Base-10 | Base-2 | Base-16
        ---------+--------+--------
        0       | 0      | 0
        1       | 1      | 1
        2       | 10     | 2
        3       | 11     | 3
        4       | 100    | 4
        5       | 101    | 5
        6       | 110    | 6
        7       | 111    | 7
        8       | 1000   | 8
        9       | 1001   | 9
        10      | 1010   | A
        11      | 1011   | B
        12      | 1100   | C
        13      | 1101   | D
        14      | 1110   | E
        15      | 1111   | F

    To convert from base 16 to base 10 -> we can ignore numeric characters and focus on letters. 

    For each hexadecimal character we need to calculate the decimal value and add up the total:

    The right most hex is multipled by 16^0, the next one to the left is multiplied by 16^1 etc...
    """

    
