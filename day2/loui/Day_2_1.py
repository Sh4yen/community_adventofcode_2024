import numpy as np
import scipy.ndimage as sp

# lies die Input datei ein
def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Jede Zeile im file wird eine Liste von Zahlen
        # Die Listen werden horizontal in eine Matrix gespeichert
        # Jdede Zeile entspricht einer Zeile im file
        # Jede Spalte entspricht einer Zahl in der Zeile
        data = [list(map(int, line.split(" "))) for line in lines]
    return data

data = read_input_file('input.txt')

# Behalte nur die aufsteigenden und absteigenden Zeilen, enthält auch zeilen wie [1, 2, 2, 3] diese dopplungen müssen 
# noch entfernt werden
# [::-1] dreht die Liste um, np.sort(row)[::-1] ist also die absteigende Reihenfolge
rise_fall_data = [row for row in data if np.array_equal(row, np.sort(row)) or np.array_equal(row, np.sort(row)[::-1])]
# Entferne alle Zeilen die dopplungen enthalten, eine Zeile wird nur beibehalten, wenn sie genau so lang ist wie die 
# Menge ihrer einzigartigen Elemente
unique_rise_fall_data = [row for row in rise_fall_data if len(row) == len(set(row))]




gewichtung = np.array([-1, 1])
# Horizontale sprunggröße zwischen allen elementen der matrix berechnen
# Faltung (convolution) jeder Zeile von unique_rise_fall_data mit dem Vektor [-1, 1], bestimmt sprunggröße zwischen 
# benachbarten elementen
# bsp. x = convolve1d([2, 1, 3], [-1, 1], mode="wrap") -> x = [(-2+1), (-2+3), (-3+2)] = [-1, 2, -1]
jump_data = [sp.convolve1d(row, gewichtung, mode="wrap") for row in unique_rise_fall_data]
# Es intressiert nur die sprunggröße, nicht die Richtung, daher wird der Betrag genommen
# Die letzte Spalte wird entfernt, da sie nur die Sprunggröße zwischen dem letzten und ersten Element der Zeile enthält
# diese ist nicht relevant
cut_abs_jump_data = [abs(row[:-1]) for row in jump_data]

# Behalte Nur Zeilen bei denen die Sprunggröße zwischen benachbarten Elementen in 3 oder kleiner ist
safe_cut_abs_jump_data = [row for row in cut_abs_jump_data if all(jump <= 3 for jump in row)]

# Die länge dieser Liste ist die Menge aller sicheren Regeln
# Das prüfen nach Dopplungen hätte auch durch eine jump größe von min 1 erledigt werden können
print(safe_cut_abs_jump_data)
print("_____________________________________________________________________________________________\n")
print(len(safe_cut_abs_jump_data)," Reports are sasfe")

