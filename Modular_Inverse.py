# Die Funktion extended_gcd implementiert den erweiterten euklidischen Algorithmus.
# Sie berechnet den größten gemeinsamen Teiler (gcd) von a und b sowie die Koeffizienten x und y
# für die Darstellung des gcd als lineare Kombination von a und b.

def extended_gcd(a, b):
    if a == 0:
        # Wenn a gleich 0 ist, ist der gcd b und die Koeffizienten x=0 und y=1.
        return (b, 0, 1)
    else:
        # Andernfalls führen wir den erweiterten euklidischen Algorithmus rekursiv aus.
        # Der Rückgabewert ist (gcd, x, y), wobei gcd der größte gemeinsame Teiler ist,
        # x und y die Koeffizienten sind, die die Gleichung gcd = ax + by erfüllen.
        gcd, x, y = extended_gcd(b % a, a)
        if gcd == 1:
             print(f"Schritt: gcd({b}, {a}) => gcd = {gcd}, x = {x}, y = {y}")
        return (gcd, y - (b // a) * x, x)

# Die Funktion modular_inverse berechnet das modulare Inverse von a modulo m.
def modular_inverse(a, m):
    # Wir rufen die extended_gcd-Funktion auf, um gcd und die Koeffizienten x und y zu erhalten.
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        # Wenn gcd nicht 1 ist, gibt es kein modulares Inverse.
        raise ValueError("Das modulare Inverse existiert nicht.")
    else:
        # Andernfalls berechnen wir das modulare Inverse von a modulo m.
        # Das modulare Inverse ist (x % m + m) % m, um sicherzustellen, dass das Ergebnis positiv ist.
        return (x % m + m) % m

# Aufruf
a = 8
m = 11
inverse = modular_inverse(a, m)
# Wir geben das gefundene modulare Inverse aus.
print(f"Das modulare Inverse von {a} modulo {m} ist {inverse}")
