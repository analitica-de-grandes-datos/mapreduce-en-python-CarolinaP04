#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split('\t')
        number = fields [0]
        letter =  fields[1]

        sys.stdout.write("{}\t{}\n".format(number,letter))