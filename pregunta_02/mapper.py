#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split(',',5)
        purpose =  fields[3]
        amount = fields[4]

        sys.stdout.write("{}\t{}\n".format(purpose, amount))