from B import book as bk

b1 = bk.book("Pinocho", "1854", "456", "dura", "rojo", "castellano\n")
b1.info()

from B import user as ur
u1 = ur.user("Victor", "18", "masculino", "española", "1.72", "60kg\n")
u1.salutacio()

from B import university as uy
u2 = uy.university("Jaume Balmes", "C/Pau claris", "932894829", "Barcelona", "20", "Informática")
u2.info()