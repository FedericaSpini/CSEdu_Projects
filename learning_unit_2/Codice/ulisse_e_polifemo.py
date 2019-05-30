def capitolo0Introduzione():
    opzioneSiNo = [""] * (2)
    
    opzioneSiNo[0] = "si"
    opzioneSiNo[1] = "no"
    dueOpzioni = [""] * (2)
    
    print("Marinaio1: Heeey, si sta svegliando!")
    print("Marinaio2: Hey capitano, ci sei? Sei con noi? rispondimi si o no.")
    while True:    #This simulates a Do Loop
        rispTesto = input()
        rispTesto = tuttominuscolo(rispTesto)
        if not(not controllaRisposta(opzioneSiNo, rispTesto, "Eh? che hai detto?")): break   #Exit loop
    if rispTesto == "si":
        print("Marinaio2: Bene, ti stai riprendendo!")
    else:
        print("Marinaio1: Capitano non è il momento di scherzare!")
    print("Marinaio3: Forza, alzati in piedi")
    print("Marinaio1: Ora ti farò tre semplici domande per vedere se ti sei ripreso con la testa capitano")
    print("Marinaio1: Da dove siamo salpati?")
    while True:    #This simulates a Do Loop
        rispTesto = input()
        rispTesto = tuttominuscolo(rispTesto)
        if not(not controllaRispostaAperta(rispTesto, "troia", "Marinaio1: Sul serio non te lo ricordi? Guarda che finchè non mi dici da dove siamo partiti non ti lascio andare.")): break   #Exit loop
    print("Bene, e invece dove siamo diretti per tornare a casa?")
    while True:    #This simulates a Do Loop
        rispTesto = input()
        rispTesto = tuttominuscolo(rispTesto)
        if not(not controllaRispostaAperta(rispTesto, "itaca", "Marinaio1: E dai su, lo so che pensi sempre a casa nostra a a tua moglie Penelope, dimmi come si chiama la nostra patria!")): break   #Exit loop
    print("Ottimo, ora l'ultima domanda, come ti chiami?")
    while True:    #This simulates a Do Loop
        rispTesto = input()
        rispTesto = tuttominuscolo(rispTesto)
        if not(not controllaRispostaAperta(rispTesto, "ulisse", "Marinaio2: Cavolo, se non ricorda il proprio nome deve essere più grave del previsto...")): break   #Exit loop
    print("Marinaio1: Vedo che finalmente ti sei ripreso capitano Ulisse! Stiamo per attraccare per fare rifornimenti")
    print("Ulisse e i suoi uomini sbarcarono e si avventurarono per quelle terre sconosciute. Dopo aver camminato un bel po' trovarono una caverna il cui interno era colmo di cibo: gigantesche forme di formaggio...")
    print("Marinaio2: Signore, entriamo e approfittiamo di questo dono degli Dei!")
    impostaDueOpzioni("0 Non mi sembra una buona idea...Potrebbe essere una trappola", "1 Ma certo uomini! Io stesso ho una gran fame", dueOpzioni)
    scelta = controllaRispostaIntero(2)
    if scelta == 0:
        print("Nonostante gli avvertimenti del loro capitano i marinai, che da mesi non vedevano cibo fresco, si precipitarono nella grotta a banchettare. Ulisse, dubbioso, li seguì.")
    else:
        print("Gioendo per la fortuna che avevano avuto Ulisse e i suoi si precipitarono nella grotta per abbuffarsi")

def capitolo1ArrivoAllaGrotta():
    vino = False
    treOpzioni = [""] * (3)
    dueOpzioni = [""] * (2)
    
    print("Ulisse e i suoi uomini sbarcarono e si avventurarono per quelle terre sconosciute. Dopo aver camminato un bel po' trovarono una caverna il cui interno era colmo di cibo: gigantesche forme di formaggio...")
    print("Marinaio2: Signore, entriamo e approfittiamo di questo dono degli Dei!")
    impostaTreOpzioni("0 Non mi sembra una buona idea...Potrebbe essere una trappola", "1 Ma certo uomini! Io stesso ho una gran fame", "2 Forse è il caso di non entrare a mani vuote visto che potrebbe esserci il proprietario dentro, voi due tornate alla nave a prendere le scorte di vino", treOpzioni)
    scelta = controllaRispostaIntero(len(treOpzioni))
    if scelta == 0:
        print("Nonostante gli avvertimenti del loro capitano i marinai, che da mesi non vedevano cibo fresco, si precipitarono nella grotta a banchettare. Ulisse, dubbioso, li seguì.")
    else:
        if scelta == 1:
            print("Gioendo per la fortuna che avevano avuto Ulisse e i suoi si precipitarono nella grotta per abbuffarsi")
        else:
            print("Marinaio2: È una grandissima idea capitano (così nemmeno rischiamo di strozzarci mentre ci abbuffiamo)")
            vino = True
            print("Dopo essere tornati alle navi e aver preso anfore di vino in abbondanza, Ulisse e i suoi uomini tornarono alla gigantesca caverna per abbuffarsi")
    
    return vino

