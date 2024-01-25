import math
def paint_calc(height,width,cover):

    cans = int(height) * int(width) / cover

    round_cans = math.ceil(cans)

    print(f"You'll need {round_cans} cans to paint your wall.")

test_h = input('Enter height  ')
test_w = input('Enter width  ')
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)




