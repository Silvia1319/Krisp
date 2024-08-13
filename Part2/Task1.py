def find_min_pledge(pledge_list):
    positive_pledges = sorted([x for x in pledge_list if x > 0])

    smallest_pledge = 1

    for pledge in positive_pledges:
        if pledge == smallest_pledge:
            smallest_pledge += 1
        elif pledge > smallest_pledge:
            break

    return smallest_pledge


assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1
