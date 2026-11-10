# -*- coding: utf-8 -*-
# Deutsche Fassung der FAQ und des Blogs beider Websites. Tokens in Antworten/Artikeln: {ts} {pc} {store} {mac} {win} (siehe link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Datenschutz", more="Weiterlesen",
    cta_store="📱 TripSweep im App Store laden",
    cta_play="🤖 TripSweep bei Google Play laden",
    cta_mac="💻 PhotoCull für Mac laden", cta_win="🪟 PhotoCull für Windows laden",
    cross_label={"tripsweep": "Desktop-App", "photocull": "Mobile App"},
    twin_android="Du nutzt ein Android-Telefon? Lies die Android-Anleitung:",
    twin_iphone="Du nutzt ein iPhone? Lies die iPhone-Anleitung:",
    index={
        "tripsweep": dict(
            title="TripSweep Blog – doppelte Fotos löschen, Speicher freigeben",
            desc="Praktische Anleitungen: iPhone-Speicher freigeben, doppelte und ähnliche Fotos löschen, alte Reisen aufräumen – ohne iCloud und ohne Upload deiner Fotos.",
            h1="Anleitungen zum Aufräumen deiner iPhone-Fotos",
            intro="Kurze, praktische Anleitungen, um Speicherplatz auf deinem iPhone freizugeben, Duplikate zu löschen und nur die besten Aufnahmen zu behalten."),
        "photocull": dict(
            title="PhotoCull Blog – Fotos am Mac oder PC sortieren",
            desc="Tausende Fotos am großen Bildschirm schneller sortieren, ähnliche Aufnahmen vergleichen und iPhone oder Android-Telefon vom Mac oder PC aus aufräumen.",
            h1="Anleitungen zum Sortieren deiner Fotos am Computer",
            intro="Warum ein großer Bildschirm das Sortieren von Fotos so viel schneller macht und wie du damit dein iPhone oder Android-Telefon aufräumst."),
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
     "TripSweep benötigt iOS 18 oder neuer. Die Analyse ähnlicher Fotos nutzt das Vision-Framework von Apple und ist auf neueren iPhones schneller, funktioniert aber auf jedem unterstützten Modell. Auf Android braucht TripSweep Android 11 oder neuer und ist bei <a href=\"{play}\">Google Play</a> erhältlich."),
]

