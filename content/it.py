# -*- coding: utf-8 -*-
# Italian translation of the FAQ and blog of the TripSweep site (source: en.py). Tokens in answers/articles: {ts} {pc} {store} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacy", more="Continua a leggere",
    cta_store="📱 Scarica TripSweep su App Store",
    cta_play="🤖 Scarica TripSweep su Google Play",
    cross_label={"tripsweep": "App desktop", "photocull": "App mobile"},
    twin_android="Usi un telefono Android? Leggi la guida per Android:",
    twin_iphone="Usi un iPhone? Leggi la guida per iPhone:",
    index={
        "tripsweep": dict(
            title="Blog TripSweep: spazio su iPhone e foto duplicate",
            desc="Guide pratiche per liberare spazio su iPhone, eliminare foto duplicate e simili e riordinare i vecchi viaggi, senza iCloud e senza inviare le tue foto.",
            h1="Guide per fare ordine nelle foto del tuo iPhone",
            intro="Guide brevi e pratiche per liberare spazio su iPhone, eliminare i duplicati e tenere solo gli scatti migliori."),
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
     "Sì, con <a href=\"{pc}\">PhotoCull</a> su un Mac o un PC Windows. Selezioni le foto sul grande schermo e PhotoCull le elimina direttamente tramite il cavo USB, senza limite giornaliero e senza nulla da acquistare. Con un iPhone serve che Foto di iCloud sia disattivato sull'iPhone e, su un Mac, macOS 27 o successivo (va bene qualsiasi Windows 10 o 11). L'eliminazione è definitiva sull'iPhone, le foto non passano da «Eliminati di recente», ma PhotoCull conserva per impostazione predefinita una copia sul computer per 30 giorni. Anche un telefono Android si collega tramite cavo USB, in modalità «Trasferimento file», senza nulla da installare sul telefono (Windows 10 o 11, o un Mac con macOS 27 o successivo)."),
    ("Quali iPhone e versioni di iOS supporta TripSweep?",
     "TripSweep richiede iOS 18 o successivo. L'analisi delle foto simili usa il framework Vision di Apple ed è più veloce sugli iPhone recenti, ma funziona su tutti i modelli supportati. Su Android richiede Android 11 o successivo ed è disponibile su <a href=\"{play}\">Google Play</a>."),
]

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
      <p>Se preferisci un grande schermo, <a href="{pc}">PhotoCull</a> fa lo stesso lavoro di selezione su un Mac o PC Windows, con il telefono collegato tramite cavo USB.</p>

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
}
