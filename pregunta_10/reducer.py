#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    dicc = dict()

    for line in sys.stdin:

        number, letters = line.split("\t")
        letters = letters.strip().split(',')

        for m in letters:
            if m not in dicc.keys():
                dicc[m] = number
            else:
                dicc[m] = dicc[m] + ',' + number

        tuple_letters = sorted(dicc.items(), key=lambda x: x[0])

    for letter, associated_numbers in tuple_letters:
        number1 = associated_numbers.split(",")
        number2 = sorted(number1, key=int)
        number3 = ",".join(number2)

        sys.stdout.write("{}\t{}\n".format(letter, number3))