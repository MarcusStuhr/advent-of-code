import re
from json import loads


PUZZLE_DATA_FILENAME = "day12_input.txt"


def sum_ints_in_json(obj, stop_word):
    if type(obj) == int:
        return obj
    elif type(obj) == list:
        return sum([sum_ints_in_json(next_obj, stop_word) for next_obj in obj])
    elif type(obj) != dict or stop_word in obj.values():
        return 0
    return sum_ints_in_json(obj.values(), stop_word)


def main():
    json_txt = open(PUZZLE_DATA_FILENAME).read()

    ans_part_1 = sum(map(int,re.findall(r"[-]?[0-9]+", json_txt)))
    ans_part_2 = sum_ints_in_json(loads(json_txt), "red")
    
    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)


if __name__ == "__main__":
    main()