def capitolo2ArrivaPolifemo():
    numeroMarinai = 12
    treOpzioni = [""] * (3)
    dueOpzioni = [""] * (2)
    
    print("Mentre Ulisse e tutti gli altri si godevano quel cibo fresco e delizioso, il pavimento iniziò a tremare e una figura gigantesca oscurò l'ingresso, metre entravano con lui delle pecore. Il gigante, dopo essere entrato chiuse l'ingresso con un masso gigantesco. Quando si voltò ad Ulisse e i suoi si gelò il sangue vedendo l'unico occhio sul suo volto.... Era un ciclope. Terrorizzati, Ulisse e i suoi si nascosero")
    print("Polifemo: ....(annusando l'aria e guardandosi intorno)")
    print("Improvvisamente il gigante afferrò uno degli uomini di Ulisse che non aveva fatto in tempo a nascondersi <<Voi, siete venuti qui a derubarmi perché trovavate succulento il formaggio delle mie pecore, ma non sapete quanto io trovi succulenti gli uomini>> gridò furioso e mangiò in un paio di bocconi il marinaio")
    numeroMarinai = numeroMarinai - 1
    impostaDueOpzioni("0 Ulisse agghiacciato, rimase nascosto dietro l'enorma cassapanca del ciclope", "1 Ulisse non avrebbe visto morire un altro dei suoi uomini! Prese coraggio e si fece avanti", dueOpzioni)
    scelta = controllaRispostaIntero(len(dueOpzioni))
    while scelta != 1 and numeroMarinai != 0:
        if numeroMarinai > 1:
            print("Il gigante cercò ancora e trovò un altro dei marinai... Come se fosse stato fatto di pane divorò anche lui senza pietà... solo " + str(numeroMarinai) + " marinai erano rimasti in vita")
        else:
            print("Il gigante cercò ancora e trovò un altro dei marinai... Come se fosse stato fatto di pane divorò anche lui senza pietà... solo " + str(numeroMarinai) + " marinaio era rimasto in vita")
        impostaDueOpzioni("0 Ulisse agghiacciato, rimase nascosto dietro l'enorma cassapanca del ciclope", "1 Ulisse non avrebbe visto morire un altro dei suoi uomini! Prese coraggio e si fece avanti", dueOpzioni)
        numeroMarinai = numeroMarinai - 1
        scelta = controllaRispostaIntero(len(dueOpzioni))
    
    return numeroMarinai

def capitolo3UlisseDiceIlNome():
    print("Ulisse avanzò, fuori dal suo nascondiglio, verso il ciclope...")
    print("Polifemo: E tu chi saresti, omino?")
    nomeUlisse = input()
    print("Polifemo: " + nomeUlisse + " ,che nome patetico... Credo che sarai proprio il mio prossimo spuntino! Poi mi occuperò degli altri tuoi amici ladruncoli, che ancora si nascondono nella mia grotta")
    
    return nomeUlisse

