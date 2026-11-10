# -*- coding: utf-8 -*-
# Italian translation of the FAQ and blog of both sites (source: en.py). Tokens in answers/articles: {ts} {pc} {store} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacy", more="Continua a leggere",
    cta_store="📱 Scarica TripSweep su App Store",
    cta_play="🤖 Scarica TripSweep su Google Play",
    cta_mac="💻 Scarica PhotoCull per Mac", cta_win="🪟 Scarica PhotoCull per Windows",
    cross_label={"tripsweep": "App desktop", "photocull": "App mobile"},
    twin_android="Usi un telefono Android? Leggi la guida per Android:",
    twin_iphone="Usi un iPhone? Leggi la guida per iPhone:",
    index={
        "tripsweep": dict(
            title="Blog TripSweep: spazio su iPhone e foto duplicate",
            desc="Guide pratiche per liberare spazio su iPhone, eliminare foto duplicate e simili e riordinare i vecchi viaggi, senza iCloud e senza inviare le tue foto.",
            h1="Guide per fare ordine nelle foto del tuo iPhone",
            intro="Guide brevi e pratiche per liberare spazio su iPhone, eliminare i duplicati e tenere solo gli scatti migliori."),
        "photocull": dict(
            title="Blog PhotoCull: ordinare le foto su Mac o PC",
            desc="Guide per ordinare migliaia di foto più in fretta su un grande schermo, confrontare scatti simili e liberare spazio su iPhone o Android da un Mac o un PC.",
            h1="Guide per ordinare le tue foto dal computer",
            intro="Perché un grande schermo cambia la velocità con cui ordini le foto e come sfruttarlo per liberare spazio su iPhone o su un telefono Android."),
    },
)

FAQ_TRIPSWEEP_EXTRA = [
    ("Qual è la differenza tra foto duplicate e foto simili?",
     "I duplicati sono copie identiche dello stesso file. Le foto simili sono scatti diversi della stessa scena: una raffica, cinque tentativi dello stesso tramonto, due selfie quasi uguali. I duplicati sono facili da trovare; le foto simili sono dove si nasconde la maggior parte dello spazio sprecato, e TripSweep raggruppa entrambi così puoi tenerne una e eliminare le altre."),
    ("Come sceglie TripSweep la foto migliore di un gruppo?",
     "Valuta nitidezza, punteggio estetico di Apple e volti, poi propone uno scatto per gruppo. Il suggerimento è solo un punto di partenza: puoi tenere un'altra foto, tenerne diverse o saltare il gruppo. L'analisi avviene sul tuo iPhone con il framework Vision di Apple."),
    ("Cosa trova la scheda Pulizia?",
     "Copie identiche, foto simili, foto sfocate, screenshot e video pesanti, ciascuno nella propria categoria con lo spazio che occupa. Parti dalla categoria che libera più spazio e la sistemi in pochi tocchi."),
    ("TripSweep mi suggerirà di eliminare le mie foto preferite?",
     "No. Le foto che hai contrassegnato come preferite non vengono mai proposte per l'eliminazione e non viene eliminato nulla finché non confermi."),
    ("TripSweep funziona con le foto senza posizione GPS?",
     "Sì. Le foto senza posizione vengono raggruppate per evento e per mese invece che per viaggio, quindi anche screenshot, immagini salvate e foto scattate con i servizi di localizzazione disattivati vengono ordinati."),
    ("Posso nascondere casa e ufficio dai miei viaggi?",
     "Sì. Aggiungi casa, lavoro o qualsiasi luogo che frequenti ogni giorno come luogo escluso: così la vita quotidiana non compare come viaggio e i tuoi veri viaggi risaltano. Con Pro i luoghi personalizzati sono illimitati."),
    ("Posso fare un backup o condividere un viaggio prima di eliminarlo?",
     "Sì. Puoi esportare un intero viaggio sul Mac o nell'app File, oppure condividerlo con le persone che c'erano, e poi eliminarlo dal tuo iPhone quando è al sicuro altrove."),
    ("Serve una connessione a internet o un account?",
     "No. TripSweep non richiede alcun account e funziona offline. I nomi dei luoghi vengono riconosciuti sul tuo iPhone e nessuna foto, video o posizione viene mai inviata a un server. Possono essere inviate solo statistiche d'uso anonime, disattivabili. Puoi disattivarle nella scheda Info."),
    ("Eliminare con TripSweep elimina le foto anche da iCloud?",
     "Se Foto di iCloud è attivo, eliminare una foto sul tuo iPhone la rimuove da tutti i tuoi dispositivi, perché è così che funziona Foto di iCloud. TripSweep elimina passando da «Eliminati di recente», quindi hai 30 giorni per cambiare idea, e lo spazio su iCloud si libera quando svuoti quell'album."),
    ("Posso controllare le foto del mio iPhone su un grande schermo invece che sul telefono?",
     "Sì. <a href=\"{pc}\">PhotoCull</a> è l'app desktop gratuita per Mac e Windows: mostra il rullino del tuo iPhone raggruppato per viaggio, confronta le foto simili fianco a fianco e ti permette di selezionare centinaia di foto con pochi clic. <a href=\"{pc}\">Scopri di più su PhotoCull</a>."),
    ("Posso eliminare le foto in blocco dal computer invece di toccare il telefono?",
     "Sì, con <a href=\"{pc}\">PhotoCull</a> su un Mac o un PC Windows. Selezioni le foto sul grande schermo e l'eliminazione viene applicata sul tuo iPhone da TripSweep tramite «Eliminati di recente». La versione gratuita consente 6 foto al giorno dal Mac (vedi i piani nella pagina di TripSweep), Pro 15, e Pro + Desktop elimina il limite."),
    ("Quali iPhone e versioni di iOS supporta TripSweep?",
     "TripSweep richiede iOS 18 o successivo. L'analisi delle foto simili usa il framework Vision di Apple ed è più veloce sugli iPhone recenti, ma funziona su tutti i modelli supportati. Su Android richiede Android 11 o successivo ed è disponibile su <a href=\"{play}\">Google Play</a>."),
]

