#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split('   ')
        date = fields[1]
        splitted_date = date.split('-')
        month =  splitted_date[1]

        sys.stdout.write("{}\t1\n".format(month))