from tkinter import *
from random import *
from math import *
import scipy.integrate as integrate
from urllib.request import urlopen
import time

def temp():
    global arv
    suurusk = arv.get()
    protsess = "T"
    suurusekene(suurusk,protsess)
    
def rõ():
    global arv
    suurusk = arv.get()
    protsess = "P"
    suurusekene(suurusk,protsess)
    
    
def ruum():
    global arv
    suurusk = arv.get()
    protsess = "V"
    suurusekene(suurusk,protsess)
    
def sooq():
    global arv
    suurusk = arv.get()
    protsess = "Q"
    suurusekene(suurusk,protsess)
    
def arvutama():
    global arv
    suurusk = arv.get()
    protsess = "0"
    suurusekene(suurusk,protsess)
    
def arvutus():
    global arv
    suurus = arv.get()
    if suurus == "w" or suurus== "q" or suurus== "H" or suurus == "U" or suurus == "S" or suurus == "G" or suurus =="F" or suurus =="Paisumistöö" or suurus =="Soojusenergia" or suurus =="Siseenergia" or suurus =="Entalpia" or suurus =="Gibbsi vabaenergia" or suurus =="Helmholzi vabaenergia":
        ttk.Label(window, text="Kas protsess toimub mingil konstantsel suurusel? Sisesta, kas (T,P,V,q) on konstantne?").pack()
        ttk.Button(window,text="Temperatuur",width=10, command = temp).pack()
        ttk.Button(window,text="Rõhk",width=10, command = rõ).pack()
        ttk.Button(window,text="Ruumala",width=10, command = ruum).pack()
        ttk.Button(window,text="Soojusenergia",width=10, command = sooq).pack()
    elif suurus != "":
        ttk.Button(window,text="Arvutama!",width=10, command = arvutama).pack()
    else:
        messagebox.showinfo("Info","Sisesta suurus!")

def solva():
    global t
    nimik = t.get()
    solv = solvang(nimik)
    tekst = window.nametowidget(".solvangu_tekst")
    tekst.config(text = solv)

def hea():
    tuju = str(head.get())
    if tuju == "hea":
        ttk.Label (window, text="Mida sa sooviksid arvutada? Sisesta vastava suuruse nimi või tähis.\nValikus on Paisumistöö(w), Soojusenergia(q), Siseenergia(U), Entalpia(H), Entroopia(S), Gibbsi vabaenergia(G), Helmholzi vabaenergia(F),\n Reaktsiooni gibbsi energia(Gr), Kontsentratsioon(c), Moolid(n), Molaarmass(M), Mass(m), Rõhk(P), Ruumala(V), Happe pH, Aluse pH: ").pack()
        global arv
        arv = StringVar()
        ttk.Entry(window, width = 40, textvariable = arv).pack()
        ttk.Button(window,text="Edasi!",width=10, command = arvutus).pack()
        ttk.Label(window, text="Programm kasutab arvutamiseks standardseid SI-süsteemi ühikuid. Palun teha vastavad teisendused ise!").pack()
        
    elif tuju =="halb":
        ttk.Label (window, text="Sisesta inimese nimi, keda soovid solvata: ",).pack()
        global t
        t = StringVar()
        nimi1 = ttk.Entry(window, width = 40, textvariable = t)
        nimi1.pack()
        
        ttk.Button(window,text="Solva!",width=10, command = solva).pack()
        
        tekst = ttk.Label(window, text="", name="solvangu_tekst")
        tekst.pack()
            
    else:
        ttk.Label (window, text="Ärme tee siis midagi. Eksju!").pack()
        window.update()
        time.sleep(1.5)
        window.destroy()
        
