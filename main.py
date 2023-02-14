# Hecho por Víctor 'B'
from B import book as bk

b1 = bk.book("Pinocho", "1854", "456", "dura", "rojo", "castellano\n")
b1.info()

from B import user as ur
u1 = ur.user("Victor", "18", "masculino", "española", "1.72", "60kg\n")
u1.salutacio()

from B import university as uy
u2 = uy.university("Jaume Balmes", "C/Pau claris", "932894829", "Barcelona", "20", "Informática")
u2.info()

# Hecho por Albert 'A'

from A import animal as al
p1 = al.animal("mamífer", "gran", "suau", "20anys", "llarga", "2.50m\n")
p1.salutacio()

from A import vehicle as vh
p2 = vh.vehicles("cuatre", "mercedes", "gran", "cuatre", "antic", "blau", "rápid\n")
p2.nomParts()

from A import school as sc
p3 = sc.school("1.70", "Javier", "Pérez", "1a", "16", "4t ESO")
p3.nomInfo()
