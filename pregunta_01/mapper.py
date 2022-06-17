#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split(',',5)
        credit_history =  fields[2]

        sys.stdout.write("{}\t1\n".format(credit_history))