def Molaarmass(b):
    messagebox.showinfo("Info","Arvutame molaarmassi.")
    answer = simpledialog.askstring("Küsimus","Sisesta kas failist või veebist?")
    if answer.lower() == "veebist":
        try:
            vastus = urlopen("https://www.periodni.com/solcalc-chemical_compounds.html")
            baidid = vastus.readlines()
            algne_asi = []
            tekst = []
            for i in baidid:
                kood = i.decode()
                read =  kood.replace("\a","").replace("td","").replace("\td","").replace("tr","").replace("\tr","").replace("sub","").replace("<","").replace(">","").replace("\n","").replace("/","")
                algne_asi.append(read)
                vastus.close()    
            for i in algne_asi:
                if i == "":
                    del i
                elif i[0].isnumeric():
                    tekst.append(i)
            M = simpledialog.askstring("Küsimus","Sisesta aine valem.")
            molaar1 = []
            molaar = ""
            for i in tekst:
                if M in i:
                    ind = i.index(M)
                    molaar1.append(i[ind+1:])
            pikkus = len(M)
            molaarmassid = []
            try:
                for i in molaar1:
                    if len(molaar1) != 1:
                        indeks = i.index(M)
                        molaarmassid.append(i[indeks:indeks+6+pikkus])
                    else:
                        indeks = i.index(M)
                        molaar = i[indeks+pikkus:indeks+5+pikkus]
            except:
                ""
            mm = ""
            if molaar != "" and len(molaar1) == 1:
                molaar2 = float(molaar)
                return molaar2
      
            elif len(molaarmassid) != 1 and len(molaarmassid) !=0:
                for i in molaarmassid:
                    mm += i[pikkus:]+" M \n"
                tekstike = "Leidsin mitu vastet: "+mm+"Vali missugune tundub õige molaarmass(1,..)! "
                valik = simpledialog.askinteger("Input", tekstike)
                moli = molaarmassid[int(valik)-1]
                indeks1 = moli.index(M)
                molaar3 = moli[indeks1+pikkus:indeks1+5+pikkus].strip(" ")
                molk = float(molaar3)
                return molk

            else:
                return "Antud valemit ei leitud andmebaasist!"
        except:
            return "Tekkis mingi viga!"

    elif answer.lower() == "failist":
        try:
            f = open("keemia.txt", "r")
            sisu = f.readlines()
            f.close()
            M = simpledialog.askstring("Küsimus","Sisesta aine valem.")
            molaar1 = []
            molaar = ""
            k = 0
            for i in sisu:
                if M in i:
                    molaar1.append(str(i))
            pikkus = len(M)
            molaarmassid = []
            for i in molaar1:
                if M+"\t" in i:
                    molaarmassid.append(str(i))
            for i in molaarmassid:
                molaar = i[1+pikkus:6+pikkus]
            try:
                arv = float(molaar)
                return arv
            except:
                return "Ei leidnud molaarmassi andmebaasist."
        except:
            return "Tekkis mingi viga."
    else:
        return "Tekkis mingi viga!"
    
def soojus(b):
    messagebox.showinfo("Info","Arvutame soojusenergia.")
    if b == "Q":
        messagebox.showinfo("Info","Tegemist on adiabaatilise protsessiga ning q = 0.")
        q = 0.0
        return q
    else:
        n = moolide_küsimine(b)
        T1 = simpledialog.askfloat("Input","Sisesta gaasi algtemperatuur(K): ")
        T2 = simpledialog.askfloat("Input","Sisesta gaasi lõpptemperatuur(K): ")
        molike = messagebox.askyesno("Information","Kas moolsoojus sõltub T-st või kas tegemist on suure temperatuuri vahemikuga? ")
        if molike == True:
            try:
                a = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse esimene liige(a): ")
                b = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse teine liige(b): ")
                c = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse kolmas liige(c): ")
                d = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse neljas liige(d): ")
                integraal = integrate.quad(lambda T: a + b*T + c*T**(2)+ d*T**(3), T1, T2)
                inte = round(float(integraal[0]),2)
                q = n*inte
                return q
            except:
                return "Tekkis mingi viga. Kontrolli andmed üle!"
                
        else:
            cp = simpledialog.askfloat("Input","Sisesta moolsoosjus konstantsel rõhul: ")
            try:
                q = n*cp*(T2-T1)
                return q
            except:
                return "Tekkis mingi viga. Kontrolli andmed üle!"
            
