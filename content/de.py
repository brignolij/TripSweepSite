# -*- coding: utf-8 -*-
# Deutsche Fassung der FAQ und des Blogs beider Websites. Tokens in Antworten/Artikeln: {ts} {pc} {store} {mac} {win} (siehe link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Datenschutz", more="Weiterlesen",
    cta_store="📱 TripSweep im App Store laden",
    cta_mac="💻 PhotoCull für Mac laden", cta_win="🪟 PhotoCull für Windows laden",
    cross_label={"tripsweep": "Desktop-App", "photocull": "iOS-App"},
    index={
        "tripsweep": dict(
            title="TripSweep Blog – iPhone Speicher freigeben, doppelte Fotos löschen",
            desc="Praktische Anleitungen, um iPhone Speicher freizugeben, doppelte und ähnliche Fotos zu löschen und alte Reisen aufzuräumen – ohne iCloud und ohne dass deine Fotos irgendwohin gesendet werden.",
            h1="Anleitungen zum Aufräumen deiner iPhone-Fotos",
            intro="Kurze, praktische Anleitungen, um Speicherplatz auf deinem iPhone freizugeben, Duplikate zu löschen und nur die besten Aufnahmen zu behalten."),
        "photocull": dict(
            title="PhotoCull Blog – Fotos am Mac oder PC sortieren, iPhone vom Computer aus aufräumen",
            desc="Anleitungen, um Tausende Fotos auf einem großen Bildschirm schneller zu sortieren, ähnliche Aufnahmen nebeneinander zu vergleichen und dein iPhone von einem Mac oder Windows-PC aus aufzuräumen.",
            h1="Anleitungen zum Sortieren deiner Fotos am Computer",
            intro="Warum ein großer Bildschirm das Sortieren von Fotos so viel schneller macht und wie du damit dein iPhone aufräumst."),
    },
)

FAQ_TRIPSWEEP_EXTRA = [
    ("Was ist der Unterschied zwischen doppelten und ähnlichen Fotos?",
     "Doppelte Fotos sind identische Kopien derselben Datei. Ähnliche Fotos sind verschiedene Aufnahmen derselben Szene: eine Serienaufnahme, fünf Versuche für denselben Sonnenuntergang, zwei fast gleiche Selfies. Doppelte Fotos sind leicht zu erkennen; bei ähnlichen Fotos steckt der meiste verschwendete Speicherplatz, und TripSweep gruppiert beides, sodass du eines behältst und den Rest löschst."),
    ("Wie wählt TripSweep das beste Foto einer Gruppe aus?",
     "Es berücksichtigt Schärfe, die ästhetische Bewertung von Apple und Gesichter und schlägt dann ein Foto pro Gruppe vor. Der Vorschlag ist nur ein Ausgangspunkt: Du kannst ein anderes Foto behalten, mehrere behalten oder die Gruppe überspringen. Die Analyse läuft auf deinem iPhone mit dem Vision-Framework von Apple."),
    ("Was findet der Tab „Aufräumen“?",
     "Identische Kopien, ähnliche Fotos, unscharfe Fotos, Screenshots und große Videos, jeweils in einer eigenen Kategorie mit dem belegten Speicherplatz. Du beginnst mit der Kategorie, die am meisten Platz freigibt, und sortierst sie in wenigen Taps."),
    ("Schlägt TripSweep vor, meine Lieblingsfotos zu löschen?",
     "Nein. Fotos, die du als Favoriten markiert hast, werden nie zum Löschen vorgeschlagen, und nichts wird gelöscht, bevor du es bestätigst."),
    ("Funktioniert TripSweep auch bei Fotos ohne GPS-Standort?",
     "Ja. Fotos ohne Standort werden statt nach Reise nach Ereignis und Monat gruppiert, sodass auch Screenshots, gespeicherte Bilder und Fotos, die ohne Ortungsdienste aufgenommen wurden, sortiert werden."),
    ("Kann ich mein Zuhause und meinen Arbeitsplatz aus den Reisen ausblenden?",
     "Ja. Füge dein Zuhause, deinen Arbeitsplatz oder jeden Ort, an dem du täglich vorbeikommst, als ausgeschlossenen Ort hinzu. So erscheint der Alltag nicht als Reise und deine echten Reisen treten hervor. Mit Pro sind eigene Orte unbegrenzt möglich."),
    ("Kann ich eine Reise sichern oder teilen, bevor ich sie lösche?",
     "Ja. Du kannst eine ganze Reise auf deinen Mac oder in die Dateien-App exportieren oder mit den Personen teilen, die dabei waren, und sie dann von deinem iPhone löschen, sobald sie anderswo sicher liegt."),
    ("Brauche ich eine Internetverbindung oder ein Konto?",
     "Nein. TripSweep braucht kein Konto und funktioniert offline. Ortsnamen werden auf deinem iPhone erkannt, und kein Foto, kein Video und kein Standort wird jemals an einen Server gesendet. Es können nur anonyme, abschaltbare Nutzungsstatistiken gesendet werden. Du kannst sie im Tab Info abschalten."),
    ("Löscht das Löschen in TripSweep meine Fotos auch aus iCloud?",
     "Wenn die iCloud-Fotos aktiviert sind, wird ein auf dem iPhone gelöschtes Foto von all deinen Geräten entfernt, weil iCloud-Fotos so funktioniert. TripSweep löscht über „Zuletzt gelöscht“, sodass du 30 Tage Zeit hast, es dir anders zu überlegen, und der iCloud-Speicherplatz wird frei, sobald dieses Album geleert wird."),
    ("Kann ich meine iPhone-Fotos auf einem großen Bildschirm statt am Telefon durchsehen?",
     "Ja. <a href=\"{pc}\">PhotoCull</a> ist die kostenlose Desktop-Begleiter-App für Mac und Windows: Sie zeigt die Fotomediathek deines iPhones nach Reisen gruppiert, vergleicht ähnliche Fotos nebeneinander und lässt dich Hunderte Fotos mit wenigen Klicks markieren. <a href=\"{pc}\">Mehr über PhotoCull erfahren</a>."),
    ("Kann ich Fotos gesammelt vom Computer löschen, statt auf dem Telefon zu tippen?",
     "Ja, mit <a href=\"{pc}\">PhotoCull</a> auf einem Mac oder Windows-PC. Du markierst die Fotos auf dem großen Bildschirm, und das Löschen wird von TripSweep über „Zuletzt gelöscht“ auf deinem iPhone ausgeführt. Die kostenlose Version erlaubt 6 Fotos pro Tag vom Mac aus (siehe die Tarife auf der TripSweep-Seite), Pro 15, und Pro + Desktop hebt das Limit auf."),
    ("Welche iPhones und iOS-Versionen unterstützt TripSweep?",
     "TripSweep benötigt iOS 18 oder neuer. Die Analyse ähnlicher Fotos nutzt das Vision-Framework von Apple und ist auf neueren iPhones schneller, funktioniert aber auf jedem unterstützten Modell."),
]