def capitolo4UlisseOffreDaBere(nomeUlisse, vino):
    finaleRaggiunto = False
    treOpzioni = [""] * (3)
    
    impostaTreOpzioni("0 Ulisse cercò di scappare: magari l'uscita della grotta non era chiusa così bene", "1 Ulisse decise di provare ad ingannare Polifemo per mandarlo sulla sua nave", "2 Ulisse decise di offrire a Polifemo il vino che avevano portato", treOpzioni)
    scelta = controllaRispostaIntero(len(treOpzioni))
    if scelta == 0:
        print("Ulisse, in preda al panico, tentò di correre verso l'uscita della caverna, ma Polifemo lo afferrò <<Hahahaha>> gridò trionfante <<Sei proprio patetico caro il mio " + nomeUlisse + "!>> Quindi lo divorò")
        finaleRaggiunto = True
    else:
        if scelta == 1:
            print("<<Perché non mi lasci tornare alla mia nave?>> gridò Ulisse, mentre il gigante lo fissava con l'unico occhio <<Potrei portarti...>>")
            print("<<CREDI FORSE CHE IL CICLOPE POLIFEMO, FIGLIO DEL GRANDE POSEIDONE, SI LASCI INGANNARE DA UNA NULLITA' COME TE?!>> Tuono il mostro facendo gelare il sangue nelle vene di Ulisse. Poi lo afferrò e lo divorò")
            finaleRaggiunto = True
        else:
            if vino == True:
                pass
            else:
                finaleRaggiunto = True
                print("Solo in quel momento Ulisse si ricordo di non essere andato a prendere il vino con i suoi uomini... Polifemo accettò la proposta, ma quando capì che il re di Itaca gli aveva mentito lo divorò.")
    
    return finaleRaggiunto

def capitolo5PolifemoBeve(nomeUlisse):
    finaleRaggiunto = False
    numeroBevute = 0
    treOpzioni = [""] * (3)
    dueOpzioni = [""] * (2)
    
    scelta = -1
    print("Polifemo accettò di buon grado la proposta di Ulisse di bere e si scolò un'intera botte d vino")
    while scelta != 0 and scelta != 2 and numeroBevute <= 5:
        numeroBevute = numeroBevute + 1
        print("Per la miseria se beveva di gusto!")
        impostaTreOpzioni("0 Ulisse tentò di fuggire dal gigante, mentre questo beveva", "1 Ulisse offrì altro vino a Polifemo", "2 Ulisse iniziò a parlare con il ciclope", treOpzioni)
        scelta = controllaRispostaIntero(len(treOpzioni))
    if scelta == 1:
        print("Alla fine dell'ennesima bevuta, il ciclope crollò a terra, profondamente addormentato")
    else:
        if scelta == 0:
            finaleRaggiunto = True
            print("Tentando di approfittare della distrazione di Polifemo Ulisse iniziò ad aggirarsi per la caverna in cerca di una via di fuga, ma il gigante, non ancora ubriaco, lo vide <<CERCARVI DI FREGARMI!>> tuonò. Quindi afferrò l'uomo e lo divorò")
        else:
            finaleRaggiunto = True
            capitolo6Spinoff()
    
    return finaleRaggiunto

def capitolo6Spinoff():
    treOpzioni = [""] * (3)
    
    impostaTreOpzioni("0 Ma non pensi di essere sprecato per passare la tua vita a badare alle pecore?", "1 In realtà, così da vicino, sembri uno in gamba", "2 Secondo me dovresti smetterla di mangiare gli uomini", treOpzioni)
    scelta = controllaRispostaIntero(len(treOpzioni))
    print("Polifemo: (sob!) Io vorrei viaggiare e vedere il mondo... Ma poi gli uomini mi additano come un mostro e allora ho voglia di fargliela pagare e me li mangio")
    impostaTreOpzioni("0 Non dire così, a me non sembri un mostro", "1 E grazie che ti trattano come un mostro! Mangi la gente appena la vedi", "2 Dovresti pensare a cambiare vita anzi che piangerti addosso", treOpzioni)
    scelta = controllaRispostaIntero(len(treOpzioni))

def capitolo7IlPiano(numeroMarinai, nomeUlisse):
    finaleRaggiunto = False
    treOpzioni = [""] * (3)
    
    print("Poiché ormai il ciclope russava sonoramente, Ulisse e gli " + str(numeroMarinai) + " rimasti uscirono allo scoperto.")
    print("Ulisse aveva un piano e sottovoce lo spiegò ai marinai: c'era un lungo palo nella grotta che avrebbero preso e intagliato in modo da renderlo appuntito. Quindi avrebbero arroventato la punta sul fuoco che ancora scoppiettava nella grotta e infine l'avrebbero usato per accecare Polifemo")
    if numeroMarinai > 3:
        print("Determinati ad uscire da lì i greci seguirono il piano del loro capo: il vino che Polifemo aveva bevuto era terribilmente forte se non veniva diluito con dell'acqua, per cui il gigante non si accorse di nulla.")
        print("Polifemo urlò di dolore appena il palo arroventato gli venne spinto nell'unico occhio e coprendosi il viso si alzò, tastando per tutta la caverna furibondo")
    else:
        finaleRaggiunto = True
        print("Purtroppo troppi tra loro erano stati uccisi da Polifemo e non riuscirono a sollevare l'enorme palo per affilarne la punta... Il gigante si svegliò, li tenne chiusi lì dentro e li mangio uno ad uno nei giorni successivi.")
    
    return finaleRaggiunto