def sise(b):
    messagebox.showinfo("Info","Arvutame siseenergia.")
    if b == "T":
        messagebox.showinfo("Info","Tegemist on isotermilise protsessiga ning U = 0, sest T = const.")
        U = 0.0
        return U
    else:
    
        Küs = messagebox.askyesno("Information","Kas sa tead soojushulka? ")
        if Küs == True:
            q = simpledialog.askfloat("Input","Sisesta aine soojushulk(J): ")  
        else:
            q = soojus(b)
            if q != "Tekkis mingi viga. Kontrolli andmed üle!":
                messagebox.showinfo("Info","Soojusenergia on "+str(q)+" J.")
        Küs = messagebox.showinfo("Information","Kas sa tead paisumistööd? ")
        if Küs == True:
            w = simpledialog.askfloat("Input","Sisesta tehtud paisumistöö(J): ")
        else:
            w = töö(b)
            if w != "Tekkis mingi viga. Kontrolli andmed üle!":
                messagebox.showinfo("Info","Paisumistöö on "+str(w)+" J.")
        try:
            U = q + w
            return U
        except:
            return "Tekkis mingi viga. Kontrolli sisestatud andmed üle!"
        
def moolide_küsimine(b):
    answer = messagebox.askyesno("Küsimus","Kas sa tead aine moolide arvu?")
    if answer == True:
        n = simpledialog.askfloat("Input", "Sisesta reaktsiooni moolide arv(mol): ")
        return n
    else:
        try:
            n = mool(b)
            indeks = str(n).index(".")
            if str(n)[0:indeks].isnumeric() and str(n)[indeks+1:].isnumeric():
                messagebox.showinfo("Info","Seega aine moolide arv on "+str(round(n,4))+" mooli.")
                return n
            else:
                print(n)
        except:
            return "Tekkis mingi viga"
        
def mool(b):
    messagebox.showinfo("Info","Arvutame moolide arvu.")
    m = simpledialog.askfloat("Input", "Sisesta aine mass(g): ")
    answer = messagebox.askyesno("Küsimus","Kas sa tead aine moolaarmassi?")
    if answer == True:
        M = simpledialog.askfloat("Input", "Sisesta aine molaarmass(g/mol): ")
    else:
        try: 
            M = Molaarmass(b)
            indeks = str(M).index(".")
            if str(M)[0:indeks].isnumeric() and str(M)[indeks+1:].isnumeric():
                messagebox.showinfo("Info","Aine molaarmass on "+str(M)+" g/mol.")
            else:
                messagebox.showinfo("Info",M)
        except:
            M = 0
    try:       
        n = m / M
        return n
    except:
        return "Tekkis mingi viga!"
    
