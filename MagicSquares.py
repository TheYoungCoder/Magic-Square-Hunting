TestMagicSquare = [[50, 1, 20], [4, 10, 25], [5, 100, 2]]
import random


def CreateRandomSquare():
    magic_square = []
    for i in range(3):
        magic_row = []
        for i in range(3):
            magic_row.append(random.randint(1, 10))
        magic_square.append(magic_row)
    return magic_square
    

def AreUnique(magic_square):
    #Converts 2d array to flat list
    flat_magic_square = [item for sublist in magic_square for item in sublist]

    #Checks list for duplicates
    return not (len(flat_magic_square) != len(set(flat_magic_square)))


def IsMultiplicationSquare(magic_square):
    #Rows
    product_row_one = magic_square[0][0] * magic_square[0][1] * magic_square[0][2]
    product_row_two = magic_square[1][0] * magic_square[1][1] * magic_square[1][2]
    product_row_three = magic_square[2][0] * magic_square[2][1] * magic_square[2][2]
    #Colomns
    product_col_one = magic_square[0][0] * magic_square[1][0] * magic_square[2][0]
    product_col_two = magic_square[0][0] * magic_square[1][0] * magic_square[2][0]
    product_col_three = magic_square[0][0] * magic_square[1][0] * magic_square[2][0]
    #Y = X and Y = -X
    product_y_x = magic_square[0][0] * magic_square[1][1] * magic_square[2][2]
    product_y_minusx = magic_square[0][2] * magic_square[1][1] * magic_square[2][0]

    #Assemble the products into a list
    products = [product_row_one, product_row_two, product_row_three, product_col_one, product_col_two, product_col_three, product_y_x, product_y_minusx]

    #Check they are all the same product
    return (products.count(products[0]) == len(products))


def IsSumSquare(magic_square):
    #Rows
    sum_row_one = magic_square[0][0] + magic_square[0][1] + magic_square[0][2]
    sum_row_two = magic_square[1][0] + magic_square[1][1] + magic_square[1][2]
    sum_row_three = magic_square[2][0] + magic_square[2][1] + magic_square[2][2]
    #Colomns
    sum_col_one = magic_square[0][0] + magic_square[1][0] + magic_square[2][0]
    sum_col_two = magic_square[0][0] + magic_square[1][0] + magic_square[2][0]
    sum_col_three = magic_square[0][0] + magic_square[1][0] + magic_square[2][0]
    #Y = X and Y = -X
    sum_y_x = magic_square[0][0] + magic_square[1][1] + magic_square[2][2]
    sum_y_minusx = magic_square[0][2] + magic_square[1][1] + magic_square[2][0]

    #Assemble the products into a list
    sums = [sum_row_one, sum_row_two, sum_row_three, sum_col_one, sum_col_two, sum_col_three, sum_y_x, sum_y_minusx]

    #Check they are all the same sum
    return (sums.count(sums[0]) == len(sums))


while True:
    PotentialSquare = CreateRandomSquare()
    if AreUnique(PotentialSquare):
        if IsMultiplicationSquare(PotentialSquare):
            print("Time", PotentialSquare)
        if IsSumSquare(PotentialSquare):
            print("Sum", PotentialSquare)