FAQ_PHOTOCULL = dict(
    title="FAQ PhotoCull: ordinare ed eliminare foto da un Mac o PC Windows",
    desc="Come ordinare migliaia di foto dal computer, confrontare scatti simili, liberare spazio su iPhone o Android da Mac o PC: risposte su PhotoCull.",
    nav_home="PhotoCull", nav_desktop="App mobile",
    h1="Domande e risposte",
    intro="Come ordinare le tue foto più in fretta dal computer, liberare spazio su iPhone o su un telefono Android da un Mac o PC, e cosa fa (e non fa mai) PhotoCull con le tue foto.",
    qa=[
        ("Come ordino le foto dell'iPhone dal computer, Mac o PC?",
         "Collega l'iPhone al computer con un cavo USB, sbloccalo e tocca Autorizza, poi apri <a href=\"{pc}\">PhotoCull</a>: raggruppa il rullino per viaggio, confronta gli scatti simili fianco a fianco e seleziona centinaia di foto in pochi clic. Guide passo passo: <a href=\"{post:sort-iphone-photos-on-mac}\">sul Mac</a> e <a href=\"{post:sort-iphone-photos-on-pc}\">su un PC Windows</a>."),
        ("Perché ordinare le foto sul computer invece che sull'iPhone?",
         "Un grande schermo mostra più foto contemporaneamente, mouse e tastiera ne selezionano centinaia in pochi secondi e confrontare gli scatti fianco a fianco è più facile che passare avanti e indietro. Ordinare un rullino di migliaia di foto richiede diverse sessioni sul telefono e una sessione molto più breve su un Mac o PC."),
        ("Che cos'è PhotoCull?",
         "PhotoCull è un'app desktop gratuita per Mac e Windows che raggruppa le tue foto per viaggio, confronta gli scatti simili fianco a fianco ed elimina in blocco ciò che non vale la pena tenere. Legge il rullino del tuo iPhone via USB, o qualsiasi cartella di foto sul tuo computer, e funziona 100% sul dispositivo."),
        ("Come ordino rapidamente migliaia di foto?",
         "Apri la vista Viaggi: la tua libreria è raggruppata per viaggio con lo spazio occupato da ciascuno, così parti dal più pesante. All'interno di un viaggio, seleziona le foto in blocco, confronta quelle simili fianco a fianco e tieni lo scatto migliore di ogni gruppo. Gli stessi filtri dell'app iOS (viaggi di un solo giorno, luoghi esclusi come casa o lavoro, dimensione) restringono la ricerca."),
        ("Come libero spazio su iPhone da un Mac o PC?",
         "Collega il tuo iPhone via USB, apri PhotoCull, seleziona i viaggi e le foto che non ti servono più e conferma. L'eliminazione viene applicata sull'iPhone dall'<a href=\"{ts}\">app TripSweep</a> gratuita tramite «Eliminati di recente», quindi libera spazio non appena svuoti quell'album."),
        ("Posso eliminare le foto dal mio iPhone direttamente dal computer?",
         "Sì, da un Mac o da un PC Windows, con l'<a href=\"{ts}\">app TripSweep</a> installata sull'iPhone. Da un Mac, la versione gratuita consente 6 foto al giorno, Pro 15 e Pro + Desktop elimina il limite."),
        ("Eliminare da PhotoCull è definitivo?",
         "No. Le eliminazioni sull'iPhone passano sempre dall'album «Eliminati di recente» dell'app Foto, dove le foto restano per 30 giorni e possono essere ripristinate. PhotoCull non esegue mai un'eliminazione definitiva immediata."),
        ("Come collego il mio iPhone a PhotoCull?",
         "Usa un cavo USB, sblocca l'iPhone e tocca «Autorizza» quando richiesto. Su Mac non serve altro. Su Windows, installa la app gratuita Apple Devices dal Microsoft Store, che fornisce il driver con cui PhotoCull può leggere l'iPhone."),
        ("Posso ordinare le foto di un telefono Android dal Mac o dal PC?",
         "Sì. PhotoCull si collega a un telefono Android via Wi-Fi su Mac o PC Windows, oppure via USB su Windows. Trovi la stessa vista Viaggi, lo stesso confronto fianco a fianco e la stessa eliminazione in blocco dell'iPhone. Sul telefono serve l'<a href=\"{play}\">app TripSweep</a> gratuita (Android 11 o successivo), aperta sulla scheda Eliminazione."),
        ("Come collego il mio telefono Android via Wi-Fi?",
         "Metti telefono e computer sulla stessa rete Wi-Fi e apri la scheda Eliminazione di TripSweep sul telefono. In PhotoCull, clicca «Telefono Android» e scegli il tuo telefono, poi autorizza il computer dal telefono: lo stesso codice a 4 cifre compare su entrambi gli schermi. Lo fai una sola volta; la volta successiva si ricollega da solo. <a href=\"{post:sort-android-photos-on-mac}\">Guida passo passo per Mac</a>."),
        ("Perché il mio Mac non vede il telefono Android via USB?",
         "macOS non supporta in modo nativo il modo in cui i telefoni Android condividono i file via USB (MTP), quindi in genere un Mac non li vede. Usa invece la connessione Wi-Fi: funziona su qualsiasi Mac, senza installare driver. Su Windows funzionano sia l'USB sia il Wi-Fi."),
        ("La connessione Wi-Fi al mio telefono è sicura?",
         "Sì. Telefono e computer comunicano solo sulla tua rete locale, con una connessione cifrata, e solo dopo che hai autorizzato quel computer dal telefono con un codice corrispondente. Nulla passa da internet e puoi revocare un computer da TripSweep in qualsiasi momento."),
        ("Cosa succede alle foto che elimino su un telefono Android?",
         "Confermi l'eliminazione sul telefono, in TripSweep, e le foto finiscono nel cestino del telefono, dove restano 30 giorni e possono essere ripristinate. PhotoCull non elimina mai nulla in modo definitivo da solo."),
        ("Mi serve l'app iOS TripSweep?",
         "Non per sfogliare, confrontare e ordinare un iPhone. Ti serve solo per eliminare le foto dall'iPhone, perché l'eliminazione viene applicata sul telefono. Un telefono Android richiede l'app TripSweep per Android anche solo per collegarsi. Le cartelle sul tuo computer si possono ordinare senza nessuna delle due."),
        ("Come trovo le foto duplicate in una cartella del Mac o del PC?",
         "Apri la cartella in PhotoCull («Apri cartella», oppure trascinala sulla finestra). L'app esplora le sottocartelle, confronta il contenuto delle foto e applica lo stesso badge «≈ N» a copie esatte, raffiche e scatti quasi identici. Tieni il migliore di ogni gruppo e sposta il resto nel Cestino. Guide: <a href=\"{post:find-duplicate-photos-on-mac}\">sul Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">su Windows</a>."),
        ("Posso usare PhotoCull su foto salvate sul mio computer, non su un iPhone?",
         "Sì. Apri una cartella qualsiasi: PhotoCull trova le foto simili al suo interno, mostra i badge su quelle simili e ti permette di confrontare ed eliminare senza limite giornaliero."),
        ("Come trova PhotoCull le foto simili?",
         "Confronta il contenuto delle tue foto, non i nomi dei file, quindi raffiche, scatti quasi identici e la stessa scena fotografata più volte finiscono nello stesso gruppo. Puoi confrontare fino a 6 foto fianco a fianco e tenere la più nitida e meglio inquadrata."),
        ("Come confronto le foto simili fianco a fianco?",
         "Seleziona un gruppo di foto simili e apri il confronto: fino a 6 foto vengono mostrate alla stessa dimensione, così puoi valutare messa a fuoco, espressioni e inquadratura. Tieni la migliore e seleziona le altre."),
        ("PhotoCull funziona su Windows?",
         "Sì: Windows 10 e 11 (64 bit). Per leggere un iPhone serve la app gratuita Apple Devices dal Microsoft Store. L'app non è ancora firmata digitalmente, quindi Windows SmartScreen può mostrare un avviso al primo avvio: scegli «Ulteriori informazioni» e poi «Esegui comunque»."),
        ("Quali Mac supporta PhotoCull?",
         "Mac con Apple Silicon e macOS 11 o successivo. L'app è firmata e notarizzata da Apple, quindi si apre senza avvisi di sicurezza."),
        ("PhotoCull è gratuito? C'è un abbonamento?",
         "PhotoCull si scarica gratis e non ci sono abbonamenti. Sfogliare, confrontare e ordinare è gratuito, e ordinare una cartella sul computer non ha mai limiti. L'eliminazione di foto da un iPhone tramite Mac è limitata a 6 al giorno gratis, 15 con TripSweep Pro e illimitata con Pro + Desktop (acquisti singoli effettuati nell'app iOS TripSweep)."),
        ("PhotoCull invia le mie foto a un server o al cloud?",
         "No. PhotoCull funziona 100% sul dispositivo: nessun account, nessun cloud, nessuna foto, video o posizione viene mai inviata altrove. Il riconoscimento dei luoghi e il rilevamento delle foto simili avvengono sul tuo computer. Possono essere inviate solo statistiche d'uso anonime, disattivabili."),
        ("PhotoCull modifica le mie foto originali?",
         "No. PhotoCull legge le tue foto solo per mostrarle e confrontarle. L'unica modifica che fa è l'eliminazione che confermi tu."),
        ("Come nascondo casa e ufficio dalla vista dei viaggi?",
         "Aggiungili come luoghi esclusi: la vita quotidiana smette di comparire come viaggio e i tuoi veri viaggi risaltano. L'impostazione è la stessa dell'app iOS."),
        ("Posso fare ordine dopo una vacanza dal computer?",
         "Sì, è l'uso tipico. Dopo un viaggio, collega l'iPhone, apri quel viaggio in PhotoCull, confronta gli scatti simili, tieni il migliore di ciascuno ed elimina il resto. L'<a href=\"{ts}\">app TripSweep</a> può anche esportare l'intero viaggio prima che tu elimini qualsiasi cosa."),
        ("Posso usare PhotoCull per preparare un album fotografico o un backup?",
         "PhotoCull ti aiuta a decidere cosa vale la pena tenere: ordina il viaggio, elimina i duplicati e gli scatti quasi identici, poi fai il backup o condividi ciò che resta. L'<a href=\"{ts}\">app TripSweep</a> può esportare o condividere un intero viaggio."),
    ],
    footer_copy="© 2026 PhotoCull. Sviluppato da Jeffrey Brignoli.",
    footer_privacy="Privacy", footer_kofi="Ko-fi",
)

BLOG = {
"tripsweep": [
dict(slug="free-up-iphone-storage",
     title="Come liberare spazio su iPhone senza iCloud: guida pratica",
     desc="Dove va davvero lo spazio del tuo iPhone e i modi più rapidi per liberare gigabyte di foto e video senza pagare altro spazio iCloud.",
     h1="Come liberare spazio su iPhone senza pagare per iCloud",
     body="""      <p>«Memoria iPhone piena» significa quasi sempre una cosa sola: l'app Foto. Foto e video sono di solito la voce più grande in Impostazioni → Generali → Spazio iPhone, e gran parte di quello spazio è spreco che puoi eliminare senza perdere nemmeno un ricordo.</p>

      <h2>1. Parti da ciò che pesa di più</h2>
      <p>I video pesanti sono la vittoria più rapida: pochi minuti di video 4K occupano quanto centinaia di foto. Ordina i video per dimensione, guarda i primi secondi ed elimina quelli che non riaprirai mai. Le registrazioni dello schermo e i video ricevuti dalle app di messaggistica sono tra i principali colpevoli.</p>

      <h2>2. Elimina le foto simili, non solo i duplicati</h2>
      <p>L'app Foto sa trovare i duplicati esatti, ma il vero spreco sono gli scatti quasi identici: la raffica di dieci fotogrammi, cinque tentativi della stessa foto di gruppo, tre selfie di fila. Tieni il migliore di ogni gruppo ed elimina il resto. È qui che la maggior parte delle persone recupera più spazio, ed è la parte più difficile da fare a mano.</p>

      <h2>3. Elimina screenshot e foto sfocate</h2>
      <p>Gli screenshot si accumulano senza che te ne accorga: biglietti, mappe, conversazioni che non ti servono più. Lo stesso vale per le foto sfocate e gli scatti accidentali. Raramente meritano di restare e si controllano in fretta tutti insieme.</p>

      <h2>4. Svuota «Eliminati di recente»</h2>
      <p>Le foto eliminate restano nell'album «Eliminati di recente» per 30 giorni e continuano a occupare spazio. Quando sei sicuro delle tue scelte, svuotalo per recuperare davvero la memoria.</p>

      <h2>5. Fai ordine nei vecchi viaggi, uno alla volta</h2>
      <p>Le vecchie vacanze sono il blocco di foto più grande che non guardi mai. Procedere viaggio per viaggio è più facile che scorrere una libreria di migliaia di foto: scegli il viaggio più pesante, tieni i momenti migliori, elimina il resto.</p>

      <h2>Come TripSweep rende tutto più veloce</h2>
      <p><a href="{ts}">TripSweep</a> esegue questi passaggi per te sull'iPhone. La sua scheda Pulizia elenca copie identiche, foto simili, foto sfocate, screenshot e video pesanti, ciascuno con lo spazio che occupa. I tuoi viaggi sono raggruppati per luogo e data e ordinati per dimensione, e un pulsante «Tieni 1 per gruppo» gestisce un'intera categoria con un solo tocco. I preferiti non vengono mai proposti per l'eliminazione, le eliminazioni passano da «Eliminati di recente» e nulla lascia mai il tuo telefono: nessun account, nessun cloud. Possono essere inviate solo statistiche d'uso anonime, disattivabili.</p>
      <p>Se preferisci un grande schermo, <a href="{pc}">PhotoCull</a> fa lo stesso lavoro di selezione su un Mac o PC Windows.</p>

      <h2>Mi serve iCloud?</h2>
      <p>iCloud è un buon backup, ma non è uno strumento di pulizia: conserva tutto, compresi i duplicati. Fare ordine prima significa aver bisogno di meno spazio, ovunque si trovi.</p>"""),
dict(slug="delete-duplicate-photos-iphone",
     title="Come eliminare foto duplicate e simili su iPhone",
     desc="Trova duplicati esatti, raffiche e scatti quasi identici sul tuo iPhone, tieni il migliore ed elimina il resto in sicurezza.",
     h1="Come eliminare le foto duplicate e simili dal tuo iPhone",
     body="""      <p>I duplicati consumano silenziosamente la memoria dell'iPhone. Alcuni sono copie esatte, ma la maggior parte sono scatti quasi identici dello stesso momento. Ecco come trovarli entrambi e fare pulizia in sicurezza.</p>

      <h2>Duplicati e foto simili non sono la stessa cosa</h2>
      <p>Un duplicato esatto è lo stesso file salvato due volte, per esempio dopo un'importazione o un download. Una foto simile è uno scatto diverso della stessa scena: una raffica, qualche tentativo di foto di gruppo, un selfie ripetuto finché non eri soddisfatto. I duplicati esatti sono facili da individuare; le foto simili sono più comuni e occupano molto più spazio.</p>

      <h2>Il metodo integrato</h2>
      <p>Le versioni recenti di iOS includono un album Duplicati nell'app Foto (sotto Utility). Unisce le copie esatte ed è un buon primo passaggio. Non raggruppa le foto simili, quindi raffiche e scatti quasi identici restano nella tua libreria.</p>

      <h2>Eliminare le foto simili</h2>
      <p>Per gli scatti simili devi confrontare e scegliere. Apri il gruppo, guarda nitidezza, espressioni e inquadratura, tieni la foto migliore ed elimina le altre. Farlo a mano su migliaia di foto è lento, ed è per questo che la maggior parte delle persone non finisce mai.</p>

      <h2>Fai prima con TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> trova copie identiche e foto simili in tutta la tua libreria e mostra ogni gruppo fianco a fianco senza ritagli. Suggerisce lo scatto migliore in base a nitidezza, punteggio estetico di Apple e volti, e il pulsante «Tieni 1 per gruppo» della scheda Pulizia sistema un'intera categoria con un tocco. I tuoi preferiti non vengono mai proposti per l'eliminazione.</p>

      <h2>Elimina in sicurezza</h2>
      <ul>
        <li>Elimina tramite l'app Foto: le foto eliminate vanno in «Eliminati di recente» per 30 giorni, quindi un errore è rimediabile.</li>
        <li>Tieni i preferiti: contrassegna le foto che ami prima di fare pulizia.</li>
        <li>Controlla Foto di iCloud: se è attivo, eliminare sull'iPhone elimina ovunque.</li>
        <li>Svuota «Eliminati di recente» alla fine per recuperare lo spazio.</li>
      </ul>

      <h2>Preferisci un grande schermo?</h2>
      <p>Con <a href="{pc}">PhotoCull</a> su un Mac o PC Windows puoi confrontare fino a sei foto simili fianco a fianco e selezionarne centinaia con pochi clic.</p>"""),
dict(slug="clean-up-vacation-photos",
     title="Come riordinare le foto delle vacanze e tenere le migliori",
     desc="Trasforma mille foto di vacanza in un album da conservare: raggruppa per viaggio, elimina gli scatti quasi identici, tieni i momenti migliori.",
     h1="Come fare ordine nelle vecchie foto delle vacanze e tenere le migliori",
     body="""      <p>Un viaggio di una settimana produce facilmente mille foto e video, e la maggior parte sono quasi copie di pochi bei scatti. Ordinarli a viaggio appena concluso è facile; farlo un anno dopo è una seccatura. Questo metodo funziona in entrambi i casi.</p>

      <h2>1. Lavora viaggio per viaggio</h2>
      <p>Una libreria di 20.000 foto è schiacciante; un viaggio di 800 foto no. Raggruppa le foto per viaggio usando data e posizione e affronta un viaggio alla volta, partendo dal più pesante.</p>

      <h2>2. Elimina prima gli scatti quasi identici</h2>
      <p>Gran parte di un viaggio sono variazioni della stessa scena. Per ogni gruppo, tieni la foto più nitida con le espressioni migliori ed elimina le altre. Già solo questo spesso dimezza le dimensioni di un viaggio.</p>

      <h2>3. Controlla il resto: screenshot, foto sfocate, video pesanti</h2>
      <p>Biglietti, mappe, foto accidentali e lunghi video che non riguardi mai sono facili da eliminare quando sono elencati tutti insieme.</p>

      <h2>4. Fai un backup o condividi prima di eliminare</h2>
      <p>Esporta le foto da conservare sul tuo computer o condividile con gli amici che c'erano. Solo dopo elimina il viaggio dal telefono. Le eliminazioni vanno in «Eliminati di recente», che ti dà 30 giorni per cambiare idea.</p>

      <h2>5. Foto senza GPS</h2>
      <p>Le foto scattate con la posizione disattivata o salvate dai messaggi non hanno un luogo. Raggruppale invece per evento e per mese, così vengono ordinate anche loro.</p>

      <h2>Come ti aiuta TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> raggruppa le tue foto e i tuoi video per viaggio (o per evento e mese quando manca il GPS), mostra quanti gigabyte di foto simili contiene ogni viaggio, suggerisce lo scatto migliore di ogni gruppo ed esporta o condivide un intero viaggio. Puoi escludere casa e lavoro così la vita quotidiana non sembra un viaggio. Tutto avviene sul tuo iPhone, offline.</p>
      <p>Per fare lo stesso su un grande schermo, <a href="{pc}">PhotoCull</a> mostra i viaggi del tuo iPhone su un Mac o PC Windows.</p>"""),
dict(slug="free-up-android-storage",
     title="Come liberare spazio su Android senza Google One",
     desc="Dove va davvero lo spazio del tuo Android e i modi più rapidi per liberare gigabyte di foto e video senza pagare altro spazio nel cloud.",
     h1="Come liberare spazio su Android senza pagare per Google One",
     body="""      <p>«Memoria piena» su un telefono Android significa quasi sempre foto e video. Lo vedi chiaramente in Impostazioni → Archiviazione, e gran parte di quello spazio sono scatti che non riguarderai mai. Ecco come recuperarlo senza comprare altro spazio nel cloud.</p>

      <h2>1. Parti da ciò che pesa di più</h2>
      <p>I video lunghi sono la vittoria più rapida: pochi minuti di 4K occupano quanto centinaia di foto. Ordinali per dimensione, guarda i primi secondi ed elimina quelli che non riaprirai mai.</p>

      <h2>2. Elimina le foto simili, non solo i duplicati</h2>
      <p>Le app di pulizia trovano le copie esatte, ma il vero spreco sono gli scatti quasi identici: raffiche, cinque tentativi della stessa foto di gruppo, tre selfie di fila. Tieni il migliore di ogni gruppo ed elimina il resto.</p>

      <h2>3. Elimina screenshot e foto sfocate</h2>
      <p>Gli screenshot di biglietti, mappe e conversazioni si accumulano senza che te ne accorga, e lo stesso vale per gli scatti accidentali o sfocati. Si controllano in fretta tutti insieme.</p>

      <h2>4. Svuota il cestino</h2>
      <p>Le foto eliminate di solito restano 30 giorni nel cestino e continuano a occupare spazio. Quando sei sicuro delle tue scelte, svuotalo per recuperare davvero la memoria.</p>

      <h2>5. Fai ordine nei vecchi viaggi, uno alla volta</h2>
      <p>Le vecchie vacanze sono il blocco di foto più grande che non guardi mai. Procedere viaggio per viaggio è più facile che scorrere migliaia di foto: scegli il viaggio più pesante, tieni i momenti migliori, elimina il resto.</p>

      <h2>Come TripSweep rende tutto più veloce</h2>
      <p><a href="{ts}">TripSweep</a> esegue questi passaggi per te sul telefono. La sua scheda Pulizia elenca copie identiche, foto simili, foto sfocate, screenshot e video pesanti, ciascuno con lo spazio che occupa, e i tuoi viaggi sono raggruppati automaticamente. È gratuita su <a href="{play}">Google Play</a> (Android 11 o successivo) e funziona 100% sul telefono.</p>
      <p>Se preferisci un grande schermo, <a href="{pc}">PhotoCull</a> fa lo stesso lavoro di selezione su un Mac o PC Windows, collegato via Wi-Fi.</p>

      <h2>Mi serve Google One?</h2>
      <p>Lo spazio nel cloud è un buon backup, ma non è uno strumento di pulizia: conserva tutto, compresi i duplicati. Fare ordine prima significa aver bisogno di meno spazio, ovunque si trovi.</p>"""),
dict(slug="delete-duplicate-photos-android",
     title="Come eliminare foto duplicate e simili su Android",
     desc="Trova duplicati esatti, raffiche e scatti quasi identici sul tuo Android, tieni il migliore ed elimina il resto in sicurezza.",
     h1="Come eliminare le foto duplicate e simili sul tuo telefono Android",
     body="""      <p>I duplicati divorano in silenzio la memoria di un telefono Android. Alcuni sono copie esatte, ma la maggior parte sono scatti quasi identici dello stesso momento. Ecco come trovare entrambi e fare ordine in sicurezza.</p>

      <h2>Duplicati e foto simili non sono la stessa cosa</h2>
      <p>Un duplicato esatto è lo stesso file salvato due volte, per esempio dopo un download, un'app di messaggistica o un ripristino. Una foto simile è uno scatto diverso della stessa scena: una raffica, qualche tentativo di foto di gruppo, un selfie ripetuto finché non veniva bene. I gestori di file trovano il primo tipo; il secondo occupa molto più spazio.</p>

      <h2>Cosa offre Android</h2>
      <p>Le app di gestione file sanno elencare i file duplicati esatti e la galleria mostra le raffiche. Nessuna delle due confronta per te gli scatti quasi identici né ti aiuta a scegliere il migliore, così finisci a passare da una foto all'altra una per una.</p>

      <h2>Un metodo più rapido</h2>
      <p><strong>1. Raggruppa per scena.</strong> <a href="{ts}">TripSweep</a> confronta il contenuto delle tue foto, non i loro nomi, e raggruppa gli scatti della stessa scena: una raffica di dieci diventa una sola decisione.</p>
      <p><strong>2. Tieni il migliore.</strong> Propone uno scatto per gruppo; puoi tenerne un altro, tenerne diversi o saltare il gruppo.</p>
      <p><strong>3. Elimina in sicurezza.</strong> Le foto eliminate vanno nel cestino del telefono per 30 giorni, così puoi rimediare a una scelta sbagliata.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto avviene sul telefono: nessun account, nessun invio. TripSweep è gratuita su <a href="{play}">Google Play</a> (Android 11 o successivo).</li>
        <li>Per un intero rullino, confrontare su un grande schermo con <a href="{pc}">PhotoCull</a> su un Mac o PC è ancora più veloce.</li>
      </ul>"""),
],
"photocull": [
dict(slug="sort-iphone-photos-on-mac",
     title="Come ordinare le foto dell'iPhone sul Mac",
     desc="Ordina migliaia di foto dell'iPhone sul Mac: cosa fanno Foto e Acquisizione Immagine, e un metodo più rapido per raggruppare, confrontare ed eliminare.",
     h1="Come ordinare le foto dell'iPhone sul Mac",
     body="""      <p>Ordinare un rullino pieno sull'iPhone vuol dire ore di tocchi. Sul Mac vedi molte più foto insieme, selezioni con il mouse e confronti gli scatti su un grande schermo. Ecco come fare, con gli strumenti di macOS e con un'app dedicata.</p>

      <h2>Con gli strumenti integrati in macOS</h2>
      <ul>
        <li><strong>Foto:</strong> importa una copia delle foto dell'iPhone sul Mac. Utile come backup, ma non ti dice cosa eliminare sull'iPhone.</li>
        <li><strong>Acquisizione Immagine:</strong> elenca le foto dell'iPhone come semplici file, senza raggrupparle per viaggio né confrontare gli scatti simili.</li>
      </ul>
      <p>Funzionano entrambi, ma con migliaia di foto scorri comunque un unico lungo elenco.</p>

      <h2>Con PhotoCull, passo dopo passo</h2>
      <p><strong>1. Installa PhotoCull.</strong> <a href="{mac}">Scaricalo gratis</a>: macOS 11 o successivo su Apple Silicon, firmato e autenticato da Apple.</p>
      <p><strong>2. Collega l'iPhone.</strong> Collegalo con un cavo USB, sbloccalo e tocca Autorizza.</p>
      <p><strong>3. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo e mostra lo spazio occupato da ogni viaggio. Inizia dal più pesante.</p>
      <p><strong>4. Confronta e seleziona.</strong> Le foto simili hanno un badge: aprine fino a sei fianco a fianco, tieni la migliore e seleziona le altre, insieme a screenshot e video pesanti che non ti servono.</p>
      <p><strong>5. Elimina in sicurezza.</strong> L'eliminazione viene applicata sull'iPhone dall'<a href="{ts}">app TripSweep</a>, gratuita, tramite «Eliminati di recente»: hai 30 giorni per cambiare idea.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto resta sul tuo Mac e sul tuo iPhone: nessun account, nessun cloud, nessun invio.</li>
        <li>PhotoCull non modifica mai gli originali ed elimina solo ciò che confermi.</li>
        <li>Dal Mac, la versione gratuita consente 6 eliminazioni al giorno, TripSweep Pro 15 e Pro + Desktop è illimitato. Sfogliare e ordinare è gratis, e ordinare una cartella di foto sul Mac non ha mai limiti.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="Come ordinare le foto dell'iPhone su un PC Windows",
     desc="Ordina migliaia di foto dell'iPhone su Windows 10 o 11: cosa mostrano l'app Foto ed Esplora file, e un metodo più rapido per ordinare ed eliminare.",
     h1="Come ordinare le foto dell'iPhone su un PC Windows",
     body="""      <p>Hai un iPhone ma un computer Windows? Puoi comunque ordinare le foto su un grande schermo invece che sul telefono. Ecco cosa sa fare Windows da solo, e un metodo più rapido.</p>

      <h2>Con gli strumenti integrati in Windows</h2>
      <ul>
        <li><strong>App Foto:</strong> importa una copia delle foto dell'iPhone sul PC. Va bene per un backup, ma non ti aiuta a scegliere cosa eliminare.</li>
        <li><strong>Esplora file:</strong> mostra le foto dell'iPhone in cartelle come 100APPLE, con nomi come IMG_0001, senza viaggi né confronto degli scatti simili.</li>
      </ul>

      <h2>Con PhotoCull, passo dopo passo</h2>
      <p><strong>1. Installa Apple Devices.</strong> Installa l'app gratuita Apple Devices dal Microsoft Store: Windows ne ha bisogno per leggere un iPhone.</p>
      <p><strong>2. Installa PhotoCull.</strong> Dal Microsoft Store oppure <a href="{win}">scaricandolo gratis</a> (Windows 10/11, 64 bit). Il download non è ancora firmato, quindi SmartScreen può mostrare un avviso al primo avvio.</p>
      <p><strong>3. Collega l'iPhone.</strong> Collegalo con un cavo USB, sbloccalo e tocca Autorizza.</p>
      <p><strong>4. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo e mostra lo spazio occupato da ogni viaggio. Inizia dal più pesante.</p>
      <p><strong>5. Confronta, seleziona, elimina.</strong> Le foto simili hanno un badge: confrontane fino a sei fianco a fianco, tieni la migliore e seleziona le altre. L'eliminazione viene applicata sull'iPhone dall'<a href="{ts}">app TripSweep</a>, gratuita, tramite «Eliminati di recente»: hai 30 giorni per cambiare idea.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto resta sul tuo PC e sul tuo iPhone: nessun account, nessun cloud, nessun invio.</li>
        <li>PhotoCull non modifica mai gli originali ed elimina solo ciò che confermi.</li>
        <li>Sfogliare e ordinare è gratis, e ordinare una cartella di foto già sul PC non ha mai limiti.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Come ordinare migliaia di foto più in fretta su Mac o PC Windows",
     desc="Perché ordinare le foto su un grande schermo è molto più veloce che sul telefono, e un metodo semplice per esaminare migliaia di foto in una sola sessione.",
     h1="Come ordinare migliaia di foto più in fretta su Mac o PC",
     body="""      <p>Se il tuo rullino contiene diecimila foto, ordinarlo sullo schermo di un telefono è un progetto che non finirai mai. Su un computer può bastare una serata. Ecco perché, e un metodo che funziona.</p>

      <h2>Perché un computer è più veloce</h2>
      <ul>
        <li><strong>Più cose sullo schermo:</strong> decine di foto alla volta invece di una manciata.</li>
        <li><strong>Selezione precisa:</strong> mouse e tastiera selezionano centinaia di foto in pochi secondi.</li>
        <li><strong>Vero confronto:</strong> foto simili una accanto all'altra a una dimensione in cui messa a fuoco ed espressioni sono ben visibili.</li>
      </ul>

      <h2>Un metodo che funziona</h2>
      <p><strong>1. Raggruppa per viaggio.</strong> Ordinare per data e luogo divide la libreria in parti gestibili. Parti dal viaggio che occupa più spazio.</p>
      <p><strong>2. Elimina le quasi copie.</strong> Confronta ogni gruppo di scatti simili, tieni il migliore e seleziona gli altri.</p>
      <p><strong>3. Filtra il rumore.</strong> Nascondi i luoghi che non ti interessano (casa, lavoro) così i veri viaggi risaltano, e filtra per dimensione per trovare i file pesanti.</p>
      <p><strong>4. Elimina in un colpo solo.</strong> Seleziona centinaia di foto e conferma una volta sola.</p>

      <h2>PhotoCull fa esattamente questo</h2>
      <p><a href="{pc}">PhotoCull</a> è un'app desktop gratuita per Mac e Windows. La sua vista Viaggi raggruppa la libreria per viaggio e mostra lo spazio occupato da ciascuno, le foto simili hanno un badge e puoi confrontarne fino a sei fianco a fianco. Legge un iPhone via USB o qualsiasi cartella sul tuo computer, funziona 100% sul dispositivo e non modifica mai i tuoi originali.</p>
      <p>Le eliminazioni su un iPhone passano dall'<a href="{ts}">app TripSweep</a> gratuita e da «Eliminati di recente», quindi un errore si può annullare per 30 giorni. Ordinare una cartella sul computer non ha mai limiti.</p>

      <h2>Consigli per una sessione lunga</h2>
      <ul>
        <li>Lavora viaggio per viaggio, non scorrendo l'intera libreria.</li>
        <li>Decidi in fretta: se due scatti si assomigliano, tienine uno.</li>
        <li>Elimina alla fine di ogni viaggio, così i progressi si vedono.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="Come liberare spazio su iPhone da un Mac o PC Windows",
     desc="Collega il tuo iPhone, ordina le foto su un grande schermo ed elimina ciò che non ti serve, senza iCloud e senza inviare nulla online.",
     h1="Come liberare spazio su iPhone da un Mac o PC Windows",
     body="""      <p>Fare pulizia su un iPhone pieno direttamente dall'iPhone è noioso. Da un computer vedi molte più foto alla volta e decidi più in fretta. Ecco l'intero procedimento.</p>

      <h2>Cosa ti serve</h2>
      <ul>
        <li>Un Mac (Apple Silicon, macOS 11+) o un PC Windows 10/11.</li>
        <li>Un cavo USB. Su Windows, anche la app gratuita Apple Devices dal Microsoft Store.</li>
        <li><a href="{pc}">PhotoCull</a>, gratuito per entrambi i sistemi.</li>
        <li>Per eliminare dall'iPhone: l'<a href="{ts}">app TripSweep</a> gratuita sull'iPhone.</li>
      </ul>

      <h2>Passo dopo passo</h2>
      <p><strong>1. Collega e autorizza.</strong> Collega l'iPhone, sbloccalo e tocca Autorizza.</p>
      <p><strong>2. Apri la vista Viaggi.</strong> PhotoCull raggruppa il tuo rullino per viaggio e mostra lo spazio occupato da ciascuno.</p>
      <p><strong>3. Ordina i viaggi più pesanti.</strong> Confronta gli scatti simili, tieni il migliore e seleziona il resto, più gli screenshot e i video pesanti che non ti servono.</p>
      <p><strong>4. Conferma l'eliminazione.</strong> Da un Mac, l'eliminazione viene applicata sull'iPhone da TripSweep tramite «Eliminati di recente», e lo stesso vale su Windows. Nulla viene cancellato definitivamente subito.</p>
      <p><strong>5. Svuota «Eliminati di recente».</strong> Lo spazio torna disponibile una volta svuotato l'album.</p>

      <h2>È sicuro?</h2>
      <p>Sì: le tue foto restano sui tuoi dispositivi, senza account, senza cloud e senza upload. Le foto eliminate restano 30 giorni in «Eliminati di recente», e PhotoCull si limita a leggere le tue foto finché non confermi.</p>

      <h2>Quante foto posso eliminare al giorno?</h2>
      <p>Da un Mac, la versione gratuita consente 6 foto al giorno, TripSweep Pro 15 e Pro + Desktop è illimitato (vedi i piani nella pagina di TripSweep). Sono tutti acquisti singoli, senza abbonamento. Sfogliare, confrontare e ordinare è gratuito, e ordinare una cartella sul computer non ha mai limiti.</p>

      <h2>Su Windows</h2>
      <p>I passaggi sono gli stessi su Windows 10 e 11. Installa prima la app gratuita Apple Devices dal Microsoft Store, così PhotoCull può leggere l'iPhone. L'app non è ancora firmata digitalmente, quindi SmartScreen può mostrare un avviso al primo avvio.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Come confrontare foto simili fianco a fianco e tenere la migliore",
     desc="Una routine semplice per scegliere lo scatto migliore tra foto quasi identiche: cosa guardare e come farlo in fretta su un grande schermo.",
     h1="Come confrontare foto simili e tenere la migliore",
     body="""      <p>Hai scattato sei foto dello stesso momento e sembrano tutte buone. Scegliere la migliore richiede pochi secondi con il metodo giusto e qualche minuto con quello sbagliato.</p>

      <h2>Cosa controllare, in quest'ordine</h2>
      <ol>
        <li><strong>Messa a fuoco.</strong> Ingrandisci sugli occhi o sul soggetto principale. Un soggetto sfocato è motivo di esclusione.</li>
        <li><strong>Espressioni.</strong> Occhi aperti, sorrisi naturali, nessuno a metà di un battito di ciglia.</li>
        <li><strong>Inquadratura.</strong> Niente tagliato fuori, sfondo pulito, orizzonte dritto.</li>
        <li><strong>Momento.</strong> Se due scatti si equivalgono, tieni quello che sembra più vivo.</li>
      </ol>

      <h2>Perché il confronto fianco a fianco conta</h2>
      <p>Passare da una foto all'altra rende difficile vedere le piccole differenze. Vederle una accanto all'altra alla stessa dimensione rende evidente quella più nitida o meglio inquadrata. Lo schermo di un computer ne mostra fino a sei insieme, dove un telefono ne mostra una.</p>

      <h2>Una routine più veloce</h2>
      <p>Raggruppa prima le foto simili, così non devi mai cercarle nella libreria. Per ogni gruppo, apri il confronto, scegline una e seleziona le altre. Decidi in secondi, non in minuti.</p>

      <h2>Fallo con PhotoCull</h2>
      <p><a href="{pc}">PhotoCull</a> mostra un badge sulle foto simili, ne apre fino a sei fianco a fianco e ti permette di selezionare le altre con un clic. Funziona su un iPhone collegato via USB o su qualsiasi cartella del tuo Mac o PC, offline, e non modifica mai i tuoi originali.</p>
      <p>Sul telefono stesso, l'<a href="{ts}">app TripSweep</a> suggerisce lo scatto migliore di ogni gruppo in base a nitidezza, punteggio estetico di Apple e volti, e il suo pulsante «Tieni 1 per gruppo» gestisce un'intera categoria in una volta.</p>

      <h2>Tieni, senza rimpianti</h2>
      <p>Quando hai dubbi, tienine due. Le eliminazioni su un iPhone passano da «Eliminati di recente» per 30 giorni, quindi puoi ancora cambiare idea.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="Come trovare foto duplicate e simili sul Mac",
     desc="Trova copie esatte, raffiche e scatti quasi identici nelle cartelle di foto del Mac o su un disco esterno, tieni il migliore e sposta il resto nel Cestino.",
     h1="Come trovare foto duplicate e simili sul Mac",
     body="""      <p>Anni di importazioni, schede della fotocamera e backup lasciano le stesse foto sparse in tante cartelle del Mac. Alcune sono copie esatte; la maggior parte sono scatti quasi identici dello stesso momento. Ecco come trovare entrambe, tenere la migliore e liberare spazio, senza toccare la libreria di Foto.</p>

      <h2>Cosa offre macOS</h2>
      <ul>
        <li><strong>Finder:</strong> ordinare una cartella per nome o dimensione aiuta a individuare le copie evidenti come «IMG_1234 copia.jpg», ma non due scatti diversi della stessa scena.</li>
        <li><strong>Foto:</strong> l'album Duplicati copre solo le foto già presenti nella libreria di Foto, non le altre cartelle né i dischi.</li>
      </ul>

      <h2>Con PhotoCull, passo dopo passo</h2>
      <p><strong>1. Installa PhotoCull.</strong> <a href="{mac}">Scaricalo gratis</a>: macOS 11 o successivo su Apple Silicon, firmato e autenticato da Apple.</p>
      <p><strong>2. Apri la cartella.</strong> Clicca su «Apri cartella» oppure trascina una cartella sulla finestra. Le sottocartelle sono incluse, così come i dischi esterni.</p>
      <p><strong>3. Guarda i badge.</strong> PhotoCull confronta il contenuto delle foto, non i nomi: copie esatte, raffiche e scatti quasi identici ricevono lo stesso badge «≈ N».</p>
      <p><strong>4. Tieni la migliore.</strong> Apri un gruppo per confrontare fino a sei foto fianco a fianco, tieni la più nitida e seleziona le altre.</p>
      <p><strong>5. Elimina in sicurezza.</strong> I file selezionati vanno nel Cestino del Mac, dove «Ripristina» li rimette al loro posto se cambi idea.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Sono supportati JPEG, HEIC, PNG, TIFF, WebP e file RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), oltre ai video MOV e MP4.</li>
        <li>Le foto sono datate in base ai dati EXIF, quindi anche le cartelle copiate restano ordinate per il giorno dello scatto.</li>
        <li>Ordinare una cartella è gratis e senza limiti. Tutto funziona sul tuo Mac: nessun account, nessun invio.</li>
        <li>Le librerie di Foto e i pacchetti di app dentro la cartella vengono ignorati, così PhotoCull non entra mai nei file di un'altra app.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Come trovare foto duplicate e simili su Windows",
     desc="Trova copie esatte, raffiche e scatti quasi identici nelle cartelle di foto del PC o su un disco esterno, tieni il migliore e sposta il resto nel Cestino.",
     h1="Come trovare foto duplicate e simili su Windows 10 o 11",
     body="""      <p>Backup del telefono, schede della fotocamera e vecchie copie lasciano le stesse foto in più cartelle del PC. Alcune sono duplicati esatti, la maggior parte sono scatti quasi identici. Ecco come trovare entrambi e fare pulizia in sicurezza.</p>

      <h2>Cosa offre Windows</h2>
      <ul>
        <li><strong>Esplora file:</strong> ordinare per nome, dimensione o data aiuta con le copie evidenti, ma non capisce che due file diversi mostrano la stessa scena.</li>
        <li><strong>App Foto:</strong> ottima per visualizzare e importare, ma senza uno strumento per trovare scatti simili e scegliere il migliore.</li>
      </ul>

      <h2>Con PhotoCull, passo dopo passo</h2>
      <p><strong>1. Installa PhotoCull.</strong> Scaricalo gratis <a href="{win}">per Windows 10 o 11</a> (64 bit), oppure dal Microsoft Store.</p>
      <p><strong>2. Apri la cartella.</strong> Clicca su «Apri cartella» oppure trascina una cartella sulla finestra. Sottocartelle e dischi esterni sono inclusi.</p>
      <p><strong>3. Guarda i badge.</strong> PhotoCull confronta ciò che mostrano le foto, non i nomi dei file: copie esatte, raffiche e scatti quasi identici ricevono lo stesso badge «≈ N».</p>
      <p><strong>4. Tieni la migliore.</strong> Confronta fino a sei foto fianco a fianco, tieni la più nitida e seleziona le altre.</p>
      <p><strong>5. Elimina in sicurezza.</strong> I file selezionati vanno nel Cestino, quindi puoi ripristinarli.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Sono supportati JPEG, HEIC, PNG, TIFF, WebP e file RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), oltre ai video MOV e MP4. Per le anteprime HEIC servono le Estensioni immagine HEIF gratuite di Microsoft.</li>
        <li>Le foto sono datate in base ai dati EXIF, quindi anche le cartelle copiate restano ordinate per il giorno dello scatto.</li>
        <li>Ordinare una cartella è gratis e senza limiti. Tutto funziona sul tuo PC: nessun account, nessun invio.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Come ordinare una grande cartella di foto su Mac o PC",
     desc="Vecchi backup, schede SD, un disco esterno pieno di foto: un metodo semplice per ordinare migliaia di file per viaggio ed eliminare le quasi copie.",
     h1="Come ordinare una grande cartella di foto, o un intero disco esterno",
     body="""      <p>Ce l'abbiamo tutti: una cartella chiamata «Foto da ordinare», un vecchio backup del telefono, un disco esterno riempito in dieci anni. Migliaia di file, nessun ordine, tante quasi copie. Ecco un metodo per sistemare tutto in una sola sessione.</p>

      <h2>1. Apri tutta la cartella in una volta</h2>
      <p>Non andare cartella per cartella. Apri la cartella principale in <a href="{pc}">PhotoCull</a> («Apri cartella», oppure trascinala sulla finestra): le sottocartelle sono incluse e ogni foto è datata in base ai dati EXIF, non al giorno in cui è stata copiata.</p>

      <h2>2. Lascia emergere i viaggi</h2>
      <p>La vista Viaggi raggruppa le foto per data e luogo e mostra lo spazio occupato da ciascun gruppo. Dieci anni di file diventano un elenco di viaggi ed eventi, e parti dal più pesante.</p>

      <h2>3. Riduci le quasi copie</h2>
      <p>Raffiche, scatti ripetuti e copie della stessa foto hanno un badge «≈ N». Confrontane fino a sei fianco a fianco, tieni la migliore e seleziona le altre. Questo passaggio da solo spesso elimina buona parte dei file.</p>

      <h2>4. Seleziona gli scarti più ovvi</h2>
      <p>Screenshot, foto mosse, video accidentali: selezionali man mano. Nulla viene eliminato finché non confermi.</p>

      <h2>5. Elimina in sicurezza</h2>
      <p>I file confermati vanno nel Cestino su Mac o nel Cestino di Windows, quindi un errore si può annullare. Svuotalo quando sei sicuro.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>I file RAW delle fotocamere (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sono supportati insieme a JPEG, HEIC, PNG e video.</li>
        <li>Ordinare le cartelle è gratis e senza limiti, su Mac (<a href="{mac}">download</a>) e Windows (<a href="{win}">download</a>).</li>
        <li>I tuoi originali non vengono mai modificati: l'unica modifica di PhotoCull è l'eliminazione che confermi.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="Come ordinare le foto del tuo Android sul Mac",
     desc="Un Mac non legge i telefoni Android via USB. Come ordinare comunque migliaia di foto Android sul Mac, via Wi-Fi, ed eliminare ciò che non serve.",
     h1="Come ordinare le foto del tuo Android sul Mac",
     body="""      <p>Collega un telefono Android a un Mac e, il più delle volte, non succede nulla: macOS non legge i telefoni Android via USB come fa Windows. Eppure un Mac è il posto migliore per ordinare un grande rullino, con uno schermo ampio, un mouse e il confronto fianco a fianco. Ecco cosa funziona.</p>

      <h2>Cosa sa fare macOS da solo</h2>
      <ul>
        <li><strong>Acquisizione Immagine:</strong> può vedere il telefono se scegli «Trasferisci foto» (PTP) nella notifica USB, ma solo come elenco piatto di file, senza raggruppamenti e senza confronto tra scatti simili.</li>
        <li><strong>Android File Transfer di Google:</strong> non è più mantenuto e comunque si limita a copiare file.</li>
        <li><strong>Caricamento nel cloud:</strong> inviare tutto a un servizio online solo per ordinare è lento, consuma il tuo piano dati e mette le tue foto sul server di qualcun altro.</li>
      </ul>

      <h2>Con PhotoCull, via Wi-Fi, passo dopo passo</h2>
      <p><strong>1. Installa le due app.</strong> <a href="{mac}">Scarica PhotoCull per Mac</a> gratis (macOS 11 o successivo su Apple Silicon) e installa sul telefono l'<a href="{play}">app TripSweep da Google Play</a>, gratuita (Android 11 o successivo).</p>
      <p><strong>2. Stesso Wi-Fi.</strong> Collega il telefono alla stessa rete Wi-Fi del Mac e apri la scheda Eliminazione di TripSweep.</p>
      <p><strong>3. Collegati una volta sola.</strong> In PhotoCull, clicca «Telefono Android» e scegli il tuo telefono. Autorizza il Mac dal telefono: lo stesso codice a 4 cifre compare su entrambi gli schermi. La volta successiva si ricollega da solo.</p>
      <p><strong>4. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo, con lo spazio occupato da ogni viaggio. Le foto simili hanno un badge: confrontane fino a sei fianco a fianco, tieni la migliore, seleziona le altre.</p>
      <p><strong>5. Elimina in sicurezza.</strong> Clicca Elimina e conferma sul telefono, in TripSweep. Le foto vanno nel cestino del telefono per 30 giorni, così puoi rimediare a un errore.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>La connessione resta sulla tua rete locale ed è cifrata; nulla passa da internet.</li>
        <li>PhotoCull non modifica mai gli originali ed elimina solo ciò che confermi sul telefono.</li>
        <li>Dal computer, la versione gratuita consente 6 eliminazioni al giorno, TripSweep Pro 15 e Pro + Desktop è illimitato. Sfogliare e ordinare è sempre gratis.</li>
        <li>Hai anche un iPhone? Si collega al Mac con un cavo USB.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="Come ordinare le foto del tuo Android su un PC Windows",
     desc="Ordina migliaia di foto Android su Windows 10 o 11: cosa mostrano Esplora file e l'app Foto, e un metodo più rapido per raggruppare, confrontare ed eliminare.",
     h1="Come ordinare le foto del tuo Android su un PC Windows",
     body="""      <p>Windows legge bene i telefoni Android, ma leggere non vuol dire ordinare. Con migliaia di foto, gli strumenti integrati ti lasciano a scorrere un unico lungo elenco di nomi di file. Ecco cosa fanno e un metodo più rapido per liberare il telefono dal PC.</p>

      <h2>Con gli strumenti integrati in Windows</h2>
      <ul>
        <li><strong>Esplora file:</strong> dopo aver scelto «Trasferimento file» sul telefono, la sua cartella DCIM compare come semplici file. Da lì puoi eliminare, ma senza raggruppamenti e senza confronto tra scatti simili.</li>
        <li><strong>App Foto:</strong> importa una copia sul PC. Un buon backup, ma non ti dice cosa togliere dal telefono.</li>
        <li><strong>Collegamento al telefono:</strong> mostra solo le foto recenti, una alla volta.</li>
      </ul>

      <h2>Con PhotoCull, passo dopo passo</h2>
      <p><strong>1. Installa le due app.</strong> Scarica PhotoCull gratis <a href="{win}">per Windows 10 o 11</a> e installa sul telefono l'<a href="{play}">app TripSweep da Google Play</a>, gratuita (Android 11 o successivo).</p>
      <p><strong>2. Collegati via USB o Wi-Fi.</strong> Via USB: collega il telefono e scegli «Trasferimento file» nella notifica USB. Via Wi-Fi: metti entrambi sulla stessa rete. Poi apri la scheda Eliminazione di TripSweep e clicca «Telefono Android» in PhotoCull.</p>
      <p><strong>3. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo e mostra lo spazio occupato da ogni viaggio. Inizia dal più pesante.</p>
      <p><strong>4. Confronta e seleziona.</strong> Le foto simili hanno un badge: aprine fino a sei fianco a fianco, tieni la migliore e seleziona le altre, insieme a screenshot e video pesanti.</p>
      <p><strong>5. Elimina in sicurezza.</strong> Conferma sul telefono, in TripSweep: le foto vanno nel cestino del telefono per 30 giorni.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto resta sul tuo PC e sul tuo telefono: nessun account, nessun cloud, nessun invio.</li>
        <li>Eliminare da Esplora file è immediato e definitivo; passando da TripSweep conservi la rete di sicurezza dei 30 giorni.</li>
        <li>Dal PC, la versione gratuita consente 6 eliminazioni al giorno, TripSweep Pro 15 e Pro + Desktop è illimitato. Ordinare una cartella sul PC non ha mai limiti.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="Come liberare spazio su Android da un Mac o PC Windows",
     desc="Collega il tuo telefono Android, ordina le foto su un grande schermo ed elimina ciò che non serve, senza Google One e senza caricare nulla online.",
     h1="Come liberare spazio sul tuo telefono Android da un Mac o PC",
     body="""      <p>Quando un telefono Android resta senza spazio, il motivo sono quasi sempre foto e video. Sistemarli su un piccolo schermo è lento. Da un computer vedi di più in una volta e decidi più in fretta, senza comprare altro spazio nel cloud.</p>

      <h2>Perché un computer aiuta</h2>
      <p>Un grande schermo mostra decine di foto insieme, un mouse ne seleziona centinaia in pochi secondi e confrontare scatti quasi identici fianco a fianco è molto più facile che passare avanti e indietro. Un rullino che sul telefono richiederebbe una serata si sistema in pochi minuti.</p>

      <h2>Il metodo</h2>
      <p><strong>1. Collega il telefono.</strong> Installa <a href="{pc}">PhotoCull</a> sul tuo Mac o PC e l'<a href="{play}">app TripSweep</a> gratuita sul telefono. Collegati via Wi-Fi (Mac e Windows) o via USB (Windows), con TripSweep aperta sulla scheda Eliminazione.</p>
      <p><strong>2. Parti da ciò che pesa di più.</strong> La vista Viaggi mostra lo spazio occupato da ogni viaggio; i video lunghi e le vecchie vacanze di solito liberano di più.</p>
      <p><strong>3. Elimina gli scatti quasi identici.</strong> Raffiche e scatti ripetuti della stessa scena hanno un badge. Confrontali fianco a fianco, tieni il migliore, seleziona gli altri.</p>
      <p><strong>4. Elimina screenshot e foto sfocate.</strong> Raramente meritano di restare e si selezionano in blocco in un attimo.</p>
      <p><strong>5. Conferma sul telefono.</strong> TripSweep applica l'eliminazione e sposta le foto nel cestino del telefono, dove restano 30 giorni. Svuota il cestino quando sei sicuro, per recuperare lo spazio.</p>

      <h2>Mi serve Google One?</h2>
      <p>Lo spazio nel cloud è un buon backup, ma conserva tutto, compresi i duplicati. Fare ordine prima significa aver bisogno di meno spazio, sul telefono e nel cloud.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Nessun account e nessun invio: telefono e computer comunicano sulla tua rete o via cavo.</li>
        <li>Dal computer, la versione gratuita consente 6 eliminazioni al giorno, Pro 15 e Pro + Desktop è illimitato.</li>
      </ul>"""),
],
}