FAQ_PHOTOCULL = dict(
    title="PhotoCull FAQ – Fotos am Mac oder Windows-PC sortieren und löschen",
    desc="Wie du Tausende Fotos am Computer sortierst, ähnliche Aufnahmen vergleichst, iPhone Speicher von einem Mac oder PC aus freigibst und sicher löschst – Antworten zu PhotoCull, 100 % auf dem Gerät.",
    nav_home="PhotoCull", nav_desktop="iOS-App",
    h1="Fragen und Antworten",
    intro="Wie du deine Fotos am Computer schneller sortierst, dein iPhone von einem Mac oder PC aus aufräumst und was PhotoCull mit deinen Fotos macht (und nie macht).",
    qa=[
        ("Warum Fotos am Computer statt auf dem iPhone sortieren?",
         "Ein großer Bildschirm zeigt mehr Fotos auf einmal, mit Maus und Tastatur wählst du Hunderte in Sekunden aus, und Aufnahmen nebeneinander zu vergleichen ist einfacher, als hin und her zu blättern. Eine Fotomediathek mit Tausenden Fotos zu sortieren, kostet am Telefon mehrere Sitzungen und am Mac oder PC deutlich weniger Zeit."),
        ("Was ist PhotoCull?",
         "PhotoCull ist eine kostenlose Desktop-App für Mac und Windows, die deine Fotos nach Reisen gruppiert, ähnliche Aufnahmen nebeneinander vergleicht und alles, was nicht behalten werden muss, gesammelt löscht. Sie liest die Fotomediathek deines iPhones per USB oder einen beliebigen Fotoordner auf deinem Computer und arbeitet 100 % auf dem Gerät."),
        ("Wie sortiere ich Tausende Fotos schnell?",
         "Öffne die Ansicht „Reisen“: Deine Mediathek ist nach Reisen gruppiert, mit dem Speicherplatz jeder Reise, sodass du mit der größten beginnst. Markiere innerhalb einer Reise Fotos gesammelt, vergleiche die ähnlichen nebeneinander und behalte die beste Aufnahme jeder Gruppe. Dieselben Filter wie in der iOS-App (eintägige Reisen, ausgeschlossene Orte wie Zuhause oder Arbeit, Größe) grenzen die Auswahl weiter ein."),
        ("Wie gebe ich iPhone Speicher von einem Mac oder PC aus frei?",
         "Verbinde dein iPhone per USB, öffne PhotoCull, markiere die Reisen und Fotos, die du nicht mehr brauchst, und bestätige. Das Löschen wird auf dem iPhone von der kostenlosen <a href=\"{ts}\">TripSweep-App</a> über „Zuletzt gelöscht“ ausgeführt und gibt Speicherplatz frei, sobald du dieses Album leerst."),
        ("Kann ich Fotos direkt vom Computer aus von meinem iPhone löschen?",
         "Ja, von einem Mac oder einem Windows-PC, wenn die <a href=\"{ts}\">TripSweep-App</a> auf dem iPhone installiert ist. Vom Mac aus erlaubt die kostenlose Version 6 Fotos pro Tag, Pro 15, und Pro + Desktop hebt das Limit auf."),
        ("Ist das Löschen mit PhotoCull endgültig?",
         "Nein. Löschungen auf dem iPhone laufen immer über das Album „Zuletzt gelöscht“ der Fotos-App, wo Fotos 30 Tage lang bleiben und wiederhergestellt werden können. PhotoCull führt nie ein sofortiges, endgültiges Löschen aus."),
        ("Wie verbinde ich mein iPhone mit PhotoCull?",
         "Verwende ein USB-Kabel, entsperre das iPhone und tippe auf „Vertrauen“, wenn du dazu aufgefordert wirst. Am Mac ist nichts weiter nötig. Installiere unter Windows die kostenlose App Apple Devices aus dem Microsoft Store, die den Treiber bereitstellt, mit dem PhotoCull das iPhone lesen kann."),
        ("Brauche ich die iOS-App TripSweep?",
         "Nicht zum Durchsehen, Vergleichen und Sortieren. Du brauchst sie nur, um Fotos vom iPhone zu löschen, weil das Löschen auf dem Telefon ausgeführt wird. Ordner auf deinem Computer lassen sich auch ohne sie sortieren."),
        ("Kann ich PhotoCull für Fotos auf meinem Computer verwenden, nicht auf einem iPhone?",
         "Ja. Öffne einen beliebigen Ordner: PhotoCull findet darin ähnliche Fotos, zeigt Markierungen an den ähnlichen und lässt dich ohne Tageslimit vergleichen und löschen."),
        ("Wie findet PhotoCull ähnliche Fotos?",
         "Es vergleicht den Inhalt deiner Fotos, nicht ihre Dateinamen, sodass Serienaufnahmen, fast identische Aufnahmen und dieselbe mehrfach aufgenommene Szene in derselben Gruppe landen. Du kannst bis zu 6 Fotos nebeneinander vergleichen und das schärfste, am besten komponierte behalten."),
        ("Wie vergleiche ich ähnliche Fotos nebeneinander?",
         "Wähle eine Gruppe ähnlicher Fotos aus und öffne den Vergleich: Bis zu 6 Fotos werden gleich groß angezeigt, sodass du Schärfe, Gesichtsausdrücke und Bildausschnitt beurteilen kannst. Behalte das beste und markiere den Rest."),
        ("Funktioniert PhotoCull unter Windows?",
         "Ja: Windows 10 und 11 (64 Bit). Zum Lesen eines iPhones ist die kostenlose App Apple Devices aus dem Microsoft Store nötig. Die App ist noch nicht codesigniert, daher zeigt Windows SmartScreen beim ersten Start eventuell eine Warnung: Wähle „Weitere Informationen“ und dann „Trotzdem ausführen“."),
        ("Welche Macs unterstützt PhotoCull?",
         "Macs mit Apple Silicon unter macOS 11 oder neuer. Die App ist von Apple signiert und notarisiert, sodass sie ohne Sicherheitswarnung geöffnet wird."),
        ("Ist PhotoCull kostenlos? Gibt es ein Abo?",
         "PhotoCull ist kostenlos erhältlich und es gibt kein Abo. Durchsehen, Vergleichen und Sortieren sind kostenlos, und das Sortieren eines Ordners auf deinem Computer ist nie begrenzt. Das Löschen von Fotos von einem iPhone aus am Mac ist in der kostenlosen Version auf 6 pro Tag begrenzt, mit TripSweep Pro auf 15 und mit Pro + Desktop unbegrenzt (Einmalkäufe in der iOS-App TripSweep)."),
        ("Sendet PhotoCull meine Fotos an einen Server oder in die Cloud?",
         "Nein. PhotoCull arbeitet 100 % auf dem Gerät: kein Konto, keine Cloud, und kein Foto, kein Video und kein Standort wird jemals irgendwohin gesendet. Die Ortserkennung und die Erkennung ähnlicher Fotos laufen auf deinem Computer. Es können nur anonyme, abschaltbare Nutzungsstatistiken gesendet werden."),
        ("Verändert PhotoCull meine Originalfotos?",
         "Nein. PhotoCull liest deine Fotos nur, um sie anzuzeigen und zu vergleichen. Die einzige Änderung, die es je vornimmt, ist das Löschen, das du bestätigst."),
        ("Wie blende ich mein Zuhause und meinen Arbeitsplatz in der Reiseansicht aus?",
         "Füge sie als ausgeschlossene Orte hinzu: Der Alltag erscheint dann nicht mehr als Reise und deine echten Reisen treten hervor. Die Einstellung ist dieselbe wie in der iOS-App."),
        ("Kann ich nach einem Urlaub am Computer aufräumen?",
         "Ja, das ist der typische Einsatz. Verbinde nach einer Reise das iPhone, öffne diese Reise in PhotoCull, vergleiche die ähnlichen Aufnahmen, behalte die beste jeder Gruppe und lösche den Rest. Die <a href=\"{ts}\">TripSweep-App</a> kann die ganze Reise auch exportieren, bevor du etwas löschst."),
        ("Kann ich PhotoCull nutzen, um ein Fotoalbum oder ein Backup vorzubereiten?",
         "PhotoCull hilft dir zu entscheiden, was behaltenswert ist: Sortiere die Reise, entferne die doppelten und fast identischen Aufnahmen und sichere oder teile dann, was übrig bleibt. Die <a href=\"{ts}\">TripSweep-App</a> kann eine ganze Reise exportieren oder teilen."),
    ],
    footer_copy="© 2026 PhotoCull. Entwickelt von Jeffrey Brignoli.",
    footer_privacy="Datenschutz", footer_kofi="Ko-fi",
)

