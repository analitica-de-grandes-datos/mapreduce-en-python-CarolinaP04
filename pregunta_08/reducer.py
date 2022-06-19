#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from statistics import mean
import sys

if __name__ == '__main__':

    curkey = None
    value_list = []

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            value_list.append(val)
        else:
            if curkey is not None:
                suma = sum(value_list)
                promedio = mean(value_list)
                value_list.clear()
                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, promedio))

            curkey = key
            value_list.append(val)

    suma = sum(value_list)
    promedio = mean(value_list)
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, promedio))