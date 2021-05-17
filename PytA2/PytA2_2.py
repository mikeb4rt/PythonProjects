def viatge(alumnes):
    if alumnes < 30:
        return 115
    elif alumnes >= 30 and alumnes <=49:
        return 95
    elif alumnes > 49 and alumnes <= 99:
        return 70
    else:
        return 65

quantitat_alumnes = int(input("Quats alumnes son al viatge"))
print(f"El total del viaje son {4000 + viatge(quantitat_alumnes)} €")