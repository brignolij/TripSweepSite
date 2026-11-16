# -*- coding: utf-8 -*-
# Deutsche Fassung der FAQ und des Blogs der TripSweep-Website. Tokens in Antworten/Artikeln: {ts} {pc} {store} (siehe link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Datenschutz", more="Weiterlesen",
    cta_store="📱 TripSweep im App Store laden",
    cta_play="🤖 TripSweep bei Google Play laden",
    cross_label={"tripsweep": "Desktop-App", "photocull": "Mobile App"},
    twin_android="Du nutzt ein Android-Telefon? Lies die Android-Anleitung:",
    twin_iphone="Du nutzt ein iPhone? Lies die iPhone-Anleitung:",
    index={
        "tripsweep": dict(
            title="TripSweep Blog – doppelte Fotos löschen, Speicher freigeben",
            desc="Praktische Anleitungen: iPhone-Speicher freigeben, doppelte und ähnliche Fotos löschen, alte Reisen aufräumen – ohne iCloud und ohne Upload deiner Fotos.",
            h1="Anleitungen zum Aufräumen deiner iPhone-Fotos",
            intro="Kurze, praktische Anleitungen, um Speicherplatz auf deinem iPhone freizugeben, Duplikate zu löschen und nur die besten Aufnahmen zu behalten."),
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
     "Ja, mit <a href=\"{pc}\">PhotoCull</a> auf einem Mac oder Windows-PC. Du markierst die Fotos auf dem großen Bildschirm und PhotoCull löscht sie bei einem iPhone direkt über das USB-Kabel: ohne Tageslimit, ohne etwas zu kaufen und ohne TripSweep. Voraussetzung ist, dass iCloud-Fotos auf dem iPhone ausgeschaltet ist und auf einem Mac macOS 27 oder neuer läuft (Windows funktioniert auch). Das Löschen ist auf dem iPhone endgültig, die Fotos landen nicht in „Zuletzt gelöscht“, aber PhotoCull bewahrt standardmäßig 30 Tage lang eine Kopie auf deinem Computer auf. TripSweep bleibt eine Option: Es löscht über „Zuletzt gelöscht“ (30 Tage) und ist der Weg, wenn iCloud-Fotos eingeschaltet ist oder auf macOS 26 oder älter. Löschungen, die vom Computer aus über TripSweep angefordert werden, so funktioniert auch ein Android-Telefon, sind auf 6 Fotos pro Tag kostenlos und 15 mit Pro begrenzt."),
    ("Welche iPhones und iOS-Versionen unterstützt TripSweep?",
     "TripSweep benötigt iOS 18 oder neuer. Die Analyse ähnlicher Fotos nutzt das Vision-Framework von Apple und ist auf neueren iPhones schneller, funktioniert aber auf jedem unterstützten Modell. Auf Android braucht TripSweep Android 11 oder neuer und ist bei <a href=\"{play}\">Google Play</a> erhältlich."),
]

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
}
