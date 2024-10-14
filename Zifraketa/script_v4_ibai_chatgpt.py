import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "texto.txt")

# Read the input text from "texto.txt"
with open(file_path, 'r') as f:
    mezua = f.read()

j = 0

# Letren portzentai errealak.
zerrendaLetra = ['E', 'A', 'O', 'L', 'S', 'N', 'D', 'R', 'U', 'I', 'T', 'C', 'P', 'M', 'Y', 'Q', 'B', 'H', 'G', 'F', 'V', 'J', 'Ñ', 'Z', 'X', 'K', 'W']
zerrendaPortzentaia = [16.78, 11.96, 8.69, 8.67, 7.88, 7.01, 6.87, 4.94, 4.80, 4.15, 3.31, 2.92, 2.776, 2.12, 1.54, 1.53, 0.92, 0.89, 0.73, 0.52, 0.39, 0.30, 0.29, 0.15, 0.06, 0.00, 0.00]
zerrendaPortzentaia2 = []
ekibalentzia = []

# Mezuko letra kopurua zenbatu.
kont = 0
while kont < len(mezua):
    if mezua[kont] not in ('.', ' ', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        j += 1
    kont += 1
kont = 0

# Mezuko letren portzentaia kalkulatu.
while kont < 27:
    letra = zerrendaLetra[kont]
    i = 0
    letraKant = 0
    while i < len(mezua):
        if letra == mezua[i]:
            letraKant += 1
        i += 1
    zerrendaPortzentaia2.append(letraKant / j * 100)
    ekibalentzia.extend(letra)
    kont += 1

# Mezuko portzentaiak ordenatu
zerrendaKonb = list(zip(ekibalentzia, zerrendaPortzentaia2))
zerrendaKonb = sorted(zerrendaKonb, key=lambda x: x[1], reverse=True)
ekibalentzia, zerrendaPortzentaia2 = zip(*zerrendaKonb)
ekibalentzia = list(ekibalentzia)
ekibalentzia2 = list(ekibalentzia)  # Hasierako egoera gorde, ez da beharrezkoa baina aldaketak ikusteko ondo dago.
zerrendaPortzentaia2 = list(zerrendaPortzentaia2)
hiztegi = dict(zip(ekibalentzia, zerrendaLetra))
mezuItzulia = ''.join(hiztegi.get(char, char) for char in mezua)
print(mezuItzulia)

# Mezua deszifratu.
while True:
    charAldat = input("\nIdatzi aldatu nahi dituzun bi letrak. Ateratzeko, '0': ")
    
    if charAldat == "0":
        print("Aio, Pelaio!")
        break
    elif len(charAldat) != 2 or charAldat[0] not in ekibalentzia or charAldat[1] not in ekibalentzia:
        print("Mesedez, sartu bi letrak larriz eta bata bestearen jarraian, tarterik gabe.")
        continue

    # Letrak aldatu.
    idx1, idx2 = ekibalentzia.index(charAldat[0]), ekibalentzia.index(charAldat[1])
    ekibalentzia[idx1], ekibalentzia[idx2] = ekibalentzia[idx2], ekibalentzia[idx1]
    hiztegi = dict(zip(ekibalentzia, zerrendaLetra))
    mezuItzulia = mezuItzulia.translate(str.maketrans(charAldat[0] + charAldat[1], charAldat[1] + charAldat[0]))
    
    # Mezua berridatzi eta hiztegia(k) erakutsi.
    print("Mezu eguneratua:\n", mezuItzulia)
    print("Hasierako hiztegia:")
    for x in ekibalentzia2:
        print(x + " ", end="")
    print("\nOraingo hiztegia:")
    for x in ekibalentzia:
        print(x + " ", end="")

# Save the translated message and mapping to a file
output_path = os.path.join(script_dir, "../output.txt")
with open(output_path, "w") as f:
    f.write("Final translated message:\n")
    f.write(mezuItzulia + "\n\n")
    f.write("Letter mappings (original -> swapped):\n")
    for key, value in hiztegi.items():
        f.write(f"{key} -> {value}\n")

print("\nTranslation saved to 'output.txt'.")

    # Ari ari ari, Gaizka lehendakari!
