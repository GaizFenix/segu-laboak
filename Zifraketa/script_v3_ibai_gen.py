import re
from collections import Counter
import os

# mezua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"
j=0

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "texto.txt")


with open(file_path, 'r') as f:
    lines = f.read()

text = re.sub(r'[^a-zA-ZñÑ]', '', lines).lower() # Text to lowercase, excluding non-alphabetic characters
letter_counts = Counter(text)

# Letren portzentai errealak.
zerrendaLetra = ['E','A','O','L','S','N','D','R','U','I','T','C','P','M','Y','Q','B','H','G','F','V','J','Ñ','Z','X','K','W']
zerrendaPortzentaia = [16.78,11.96,8.69,8.67,7.88,7.01,6.87,4.94,4.80,4.15,3.31,2.92,2.776,2.12,1.54,1.53,0.92,0.89,0.73,0.52,0.39,0.30,0.29,0.15,0.06,0.00,0.00]
zerrendaPortzentaia2 = []
ekibalentzia = []

# Mezuko letra kopurua zenbatu.
total_letters = sum(letter_counts.values())

# Mezuko letren portzentaia kalkulatu.
for letra in zerrendaLetra:
    letra = letra.lower()  # Ensure the letter is in lowercase to match the text
    letraKant = letter_counts.get(letra, 0)  # Get the count of the letter from letter_counts, default to 0 if not found
    zerrendaPortzentaia2.append(letraKant / total_letters * 100)  # Calculate the frequency percentage
    ekibalentzia.extend(letra)

# Mezuko portzentaiak ordenatu
zerrendaKonb = list(zip(ekibalentzia, zerrendaPortzentaia2))
zerrendaKonb = sorted(zerrendaKonb, key=lambda x: x[1], reverse=True)
ekibalentzia, zerrendaPortzentaia2 = zip(*zerrendaKonb)
ekibalentzia = list(ekibalentzia)
ekibalentzia2 = list(ekibalentzia) # Hasierako egoera gorde, ez da beharrezkoa baina aldaketak ikusteko ondo dago.
zerrendaPortzentaia2 = list(zerrendaPortzentaia2)
hiztegi = dict(zip(ekibalentzia, zerrendaLetra))
mezuItzulia = ''.join(hiztegi.get(char, char) for char in text)
print(lines)

atera, zuzena1, zuzena2 = False, False, False

# Decypher
while not atera:
    while not zuzena1:
        char1 = input("Sartu lehenengo letra: ")
        char1 = char1.lower()
        if (char1 == "0"):
            print("Aio, Pelaio!")
            atera = True
            break
        elif (char1 not in ekibalentzia):
            print("Mesedez, sartu letra egokia.")
            continue
        else:
            zuzena1 = True

    if atera:
        break

    while not zuzena2:
        char2 = input("Sartu bigarren letra: ")
        char2 = char2.lower()
        if (char2 == "0"):
            print("Aio, Pelaio!")
            atera = True
            break
        elif (char2 not in ekibalentzia):
            print("Mesedez, sartu letra egokia.")
            continue
        else:
            zuzena2 = True
    
# Mezua deszifratu.
# while True:
#    charAldat = input("\nIdatzi aldatu nahi dituzun bi letrak. Ateratzeko, 'exit'. Egiaztatzeko, 'check': ")
#    if (charAldat == "exit" or charAldat == "EXIT"):
#        print("Aio, Pelaio!")
#        break
#    elif (charAldat == "check" or charAldat == "CHECK"):
#        if mezuItzulia == "CON DURRUTI MORIA EL DIRIGENTE QUE, A SU MANERA, MEJOR EXPRESABA COMO COMBATIR AL FASCISMO DESDE UN CRITERIO DE INDEPENDENCIA DE CLASE, A DIFERENCIA DEL COLABORACIONISMO FRENTEPOPULISTA DE LA DIRECCION ANARQUISTA. DURRUTI FUE UN FACTOR DE PRIMER ORDEN EN EL PAPEL DE LA CLASE OBRERA EN CATALUNYA EN JULIO DE 1936. PERO DURRUTI, COMO OCURRE CON LAS PERSONALIDADES EN LA HISTORIA, NO CAYO DEL CIELO. PERSONIFICABA LA TRADICION REvOLUCIONARIA DE LA CLASE OBRERA. SU ENORME POPULARIDAD ENTRE LA CLASE TRABAJADORA, REFLEJADA EN EL ENTIERRO MULTITUDINARIO EN BARCELONA EL 22 DE NOvIEMBRE DE 1936, MUESTRA ESA IDENTIFICACION. SU MUERTE FUE SIN DUDA UN GOLPE OBJETIvO AL PROCESO REvOLUCIONARIO EN MARCHA. SIN DURRUTI QUEDO MAS LIBRE EL CAMINO PARA QUE EL ESTALINISMO, CON LA COMPLICIDAD DEL GOBIERNO DEL FRENTE POPULAR Y DE LA DIRECCION ANARQUISTA, TERMINARA EN MAYO DE 1937 LA TAREA DE LIQUIDAR LA REvOLUCION, DESMORALIZANDO A LA CLASE OBRERA Y FACILITANDO CON ELLO EL POSTERIOR TRIUNFO FRANQUISTA":
#            print("Apa hi! Mezua deszifratu dek!")
#            break
#        else:
#            print("Keba, motel, hoi ez dek mezua! Jarraitu aldatzen!")
#            continue
#    elif len(charAldat) != 2 or charAldat[0] not in ekibalentzia or charAldat[1] not in ekibalentzia:
#        print("Mesedez, sartu bi letrak larriz eta bata bestearen jarraian, tarterik gabe.")
#        continue
    
    
    # Letrak aldatu.
    idx1, idx2 = ekibalentzia.index(char1), ekibalentzia.index(char2)
    ekibalentzia[idx1], ekibalentzia[idx2] = ekibalentzia[idx2], ekibalentzia[idx1]
    hiztegi = dict(zip(ekibalentzia, zerrendaLetra))
    mezuItzulia = mezuItzulia.translate(str.maketrans(char1 + char2, char2 + char1))
    
    # Mezua berridatzi eta hiztegia(k) erakutsi.
    print("Mezu eguneratua:\n", mezuItzulia)
    print("Hasierako hiztegia:")
    for x in ekibalentzia2:
        print(x + " ", end="")
    print("\nOraingo hiztegia:")
    for x in ekibalentzia:
        print(x + " ", end="")

    zuzena1, zuzena2 = False

# Mezua gorde.
with open("../output.txt", "w") as f:
    f.write(mezuItzulia + "\n\n")
    for e1, e2 in zip(ekibalentzia2, ekibalentzia):
        f.write(f"{e1} {e2}\n")

    # Ari ari ari, Gaizka lehendakari!