FAQ_PHOTOCULL = dict(
    title="PhotoCull FAQ – Fotos am Mac oder PC sortieren und löschen",
    desc="Tausende Fotos am Computer sortieren, ähnliche Aufnahmen vergleichen, iPhone oder Android-Telefon vom Mac oder PC aus aufräumen: Antworten zu PhotoCull.",
    nav_home="PhotoCull", nav_desktop="Mobile App",
    h1="Fragen und Antworten",
    intro="Wie du deine Fotos am Computer schneller sortierst, dein iPhone oder Android-Telefon von einem Mac oder PC aus aufräumst und was PhotoCull mit deinen Fotos macht (und nie macht).",
    qa=[
        ('Wie sortiere ich meine iPhone-Fotos am Computer, Mac oder PC?',
         "Verbinde das iPhone per USB-Kabel mit dem Computer, entsperre es und tippe auf „Vertrauen“, dann öffne <a href=\"{pc}\">PhotoCull</a>: Es gruppiert deine Fotorolle nach Reise, vergleicht ähnliche Aufnahmen nebeneinander und markiert Hunderte Fotos mit wenigen Klicks. Schritt-für-Schritt-Anleitungen: <a href=\"{post:sort-iphone-photos-on-mac}\">am Mac</a> und <a href=\"{post:sort-iphone-photos-on-pc}\">am Windows-PC</a>."),
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
        ("Kann ich die Fotos eines Android-Telefons an meinem Mac oder PC sortieren?",
         "Ja. PhotoCull verbindet sich mit einem Android-Telefon per WLAN an einem Mac oder Windows-PC oder per USB unter Windows. Du bekommst dieselbe Reiseansicht, denselben Vergleich nebeneinander und dasselbe gesammelte Löschen wie beim iPhone. Das Telefon braucht die kostenlose <a href=\"{play}\">TripSweep-App</a> (Android 11 oder neuer), geöffnet im Tab „Löschen“."),
        ("Wie verbinde ich mein Android-Telefon per WLAN?",
         "Bringe Telefon und Computer in dasselbe WLAN und öffne in TripSweep auf dem Telefon den Tab „Löschen“. Klicke in PhotoCull auf „Android-Telefon“ und wähle dein Telefon, dann erlaubst du den Computer auf dem Telefon: Auf beiden Bildschirmen erscheint derselbe 4-stellige Code. Das machst du nur einmal; beim nächsten Mal verbindet es sich von selbst. <a href=\"{post:sort-android-photos-on-mac}\">Schritt-für-Schritt-Anleitung für den Mac</a>."),
        ("Warum sieht mein Mac mein Android-Telefon nicht per USB?",
         "macOS unterstützt die Art, wie Android-Telefone Dateien per USB freigeben (MTP), von Haus aus nicht, deshalb sieht ein Mac sie meist nicht. Nutze stattdessen die WLAN-Verbindung: Sie funktioniert an jedem Mac, ohne Treiber. Unter Windows funktionieren USB und WLAN."),
        ("Ist die WLAN-Verbindung zu meinem Telefon sicher?",
         "Ja. Telefon und Computer sprechen nur in deinem lokalen Netzwerk miteinander, über eine verschlüsselte Verbindung, und erst nachdem du den Computer auf dem Telefon mit einem übereinstimmenden Code erlaubt hast. Nichts läuft über das Internet, und du kannst einen Computer jederzeit in TripSweep wieder sperren."),
        ("Was passiert mit Fotos, die ich auf einem Android-Telefon lösche?",
         "Du bestätigst das Löschen auf dem Telefon in TripSweep, und die Fotos landen im Papierkorb des Telefons, wo sie 30 Tage bleiben und wiederhergestellt werden können. PhotoCull löscht von sich aus nie etwas endgültig."),
        ("Brauche ich die iOS-App TripSweep?",
         "Nicht zum Durchsehen, Vergleichen und Sortieren eines iPhones. Du brauchst sie nur, um Fotos vom iPhone zu löschen, weil das Löschen auf dem Telefon ausgeführt wird. Ein Android-Telefon braucht die TripSweep-App für Android, um sich überhaupt zu verbinden. Ordner auf deinem Computer lassen sich auch ohne beide sortieren."),
        ("Wie finde ich doppelte Fotos in einem Ordner auf meinem Mac oder PC?",
         "Öffne den Ordner in PhotoCull („Ordner öffnen“ oder per Drag-and-drop ins Fenster ziehen). Die App durchsucht auch die Unterordner, vergleicht, was auf den Fotos zu sehen ist, und versieht exakte Kopien, Serienaufnahmen und fast identische Aufnahmen mit demselben „≈ N“-Abzeichen. Behalte die beste Aufnahme jeder Gruppe und schicke den Rest in den Papierkorb. Anleitungen: <a href=\"{post:find-duplicate-photos-on-mac}\">am Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">unter Windows</a>."),
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
dict(slug="free-up-android-storage",
     title="Android-Speicher freigeben ohne Google One",
     desc="Wohin der Speicher deines Android-Telefons wirklich geht und wie du am schnellsten Gigabyte an Fotos und Videos freigibst, ohne mehr Cloud-Speicher zu bezahlen.",
     h1="Android-Speicher freigeben, ohne für Google One zu bezahlen",
     body="""      <p>„Speicher voll“ auf einem Android-Telefon bedeutet fast immer: Fotos und Videos. Das zeigt dir Einstellungen → Speicher deutlich, und der Großteil davon sind Aufnahmen, die du dir nie wieder ansehen wirst. So bekommst du den Platz zurück, ohne mehr Cloud-Speicher zu kaufen.</p>

      <h2>1. Beginne mit dem, was am meisten wiegt</h2>
      <p>Große Videos bringen den schnellsten Erfolg: Ein paar Minuten 4K-Video brauchen so viel Platz wie Hunderte Fotos. Sortiere sie nach Größe, sieh dir die ersten Sekunden an und lösche die, die du nie wieder öffnen wirst.</p>

      <h2>2. Ähnliche Fotos löschen, nicht nur Duplikate</h2>
      <p>Aufräum-Apps finden exakte Kopien, aber die eigentliche Verschwendung sind fast identische Aufnahmen: Serienaufnahmen, fünf Versuche für dasselbe Gruppenfoto, drei Selfies hintereinander. Behalte das beste jeder Gruppe und lösche den Rest.</p>

      <h2>3. Screenshots und unscharfe Fotos entfernen</h2>
      <p>Screenshots von Tickets, Karten und Unterhaltungen sammeln sich unbemerkt an, ebenso unscharfe oder versehentliche Aufnahmen. Als Stapel lassen sie sich schnell durchsehen.</p>

      <h2>4. Den Papierkorb leeren</h2>
      <p>Gelöschte Fotos warten meist 30 Tage im Papierkorb und belegen weiter Speicher. Wenn du mit deiner Auswahl zufrieden bist, leere ihn, um den Speicherplatz tatsächlich zurückzubekommen.</p>

      <h2>5. Alte Reisen aufräumen, eine nach der anderen</h2>
      <p>Alte Urlaube sind der größte Block an Fotos, die du dir nie ansiehst. Reise für Reise vorzugehen ist einfacher, als durch Tausende Fotos zu scrollen: Nimm die größte Reise, behalte die Highlights, lösche den Rest.</p>

      <h2>Wie TripSweep das schneller macht</h2>
      <p><a href="{ts}">TripSweep</a> erledigt diese Schritte für dich direkt auf dem Telefon. Der Tab „Aufräumen“ listet identische Kopien, ähnliche Fotos, unscharfe Fotos, Screenshots und große Videos auf, jeweils mit dem belegten Speicherplatz, und deine Reisen werden automatisch gruppiert. Die App ist kostenlos bei <a href="{play}">Google Play</a> erhältlich (Android 11 oder neuer) und arbeitet 100 % auf dem Telefon.</p>
      <p>Wenn du einen großen Bildschirm bevorzugst, erledigt <a href="{pc}">PhotoCull</a> dieselbe Sortierung an einem Mac oder Windows-PC, verbunden per WLAN.</p>

      <h2>Brauche ich Google One?</h2>
      <p>Cloud-Speicher ist ein gutes Backup, aber kein Aufräumwerkzeug: Er speichert alles, auch die Duplikate. Wer zuerst aufräumt, braucht weniger Speicherplatz, egal wo.</p>"""),
dict(slug="delete-duplicate-photos-android",
     title="Doppelte und ähnliche Fotos auf Android löschen",
     desc="Finde exakte Duplikate, Serienaufnahmen und fast identische Aufnahmen auf deinem Android-Telefon, behalte die beste und lösche den Rest sicher.",
     h1="So löschst du doppelte und ähnliche Fotos auf deinem Android-Telefon",
     body="""      <p>Duplikate fressen unbemerkt den Speicher eines Android-Telefons. Manche sind exakte Kopien, die meisten aber fast identische Aufnahmen desselben Moments. So findest du beides und räumst sicher auf.</p>

      <h2>Duplikate und ähnliche Fotos sind nicht dasselbe</h2>
      <p>Ein exaktes Duplikat ist dieselbe Datei, zweimal gespeichert, zum Beispiel nach einem Download, einer Messenger-App oder einer Wiederherstellung. Ein ähnliches Foto ist eine andere Aufnahme derselben Szene: eine Serienaufnahme, mehrere Versuche für ein Gruppenfoto, ein Selfie, das so lange wiederholt wurde, bis es gefiel. Datei-Reiniger finden die erste Art; die zweite braucht weit mehr Platz.</p>

      <h2>Was Android bietet</h2>
      <p>Datei-Manager-Apps können exakte Duplikate auflisten, und deine Galerie zeigt Serienaufnahmen. Keine von beiden vergleicht fast identische Aufnahmen für dich oder hilft dir, die beste zu wählen, sodass du am Ende Foto für Foto hin und her blätterst.</p>

      <h2>Ein schnellerer Weg</h2>
      <p><strong>1. Nach Szene gruppieren.</strong> <a href="{ts}">TripSweep</a> vergleicht den Inhalt deiner Fotos, nicht ihre Namen, und gruppiert Aufnahmen derselben Szene, sodass aus einer Serie von zehn Bildern eine einzige Entscheidung wird.</p>
      <p><strong>2. Die beste behalten.</strong> Es schlägt ein Foto pro Gruppe vor; du kannst ein anderes behalten, mehrere behalten oder die Gruppe überspringen.</p>
      <p><strong>3. Sicher löschen.</strong> Gelöschte Fotos landen 30 Tage im Papierkorb des Telefons, ein Fehler lässt sich also rückgängig machen.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles läuft auf dem Telefon: kein Konto, kein Upload. TripSweep ist kostenlos bei <a href="{play}">Google Play</a> erhältlich (Android 11 oder neuer).</li>
        <li>Für eine ganze Fotorolle geht der Vergleich am großen Bildschirm mit <a href="{pc}">PhotoCull</a> an einem Mac oder PC noch schneller.</li>
      </ul>"""),
],
"photocull": [
dict(slug="sort-iphone-photos-on-mac",
     title="iPhone-Fotos am Mac sortieren: so geht's",
     desc="Tausende iPhone-Fotos am Mac sortieren: was Fotos und Digitale Bilder können und was nicht, und ein schnellerer Weg zum Gruppieren und Löschen.",
     h1="So sortierst du deine iPhone-Fotos am Mac",
     body="""      <p>Eine volle Fotorolle auf dem iPhone zu sortieren heißt stundenlang tippen. Am Mac siehst du viel mehr Fotos auf einmal, wählst mit der Maus aus und vergleichst Aufnahmen auf einem großen Bildschirm. So geht es, mit den Werkzeugen von macOS und mit einer eigenen App.</p>

      <h2>Mit den Werkzeugen von macOS</h2>
      <ul>
        <li><strong>Fotos:</strong> importiert eine Kopie deiner iPhone-Fotos auf den Mac. Nützlich als Backup, aber es sagt dir nicht, was du auf dem iPhone löschen kannst.</li>
        <li><strong>Digitale Bilder:</strong> listet die Fotos des iPhone als einfache Dateien auf, ohne Gruppierung nach Reise und ohne Vergleich ähnlicher Aufnahmen.</li>
      </ul>
      <p>Beides funktioniert, aber bei Tausenden Fotos scrollst du trotzdem durch eine einzige lange Liste.</p>

      <h2>Mit PhotoCull, Schritt für Schritt</h2>
      <p><strong>1. PhotoCull installieren.</strong> <a href="{mac}">Kostenlos herunterladen</a>: macOS 11 oder neuer auf Apple Silicon, von Apple signiert und notarisiert.</p>
      <p><strong>2. iPhone anschließen.</strong> Verbinde es per USB-Kabel, entsperre es und tippe auf „Vertrauen“.</p>
      <p><strong>3. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert deine Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Fang mit der größten an.</p>
      <p><strong>4. Vergleichen und markieren.</strong> Ähnliche Fotos tragen ein Abzeichen: Öffne bis zu sechs nebeneinander, behalte das beste und markiere den Rest, dazu Bildschirmfotos und große Videos, die du nicht brauchst.</p>
      <p><strong>5. Sicher löschen.</strong> Die Löschung wird auf dem iPhone von der kostenlosen <a href="{ts}">TripSweep-App</a> über „Zuletzt gelöscht“ ausgeführt: Du hast 30 Tage Zeit, es dir anders zu überlegen.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles bleibt auf deinem Mac und deinem iPhone: kein Konto, keine Cloud, kein Upload.</li>
        <li>PhotoCull verändert nie deine Originale und löscht nur, was du bestätigst.</li>
        <li>Vom Mac aus erlaubt die Gratisversion 6 Löschungen pro Tag, TripSweep Pro 15, und Pro + Desktop ist unbegrenzt. Durchsehen und Sortieren sind kostenlos, und das Sortieren eines Fotoordners auf dem Mac ist nie begrenzt.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="iPhone-Fotos am Windows-PC sortieren: so geht's",
     desc="Tausende iPhone-Fotos unter Windows 10 oder 11 sortieren: was die Fotos-App und der Explorer zeigen, und ein schnellerer Weg zum Sortieren und Löschen.",
     h1="So sortierst du deine iPhone-Fotos am Windows-PC",
     body="""      <p>iPhone, aber ein Windows-Computer? Du kannst deine Fotos trotzdem auf einem großen Bildschirm sortieren statt auf dem Telefon. Hier steht, was Windows allein kann, und ein schnellerer Weg.</p>

      <h2>Mit den Werkzeugen von Windows</h2>
      <ul>
        <li><strong>Fotos-App:</strong> importiert eine Kopie deiner iPhone-Fotos auf den PC. Gut als Backup, aber sie hilft dir nicht bei der Entscheidung, was weg kann.</li>
        <li><strong>Datei-Explorer:</strong> zeigt die Fotos des iPhone in Ordnern wie 100APPLE, benannt IMG_0001 und so weiter, ohne Reisen und ohne Vergleich ähnlicher Aufnahmen.</li>
      </ul>

      <h2>Mit PhotoCull, Schritt für Schritt</h2>
      <p><strong>1. Apple Devices installieren.</strong> Installiere die kostenlose App Apple Devices aus dem Microsoft Store: Windows braucht sie, um ein iPhone zu lesen.</p>
      <p><strong>2. PhotoCull installieren.</strong> Aus dem Microsoft Store oder <a href="{win}">kostenlos herunterladen</a> (Windows 10/11, 64 Bit). Der Download ist noch nicht signiert, daher kann SmartScreen beim ersten Start warnen.</p>
      <p><strong>3. iPhone anschließen.</strong> Verbinde es per USB-Kabel, entsperre es und tippe auf „Vertrauen“.</p>
      <p><strong>4. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert deine Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Fang mit der größten an.</p>
      <p><strong>5. Vergleichen, markieren, löschen.</strong> Ähnliche Fotos tragen ein Abzeichen: Vergleiche bis zu sechs nebeneinander, behalte das beste und markiere den Rest. Die Löschung wird auf dem iPhone von der kostenlosen <a href="{ts}">TripSweep-App</a> über „Zuletzt gelöscht“ ausgeführt: Du hast 30 Tage Zeit, es dir anders zu überlegen.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles bleibt auf deinem PC und deinem iPhone: kein Konto, keine Cloud, kein Upload.</li>
        <li>PhotoCull verändert nie deine Originale und löscht nur, was du bestätigst.</li>
        <li>Durchsehen und Sortieren sind kostenlos, und das Sortieren eines Fotoordners, der schon auf dem PC liegt, ist nie begrenzt.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Tausende Fotos am Mac oder Windows-PC schneller sortieren",
     desc="Warum das Sortieren am großen Bildschirm so viel schneller geht als am Telefon – und eine einfache Methode für Tausende Fotos in einer Sitzung.",
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
     desc="Eine einfache Routine, um unter fast identischen Fotos die beste Aufnahme zu wählen: worauf du achtest und wie es am großen Bildschirm schnell geht.",
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
dict(slug="find-duplicate-photos-on-mac",
     title="Doppelte und ähnliche Fotos am Mac finden und löschen",
     desc="Doppelte Fotos am Mac finden: exakte Kopien, Serien und fast identische Aufnahmen in Ordnern oder auf einer externen Festplatte, den Rest in den Papierkorb.",
     h1="So findest du doppelte und ähnliche Fotos am Mac",
     body="""      <p>Jahre voller Importe, Speicherkarten und Backups verteilen dieselben Fotos auf viele Ordner deines Macs. Manche sind exakte Kopien, die meisten sind fast identische Aufnahmen desselben Moments. So findest du beides, behältst die beste Aufnahme und gibst Speicherplatz frei, ohne deine Fotos-Mediathek anzufassen.</p>

      <h2>Was macOS bietet</h2>
      <ul>
        <li><strong>Finder:</strong> Ein Ordner nach Name oder Größe sortiert verrät offensichtliche Kopien wie „IMG_1234 Kopie.jpg“, aber keine zwei verschiedenen Aufnahmen derselben Szene.</li>
        <li><strong>Fotos:</strong> Das Album „Duplikate“ deckt nur Fotos ab, die schon in der Fotos-Mediathek liegen, nicht deine anderen Ordner oder Festplatten.</li>
      </ul>

      <h2>Mit PhotoCull, Schritt für Schritt</h2>
      <p><strong>1. PhotoCull installieren.</strong> <a href="{mac}">Kostenlos herunterladen</a>: macOS 11 oder neuer auf Apple Silicon, von Apple signiert und notarisiert.</p>
      <p><strong>2. Ordner öffnen.</strong> Klicke auf „Ordner öffnen“ oder ziehe einen Ordner ins Fenster. Unterordner sind eingeschlossen, ebenso externe Festplatten.</p>
      <p><strong>3. Auf die Abzeichen achten.</strong> PhotoCull vergleicht den Inhalt der Fotos, nicht ihre Namen: Exakte Kopien, Serienaufnahmen und fast identische Aufnahmen tragen dasselbe „≈ N“-Abzeichen.</p>
      <p><strong>4. Die beste Aufnahme behalten.</strong> Öffne eine Gruppe, vergleiche bis zu sechs Fotos nebeneinander, behalte das schärfste und markiere den Rest.</p>
      <p><strong>5. Sicher löschen.</strong> Markierte Dateien landen im Papierkorb deines Macs, wo du sie mit „Zurücklegen“ wiederherstellen kannst, falls du es dir anders überlegst.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Unterstützt werden JPEG, HEIC, PNG, TIFF, WebP und RAW-Dateien (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sowie MOV- und MP4-Videos.</li>
        <li>Fotos werden nach ihren EXIF-Daten datiert, kopierte Ordner sortieren sich also weiterhin nach dem Tag der Aufnahme.</li>
        <li>Das Sortieren eines Ordners ist kostenlos und nie begrenzt. Alles läuft auf deinem Mac: kein Konto, kein Upload.</li>
        <li>Fotos-Mediatheken und App-Pakete im Ordner werden übersprungen, PhotoCull wühlt also nie in den Dateien einer anderen App.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Doppelte und ähnliche Fotos unter Windows finden",
     desc="Doppelte Fotos unter Windows finden: exakte Kopien, Serien und fast identische Aufnahmen in Ordnern oder auf externen Festplatten, den Rest in den Papierkorb.",
     h1="So findest du doppelte und ähnliche Fotos unter Windows 10 oder 11",
     body="""      <p>Handy-Backups, Speicherkarten und alte Kopien legen dieselben Fotos in mehreren Ordnern deines PCs ab. Manche sind exakte Duplikate, die meisten sind fast identische Aufnahmen. So findest du beides und räumst sicher auf.</p>

      <h2>Was Windows bietet</h2>
      <ul>
        <li><strong>Datei-Explorer:</strong> Sortieren nach Name, Größe oder Datum hilft bei offensichtlichen Kopien, erkennt aber nicht, dass zwei verschiedene Dateien dieselbe Szene zeigen.</li>
        <li><strong>Fotos-App:</strong> gut zum Ansehen und Importieren, aber ohne Werkzeug, um ähnliche Aufnahmen zu finden und die beste auszuwählen.</li>
      </ul>

      <h2>Mit PhotoCull, Schritt für Schritt</h2>
      <p><strong>1. PhotoCull installieren.</strong> Kostenlos <a href="{win}">für Windows 10 oder 11</a> (64 Bit) herunterladen oder aus dem Microsoft Store holen.</p>
      <p><strong>2. Ordner öffnen.</strong> Klicke auf „Ordner öffnen“ oder ziehe einen Ordner ins Fenster. Unterordner und externe Festplatten sind eingeschlossen.</p>
      <p><strong>3. Auf die Abzeichen achten.</strong> PhotoCull vergleicht, was die Fotos zeigen, nicht ihre Dateinamen: Exakte Kopien, Serienaufnahmen und fast identische Aufnahmen tragen dasselbe „≈ N“-Abzeichen.</p>
      <p><strong>4. Die beste Aufnahme behalten.</strong> Vergleiche bis zu sechs Fotos nebeneinander, behalte das schärfste und markiere den Rest.</p>
      <p><strong>5. Sicher löschen.</strong> Markierte Dateien landen im Papierkorb, du kannst sie also wiederherstellen.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Unterstützt werden JPEG, HEIC, PNG, TIFF, WebP und RAW-Dateien (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sowie MOV- und MP4-Videos. Für HEIC-Vorschaubilder braucht Windows die kostenlosen HEIF-Bilderweiterungen von Microsoft.</li>
        <li>Fotos werden nach ihren EXIF-Daten datiert, kopierte Ordner sortieren sich also weiterhin nach dem Tag der Aufnahme.</li>
        <li>Das Sortieren eines Ordners ist kostenlos und nie begrenzt. Alles läuft auf deinem PC: kein Konto, kein Upload.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Großen Fotoordner oder externe Festplatte sortieren",
     desc="Alte Backups, Speicherkarten, eine externe Festplatte voller Fotos: eine einfache Methode, Tausende Dateien nach Reisen zu sortieren und Doppelte zu entfernen.",
     h1="So sortierst du einen großen Fotoordner oder eine ganze externe Festplatte",
     body="""      <p>Jeder hat so einen: einen Ordner „Fotos sortieren“, ein altes Handy-Backup, eine externe Festplatte, die über zehn Jahre voll geworden ist. Tausende Dateien, keine Ordnung, viele fast identische Aufnahmen. Hier eine Methode, die du in einer Sitzung schaffst.</p>

      <h2>1. Den ganzen Ordner auf einmal öffnen</h2>
      <p>Geh nicht Ordner für Ordner vor. Öffne den obersten Ordner in <a href="{pc}">PhotoCull</a> („Ordner öffnen“ oder ins Fenster ziehen): Unterordner sind eingeschlossen, und jedes Foto wird nach seinen EXIF-Daten datiert, nicht nach dem Tag, an dem es kopiert wurde.</p>

      <h2>2. Die Reisen sichtbar machen</h2>
      <p>Die Ansicht „Reisen“ gruppiert Fotos nach Datum und Ort und zeigt den Speicherplatz jeder Gruppe. Zehn Jahre Dateien werden zu einer Liste von Reisen und Ereignissen, und du beginnst mit der größten.</p>

      <h2>3. Die Beinahe-Kopien zusammenfassen</h2>
      <p>Serienaufnahmen, wiederholte Versuche und Kopien derselben Aufnahme tragen ein „≈ N“-Abzeichen. Vergleiche bis zu sechs nebeneinander, behalte die beste und markiere den Rest. Allein dieser Schritt entfernt oft einen großen Teil der Dateien.</p>

      <h2>4. Das Offensichtliche markieren</h2>
      <p>Bildschirmfotos, verwackelte Aufnahmen, versehentliche Videos: Markiere sie nebenbei. Gelöscht wird erst, wenn du bestätigst.</p>

      <h2>5. Sicher löschen</h2>
      <p>Bestätigte Dateien landen im Papierkorb (am Mac wie unter Windows), ein Fehler lässt sich also rückgängig machen. Leere ihn erst, wenn du sicher bist.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>RAW-Dateien von Kameras (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) werden neben JPEG, HEIC, PNG und Videos unterstützt.</li>
        <li>Das Sortieren von Ordnern ist kostenlos und nie begrenzt, am Mac (<a href="{mac}">Download</a>) und unter Windows (<a href="{win}">Download</a>).</li>
        <li>Deine Originale werden nie verändert: Die einzige Änderung von PhotoCull ist das Löschen, das du bestätigst.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="Android-Fotos am Mac sortieren: so geht's",
     desc="Ein Mac liest Android-Telefone nicht per USB. So sortierst du Tausende Android-Fotos trotzdem am Mac, per WLAN, und löschst, was du nicht brauchst.",
     h1="So sortierst du deine Android-Fotos am Mac",
     body="""      <p>Schließt du ein Android-Telefon an einen Mac an, passiert meist nichts: macOS liest Android-Telefone nicht per USB, wie Windows es tut. Dabei ist ein Mac der beste Ort, um eine große Fotorolle zu sortieren, mit großem Bildschirm, Maus und Vergleich nebeneinander. Das funktioniert.</p>

      <h2>Was macOS allein kann</h2>
      <ul>
        <li><strong>Digitale Bilder:</strong> sieht das Telefon eventuell, wenn du in der USB-Benachrichtigung „Fotos übertragen“ (PTP) wählst, aber nur als flache Dateiliste, ohne Gruppierung und ohne Vergleich ähnlicher Aufnahmen.</li>
        <li><strong>Android File Transfer von Google:</strong> wird nicht mehr gepflegt und kopiert ohnehin nur Dateien.</li>
        <li><strong>Cloud-Upload:</strong> alles an einen Online-Dienst zu senden, nur um es zu sortieren, ist langsam, verbraucht dein Datenvolumen und legt deine Fotos auf dem Server eines anderen ab.</li>
      </ul>

      <h2>Mit PhotoCull, per WLAN, Schritt für Schritt</h2>
      <p><strong>1. Beide Apps installieren.</strong> <a href="{mac}">PhotoCull für Mac kostenlos herunterladen</a> (macOS 11 oder neuer auf Apple Silicon) und die kostenlose <a href="{play}">TripSweep-App aus Google Play</a> auf dem Telefon installieren (Android 11 oder neuer).</p>
      <p><strong>2. Dasselbe WLAN.</strong> Bringe das Telefon in dasselbe WLAN wie den Mac und öffne in TripSweep den Tab „Löschen“.</p>
      <p><strong>3. Einmal verbinden.</strong> Klicke in PhotoCull auf „Android-Telefon“ und wähle dein Telefon. Erlaube den Mac auf dem Telefon: Auf beiden Bildschirmen erscheint derselbe 4-stellige Code. Beim nächsten Mal verbindet es sich von selbst.</p>
      <p><strong>4. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert die Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Ähnliche Fotos tragen ein Abzeichen: Vergleiche bis zu sechs nebeneinander, behalte das beste und markiere den Rest.</p>
      <p><strong>5. Sicher löschen.</strong> Klicke auf „Löschen“ und bestätige auf dem Telefon in TripSweep. Die Fotos landen 30 Tage im Papierkorb des Telefons, ein Fehler lässt sich also rückgängig machen.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Die Verbindung bleibt in deinem lokalen Netzwerk und ist verschlüsselt; nichts läuft über das Internet.</li>
        <li>PhotoCull verändert nie deine Originale und löscht nur, was du auf dem Telefon bestätigst.</li>
        <li>Vom Computer aus erlaubt die Gratisversion 6 Löschungen pro Tag, TripSweep Pro 15, und Pro + Desktop ist unbegrenzt. Durchsehen und Sortieren sind immer kostenlos.</li>
        <li>Du hast auch ein iPhone? Es wird stattdessen per USB-Kabel mit dem Mac verbunden.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="Android-Fotos am Windows-PC sortieren: so geht's",
     desc="Tausende Android-Fotos unter Windows 10 oder 11 sortieren: was Datei-Explorer und Fotos-App zeigen, und ein schnellerer Weg zum Vergleichen und Löschen.",
     h1="So sortierst du deine Android-Fotos am Windows-PC",
     body="""      <p>Windows liest Android-Telefone gut, aber Lesen ist noch kein Sortieren. Bei Tausenden Fotos lassen dich die integrierten Werkzeuge durch eine einzige lange Liste von Dateinamen scrollen. Hier steht, was sie können, und ein schnellerer Weg, das Telefon von deinem PC aus aufzuräumen.</p>

      <h2>Mit den Werkzeugen von Windows</h2>
      <ul>
        <li><strong>Datei-Explorer:</strong> Nachdem du am Telefon „Dateiübertragung“ gewählt hast, erscheint der Ordner DCIM als Dateien. Du kannst dort löschen, aber ohne Gruppierung und ohne Vergleich ähnlicher Aufnahmen.</li>
        <li><strong>Fotos-App:</strong> importiert eine Kopie auf den PC. Gut als Backup, aber sie sagt dir nicht, was du vom Telefon entfernen kannst.</li>
        <li><strong>Smartphone-Link:</strong> zeigt nur die letzten Fotos, eines nach dem anderen.</li>
      </ul>

      <h2>Mit PhotoCull, Schritt für Schritt</h2>
      <p><strong>1. Beide Apps installieren.</strong> Hole dir PhotoCull kostenlos <a href="{win}">für Windows 10 oder 11</a> und die kostenlose <a href="{play}">TripSweep-App aus Google Play</a> auf dem Telefon (Android 11 oder neuer).</p>
      <p><strong>2. Per USB oder WLAN verbinden.</strong> Per USB: Schließe das Telefon an und wähle in der USB-Benachrichtigung „Dateiübertragung“. Per WLAN: Bringe beide in dasselbe Netzwerk. Öffne dann in TripSweep den Tab „Löschen“ und klicke in PhotoCull auf „Android-Telefon“.</p>
      <p><strong>3. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert die Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Fang mit der größten an.</p>
      <p><strong>4. Vergleichen und markieren.</strong> Ähnliche Fotos tragen ein Abzeichen: Öffne bis zu sechs nebeneinander, behalte das beste und markiere den Rest, dazu Screenshots und große Videos.</p>
      <p><strong>5. Sicher löschen.</strong> Bestätige auf dem Telefon in TripSweep: Die Fotos landen 30 Tage im Papierkorb des Telefons.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles bleibt auf deinem PC und deinem Telefon: kein Konto, keine Cloud, kein Upload.</li>
        <li>Das Löschen im Datei-Explorer ist sofort und endgültig; über TripSweep bleibt das Sicherheitsnetz von 30 Tagen erhalten.</li>
        <li>Vom PC aus erlaubt die Gratisversion 6 Löschungen pro Tag, TripSweep Pro 15, und Pro + Desktop ist unbegrenzt. Das Sortieren eines Ordners auf dem PC ist nie begrenzt.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="Android-Speicher freigeben: vom Mac oder PC aus aufräumen",
     desc="Verbinde dein Android-Telefon, sortiere Fotos am großen Bildschirm und lösche, was du nicht brauchst, ohne Google One und ohne etwas hochzuladen.",
     h1="So gibst du Android-Speicher von einem Mac oder PC aus frei",
     body="""      <p>Wenn einem Android-Telefon der Platz ausgeht, sind fast immer Fotos und Videos der Grund. Sie am kleinen Bildschirm aufzuräumen ist mühsam. Am Computer siehst du mehr auf einmal und entscheidest schneller, ohne mehr Cloud-Speicher zu kaufen.</p>

      <h2>Warum ein Computer hilft</h2>
      <p>Ein großer Bildschirm zeigt Dutzende Fotos auf einmal, mit der Maus wählst du Hunderte in Sekunden aus, und fast identische Aufnahmen nebeneinander zu vergleichen ist viel einfacher, als hin und her zu wischen. Eine Fotorolle, die am Telefon einen ganzen Abend dauert, ist in Minuten erledigt.</p>

      <h2>Die Methode</h2>
      <p><strong>1. Das Telefon verbinden.</strong> Installiere <a href="{pc}">PhotoCull</a> auf deinem Mac oder PC und die kostenlose <a href="{play}">TripSweep-App</a> auf dem Telefon. Verbinde per WLAN (Mac und Windows) oder per USB (Windows), mit TripSweep geöffnet im Tab „Löschen“.</p>
      <p><strong>2. Mit dem Schwersten beginnen.</strong> Die Ansicht „Reisen“ zeigt den Platz jeder Reise; lange Videos und alte Urlaube geben meist am meisten frei.</p>
      <p><strong>3. Die Beinahe-Kopien entfernen.</strong> Serienaufnahmen und wiederholte Aufnahmen derselben Szene tragen ein Abzeichen. Vergleiche sie nebeneinander, behalte die beste und markiere den Rest.</p>
      <p><strong>4. Screenshots und unscharfe Aufnahmen entfernen.</strong> Sie haben selten einen Platz verdient und sind als Stapel schnell markiert.</p>
      <p><strong>5. Auf dem Telefon bestätigen.</strong> TripSweep führt das Löschen aus und verschiebt die Fotos in den Papierkorb des Telefons, wo sie 30 Tage bleiben. Leere den Papierkorb, wenn du sicher bist, um den Platz zurückzubekommen.</p>

      <h2>Brauche ich Google One?</h2>
      <p>Cloud-Speicher ist ein gutes Backup, aber er behält alles, auch die Duplikate. Wer zuerst aufräumt, braucht weniger Speicherplatz, auf dem Telefon und in der Cloud.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Kein Konto und kein Upload: Telefon und Computer sprechen über dein eigenes Netzwerk oder Kabel miteinander.</li>
        <li>Vom Computer aus erlaubt die Gratisversion 6 Löschungen pro Tag, Pro 15, und Pro + Desktop ist unbegrenzt.</li>
      </ul>"""),
],
}
