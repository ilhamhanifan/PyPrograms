class Induk:

    def methodInduk(self):

        print "Ini adalah Method Induk"

class Turunan(Induk):

    def methodTurunan(self):

         print "Ini adalah Method Turunan"

i = Induk()

i.methodInduk()

t = Turunan()

t.methodTurunan()
t.methodInduk()
