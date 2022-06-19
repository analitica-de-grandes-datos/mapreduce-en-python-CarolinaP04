#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    tuple_list =[]

    for line in sys.stdin:

        key, date, value = line.split("\t")
        value = int(value)
        tuple = (key, date, value)
        tuple_list.append(tuple)

    tuple_list = sorted(tuple_list, key = lambda x: x[2])
    subset_tuple_list = tuple_list[0:6]

    for tuple in subset_tuple_list:
        sys.stdout.write("{}   {}   {}\n".format(tuple[0], tuple[1], tuple[2]))