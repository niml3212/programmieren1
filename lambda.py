    bedingungen = [
        (lambda x: x <= 0.5, "Ausgabe für Wert ≤ 0.5"),
        (lambda x: 0.5 < x <= 1.0, "Ausgabe für 0.5 < Wert ≤ 1.0"),
        (lambda x: 1.0 < x <= 2.0, "Ausgabe für 1.0 < Wert ≤ 2.0"),
        (lambda x: 2.0 < x <= 3.0, "Ausgabe für 2.0 < Wert ≤ 3.0"),
        (lambda x: 3.0 < x <= 6.0, "Ausgabe für 3.0 < Wert ≤ 6.0"),
        (lambda x: x > 6.0, "Ausgabe für Wert > 6.0"),
    ]
"Lambda sind funktionen in einer Zeile"