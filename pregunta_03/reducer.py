#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator

if __name__ == '__main__':

    records = list()

    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        records.append((key, val))

    #ordernar lista de tuplas
    records = sorted(records, key=operator.itemgetter(1), reverse=False)

    for key, val in records:
        sys.stdout.write("{},{}\n".format(key, val))