def solvang(a):
    tegusõnad = ["on", "oli", "tahab olla", "kindlasti on","absoluutselt ei ole","on oma halvimatel päevadel","oli minevikus", "istub", "eksisteerib", "värvib", "kirjutab", "jookseb", "seisab", "kogub mõttetuid asju", "lehvitab", "sööb", "kuritarvitab vanemate usaldust", "hüppab", "lõhnab", "joob alkoholi", "loeb raamatut", "kokkab", "maalib", "pildistab","naljatab", "toetab EKREt"]
    semi = tegusõnad.index("istub")
    tegu = tegusõnad[randint(0, len(tegusõnad)-1)]
    määrsõnad = ["väga", "eriti", "natukene", "kergelt", "raskelt", "alati", "tõenäoliselt", "suhteliselt", "väidetavalt", "poolearuselt", "päikseliselt", "äikseliselt", "ainult natukene", "rõvedalt", "mõnusalt", "saatanlikult", "uskumatult", "värvikalt", "hedonistlikult", "ropult", "tüütult", "päris vingelt", "keskpäraselt", "barbaarselt"]
    määr = määrsõnad[randint(0, len(määrsõnad)-1)]
    omadussõnad1 = ["esteetiline", "edgy", "kole", "ülekasvanud", "EKRE toetaja", "rahulik", "halb", "konkreetne", "väike", "suur", "vale", "tilluke", "noor", "nilbe", "EKA tudeng", "kihiline nagu sibul", "Shrek", "töötu", "arstitudeng", "abouliline", "põlastusväärne", "absurdne", "akadeemiline", "furry", "Hale™", "silmatorkav", "julm", "keskpärane", "väsitav", "barbaarne", "tormakas", "äraostetav", "matslik", "Kadrinast pärit", "dramaatiline", "sassis", "kummaline", "egoistlik", "liialdav", "innukas", "pedantne", "jonnakas", "tõrges", "pahur", "isemeelne", "otsekohene", "sünge", "kergeusklik", "kõle", "ebaühtlane", "ebakompetentne", "sallimatu", "vastutustundetu", "vilets", "väheviljakas"]
    omadussõnad2 = ["esteetiliselt", "edgylt", "koledalt", "rahulikult", "halvasti", "konkreetselt", "suurelt", "valesti", "nilbelt", "kihiliselt", "tobedalt", "põlastusväärselt", "absurdselt", "süüdlaslikult", "barbaarselt", "ajuvabalt", "jõuluselt", "dramaatiliselt", "tühjalt", "tuhmilt", "innukalt", "pedantselt", "ebaühtlaselt", "viletsalt"]
    if tegusõnad.index(tegu) < semi:
        omad = omadussõnad1[randint(0, len(omadussõnad1)-1)]
    else:
        omad = omadussõnad2[randint(0, len(omadussõnad2)-1)]
    päikesed = ["Päikest!:)", "Äikest!:(", "Häid Mõtteid!:)", "Head Elu!:)", "Võta Heaks!:)", "Hea Inimene!:)", "Halbu mõtteid!:(", "Pealtnägemiseni!:)", "Trehvamiseni!:)"]
    päike = päikesed[randint(0,len(päikesed)-1)]
    solv = str(a).title()+" "+str(tegu)+" "+str(määr)+" "+str(omad)+", "+str(päike)
    return solv
    
def töö(b):
    ttk.Label (window, text="Arvutame paisumistöö.").pack()
    if b == "V":
        messagebox.showinfo("Info","Tegemist on isokoorilise protsessiga ning w = 0, sest V = const.")
        w = 0.0
        return w
    
    V1 = simpledialog.askfloat("Input", "Sisesta süsteemi algne ruumala(m3): ")
    V2 = simpledialog.askfloat("Input", "Sisesta süsteemi lõpu ruumala(m3): ")
    if b == "P":
        P = simpledialog.askfloat("Input", "Sisesta süsteemi rõhk(Pa): ")
        V = V2 - V1
        w = -1*V*P
        return w
    else:
        T = simpledialog.askfloat("Input", "Sisesta gaasi temperatuur(K): ")
        n = moolide_küsimine(b)
        R = 8.314
        try:
            w = -1*n*R*T*log(V2/V1)
            return w
        except:
            return "Tekkis mingi viga. Kontrolli andmed üle!"
        