def controllaRisposta(opzioni, opzione, fraseErrore):
    controllo = False
    for i in range(0, len(opzioni) - 1 + 1, 1):
        if opzioni[i] == opzione:
            controllo = True
    if controllo:
        pass
    else:
        print(fraseErrore)
    
    return controllo

def controllaRispostaAperta(rispData, rispGiusta, fraseErrore):
    controllo = False
    if rispData == rispGiusta:
        controllo = True
    else:
        print(fraseErrore)
    
    return controllo

def controllaRispostaIntero(numeroOpzioni):
    opzioneSelezionata = int(input())
    while opzioneSelezionata < 0 or opzioneSelezionata >= numeroOpzioni:
        print("Opzione selezionata non valida")
        opzioneSelezionata = int(input())
    
    return opzioneSelezionata

def impostaDueOpzioni(primaOpzione, secondaOpzione, dueOpzioni):
    dueOpzioni[0] = primaOpzione
    dueOpzioni[1] = secondaOpzione
    for numeroOpzione in range(0, len(dueOpzioni) - 1 + 1, 1):
        print(dueOpzioni[numeroOpzione])

def impostaTreOpzioni(primaOpzione, secondaOpzione, terzaOpzione, treOpzioni):
    treOpzioni[0] = primaOpzione
    treOpzioni[1] = secondaOpzione
    treOpzioni[2] = terzaOpzione
    for numeroOpzione in range(0, len(treOpzioni) - 1 + 1, 1):
        print(treOpzioni[numeroOpzione])

def tuttominuscolo(stringa):
    minstringa = ""
    for i in range(0, len(stringa) - 1 + 1, 1):
        carattereCorrente = stringa[i]
        if ord(carattereCorrente) < 97:
            nuovoCarattere = 0
            nuovoCarattere = ord(carattereCorrente) + 32
            carattereCorrente = chr(nuovoCarattere)
        minstringa = minstringa + carattereCorrente
    
    return minstringa

# Main
dueOpzioni = [""] * (2)

vino = False
finaleRaggiunto = False

# L'introduzione è un pezzo della storia messo in una funzione a parte: non varia il corso della storia, ma presenta comunque delle interazioni con il giocatore.
# "Arrivo alla grotta che imposta la variabile vino a true o false a seconda delle scelte effettuate"
vino = capitolo1ArrivoAllaGrotta()

# Arrivo di Polifemo, che in questo capitolo mangia un certo numero di marinai... se i marinai rimasti saranno troppo pochi, non saranno in grado di attuare il piano di Ulisse
numeroMarinai = capitolo2ArrivaPolifemo()
if numeroMarinai == 0:
    print("Ulisse disperato per aver visto morire tutti i suoi compagni urlò di disperazione. Polifemo lo trovò per questo e trionfante, mangiò anche lui")
    finaleRaggiunto = True
if not finaleRaggiunto:
    
    # "Se non sono morti tutti i marinai, ma Ulisse ha deciso di intervenire, allora interagisce con polifemo: nel capitolo3 gli dice come si chiama, nel capitolo4 gli offre da bere e se non aveva preso il vino sarà un problema"
    nomeUlisse = capitolo3UlisseDiceIlNome()
    finaleRaggiunto = capitolo4UlisseOffreDaBere(nomeUlisse, vino)
    if finaleRaggiunto == False:
        finaleRaggiunto = capitolo5PolifemoBeve(nomeUlisse)
        if finaleRaggiunto == False:
            
            # Il capitolo 7 è quello in cui, se è rimasto un numero sufficiente di uomini, Ulisse e i suoi accecano Polifemo
            finaleRaggiunto = capitolo7IlPiano(numeroMarinai, nomeUlisse)
            if finaleRaggiunto == False:
                pass
            else:
                
                # E' già stato raggiunto un finale, non fare niente
        else:
            
            # E' già stato raggiunto un finale, non fare niente
    else:
        
        # E' già stato raggiunto un finale, non fare niente
else:
    
    # E' già stato raggiunto un finale, non fare niente
