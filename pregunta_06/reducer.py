#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
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
                maximo = max(value_list)
                minimo = min(value_list)
                value_list.clear()

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))

            curkey = key
            value_list.append(val)
    
    maximo = max(value_list)
    minimo = min(value_list)

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))