def entalpia(b):
    messagebox.showinfo("Info","Arvutame entalpia.")
    if b == "P":
        messagebox.showinfo("Info","Tegemist on isobaarilise protsessiga ning p = 0 ning H = q.")
        Küs = messagebox.askyesno("Küsimus","Kas sa tead soojushulka? ")
        if Küs == True:
            H = simpledialog.askfloat("Input","Sisesta soojushulk: ")
            return H
        else:
            H = soojus(b)
            return H
    elif b == "T":
        messagebox.showinfo("Info","Tegemist on isotermilise protsessiga ning H = 0, sest T = const.")
        H = 0.0
        return H
    else:
        Küs = messagebox.askyesno("Küsimus","Kas sa tead soojushulka? ")
        if Küs == True:
            q = simpledialog.askfloat("Input","Sisesta soojushulk: ")
        else:
            q = soojus(b)
            if q!= "Tekkis mingi viga. Kontrolli andmed üle!":
                messagebox.showinfo("Info","Soojusenergia on "+str(q)+" J.")
        Küs1 = messagebox.askyesno("Küsimus","Kas sa tead paisumistööd? ")
        if Küs1 == True:
            w = simpledialog.askfloat("Input","Sisesta tehtud paisumistöö(J): ")
        else:
            w = töö(b)
            if w!= "Tekkis mingi viga. Kontrolli andmed üle!":
                messagebox.showinfo("Info","Paisumistöö on "+str(w)+" J.")
        try:
            H = q + w + w
            return H
        except:
            return "Tekkis mingi viga. Kontrolli sisestatud andmed üle!"
        
