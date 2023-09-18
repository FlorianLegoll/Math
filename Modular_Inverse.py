def extended_gcd(a, m):
    # Initialisierung der Anfangswerte
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        # Berechnung des Quotienten und Rests
        quotient, a, m = a // m, m, a % m
        # Aktualisierung der Bézout-Koeffizienten
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1

    # x0 ist das modulare Inverse von a modulo b
    return x0

def modular_inverse(a, m):
    # Berechnung des GCD von a und m
    gcd = extended_gcd(a, m)
    
    # Überprüfung, ob a und m teilerfremd sind (GCD(a, m) = 1)
    if gcd != 1:
        raise ValueError("Das modulare Inverse existiert nicht, da a und m nicht teilerfremd sind.")
    
    # Berechnung des modularen Inversen
    inverse = (extended_gcd(a, m) % m + m) % m
    
    return inverse

# Beispielaufruf
a = 3
m = 11
inverse = modular_inverse(a, m)
print(f"Das modulare Inverse von {a} modulo {m} ist {inverse}")
def extended_gcd(a, m):
    # Initialisierung der Anfangswerte
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        # Berechnung des Quotienten und Rests
        quotient, a, m = a // m, m, a % m
        # Aktualisierung der Bézout-Koeffizienten
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1

    # x0 ist das modulare Inverse von a modulo b
    return x0

def modular_inverse(a, m):
    # Berechnung des GCD von a und m
    gcd = extended_gcd(a, m)
    
    # Überprüfung, ob a und m teilerfremd sind (GCD(a, m) = 1)
    if gcd != 1:
        raise ValueError("Das modulare Inverse existiert nicht, da a und m nicht teilerfremd sind.")
    
    # Berechnung des modularen Inversen
    inverse = (extended_gcd(a, m) % m + m) % m
    
    return inverse

# Beispielaufruf
a = 3
m = 11
inverse = modular_inverse(a, m)
print(f"Das modulare Inverse von {a} modulo {m} ist {inverse}")