BLOG = {
"tripsweep": [
dict(slug="free-up-iphone-storage",
     title="iPhone Speicher freigeben ohne iCloud – eine praktische Anleitung",
     desc="Wohin der Speicher deines iPhones wirklich geht und wie du am schnellsten Gigabyte an Fotos und Videos freigibst, ohne mehr iCloud-Speicher zu bezahlen.",
     h1="iPhone Speicher freigeben, ohne für iCloud zu bezahlen",
     body="""      <p>„iPhone-Speicher voll“ bedeutet fast immer dasselbe: die Fotos-App. Fotos und Videos sind meist der größte Posten unter Einstellungen → Allgemein → iPhone-Speicher, und der Großteil davon ist Ballast, den du entfernen kannst, ohne eine einzige Erinnerung zu verlieren.</p>

      <h2>1. Beginne mit dem, was am meisten wiegt</h2>
      <p>Große Videos bringen den schnellsten Erfolg: Ein paar Minuten 4K-Video brauchen so viel Platz wie Hunderte Fotos. Sortiere deine Videos nach Größe, sieh dir die ersten Sekunden an und lösche die, die du nie wieder öffnen wirst. Bildschirmaufnahmen und Videos, die dir Messenger-Apps geschickt haben, sind häufige Verursacher.</p>

      <h2>2. Ähnliche Fotos löschen, nicht nur Duplikate</h2>
      <p>Die Fotos-App findet exakte Duplikate, aber die eigentliche Verschwendung sind fast identische Aufnahmen: die Serie mit zehn Bildern, fünf Versuche für dasselbe Gruppenfoto, drei Selfies hintereinander. Behalte das beste jeder Gruppe und lösche den Rest. Hier gewinnen die meisten den meisten Platz zurück, und es ist der Teil, der von Hand am schwierigsten ist.</p>

      <h2>3. Screenshots und unscharfe Fotos entfernen</h2>
      <p>Screenshots sammeln sich unbemerkt an: Tickets, Karten, Unterhaltungen, die du nicht mehr brauchst. Mit unscharfen Fotos und versehentlichen Aufnahmen ist es genauso. Sie haben selten einen Platz verdient und lassen sich als Stapel schnell durchsehen.</p>

      <h2>4. „Zuletzt gelöscht“ leeren</h2>
      <p>Gelöschte Fotos bleiben 30 Tage im Album „Zuletzt gelöscht“ und belegen weiter Speicher. Wenn du mit deiner Auswahl zufrieden bist, leere es, um den Speicherplatz tatsächlich zurückzubekommen.</p>

      <h2>5. Alte Reisen aufräumen, eine nach der anderen</h2>
      <p>Alte Urlaube sind der größte Block an Fotos, die du dir nie ansiehst. Reise für Reise vorzugehen ist einfacher, als durch eine Mediathek mit Tausenden Fotos zu scrollen: Nimm die größte Reise, behalte die Highlights, lösche den Rest.</p>

      <h2>Wie TripSweep das schneller macht</h2>
      <p><a href="{ts}">TripSweep</a> erledigt diese Schritte für dich direkt auf dem iPhone. Der Tab „Aufräumen“ listet identische Kopien, ähnliche Fotos, unscharfe Fotos, Screenshots und große Videos auf, jeweils mit dem belegten Speicherplatz. Deine Reisen sind nach Ort und Datum gruppiert und nach Größe sortiert, und die Schaltfläche „1 pro Gruppe behalten“ erledigt eine ganze Kategorie mit einem Tap. Favoriten werden nie zum Löschen vorgeschlagen, gelöscht wird über „Zuletzt gelöscht“, und nichts verlässt jemals dein Telefon: kein Konto, keine Cloud. Es können nur anonyme, abschaltbare Nutzungsstatistiken gesendet werden.</p>
      <p>Wenn du einen großen Bildschirm bevorzugst, erledigt <a href="{pc}">PhotoCull</a> dieselbe Sortierung an einem Mac oder Windows-PC.</p>

      <h2>Brauche ich iCloud?</h2>
      <p>iCloud ist ein gutes Backup, aber kein Aufräumwerkzeug: Es speichert alles, auch die Duplikate. Wer zuerst aufräumt, braucht weniger Speicherplatz, egal wo.</p>"""),
dict(slug="delete-duplicate-photos-iphone",
     title="Doppelte und ähnliche Fotos auf dem iPhone löschen",
     desc="Finde exakte Duplikate, Serienaufnahmen und fast identische Aufnahmen auf deinem iPhone, behalte die beste und lösche den Rest sicher.",
     h1="So löschst du doppelte und ähnliche Fotos auf deinem iPhone",
     body="""      <p>Duplikate fressen unbemerkt iPhone-Speicher. Manche sind exakte Kopien, die meisten aber fast identische Aufnahmen desselben Moments. So findest du beides und räumst sicher auf.</p>

      <h2>Duplikate und ähnliche Fotos sind nicht dasselbe</h2>
      <p>Ein exaktes Duplikat ist dieselbe Datei, zweimal gespeichert, zum Beispiel nach einem Import oder einem Download. Ein ähnliches Foto ist eine andere Aufnahme derselben Szene: eine Serienaufnahme, mehrere Versuche für ein Gruppenfoto, ein Selfie, das so lange wiederholt wurde, bis es gefiel. Exakte Duplikate sind leicht zu erkennen; ähnliche Fotos sind häufiger und brauchen weit mehr Platz.</p>

      <h2>Die integrierte Methode</h2>
      <p>Neuere iOS-Versionen enthalten in der Fotos-App ein Album „Duplikate“ (unter „Dienstprogramme“). Es führt exakte Kopien zusammen und ist ein guter erster Durchgang. Ähnliche Fotos gruppiert es nicht, sodass Serienaufnahmen und fast identische Aufnahmen in deiner Mediathek bleiben.</p>

      <h2>Ähnliche Fotos entfernen</h2>
      <p>Bei ähnlichen Aufnahmen musst du vergleichen und auswählen. Öffne die Gruppe, achte auf Schärfe, Gesichtsausdrücke und Bildausschnitt, behalte das beste Foto und lösche die anderen. Das bei Tausenden Fotos von Hand zu tun, dauert lange, weshalb die meisten nie fertig werden.</p>

      <h2>Schneller mit TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> findet identische Kopien und ähnliche Fotos in deiner gesamten Mediathek und zeigt jede Gruppe nebeneinander ohne Zuschnitt. Es schlägt die beste Aufnahme anhand von Schärfe, der ästhetischen Bewertung von Apple und Gesichtern vor, und die Schaltfläche „1 pro Gruppe behalten“ im Tab „Aufräumen“ sortiert eine ganze Kategorie mit einem Tap. Deine Favoriten werden nie zum Löschen vorgeschlagen.</p>

      <h2>Sicher löschen</h2>
      <ul>
        <li>Über die Fotos-App löschen: Gelöschte Fotos landen 30 Tage in „Zuletzt gelöscht“, ein Fehler lässt sich also rückgängig machen.</li>
        <li>Favoriten behalten: Markiere die Fotos, die du liebst, bevor du aufräumst.</li>
        <li>iCloud-Fotos prüfen: Wenn es aktiviert ist, wird beim Löschen auf dem iPhone überall gelöscht.</li>
        <li>Am Ende „Zuletzt gelöscht“ leeren, um den Speicherplatz zurückzubekommen.</li>
      </ul>

      <h2>Lieber auf einem großen Bildschirm?</h2>
      <p>Mit <a href="{pc}">PhotoCull</a> an einem Mac oder Windows-PC kannst du bis zu sechs ähnliche Fotos nebeneinander vergleichen und Hunderte mit wenigen Klicks markieren.</p>"""),
dict(slug="clean-up-vacation-photos",
     title="Alte Urlaubsfotos aufräumen und die besten behalten",
     desc="Aus tausend Urlaubsfotos ein Album zum Behalten machen: nach Reise gruppieren, fast identische Aufnahmen entfernen, die Highlights behalten.",
     h1="So räumst du alte Urlaubsfotos auf und behältst die besten",
     body="""      <p>Eine einwöchige Reise ergibt leicht tausend Fotos und Videos, und die meisten davon sind Beinahe-Kopien weniger guter Aufnahmen. Sie zu sortieren, solange die Reise frisch ist, ist einfach; ein Jahr später ist es eine lästige Pflicht. Diese Methode funktioniert für beides.</p>

      <h2>1. Reise für Reise vorgehen</h2>
      <p>Eine Mediathek mit 20.000 Fotos ist überwältigend, eine Reise mit 800 Fotos nicht. Gruppiere deine Fotos anhand von Datum und Ort nach Reisen und bearbeite jeweils eine Reise, beginnend mit der größten.</p>

      <h2>2. Zuerst die fast identischen Aufnahmen entfernen</h2>
      <p>Der Großteil einer Reise besteht aus Variationen derselben Szene. Behalte in jeder Gruppe die schärfste mit den besten Gesichtsausdrücken und lösche die anderen. Allein das halbiert oft die Größe einer Reise.</p>

      <h2>3. Den Rest durchsehen: Screenshots, unscharfe Fotos, große Videos</h2>
      <p>Tickets, Karten, versehentliche Fotos und lange Videos, die du dir nie wieder ansiehst, lassen sich leicht entfernen, sobald sie zusammen aufgelistet sind.</p>

      <h2>4. Vor dem Löschen sichern oder teilen</h2>
      <p>Exportiere die Fotos, die du behalten willst, auf deinen Computer oder teile sie mit den Freunden, die dabei waren. Erst dann löschst du die Reise von deinem Telefon. Gelöschtes landet in „Zuletzt gelöscht“, wo du 30 Tage Zeit hast, es dir anders zu überlegen.</p>

      <h2>5. Fotos ohne GPS</h2>
      <p>Fotos, die ohne Standort aufgenommen oder aus Nachrichten gespeichert wurden, haben keinen Ort. Gruppiere sie stattdessen nach Ereignis und Monat, damit auch sie sortiert werden.</p>

      <h2>Wie TripSweep hilft</h2>
      <p><a href="{ts}">TripSweep</a> gruppiert deine Fotos und Videos nach Reise (oder nach Ereignis und Monat, wenn es kein GPS gibt), zeigt, wie viele Gigabyte ähnlicher Fotos jede Reise enthält, schlägt die beste Aufnahme jeder Gruppe vor und exportiert oder teilt eine ganze Reise. Du kannst Zuhause und Arbeit ausschließen, damit der Alltag nicht wie eine Reise aussieht. Alles läuft auf deinem iPhone, offline.</p>
      <p>Um dasselbe auf einem großen Bildschirm zu tun, zeigt <a href="{pc}">PhotoCull</a> die Reisen deines iPhones an einem Mac oder Windows-PC.</p>"""),
],
"photocull": [
dict(slug="sort-photos-on-computer",
     title="Tausende Fotos am Mac oder Windows-PC schneller sortieren",
     desc="Warum das Sortieren von Fotos auf einem großen Bildschirm so viel schneller geht als am Telefon, und eine einfache Methode, Tausende Fotos in einer Sitzung durchzugehen.",
     h1="So sortierst du Tausende Fotos schneller am Mac oder PC",
     body="""      <p>Wenn deine Fotomediathek zehntausend Fotos enthält, ist das Sortieren auf dem Telefonbildschirm ein Projekt, das du nie abschließen wirst. Am Computer kann es ein einziger Abend sein. Hier steht, warum, und eine Methode, die funktioniert.</p>

      <h2>Warum ein Computer schneller ist</h2>
      <ul>
        <li><strong>Mehr auf dem Bildschirm:</strong> Dutzende Fotos auf einmal statt einer Handvoll.</li>
        <li><strong>Präzise Auswahl:</strong> Mit Maus und Tastatur wählst du Hunderte Fotos in Sekunden aus.</li>
        <li><strong>Echter Vergleich:</strong> Ähnliche Fotos nebeneinander, in einer Größe, in der Schärfe und Gesichtsausdrücke sichtbar sind.</li>
      </ul>

      <h2>Eine Methode, die funktioniert</h2>
      <p><strong>1. Nach Reisen gruppieren.</strong> Das Sortieren nach Datum und Ort teilt die Mediathek in überschaubare Stücke. Beginne mit der Reise, die am meisten Platz belegt.</p>
      <p><strong>2. Die Beinahe-Kopien entfernen.</strong> Vergleiche jede Gruppe ähnlicher Aufnahmen, behalte die beste und markiere den Rest.</p>
      <p><strong>3. Störendes ausfiltern.</strong> Blende Orte aus, die dich nicht interessieren (Zuhause, Arbeit), damit echte Reisen hervortreten, und filtere nach Größe, um schwere Dateien zu finden.</p>
      <p><strong>4. Auf einmal löschen.</strong> Markiere Hunderte Fotos und bestätige einmal.</p>

      <h2>PhotoCull macht genau das</h2>
      <p><a href="{pc}">PhotoCull</a> ist eine kostenlose Desktop-App für Mac und Windows. Die Ansicht „Reisen“ gruppiert die Mediathek nach Reisen und zeigt den Speicherplatz jeder Reise, ähnliche Fotos tragen eine Markierung, und du kannst bis zu sechs nebeneinander vergleichen. Sie liest ein iPhone per USB oder einen beliebigen Ordner auf deinem Computer, arbeitet 100 % auf dem Gerät und verändert deine Originale nie.</p>
      <p>Löschungen auf einem iPhone laufen über die kostenlose <a href="{ts}">TripSweep-App</a> und „Zuletzt gelöscht“, sodass sich ein Fehler 30 Tage lang rückgängig machen lässt. Das Sortieren eines Ordners auf deinem Computer ist nie begrenzt.</p>

      <h2>Tipps für eine lange Sitzung</h2>
      <ul>
        <li>Reise für Reise vorgehen, nicht durch die ganze Mediathek scrollen.</li>
        <li>Schnell entscheiden: Wenn zwei Aufnahmen gleich aussehen, behalte eine.</li>
        <li>Am Ende jeder Reise löschen, damit der Fortschritt sichtbar ist.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="iPhone Speicher freigeben: vom Mac oder Windows-PC aus aufräumen",
     desc="Schließe dein iPhone an, sortiere Fotos auf einem großen Bildschirm und lösche, was du nicht brauchst – ohne iCloud und ohne dass etwas online gesendet wird.",
     h1="So gibst du iPhone Speicher von einem Mac oder Windows-PC aus frei",
     body="""      <p>Ein volles iPhone am iPhone selbst aufzuräumen ist mühsam. Am Computer siehst du weit mehr Fotos auf einmal und entscheidest schneller. Hier der ganze Ablauf.</p>

      <h2>Was du brauchst</h2>
      <ul>
        <li>Einen Mac (Apple Silicon, macOS 11+) oder einen Windows-10/11-PC.</li>
        <li>Ein USB-Kabel. Unter Windows zusätzlich die kostenlose App Apple Devices aus dem Microsoft Store.</li>
        <li><a href="{pc}">PhotoCull</a>, kostenlos für beide Systeme.</li>
        <li>Zum Löschen vom iPhone: die kostenlose <a href="{ts}">TripSweep-App</a> auf dem iPhone.</li>
      </ul>

      <h2>Schritt für Schritt</h2>
      <p><strong>1. Verbinden und vertrauen.</strong> Schließe das iPhone an, entsperre es und tippe auf „Vertrauen“.</p>
      <p><strong>2. Die Ansicht „Reisen“ öffnen.</strong> PhotoCull gruppiert deine Fotomediathek nach Reisen und zeigt den Speicherplatz jeder Reise.</p>
      <p><strong>3. Die größten Reisen sortieren.</strong> Vergleiche ähnliche Aufnahmen, behalte die beste und markiere den Rest, dazu Screenshots und große Videos, die du nicht brauchst.</p>
      <p><strong>4. Das Löschen bestätigen.</strong> Vom Mac aus wird das Löschen von TripSweep über „Zuletzt gelöscht“ auf dem iPhone ausgeführt, unter Windows ebenso. Nichts wird sofort endgültig gelöscht.</p>
      <p><strong>5. „Zuletzt gelöscht“ leeren.</strong> Der Speicherplatz kommt zurück, sobald das Album geleert ist.</p>

      <h2>Ist das sicher?</h2>
      <p>Ja: Deine Fotos bleiben auf deinen Geräten, ohne Konto, ohne Cloud und ohne Upload. Gelöschte Fotos bleiben 30 Tage in „Zuletzt gelöscht“, und PhotoCull liest deine Fotos nur, bis du bestätigst.</p>

      <h2>Wie viele Fotos kann ich pro Tag löschen?</h2>
      <p>Vom Mac aus erlaubt die kostenlose Version 6 Fotos pro Tag, TripSweep Pro 15, und Pro + Desktop ist unbegrenzt (siehe die Tarife auf der TripSweep-Seite). Alles sind Einmalkäufe ohne Abo. Durchsehen, Vergleichen und Sortieren sind kostenlos, und das Sortieren eines Ordners auf deinem Computer ist nie begrenzt.</p>

      <h2>Unter Windows</h2>
      <p>Die Schritte sind unter Windows 10 und 11 dieselben. Installiere zuerst die kostenlose App Apple Devices aus dem Microsoft Store, damit PhotoCull das iPhone lesen kann. Die App ist noch nicht codesigniert, daher warnt SmartScreen beim ersten Start eventuell.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Ähnliche Fotos nebeneinander vergleichen und das beste behalten",
     desc="Eine einfache Routine, um unter fast identischen Fotos die beste Aufnahme zu wählen: worauf du achten solltest und wie es auf einem großen Bildschirm schnell geht.",
     h1="So vergleichst du ähnliche Fotos und behältst das beste",
     body="""      <p>Du hast sechs Fotos desselben Moments gemacht und alle sehen gut aus. Mit der richtigen Methode dauert die Wahl der besten Sekunden, mit der falschen mehrere Minuten.</p>

      <h2>Worauf du achten solltest, in dieser Reihenfolge</h2>
      <ol>
        <li><strong>Schärfe.</strong> Zoome auf die Augen oder das Hauptmotiv. Ein unscharfes Motiv ist ein Ausschlusskriterium.</li>
        <li><strong>Gesichtsausdrücke.</strong> Augen offen, natürliches Lächeln, niemand mitten im Blinzeln.</li>
        <li><strong>Bildausschnitt.</strong> Nichts abgeschnitten, ein sauberer Hintergrund, ein gerader Horizont.</li>
        <li><strong>Moment.</strong> Wenn zwei Aufnahmen gleich gut sind, behalte die, die lebendiger wirkt.</li>
      </ol>

      <h2>Warum nebeneinander wichtig ist</h2>
      <p>Beim Hin- und Herblättern zwischen Fotos sind kleine Unterschiede schwer zu erkennen. Nebeneinander in gleicher Größe wird die schärfste oder am besten komponierte Aufnahme offensichtlich. Ein Computerbildschirm zeigt bis zu sechs auf einmal, wo ein Telefon nur eine zeigt.</p>

      <h2>Eine schnellere Routine</h2>
      <p>Gruppiere ähnliche Fotos zuerst, damit du sie nie in der Mediathek suchen musst. Öffne für jede Gruppe den Vergleich, wähle eines aus und markiere die anderen. Du entscheidest in Sekunden, nicht in Minuten.</p>

      <h2>Mit PhotoCull</h2>
      <p><a href="{pc}">PhotoCull</a> zeigt eine Markierung an ähnlichen Fotos, öffnet bis zu sechs nebeneinander und lässt dich den Rest mit einem Klick markieren. Es funktioniert mit einem per USB verbundenen iPhone oder mit jedem Ordner auf deinem Mac oder PC, offline, und verändert deine Originale nie.</p>
      <p>Auf dem Telefon selbst schlägt die <a href="{ts}">TripSweep-App</a> die beste Aufnahme jeder Gruppe anhand von Schärfe, der ästhetischen Bewertung von Apple und Gesichtern vor, und ihre Schaltfläche „1 pro Gruppe behalten“ erledigt eine ganze Kategorie auf einmal.</p>

      <h2>Behalten statt bereuen</h2>
      <p>Wenn du unsicher bist, behalte zwei. Löschungen auf einem iPhone laufen 30 Tage über „Zuletzt gelöscht“, du kannst es dir also noch anders überlegen.</p>"""),
],
}