def entroopia(b):
    messagebox.showinfo("Info","Arvutame entroopia.")
    if b == "Q":
        messagebox.showinfo("Info","Tegemist on adiabaatilise protsessiga ning q = 0. Seega avaldame q teiste muutujate kaudu.")
        n = moolide_küsimine(b)
        T1 = simpledialog.askfloat("Input","Sisesta gaasi algtemperatuur(K): ")
        T2 = simpledialog.askfloat("Input","Sisesta gaasi lõpptemperatuur(K): ")
        a = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse esimene liige(a): ")
        b = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse teine liige(b): ")
        c = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse kolmas liige(c): ")
        d = simpledialog.askfloat("Input","Sisesta moolsoosjuse sõltuvuse neljas liige(d): ")
        try:
            integraal = integrate.quad(lambda T: a/T + b + c*T+ d*T**(2), T1, T2)
            inte = round(float(integraal[0]),2)
            S = n*inte
            return S
        except:
            return "Tekkis mingi viga. Kontrolli andmed üle!"
    else:
        Küs = messagebox.askyesno("Information","Kas sa tead soojushulka? ")
        if Küs == True:
            q = simpledialog.askfloat("Input","Sisesta soojushulk: ")
        else:
            q = soojus(b)
            if q != "Tekkis mingi viga. Kontrolli andmed üle!":
                messagebox.showinfo("Info","Soojusenergia on "+str(q)+" J.")
        T = simpledialog.askfloat("Input","Sisesta gaasi algtemperatuur(K): ")
                
        try:
            S = float(q // T)
            return S
        except:
            return "Tekkis mingi viga. Kontrolli andmed üle!"
        
def gibbs(b):
    messagebox.showinfo("Info","Arvutame Gibbsi energia.")
    Küs = messagebox.askyesno("Information","Kas sa tead entalpiat? ")
    if Küs == True:
        H = simpledialog.askfloat("Input","Sisesta entalpia (J): ")
    else:
        H = entalpia(b)
    T = simpledialog.askfloat("Input","Sisesta gaasi temperatuur(K): ")
    Küs = messagebox.askyesno("Information","Kas sa tead entroopiat? ")
    if Küs == True:
        S = simpledialog.askfloat("Input","Sisesta entroopiat (J): ")
    else:
        S = entroopia(b)
    try:
        G = H - T*S
        return G
    except:
        return "Tekkis mingi viga. Kontrolli andmed üle!"
    
def helm(b):
    messagebox.showinfo("Info","Arvutame Helmholzi vabaenergia.")
    Küs = messagebox.askyesno("Information","Kas sa tead siseenerigat? ")
    if Küs == True:
        U = simpledialog.askfloat("Input","Sisesta siseenergia(J): ")
    else:
        U = sise(b)
    T = simpledialog.askfloat("Input","Sisesta gaasi temperatuur(K): ")
    Küs =messagebox.askyesno("Information","Kas sa tead entroopiat? ")
    if Küs == True:
        S = simpledialog.askfloat("Input","Sisesta entroopiat (J): ")
    else:
        S = entroopia(b)
    try:
        F = U - T*S
        return F
    except:
        return "Tekkis mingi viga. Kontrolli andmed üle!"
    
def reaktsioonigibbs(b):
    messagebox.showinfo("Info","Arvutame reaktsiooni Gibbsi energia.")
    g = simpledialog.askfloat("Input","Sisesta standardne gibbsi energia: ")
    T = simpledialog.askfloat("Input","Sisesta temperatuur(K): ")
    Q = simpledialog.askfloat("Input","Sisesta reaktsiooni tasakaalukonstant: ")
    R = 8.314
    try:
        Gr = float(g + R*T*log(Q))
        return Gr
    except:
        return "Tekkis mingi viga. Kontrolli andmed üle!"
    
def konts(b):
    messagebox.showinfo("Info","Arvutame kontsentratsiooni")
    n = moolide_küsimine(b)
    V = simpledialog.askfloat("Input","Sisesta lahuse ruumala(dm3): ")
    try:
        c = n / V
        return c
    except:
        return "Tekkis mingi viga. Proovi uuesti ja kontrolli andmed üle!"

def mass(b):
    messagebox.showinfo("Info","Arvutame massi.")
    Küs = messagebox.askyesno("Information","Kas sa tead aine molaarmassi? ")
    if Küs == True:
        M = simpledialog.askfloat("Input","Sisesta aine molaarmass(g/mol): ")     
    else:
        M = Molaarmass(b)
        indeks = str(M).index(".")
        if str(M)[0:indeks].isnumeric() and str(M)[indeks+1:].isnumeric():
            messagebox.showinfo("Info","Aine molaarmass on "+str(M)+" g/mol.")
        else:
            print(M)
    n = simpledialog.askfloat("Input","Sisesta aine moolid(mol): ")
    try:
        m = n * M
        return m
    except:
        return "Tekkis mingi viga. Proovi uuesti ja kontrolli sisestatud andmed üle!"
    
def idgaas_ruumala(b):
    messagebox.showinfo("Info","Arvutame ruumala.")
    n = moolide_küsimine(b)
    T = simpledialog.askfloat("Input","Sisesta temperatuur(K): ")
    R = 8.314
    P = simpledialog.askfloat("Input","Sisesta rõhk(Pa): ")
    try: 
        V = n*R*T/P
        return V
    except:
        return "Tekkis mingi viga. Kontrolli sisestatud andmed üle!"
    
def idgaas_rõhk(b):
    messagebox.showinfo("Info","Arvutame rõhu.")
    T = simpledialog.askfloat("Input","Sisesta temperatuur(K): ")
    R = 8.314
    V = simpledialog.askfloat("Input","Sisesta ruumala(m3): ")
    n = moolide_küsimine(b)
    try: 
        P = n*R*T/V
        return P
    except:
        return "Tekkis mingi viga. Kontrolli sisestatud andmed üle!"
    
def happe_pH(b):
    messagebox.showinfo("Info","Arvutame pH. Selle jaoks aga: ")
    Küs = messagebox.askyesno("Information","Kas sa tead kontsentratsiooni? ")
    if Küs == True:
        c = simpledialog.askfloat("Input","Sisesta aine kontsentratsioon: ")
    else:
        c = konts(b)
    Küs = messagebox.askyesno("Information","Kas on tegemist nõrga happega? ")
    if Küs == True:
        Kd = simpledialog.askfloat("Input","Sisesta happe dissotsiatsioonikonstant: ")  
        H = sqrt(Kd)*c
    else:
        H = c
    try: 
        pH = -1*log(H,10)
        return pH
    except:
        return H

def aluse_pH(b):
    messagebox.showinfo("Info","Arvutame pH. Selle jaoks aga: ")
    Küs = messagebox.askyesno("Information","Kas sa tead kontsentratsiooni? ")
    if Küs == True:
        c = simpledialog.askfloat("Input","Sisesta aine kontsentratsioon: ")   
    else:
        c = konts(b)
    Küs = messagebox.askyesno("Information","Kas on tegemist nõrga alusega? ")
    if Küs == True:
        Kd = simpledialog.askfloat("Input","Sisesta aluse dissotsiatsioonikonstant: ")
        H = sqrt(Kd)*c
    else:
        H = c
    try: 
        pOH = -1*log(H,10)
        pH = float(14 -pOH)
        return pH
    except:
        return H
    
def suurusekene(a,b):
    if a == "q" or a == "Soojusenergia":
        q3 = soojus(b)
        try:
            q = str(round(q3,4))
            q2 = q.replace("-","")
            indeks = q2.index(".")
            if q2[0:indeks].isnumeric() and q2[indeks+1:].isnumeric():
                q1 = "Soojusenergia on "+str(q)+" J."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=q1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=q).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=q3).pack()
    if a == "w" or a == "Paisumistöö":
        w3 = töö(b)
        try:
            w = str(round(w3,4))
            w2 = w.replace("-","")
            indeks = w2.index(".")
            if w2[0:indeks].isnumeric() and w2[indeks+1:].isnumeric():
                w1 = "Paisumistöö on "+str(w)+" J."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=w1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=w).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=w3).pack()
    elif a == "U" or a == "Siseenergia":
        U3 = sise(b)
        try:
            U = str(round(U3,4))
            U2 = U.replace("-","")
            indeks = U2.index(".")
            if U2[0:indeks].isnumeric() and U2[indeks+1:].isnumeric():
                U1 = "Siseenergia on "+str(U)+" J."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=U1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=U).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=U3).pack()
    elif a == "H" or a == "Entalpia":
        H3 = entalpia(b)
        try:
            H = str(round(H3,3))
            H2 = H.replace("-","")
            indeks = H2.index(".")
            if H2[0:indeks].isnumeric() and H2[indeks+1:].isnumeric():
                H1 = "Entalpia on võrdne "+H+" J."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=H1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=H).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=H3).pack()
    elif a == "S" or a == "Entroopia":
        S3 = entroopia(b)
        try:
            S = str(round(S3,4))
            S2 = S.replace("-","")
            indeks = S2.index(".")
            if S2[0:indeks].isnumeric() and S2[indeks+1:].isnumeric():
                S1 = "Entroopia on võrdne "+S+" J/K."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=S1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=S).pack()
        except:
            raknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=S3).pack()
    elif a == "G" or a == "Gibbsi vabaenergia":
        G3 = gibbs(b)
        try:
            G = str(round(G3,4))
            G2 = G.replace("-","")
            indeks = G2.index(".")
            if G2[0:indeks].isnumeric() and G2[indeks+1:].isnumeric():
                G1 = "Gibbsi energia on võrdne "+str(G)+" J."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=G1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=G).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=G3).pack()
    elif a == "F" or a == "Helmholzi vabaenergia":
        F3 = helm(b)
        try:
            F = str(round(F3,4))
            F2 = F.replace("-","")
            indeks = F2.index(".")
            if F2[0:indeks].isnumeric() and F2[indeks+1:].isnumeric():
                F1 = "Helmholzi vabaenergia on võrdne "+str(F)+" J."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=F1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=F).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=F3).pack()
    elif a == "Gr" or a == "Reaktsiooni Gibbsi energia":
        gibbsa = reaktsioonigibbs(b)
        try:
            Gr = str(round(gibbsa,4))
            Gr2 = Gr.replace("-","")
            indeks = Gr2.index(".")
            if Gr2[0:indeks].isnumeric() and Gr2[indeks+1:].isnumeric():
                Gr1 = "Gibbsi energia on võrdne "+str(Gr)+" J."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=Gr1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text="Tekkis mingi viga").pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=gibbsa).pack()
    elif a == "c" or a == "Kontsentratsioon":
        c3 = konts(b)
        try:
            c = str(round(c3,4))
            c2 = c.replace("-","")
            indeks = c2.index(".")
            if c2[0:indeks].isnumeric() and c2[indeks+1:].isnumeric():
                c1 = "Aine kontsentratsioon lahuses on "+str(c)+" M."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=c1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=c).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=c3).pack()
    elif a == "M" or a == "Molaarmass":
        Mol = str(Molaarmass(b))
        try:
            indeks = Mol.index(".")
            if Mol[0:indeks].isnumeric() and Mol[indeks+1:].isnumeric():
                M1 = "Aine molaarmass on "+Mol+" g/mol."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=M1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=Mol).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=Mol).pack()
    elif a == "n" or a == "Moolid":
        n3 = mool(b)
        try:
            n = str(round(n3,4))
            indeks = n.index(".")
            if n[0:indeks].isnumeric() and n[indeks+1:].isnumeric():
                n1 = "Moolide arv on "+str(n)+" mooli."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=n1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=n).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=n3).pack()
    elif a == "m" or a == "mass":
        m3 = mass(b)
        try:
            m = str(round(m3,4))
            indeks = m.index(".")
            if m[0:indeks].isnumeric() and m[indeks+1:].isnumeric():
                m1 = "Aine mass on "+m+" grammi."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=m1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=m).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=m3).pack()
    elif a == "V" or a == "Ruumala":
        V3 = idgaas_ruumala(b)
        try:
            V = str(round(V3,4))
            indeks = V.index(".")
            if V[0:indeks].isnumeric() and V[indeks+1:].isnumeric():
                V1 = "Gaasi ruumala on "+str(V)+" m3."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=V1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=V).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=V3).pack()
    elif a == "P" or a == "Rõhk":
        P3 = idgaas_rõhk(b)
        try:
            P = str(round(P3,4))
            indeks = P.index(".")
            if P[0:indeks].isnumeric() and P[indeks+1:].isnumeric():
                P1 = "Gaasi rõhk on "+str(P)+" Pa."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=P1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=P).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=P3).pack()
    elif a == "Happe pH":
        pH3 = happe_pH(b)
        try:
            pH = str(round(pH3,4))
            indeks = pH.index(".")
            if pH[0:indeks].isnumeric() and pH[indeks+1:].isnumeric():
                pH1 = "Lahuse pH on "+pH+"."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=pH1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=pH).pack()
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=pH3).pack()
    elif a == "Aluse pH":
        pH3 = aluse_pH(b)
        try:
            pH = str(round(pH3,4))
            indeks = pH.index(".")
            if pH[0:indeks].isnumeric() and pH[indeks+1:].isnumeric():
                pH1 = "Lahuse pH on "+pH+"."
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=pH1).pack()
            else:
                aknake = Tk()
                aknake.title("Arvutustulemus")
                ttk.Label (aknake, text=pH).pack()
            
        except:
            aknake = Tk()
            aknake.title("Arvutustulemus")
            ttk.Label (aknake, text=pH3).pack()
            
    else:
        return "Vale sisend. Proovi uuesti ning katseta valikus olevaid suurusi!"
    
    
arv = ""
t = ""
protsess = ""
arvukeseke = ""
window = Tk()
window.title("Hea")
ttk.Label (window, text="Tere! Kallis ja Hea inimene! Kell on 8 hommikul. Mida sooviksid teha?").pack()
ttk.Label(window, text="Kas oled heas või halvas tujus?").pack()
head = ttk.Entry(window, width= "50")
head.pack()
ttk.Button(window, text="Vaata, mis juhtub!", command=hea).pack()

window.mainloop()