def moyenneCB():
    MathEDHEC=float(input("note de Maths EDHEC?\n"))     
    MathEML=float(input("note de Maths EM Lyon?\n"))      
    MathEcricome=float(input("note de Maths Ecricome?\n"))       
    MathII=float(input("note de Maths ESSEC II?\n"))       
    PhiloHEC=float(input("note de philosophie HEC?\n"))       
    PhiloEDHEC=float(input("note de philosophie EDHEC?\n"))       
    PhiloEcricome=float(input("note de philosophie Ecricome?\n"))       
    AnglaisELVi=float(input("note de anglais ELVi?\n"))       
    AllemandELVi=float(input("note de Allemand ELVi?\n"))       
    AnglaisEcricome=float(input("note de Anglais Ecricome?\n"))       
    AllemandEcricome=float(input("note de Allemand Ecricome?\n"))       
    Synthèse=float(input("note de synthèse?\n"))       
    Résumé=float(input("note de résumé?\n"))       
    GéopoESCP=float(input("note de HGG ESCP?\n"))       
    GéopoESSEC=float(input("note de HGG ESSEC?\n"))       
    GéopoEcricome=float(input("note de HGG Ecricome?\n"))
       

    y=(6*MathEDHEC+MathII*2+4*PhiloEDHEC+5*AnglaisELVi+2*AllemandELVi+3*Synthèse+8*GéopoESSEC)/30 #EDHEC       
    c=(6*MathEML+MathII*2+6*PhiloHEC+4*AnglaisELVi+2*AllemandELVi+2*Synthèse+8*GéopoESCP)/30 #EMLYON       
    b=(5*MathEML+5*PhiloHEC+6*AnglaisELVi+5*AllemandELVi+3*Synthèse+6*GéopoESCP)/30 #SKEMA       
    a=(6*MathEcricome+5*PhiloEcricome+5*AnglaisEcricome+3*AllemandEcricome+2*Résumé+9*GéopoEcricome)/30 #NEOMA       
    x=(9*MathEDHEC+6*PhiloHEC+4*AnglaisELVi+3*AllemandELVi+3*Synthèse+6*GéopoESCP)/30 #AUDENCIA
        
    print("Ta note à l'EDHEC :",y)       
    print("Ta note à l'EM Lyon:",c)       
    print("Ta note à SKEMA:",b)       
    print("Ta note à NEOMA :",a)       
    print("Ta note à Audencia :",x)

    if y>12.63:
        print("Admissible à EDHEC")       
    if c>11.8:
        print("Admissible à EM LYON")       
    if b>10.8:
        print("Admissible à Skema")
    if a>10.4:
        print("Admissible à NEOMA")     
    if x>9.5:
        print("Admissible à Audencia")
if __name__ == '__main__':
    moyenneCB()