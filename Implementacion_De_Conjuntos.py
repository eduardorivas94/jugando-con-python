print("°°°°Bienvenido usuario a su gestor de materias°°°°")
print("eliga que materia desea revisar")
print("1.alumnos_De_Literatura")
print("2.alumnos_De_Matematicas")
alumnos_Literatura= ("maria", "jose", "elena", "lucia", "carlos")
alumnos_Matematicas=("ana", "luis", "carlos", "maria", "jose")
materia=input ("materia (1-2)")
if materia == "1":
    print(f"los alumnos de literatura son {alumnos_Literatura}")
elif materia == "2":
    print(f"los alumnos de matematicas son {alumnos_Matematicas}")