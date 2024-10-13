mezua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"
j=0

# Letren portzentai errealak.
zerrendaLetra=['E','A','O','L','S','N','D','R','U','I','T','C','P','M','Y','Q','B','H','G','F','V','J','Ñ','Z','X','K','W']
zerrendaPortzentaia=[16.78,11.96,8.69,8.67,7.88,7.01,6.87,4.94,4.80,4.15,3.31,2.92,2.776,2.12,1.54,1.53,0.92,0.89,0.73,0.52,0.39,0.30,0.29,0.15,0.06,0.00,0.00]
zerrendaPortzentaia2=[]
ekibalentzia=[]

# Mezuko letra kopurua zenbatu.
kont=0
while(kont<len(mezua)):
    if(mezua[kont]!='.' and mezua[kont]!=' ' and mezua[kont]!=',' and mezua[kont]!='1' and mezua[kont]!='2' and mezua[kont]!='3' and mezua[kont]!='4' and mezua[kont]!='5' and mezua[kont]!='6' and mezua[kont]!='7' and mezua[kont]!='8' and mezua[kont]!='9' and mezua[kont]!='0'):
        j=j+1
    kont=kont+1
kont=0

# Mezuko letren portzentaia kalkulatu.
while(kont<27):
    letra=zerrendaLetra[kont]
    i=0
    letraKant=0
    while(i<len(mezua)):
        if(letra==mezua[i]):
            letraKant=letraKant+1
        i=i+1
    zerrendaPortzentaia2.append(letraKant/j*100)
    ekibalentzia.extend(letra)
    kont=kont+1

# Mezuko portzentaiak ordenatu
zerrendaKonb = list(zip(ekibalentzia, zerrendaPortzentaia2))
zerrendaKonb = sorted(zerrendaKonb, key=lambda x: x[1], reverse=True)
ekibalentzia, zerrendaPortzentaia2 = zip(*zerrendaKonb)
ekibalentzia = list(ekibalentzia)
ekibalentzia2 = list(ekibalentzia) # Hasierako egoera gorde, ez da beharrezkoa baina aldaketak ikusteko ondo dago.
zerrendaPortzentaia2 = list(zerrendaPortzentaia2)
hiztegi = dict(zip(ekibalentzia, zerrendaLetra))
mezuItzulia = ''.join(hiztegi.get(char, char) for char in mezua)
print(mezuItzulia)

# Mezua deszifratu.
while True:
    charAldat = input("\nIdatzi aldatu nahi dituzun bi letrak. Ateratzeko, 'exit'. Egiaztatzeko, 'check': ")
    if (charAldat == "exit" or charAldat == "EXIT"):
        print("Aio, Pelaio!")
        break
    elif (charAldat == "check" or charAldat == "CHECK"):
        if mezuItzulia == "CON DURRUTI MORIA EL DIRIGENTE QUE, A SU MANERA, MEJOR EXPRESABA COMO COMBATIR AL FASCISMO DESDE UN CRITERIO DE INDEPENDENCIA DE CLASE, A DIFERENCIA DEL COLABORACIONISMO FRENTEPOPULISTA DE LA DIRECCION ANARQUISTA. DURRUTI FUE UN FACTOR DE PRIMER ORDEN EN EL PAPEL DE LA CLASE OBRERA EN CATALUNYA EN JULIO DE 1936. PERO DURRUTI, COMO OCURRE CON LAS PERSONALIDADES EN LA HISTORIA, NO CAYO DEL CIELO. PERSONIFICABA LA TRADICION REvOLUCIONARIA DE LA CLASE OBRERA. SU ENORME POPULARIDAD ENTRE LA CLASE TRABAJADORA, REFLEJADA EN EL ENTIERRO MULTITUDINARIO EN BARCELONA EL 22 DE NOvIEMBRE DE 1936, MUESTRA ESA IDENTIFICACION. SU MUERTE FUE SIN DUDA UN GOLPE OBJETIvO AL PROCESO REvOLUCIONARIO EN MARCHA. SIN DURRUTI QUEDO MAS LIBRE EL CAMINO PARA QUE EL ESTALINISMO, CON LA COMPLICIDAD DEL GOBIERNO DEL FRENTE POPULAR Y DE LA DIRECCION ANARQUISTA, TERMINARA EN MAYO DE 1937 LA TAREA DE LIQUIDAR LA REvOLUCION, DESMORALIZANDO A LA CLASE OBRERA Y FACILITANDO CON ELLO EL POSTERIOR TRIUNFO FRANQUISTA":
            print("Apa hi! Mezua deszifratu dek!")
            break
        else:
            print("Keba, motel, hoi ez dek mezua! Jarraitu aldatzen!")
            continue
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

    # Ari ari ari, Gaizka lehendakari!