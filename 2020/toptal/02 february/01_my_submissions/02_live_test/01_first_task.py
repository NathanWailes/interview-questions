

def getChange(money_inserted, price_of_the_item):
    amount_to_be_returned = money_inserted - price_of_the_item
    number_of_dollars_to_return = amount_to_be_returned // 1

    remaining_amount = round(amount_to_be_returned - number_of_dollars_to_return, 2)

    number_of_fifty_cent_pieces_to_return = remaining_amount // 0.50
    remaining_amount = round(remaining_amount - number_of_fifty_cent_pieces_to_return * 0.50, 2)

    number_of_25_cent_pieces_to_return = remaining_amount // 0.25
    remaining_amount = round(remaining_amount - number_of_25_cent_pieces_to_return * 0.25, 2)

    number_of_10_cent_pieces_to_return = remaining_amount // 0.10
    remaining_amount = round(remaining_amount - number_of_10_cent_pieces_to_return * 0.10, 2)

    number_of_5_cent_pieces_to_return = remaining_amount // 0.05
    remaining_amount = round(remaining_amount - number_of_5_cent_pieces_to_return * 0.05, 2)

    number_of_1_cent_pieces_to_return = remaining_amount // 0.01
    remaining_amount = round(remaining_amount - number_of_1_cent_pieces_to_return * 0.01, 2)

    return [number_of_1_cent_pieces_to_return, number_of_5_cent_pieces_to_return, number_of_10_cent_pieces_to_return,
            number_of_25_cent_pieces_to_return, number_of_fifty_cent_pieces_to_return, number_of_dollars_to_return]


if __name__ == '__main__':
    # $5 - $0.99 = $4.01
    assert(getChange(5, 0.99) == [1, 0, 0, 0, 0, 4])
    assert(getChange(3.14, 1.99) == [0, 1, 1, 0, 0, 1])
    assert(getChange(4, 3.14) == [1, 0, 1, 1, 1, 0])
    assert(getChange(0.45, 0.34) == [1, 0, 1, 0, 0, 0])
