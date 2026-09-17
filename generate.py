#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en", "fr", "it", "de", "es"]
LANG_NAMES = {"en": "English", "fr": "Français", "it": "Italiano", "de": "Deutsch", "es": "Español"}

def path_for(lang, page, from_lang):
    """Relative href from a page in from_lang to `page` (index.html/desktop.html/privacy.html) in `lang`."""
    if lang == from_lang:
        return page
    if from_lang == "en":
        return f"{lang}/{page}"
    if lang == "en":
        return f"../{page}"
    return f"../{lang}/{page}"

def asset_path(from_lang, rel):
    return ("" if from_lang == "en" else "../") + rel

SITE_ORIGIN = "https://brignolij.github.io/TripSweepSite"

def hreflang_links(page):
    links = []
    for l in LANGS:
        href = SITE_ORIGIN + ("/" if l == "en" else f"/{l}/") + page
        links.append(f'  <link rel="alternate" hreflang="{l}" href="{href}" />')
    links.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE_ORIGIN}/{page}" />')
    return "\n".join(links)

def lang_switcher(current_lang, page):
    items = []
    for l in LANGS:
        href = path_for(l, page, current_lang)
        cls = ' class="active"' if l == current_lang else ""
        items.append(f'<a href="{href}"{cls}>{l.upper()}</a>')
    return '<div class="lang-switch">' + "".join(items) + '</div>'

# ---------------------------------------------------------------------------
# Content dictionaries
# ---------------------------------------------------------------------------

INDEX = {
"en": dict(
    title="TripSweep — sort your photos by trip",
    desc="Find your photos and videos grouped by trip, see what's taking up space, sort and export in one tap. 100% offline.",
    nav_desktop="Desktop app", nav_features="Features", nav_privacy_anchor="Privacy", nav_privacy="Privacy Policy",
    badge="📱 iOS companion app",
    h1="Your photos, finally sorted by trip",
    subtitle="TripSweep automatically groups your photos and videos by trip, shows you what's taking up the most space, and lets you sort, export or delete in one tap — without ever sending your data anywhere.",
    cta_store="📱 Coming soon to the App Store", cta_kofi="☕ Support the project on Ko-fi",
    cta_desktop_link="→ Also check out PhotoCull for Mac, the desktop app that sorts your photos",
    hero_alt="List of trips in TripSweep, sorted by size",
    preview_h2="A look at the app",
    preview_alt1="List of trips, sorted by size",
    preview_alt2="TripSweep's About screen",
    features_h2="What the app does",
    features=[
        ("🧳", "Automatic grouping by trip", "Your photos and videos are grouped by trip — factoring in both time and location, so two different destinations never get mixed up."),
        ("⚖️", "The size that counts", "Each trip shows how much space it takes up. Sort by size to spot at a glance what's really worth sorting through."),
        ("📤", "Export and delete in one tap", "View, share (AirDrop, Files...) or delete an entire trip at once — always through “Recently Deleted”, never an immediate permanent delete."),
        ("📍", "Custom places", "Define your own places (Home, Work...) and exclude them from the list to keep only real trips."),
        ("🔒", "100% offline", "No photo or location ever leaves your iPhone. Place recognition works entirely without a connection, an account, or any third-party service."),
        ("🌍", "Available in 5 languages", "English, French, Italian, German, Spanish — the app automatically adapts to your iPhone's language."),
    ],
    privacy_h2="Your privacy, taken seriously",
    privacy_p="TripSweep never collects, sends, or shares any of your photos, videos, or location data. All processing — including place recognition — happens locally on your iPhone.",
    privacy_btn="Read the full privacy policy",
    footer_copy="© 2026 TripSweep. Developed by Jeffrey Brignoli.",
    footer_desktop="Desktop app", footer_privacy="Privacy", footer_kofi="Ko-fi", footer_github="GitHub",
),
"fr": dict(
    title="TripSweep — triez vos photos par voyage",
    desc="Retrouvez vos photos et vidéos regroupées par séjour, voyez ce qui prend de la place, triez et exportez en un geste. 100% hors ligne.",
    nav_desktop="Application de bureau", nav_features="Fonctionnalités", nav_privacy_anchor="Confidentialité", nav_privacy="Politique de confidentialité",
    badge="📱 Application compagnon iOS",
    h1="Vos photos, enfin triées par voyage",
    subtitle="TripSweep regroupe automatiquement vos photos et vidéos par séjour, affiche ce qui prend le plus de place, et vous laisse trier, exporter ou supprimer en un geste — sans jamais envoyer vos données où que ce soit.",
    cta_store="📱 Bientôt sur l'App Store", cta_kofi="☕ Soutenir le projet sur Ko-fi",
    cta_desktop_link="→ Découvrir aussi PhotoCull pour Mac, l'application de bureau qui trie vos photos",
    hero_alt="Liste des séjours dans TripSweep, triée par poids",
    preview_h2="Un aperçu de l'app",
    preview_alt1="Liste des séjours, triée par poids",
    preview_alt2="Écran À propos de TripSweep",
    features_h2="Ce que fait l'app",
    features=[
        ("🧳", "Regroupement automatique par séjour", "Vos photos et vidéos sont regroupées par voyage — en tenant compte à la fois du temps et du lieu, pour ne pas mélanger deux destinations différentes."),
        ("⚖️", "Le poids qui compte", "Chaque séjour affiche l'espace qu'il occupe. Triez par poids pour repérer en un coup d'œil ce qui vaut vraiment la peine d'être trié."),
        ("📤", "Export et suppression en un geste", "Visionnez, partagez (AirDrop, Fichiers...) ou supprimez un séjour entier d'un coup — toujours via « Récemment supprimés », jamais de suppression définitive immédiate."),
        ("📍", "Lieux personnalisés", "Définissez vos lieux (Domicile, Travail...) et excluez-les de la liste pour ne garder que les vrais voyages."),
        ("🔒", "100% hors ligne", "Aucune photo ni position ne quitte votre iPhone. La reconnaissance des lieux fonctionne entièrement sans connexion, sans compte, sans service tiers."),
        ("🌍", "Disponible en 5 langues", "Français, anglais, italien, allemand, espagnol — l'app s'adapte automatiquement à la langue de votre iPhone."),
    ],
    privacy_h2="Votre vie privée, prise au sérieux",
    privacy_p="TripSweep ne collecte, n'envoie et ne partage aucune de vos photos, vidéos ou données de localisation. Tout le traitement — reconnaissance de lieux incluse — se fait localement sur votre iPhone.",
    privacy_btn="Lire la politique de confidentialité complète",
    footer_copy="© 2026 TripSweep. Développé par Jeffrey Brignoli.",
    footer_desktop="Application de bureau", footer_privacy="Confidentialité", footer_kofi="Ko-fi", footer_github="GitHub",
),
"it": dict(
    title="TripSweep — ordina le tue foto per viaggio",
    desc="Ritrova le tue foto e i tuoi video raggruppati per soggiorno, scopri cosa occupa più spazio, ordina ed esporta in un gesto. 100% offline.",
    nav_desktop="App desktop", nav_features="Funzionalità", nav_privacy_anchor="Privacy", nav_privacy="Informativa sulla privacy",
    badge="📱 App compagna per iOS",
    h1="Le tue foto, finalmente ordinate per viaggio",
    subtitle="TripSweep raggruppa automaticamente le tue foto e i tuoi video per soggiorno, mostra cosa occupa più spazio e ti permette di ordinare, esportare o eliminare in un gesto — senza mai inviare i tuoi dati altrove.",
    cta_store="📱 Presto su App Store", cta_kofi="☕ Sostieni il progetto su Ko-fi",
    cta_desktop_link="→ Scopri anche PhotoCull per Mac, l'app desktop che ordina le tue foto",
    hero_alt="Elenco dei soggiorni in TripSweep, ordinato per dimensione",
    preview_h2="Uno sguardo all'app",
    preview_alt1="Elenco dei soggiorni, ordinato per dimensione",
    preview_alt2="Schermata Informazioni di TripSweep",
    features_h2="Cosa fa l'app",
    features=[
        ("🧳", "Raggruppamento automatico per soggiorno", "Le tue foto e i tuoi video sono raggruppati per viaggio — tenendo conto sia del tempo sia del luogo, per non mescolare mai due destinazioni diverse."),
        ("⚖️", "La dimensione che conta", "Ogni soggiorno mostra lo spazio che occupa. Ordina per dimensione per individuare a colpo d'occhio ciò che vale davvero la pena ordinare."),
        ("📤", "Esporta ed elimina in un gesto", "Visualizza, condividi (AirDrop, File...) o elimina un intero soggiorno in un colpo solo — sempre tramite «Eliminati di recente», mai un'eliminazione definitiva immediata."),
        ("📍", "Luoghi personalizzati", "Definisci i tuoi luoghi (Casa, Lavoro...) ed escludili dall'elenco per tenere solo i veri viaggi."),
        ("🔒", "100% offline", "Nessuna foto o posizione lascia mai il tuo iPhone. Il riconoscimento dei luoghi funziona interamente senza connessione, senza account, senza servizi di terze parti."),
        ("🌍", "Disponibile in 5 lingue", "Francese, inglese, italiano, tedesco, spagnolo — l'app si adatta automaticamente alla lingua del tuo iPhone."),
    ],
    privacy_h2="La tua privacy, presa sul serio",
    privacy_p="TripSweep non raccoglie, invia o condivide mai le tue foto, i tuoi video o i tuoi dati di posizione. Tutta l'elaborazione — incluso il riconoscimento dei luoghi — avviene localmente sul tuo iPhone.",
    privacy_btn="Leggi l'informativa sulla privacy completa",
    footer_copy="© 2026 TripSweep. Sviluppato da Jeffrey Brignoli.",
    footer_desktop="App desktop", footer_privacy="Privacy", footer_kofi="Ko-fi", footer_github="GitHub",
),
"de": dict(
    title="TripSweep — sortiere deine Fotos nach Reise",
    desc="Finde deine Fotos und Videos nach Aufenthalt gruppiert, sieh, was am meisten Platz beansprucht, sortiere und exportiere mit einer Geste. 100% offline.",
    nav_desktop="Desktop-App", nav_features="Funktionen", nav_privacy_anchor="Datenschutz", nav_privacy="Datenschutzerklärung",
    badge="📱 iOS-Begleit-App",
    h1="Deine Fotos, endlich nach Reise sortiert",
    subtitle="TripSweep gruppiert deine Fotos und Videos automatisch nach Aufenthalt, zeigt dir, was am meisten Platz beansprucht, und lässt dich mit einer Geste sortieren, exportieren oder löschen — ohne dass deine Daten jemals irgendwohin gesendet werden.",
    cta_store="📱 Bald im App Store", cta_kofi="☕ Projekt auf Ko-fi unterstützen",
    cta_desktop_link="→ Entdecke auch PhotoCull für Mac, die Desktop-App, die deine Fotos sortiert",
    hero_alt="Liste der Aufenthalte in TripSweep, nach Größe sortiert",
    preview_h2="Ein Blick auf die App",
    preview_alt1="Liste der Aufenthalte, nach Größe sortiert",
    preview_alt2="TripSweep-Infobildschirm",
    features_h2="Was die App kann",
    features=[
        ("🧳", "Automatische Gruppierung nach Aufenthalt", "Deine Fotos und Videos werden nach Reise gruppiert — unter Berücksichtigung von Zeit und Ort, damit zwei verschiedene Reiseziele nie vermischt werden."),
        ("⚖️", "Die Größe, die zählt", "Jeder Aufenthalt zeigt den belegten Speicherplatz. Sortiere nach Größe, um auf einen Blick zu erkennen, was sich wirklich zu sortieren lohnt."),
        ("📤", "Exportieren und löschen mit einer Geste", "Sieh dir einen ganzen Aufenthalt an, teile ihn (AirDrop, Dateien...) oder lösche ihn auf einmal — immer über „Kürzlich gelöscht“, nie ein sofortiges endgültiges Löschen."),
        ("📍", "Eigene Orte", "Lege eigene Orte fest (Zuhause, Arbeit...) und schließe sie aus der Liste aus, um nur echte Reisen zu behalten."),
        ("🔒", "100% offline", "Kein Foto und kein Standort verlässt jemals dein iPhone. Die Ortserkennung funktioniert vollständig ohne Verbindung, ohne Konto, ohne Drittanbieterdienste."),
        ("🌍", "In 5 Sprachen verfügbar", "Französisch, Englisch, Italienisch, Deutsch, Spanisch — die App passt sich automatisch an die Sprache deines iPhones an."),
    ],
    privacy_h2="Dein Datenschutz wird ernst genommen",
    privacy_p="TripSweep sammelt, sendet oder teilt niemals deine Fotos, Videos oder Standortdaten. Die gesamte Verarbeitung — einschließlich der Ortserkennung — erfolgt lokal auf deinem iPhone.",
    privacy_btn="Vollständige Datenschutzerklärung lesen",
    footer_copy="© 2026 TripSweep. Entwickelt von Jeffrey Brignoli.",
    footer_desktop="Desktop-App", footer_privacy="Datenschutz", footer_kofi="Ko-fi", footer_github="GitHub",
),
"es": dict(
    title="TripSweep — ordena tus fotos por viaje",
    desc="Encuentra tus fotos y vídeos agrupados por estancia, descubre qué ocupa más espacio, ordena y exporta en un gesto. 100% sin conexión.",
    nav_desktop="Aplicación de escritorio", nav_features="Funciones", nav_privacy_anchor="Privacidad", nav_privacy="Política de privacidad",
    badge="📱 Aplicación complementaria para iOS",
    h1="Tus fotos, por fin ordenadas por viaje",
    subtitle="TripSweep agrupa automáticamente tus fotos y vídeos por estancia, muestra lo que ocupa más espacio y te permite ordenar, exportar o eliminar en un gesto — sin enviar nunca tus datos a ningún sitio.",
    cta_store="📱 Próximamente en App Store", cta_kofi="☕ Apoya el proyecto en Ko-fi",
    cta_desktop_link="→ Descubre también PhotoCull para Mac, la aplicación de escritorio que ordena tus fotos",
    hero_alt="Lista de estancias en TripSweep, ordenada por tamaño",
    preview_h2="Un vistazo a la app",
    preview_alt1="Lista de estancias, ordenada por tamaño",
    preview_alt2="Pantalla Acerca de de TripSweep",
    features_h2="Qué hace la app",
    features=[
        ("🧳", "Agrupación automática por estancia", "Tus fotos y vídeos se agrupan por viaje — teniendo en cuenta tanto el tiempo como el lugar, para no mezclar nunca dos destinos distintos."),
        ("⚖️", "El tamaño que importa", "Cada estancia muestra el espacio que ocupa. Ordena por tamaño para detectar de un vistazo lo que realmente vale la pena ordenar."),
        ("📤", "Exportar y eliminar en un gesto", "Visualiza, comparte (AirDrop, Archivos...) o elimina toda una estancia de una vez — siempre a través de «Eliminados recientemente», nunca una eliminación definitiva inmediata."),
        ("📍", "Lugares personalizados", "Define tus lugares (Casa, Trabajo...) y exclúyelos de la lista para conservar solo los viajes reales."),
        ("🔒", "100% sin conexión", "Ninguna foto ni ubicación sale nunca de tu iPhone. El reconocimiento de lugares funciona completamente sin conexión, sin cuenta y sin servicios de terceros."),
        ("🌍", "Disponible en 5 idiomas", "Francés, inglés, italiano, alemán, español — la app se adapta automáticamente al idioma de tu iPhone."),
    ],
    privacy_h2="Tu privacidad, tomada en serio",
    privacy_p="TripSweep nunca recopila, envía ni comparte tus fotos, vídeos o datos de ubicación. Todo el procesamiento — incluido el reconocimiento de lugares — se realiza localmente en tu iPhone.",
    privacy_btn="Leer la política de privacidad completa",
    footer_copy="© 2026 TripSweep. Desarrollado por Jeffrey Brignoli.",
    footer_desktop="Aplicación de escritorio", footer_privacy="Privacidad", footer_kofi="Ko-fi", footer_github="GitHub",
),
}

DESKTOP = {
"en": dict(
    title="PhotoCull for Mac — the photo sorting tool",
    desc="The desktop app that sorts your photos by trip, compares and bulk-deletes — 100% offline, no subscription.",
    nav_ios="iOS app", nav_features="Features", nav_privacy="Privacy",
    badge="🖥️ Desktop app (macOS)",
    h1="The real tool for sorting thousands of photos",
    subtitle="PhotoCull is a full desktop application: it shows your entire iPhone camera roll grouped by trip, compares your photos side by side, and bulk-deletes what's no longer worth keeping — right from your Mac.",
    cta_download="💻 Download for Mac (coming soon)", cta_kofi="☕ Support the project on Ko-fi",
    features_h2="What the app does",
    features=[
        ("🧳", 'The "Trips" view', "Your entire photo library automatically grouped by trip (time AND location, just like the iOS app) — spot at a glance which trips take up the most space."),
        ("🔍", "Side-by-side comparison", "Show up to 6 similar photos at once to pick the best one — perfect for sorting through bursts and near-duplicates."),
        ("🗑️", "Safe bulk deletion", "Mark hundreds of photos in a few clicks. The actual deletion goes through the companion app on your iPhone and “Recently Deleted” (30 days) — never an immediate permanent delete."),
        ("⚖️", "The size that counts", "Sort and filter by single-day trip, by excluded place (home, work...), by size — the same filters as the iOS app, built for speed."),
        ("🔌", "Direct connection to your iPhone", "Plug in your iPhone via USB (or use simulation mode to try it out): PhotoCull reads your camera roll directly, with no iCloud and no server involved."),
        ("🔒", "100% offline", "No photo, no GPS location is ever sent anywhere. Place recognition runs entirely locally, with no account and no subscription."),
    ],
    strip_h2="Works with or without the iOS app",
    strip_p_before="PhotoCull for Mac stands entirely on its own: just plug in your iPhone via USB. If you also install ",
    strip_p_link="the iOS companion app",
    strip_p_after=", trip analysis becomes near-instant (computed directly on the phone) — but it's never required.",
    footer_copy="© 2026 PhotoCull. Developed by Jeffrey Brignoli.",
    footer_ios="iOS app", footer_privacy="Privacy", footer_kofi="Ko-fi", footer_github="GitHub",
),
"fr": dict(
    title="PhotoCull pour Mac — l'outil de tri de photos",
    desc="L'application de bureau qui trie vos photos par séjour, compare et supprime en masse — 100% hors ligne, sans abonnement.",
    nav_ios="Application iOS", nav_features="Fonctionnalités", nav_privacy="Confidentialité",
    badge="🖥️ Application de bureau (macOS)",
    h1="Le vrai outil pour trier des milliers de photos",
    subtitle="PhotoCull est une application de bureau à part entière : elle affiche tout le rouleau de votre iPhone regroupé par séjour, compare vos photos côte à côte, et supprime en masse ce qui ne vaut plus la peine d'être gardé — directement depuis votre Mac.",
    cta_download="💻 Télécharger pour Mac (bientôt)", cta_kofi="☕ Soutenir le projet sur Ko-fi",
    features_h2="Ce que fait l'app",
    features=[
        ("🧳", 'Vue "Voyages / séjours"', "Toute votre photothèque regroupée automatiquement par séjour (temps ET lieu, comme l'app iOS) — pour repérer d'un coup d'œil les voyages qui prennent le plus de place."),
        ("🔍", "Comparaison côte à côte", "Affichez jusqu'à 6 photos similaires en même temps pour choisir la meilleure — idéal pour trier les rafales et les quasi-doublons."),
        ("🗑️", "Suppression en masse, en toute sécurité", "Marquez des centaines de photos en quelques clics. La suppression réelle passe par l'app compagnon sur votre iPhone et « Récemment supprimés » (30 jours) — jamais de suppression définitive immédiate."),
        ("⚖️", "Le poids qui compte", "Triez et filtrez par séjour d'1 jour, par lieu exclu (domicile, travail...), par poids — les mêmes filtres que sur l'app iOS, pensés pour aller vite."),
        ("🔌", "Connexion directe à l'iPhone", "Branchez votre iPhone en USB (ou utilisez le mode simulation pour tester) : PhotoCull lit votre rouleau directement, sans passer par iCloud ni aucun serveur."),
        ("🔒", "100% hors ligne", "Aucune photo, aucune position GPS n'est jamais envoyée où que ce soit. La reconnaissance des lieux fonctionne entièrement en local, sans compte ni abonnement."),
    ],
    strip_h2="Fonctionne avec ou sans l'app iOS",
    strip_p_before="PhotoCull pour Mac se suffit à lui-même : connectez simplement votre iPhone en USB. Si vous installez aussi ",
    strip_p_link="l'app compagnon iOS",
    strip_p_after=", l'analyse des séjours devient quasi instantanée (calculée directement sur le téléphone) — mais ce n'est jamais obligatoire.",
    footer_copy="© 2026 PhotoCull. Développé par Jeffrey Brignoli.",
    footer_ios="Application iOS", footer_privacy="Confidentialité", footer_kofi="Ko-fi", footer_github="GitHub",
),
"it": dict(
    title="PhotoCull per Mac — lo strumento per ordinare le foto",
    desc="L'app desktop che ordina le tue foto per soggiorno, confronta ed elimina in blocco — 100% offline, senza abbonamento.",
    nav_ios="App iOS", nav_features="Funzionalità", nav_privacy="Privacy",
    badge="🖥️ App desktop (macOS)",
    h1="Il vero strumento per ordinare migliaia di foto",
    subtitle="PhotoCull è un'applicazione desktop a tutti gli effetti: mostra l'intero rullino del tuo iPhone raggruppato per soggiorno, confronta le tue foto affiancate ed elimina in blocco ciò che non vale più la pena tenere — direttamente dal tuo Mac.",
    cta_download="💻 Scarica per Mac (presto)", cta_kofi="☕ Sostieni il progetto su Ko-fi",
    features_h2="Cosa fa l'app",
    features=[
        ("🧳", 'Vista "Viaggi / soggiorni"', "Tutta la tua libreria foto raggruppata automaticamente per soggiorno (tempo E luogo, come l'app iOS) — per individuare a colpo d'occhio i viaggi che occupano più spazio."),
        ("🔍", "Confronto affiancato", "Mostra fino a 6 foto simili contemporaneamente per scegliere la migliore — ideale per ordinare raffiche e quasi-duplicati."),
        ("🗑️", "Eliminazione in blocco, in tutta sicurezza", "Contrassegna centinaia di foto in pochi clic. L'eliminazione effettiva passa dall'app compagna sul tuo iPhone e da «Eliminati di recente» (30 giorni) — mai un'eliminazione definitiva immediata."),
        ("⚖️", "La dimensione che conta", "Ordina e filtra per soggiorno di 1 giorno, per luogo escluso (casa, lavoro...), per dimensione — gli stessi filtri dell'app iOS, pensati per la velocità."),
        ("🔌", "Connessione diretta all'iPhone", "Collega il tuo iPhone via USB (oppure usa la modalità simulazione per provarla): PhotoCull legge il tuo rullino direttamente, senza passare da iCloud né da alcun server."),
        ("🔒", "100% offline", "Nessuna foto, nessuna posizione GPS viene mai inviata altrove. Il riconoscimento dei luoghi funziona interamente in locale, senza account né abbonamento."),
    ],
    strip_h2="Funziona con o senza l'app iOS",
    strip_p_before="PhotoCull per Mac si basta da solo: collega semplicemente il tuo iPhone via USB. Se installi anche ",
    strip_p_link="l'app compagna per iOS",
    strip_p_after=", l'analisi dei soggiorni diventa quasi istantanea (calcolata direttamente sul telefono) — ma non è mai obbligatoria.",
    footer_copy="© 2026 PhotoCull. Sviluppato da Jeffrey Brignoli.",
    footer_ios="App iOS", footer_privacy="Privacy", footer_kofi="Ko-fi", footer_github="GitHub",
),
"de": dict(
    title="PhotoCull für Mac — das Foto-Sortierwerkzeug",
    desc="Die Desktop-App, die deine Fotos nach Aufenthalt sortiert, vergleicht und in großen Mengen löscht — 100% offline, ohne Abo.",
    nav_ios="iOS-App", nav_features="Funktionen", nav_privacy="Datenschutz",
    badge="🖥️ Desktop-App (macOS)",
    h1="Das echte Werkzeug, um Tausende Fotos zu sortieren",
    subtitle="PhotoCull ist eine vollwertige Desktop-Anwendung: Sie zeigt deine gesamte iPhone-Fotorolle nach Aufenthalt gruppiert, vergleicht deine Fotos nebeneinander und löscht in großen Mengen, was sich nicht mehr zu behalten lohnt — direkt von deinem Mac aus.",
    cta_download="💻 Für Mac herunterladen (bald)", cta_kofi="☕ Projekt auf Ko-fi unterstützen",
    features_h2="Was die App kann",
    features=[
        ("🧳", 'Ansicht "Reisen / Aufenthalte"', "Deine gesamte Fotobibliothek automatisch nach Aufenthalt gruppiert (Zeit UND Ort, genau wie bei der iOS-App) — erkenne auf einen Blick, welche Reisen am meisten Platz beanspruchen."),
        ("🔍", "Seite-an-Seite-Vergleich", "Zeige bis zu 6 ähnliche Fotos gleichzeitig an, um das beste auszuwählen — ideal zum Sortieren von Serienbildern und Beinahe-Duplikaten."),
        ("🗑️", "Sicheres Löschen in großen Mengen", "Markiere Hunderte von Fotos in wenigen Klicks. Das eigentliche Löschen läuft über die Begleit-App auf deinem iPhone und „Kürzlich gelöscht“ (30 Tage) — nie ein sofortiges endgültiges Löschen."),
        ("⚖️", "Die Größe, die zählt", "Sortiere und filtere nach eintägigem Aufenthalt, nach ausgeschlossenem Ort (Zuhause, Arbeit...), nach Größe — dieselben Filter wie bei der iOS-App, auf Geschwindigkeit ausgelegt."),
        ("🔌", "Direkte Verbindung zum iPhone", "Schließe dein iPhone per USB an (oder nutze den Simulationsmodus zum Testen): PhotoCull liest deine Fotorolle direkt, ganz ohne iCloud und ohne Server."),
        ("🔒", "100% offline", "Kein Foto, kein GPS-Standort wird jemals irgendwohin gesendet. Die Ortserkennung läuft vollständig lokal, ohne Konto und ohne Abo."),
    ],
    strip_h2="Funktioniert mit oder ohne die iOS-App",
    strip_p_before="PhotoCull für Mac kommt vollständig allein aus: Schließe einfach dein iPhone per USB an. Wenn du zusätzlich ",
    strip_p_link="die iOS-Begleit-App",
    strip_p_after=" installierst, wird die Analyse der Aufenthalte nahezu augenblicklich (direkt auf dem Telefon berechnet) — aber das ist nie erforderlich.",
    footer_copy="© 2026 PhotoCull. Entwickelt von Jeffrey Brignoli.",
    footer_ios="iOS-App", footer_privacy="Datenschutz", footer_kofi="Ko-fi", footer_github="GitHub",
),
"es": dict(
    title="PhotoCull para Mac — la herramienta para ordenar fotos",
    desc="La aplicación de escritorio que ordena tus fotos por estancia, compara y elimina en masa — 100% sin conexión, sin suscripción.",
    nav_ios="Aplicación iOS", nav_features="Funciones", nav_privacy="Privacidad",
    badge="🖥️ Aplicación de escritorio (macOS)",
    h1="La auténtica herramienta para ordenar miles de fotos",
    subtitle="PhotoCull es una aplicación de escritorio completa: muestra todo el carrete de tu iPhone agrupado por estancia, compara tus fotos una junto a otra y elimina en masa lo que ya no vale la pena conservar — directamente desde tu Mac.",
    cta_download="💻 Descargar para Mac (próximamente)", cta_kofi="☕ Apoya el proyecto en Ko-fi",
    features_h2="Qué hace la app",
    features=[
        ("🧳", 'Vista "Viajes / estancias"', "Toda tu biblioteca de fotos agrupada automáticamente por estancia (tiempo Y lugar, igual que la app de iOS) — detecta de un vistazo los viajes que ocupan más espacio."),
        ("🔍", "Comparación lado a lado", "Muestra hasta 6 fotos similares a la vez para elegir la mejor — ideal para ordenar ráfagas y casi duplicados."),
        ("🗑️", "Eliminación en masa, con total seguridad", "Marca cientos de fotos en pocos clics. La eliminación real pasa por la app complementaria en tu iPhone y por «Eliminados recientemente» (30 días) — nunca una eliminación definitiva inmediata."),
        ("⚖️", "El tamaño que importa", "Ordena y filtra por estancia de 1 día, por lugar excluido (casa, trabajo...), por tamaño — los mismos filtros que en la app de iOS, pensados para ir rápido."),
        ("🔌", "Conexión directa con el iPhone", "Conecta tu iPhone por USB (o usa el modo de simulación para probarlo): PhotoCull lee tu carrete directamente, sin pasar por iCloud ni por ningún servidor."),
        ("🔒", "100% sin conexión", "Ninguna foto ni ubicación GPS se envía nunca a ningún sitio. El reconocimiento de lugares funciona completamente en local, sin cuenta ni suscripción."),
    ],
    strip_h2="Funciona con o sin la app de iOS",
    strip_p_before="PhotoCull para Mac se basta por sí solo: simplemente conecta tu iPhone por USB. Si además instalas ",
    strip_p_link="la app complementaria de iOS",
    strip_p_after=", el análisis de estancias se vuelve casi instantáneo (calculado directamente en el teléfono) — pero nunca es obligatorio.",
    footer_copy="© 2026 PhotoCull. Desarrollado por Jeffrey Brignoli.",
    footer_ios="Aplicación iOS", footer_privacy="Privacidad", footer_kofi="Ko-fi", footer_github="GitHub",
),
}

PRIVACY = {
"en": dict(
    title="Privacy Policy — TripSweep",
    nav_home="Home",
    h1="Privacy Policy",
    updated="Last updated: September 16, 2026",
    intro='TripSweep ("the app") is developed by Jeffrey Brignoli. This page explains what data the app uses, where it goes, and why. The project\'s guiding principle is simple: <strong>nothing ever leaves your iPhone</strong>.',
    s1_h="What the app does not do",
    s1_items=[
        "It does not collect, send, or share your photos, videos, or metadata with anyone.",
        "It does not create any user account and does not ask for any personal information (name, email...).",
        "It does not contain any advertising SDK or cross-app tracking.",
        "It does not rely on any server: place recognition (city/country) happens entirely offline, from data embedded in the app (GeoNames.org, CC BY 4.0 license), never querying an online service.",
    ],
    s2_h="Access to your photo library",
    s2_p1="The app requests full access to your photo library (Photos) for two reasons:",
    s2_items=[
        "Analyzing your photos and videos to group them by trip and calculate the space they take up — this processing happens entirely on your device.",
        "Deleting the photos you explicitly choose to delete — deletion always goes through “Recently Deleted” (30 days), never an immediate permanent delete.",
    ],
    s2_p2="No photo, thumbnail, or metadata extracted from your photo library is ever transmitted off your device.",
    s3_h="Access to your location",
    s3_p="The app requests access to your location only when you choose to manually add a “place” (for example “Home” or “Work”) in the places management feature. This location is stored locally on your device and never transmitted elsewhere. It is used only to compare distance with detected trips, so you can exclude them from the list if you wish.",
    s4_h="Syncing with the Mac app",
    s4_p1="If you also use ",
    s4_p_link="PhotoCull",
    s4_p2=" on your Mac, the companion app can exchange information with it via a direct local USB/Wi-Fi connection between your two Apple devices (a standard protocol used for iOS device syncing) — never over the Internet or via a third-party server.",
    s5_h="In-app purchases",
    s5_p="The app offers an optional paid feature (“Pro”, one-time purchase) handled exclusively by Apple via StoreKit. No payment information is collected, stored, or visible to the developer: Apple handles the entire transaction in accordance with its own privacy policy.",
    s6_h="Analytics and diagnostics",
    s6_p="The app does not currently integrate any third-party analytics or tracking tool. If you have enabled analytics data sharing with app developers (iOS Settings > Privacy & Security > Analytics & Improvements), Apple may send anonymized crash reports — this feature is handled entirely by Apple, independently of the app.",
    s7_h="Your rights",
    s7_p="Since no personal data is collected or stored by the developer outside your device, there is no external database to consult, correct, or delete. You retain full control at all times over the permissions granted to the app via iOS Settings.",
    s8_h="Contact",
    s8_p1="For any question regarding this privacy policy, you can contact the developer via ",
    s8_p2=".",
    footer_copy="© 2026 TripSweep. Developed by Jeffrey Brignoli.",
    footer_home="Home", footer_kofi="Ko-fi",
),
"fr": dict(
    title="Politique de confidentialité — TripSweep",
    nav_home="Accueil",
    h1="Politique de confidentialité",
    updated="Dernière mise à jour : 16 septembre 2026",
    intro='TripSweep (« l\'application ») est développée par Jeffrey Brignoli. Cette page explique quelles données l\'application utilise, où elles vont, et pourquoi. Le principe directeur du projet est simple : <strong>rien ne quitte votre iPhone</strong>.',
    s1_h="Ce que l'application ne fait pas",
    s1_items=[
        "Elle ne collecte, n'envoie ni ne partage vos photos, vidéos ou métadonnées avec qui que ce soit.",
        "Elle ne crée aucun compte utilisateur et ne demande aucune information personnelle (nom, email...).",
        "Elle ne contient aucun SDK publicitaire ni de suivi (tracking) inter-applications.",
        "Elle ne fonctionne avec aucun serveur : la reconnaissance des lieux (ville/pays) se fait entièrement hors ligne, à partir de données embarquées dans l'application (GeoNames.org, licence CC BY 4.0), sans jamais interroger un service en ligne.",
    ],
    s2_h="Accès à votre photothèque",
    s2_p1="L'application demande un accès complet à votre photothèque (Photos) pour deux raisons :",
    s2_items=[
        "Analyser vos photos et vidéos afin de les regrouper par séjour et calculer l'espace occupé — ce traitement a lieu entièrement sur votre appareil.",
        "Supprimer les photos que vous choisissez explicitement de supprimer — la suppression passe systématiquement par « Récemment supprimés » (30 jours), jamais une suppression définitive immédiate.",
    ],
    s2_p2="Aucune photo, vignette ou métadonnée extraite de votre photothèque n'est jamais transmise hors de votre appareil.",
    s3_h="Accès à votre position",
    s3_p="L'application demande l'accès à votre position uniquement lorsque vous choisissez d'ajouter manuellement un « lieu » (par exemple « Domicile » ou « Travail ») dans la fonctionnalité de gestion des lieux. Cette position est enregistrée localement sur votre appareil et n'est jamais transmise ailleurs. Elle sert uniquement à comparer la distance avec les séjours détectés, pour vous permettre de les exclure de la liste si vous le souhaitez.",
    s4_h="Synchronisation avec l'application Mac",
    s4_p1="Si vous utilisez également ",
    s4_p_link="PhotoCull",
    s4_p2=" sur Mac, l'application compagnon peut échanger des informations avec lui via une connexion USB/Wi-Fi locale directe entre vos deux appareils Apple (protocole standard utilisé pour la synchronisation d'appareils iOS) — jamais via Internet ni un serveur tiers.",
    s5_h="Achats intégrés",
    s5_p="L'application propose une option payante facultative (« Pro », achat unique) gérée exclusivement par Apple via StoreKit. Aucune information de paiement n'est collectée, stockée ou visible par le développeur : Apple gère l'intégralité de la transaction conformément à sa propre politique de confidentialité.",
    s6_h="Statistiques et diagnostics",
    s6_p="L'application n'intègre, à ce jour, aucun outil d'analyse ou de suivi tiers. Si vous avez activé le partage de données d'analyse avec les développeurs d'applications (Réglages iOS > Confidentialité et sécurité > Analyse et améliorations), Apple peut transmettre des rapports de plantage anonymisés — cette fonctionnalité est gérée entièrement par Apple, indépendamment de l'application.",
    s7_h="Vos droits",
    s7_p="Puisqu'aucune donnée personnelle n'est collectée ni stockée par le développeur en dehors de votre appareil, il n'existe aucune base de données externe à consulter, corriger ou supprimer. Vous gardez à tout moment le contrôle total sur les permissions accordées à l'application via Réglages iOS.",
    s8_h="Contact",
    s8_p1="Pour toute question concernant cette politique de confidentialité, vous pouvez contacter le développeur via ",
    s8_p2=".",
    footer_copy="© 2026 TripSweep. Développé par Jeffrey Brignoli.",
    footer_home="Accueil", footer_kofi="Ko-fi",
),
"it": dict(
    title="Informativa sulla privacy — TripSweep",
    nav_home="Home",
    h1="Informativa sulla privacy",
    updated="Ultimo aggiornamento: 16 settembre 2026",
    intro='TripSweep («l\'applicazione») è sviluppata da Jeffrey Brignoli. Questa pagina spiega quali dati utilizza l\'applicazione, dove vanno e perché. Il principio guida del progetto è semplice: <strong>nulla lascia mai il tuo iPhone</strong>.',
    s1_h="Cosa non fa l'applicazione",
    s1_items=[
        "Non raccoglie, invia o condivide le tue foto, i tuoi video o metadati con chiunque.",
        "Non crea alcun account utente e non richiede alcuna informazione personale (nome, email...).",
        "Non contiene alcun SDK pubblicitario né di tracciamento (tracking) tra app.",
        "Non funziona con alcun server: il riconoscimento dei luoghi (città/paese) avviene interamente offline, a partire da dati incorporati nell'applicazione (GeoNames.org, licenza CC BY 4.0), senza mai interrogare un servizio online.",
    ],
    s2_h="Accesso alla tua libreria foto",
    s2_p1="L'applicazione richiede un accesso completo alla tua libreria foto (Foto) per due motivi:",
    s2_items=[
        "Analizzare le tue foto e i tuoi video per raggrupparli per soggiorno e calcolare lo spazio occupato — questa elaborazione avviene interamente sul tuo dispositivo.",
        "Eliminare le foto che scegli esplicitamente di eliminare — l'eliminazione passa sempre attraverso «Eliminati di recente» (30 giorni), mai un'eliminazione definitiva immediata.",
    ],
    s2_p2="Nessuna foto, miniatura o metadato estratto dalla tua libreria foto viene mai trasmesso al di fuori del tuo dispositivo.",
    s3_h="Accesso alla tua posizione",
    s3_p="L'applicazione richiede l'accesso alla tua posizione solo quando scegli di aggiungere manualmente un «luogo» (ad esempio «Casa» o «Lavoro») nella funzione di gestione dei luoghi. Questa posizione viene salvata localmente sul tuo dispositivo e non viene mai trasmessa altrove. Serve unicamente a confrontare la distanza con i soggiorni rilevati, per permetterti di escluderli dall'elenco se lo desideri.",
    s4_h="Sincronizzazione con l'app Mac",
    s4_p1="Se utilizzi anche ",
    s4_p_link="PhotoCull",
    s4_p2=" su Mac, l'app compagna può scambiare informazioni con esso tramite una connessione USB/Wi-Fi locale diretta tra i tuoi due dispositivi Apple (protocollo standard utilizzato per la sincronizzazione dei dispositivi iOS) — mai tramite Internet né un server di terze parti.",
    s5_h="Acquisti in-app",
    s5_p="L'applicazione offre un'opzione a pagamento facoltativa («Pro», acquisto singolo) gestita esclusivamente da Apple tramite StoreKit. Nessuna informazione di pagamento viene raccolta, memorizzata o resa visibile allo sviluppatore: Apple gestisce l'intera transazione in conformità alla propria informativa sulla privacy.",
    s6_h="Statistiche e diagnostica",
    s6_p="Ad oggi, l'applicazione non integra alcuno strumento di analisi o tracciamento di terze parti. Se hai attivato la condivisione dei dati di analisi con gli sviluppatori di app (Impostazioni iOS > Privacy e sicurezza > Analisi e miglioramenti), Apple potrebbe trasmettere report di arresto anomalo anonimizzati — questa funzione è gestita interamente da Apple, indipendentemente dall'applicazione.",
    s7_h="I tuoi diritti",
    s7_p="Poiché nessun dato personale viene raccolto o archiviato dallo sviluppatore al di fuori del tuo dispositivo, non esiste alcun database esterno da consultare, correggere o eliminare. Mantieni sempre il controllo completo sulle autorizzazioni concesse all'applicazione tramite le Impostazioni iOS.",
    s8_h="Contatto",
    s8_p1="Per qualsiasi domanda relativa a questa informativa sulla privacy, puoi contattare lo sviluppatore tramite ",
    s8_p2=".",
    footer_copy="© 2026 TripSweep. Sviluppato da Jeffrey Brignoli.",
    footer_home="Home", footer_kofi="Ko-fi",
),
"de": dict(
    title="Datenschutzerklärung — TripSweep",
    nav_home="Startseite",
    h1="Datenschutzerklärung",
    updated="Zuletzt aktualisiert: 16. September 2026",
    intro='TripSweep ("die App") wird von Jeffrey Brignoli entwickelt. Diese Seite erklärt, welche Daten die App verwendet, wohin sie gehen und warum. Das Leitprinzip des Projekts ist einfach: <strong>nichts verlässt jemals dein iPhone</strong>.',
    s1_h="Was die App nicht tut",
    s1_items=[
        "Sie sammelt, sendet oder teilt deine Fotos, Videos oder Metadaten mit niemandem.",
        "Sie erstellt kein Benutzerkonto und fragt keine persönlichen Informationen ab (Name, E-Mail...).",
        "Sie enthält kein Werbe-SDK und kein app-übergreifendes Tracking.",
        "Sie funktioniert ohne jeden Server: Die Ortserkennung (Stadt/Land) erfolgt vollständig offline, anhand von Daten, die in der App eingebettet sind (GeoNames.org, Lizenz CC BY 4.0), ohne jemals einen Online-Dienst abzufragen.",
    ],
    s2_h="Zugriff auf deine Fotobibliothek",
    s2_p1="Die App fordert vollen Zugriff auf deine Fotobibliothek (Fotos) aus zwei Gründen an:",
    s2_items=[
        "Analyse deiner Fotos und Videos, um sie nach Aufenthalt zu gruppieren und den belegten Speicherplatz zu berechnen — diese Verarbeitung erfolgt vollständig auf deinem Gerät.",
        "Löschen der Fotos, die du ausdrücklich zum Löschen auswählst — das Löschen erfolgt immer über „Kürzlich gelöscht“ (30 Tage), nie ein sofortiges endgültiges Löschen.",
    ],
    s2_p2="Kein Foto, keine Miniaturansicht und keine Metadaten aus deiner Fotobibliothek werden jemals von deinem Gerät übertragen.",
    s3_h="Zugriff auf deinen Standort",
    s3_p="Die App fordert Zugriff auf deinen Standort nur an, wenn du dich entscheidest, manuell einen „Ort“ (zum Beispiel „Zuhause“ oder „Arbeit“) in der Funktion zur Ortsverwaltung hinzuzufügen. Dieser Standort wird lokal auf deinem Gerät gespeichert und niemals anderswohin übertragen. Er dient nur dazu, die Entfernung zu erkannten Aufenthalten zu vergleichen, damit du sie bei Bedarf aus der Liste ausschließen kannst.",
    s4_h="Synchronisierung mit der Mac-App",
    s4_p1="Wenn du zusätzlich ",
    s4_p_link="PhotoCull",
    s4_p2=" auf deinem Mac verwendest, kann die Begleit-App über eine direkte lokale USB-/WLAN-Verbindung zwischen deinen beiden Apple-Geräten Informationen mit ihr austauschen (ein Standardprotokoll, das für die Synchronisierung von iOS-Geräten verwendet wird) — niemals über das Internet oder einen Server eines Drittanbieters.",
    s5_h="In-App-Käufe",
    s5_p="Die App bietet eine optionale kostenpflichtige Funktion („Pro“, einmaliger Kauf), die ausschließlich von Apple über StoreKit abgewickelt wird. Es werden keine Zahlungsinformationen vom Entwickler erfasst, gespeichert oder eingesehen: Apple wickelt die gesamte Transaktion gemäß seiner eigenen Datenschutzerklärung ab.",
    s6_h="Statistiken und Diagnose",
    s6_p="Die App integriert derzeit kein Analyse- oder Tracking-Tool von Drittanbietern. Wenn du die Freigabe von Analysedaten für App-Entwickler aktiviert hast (iOS-Einstellungen > Datenschutz & Sicherheit > Analyse & Verbesserungen), kann Apple anonymisierte Absturzberichte übermitteln — diese Funktion wird vollständig von Apple verwaltet, unabhängig von der App.",
    s7_h="Deine Rechte",
    s7_p="Da außerhalb deines Geräts keine personenbezogenen Daten vom Entwickler erfasst oder gespeichert werden, gibt es keine externe Datenbank, die eingesehen, korrigiert oder gelöscht werden könnte. Du behältst jederzeit die volle Kontrolle über die der App erteilten Berechtigungen über die iOS-Einstellungen.",
    s8_h="Kontakt",
    s8_p1="Bei Fragen zu dieser Datenschutzerklärung kannst du den Entwickler über ",
    s8_p2=" kontaktieren.",
    footer_copy="© 2026 TripSweep. Entwickelt von Jeffrey Brignoli.",
    footer_home="Startseite", footer_kofi="Ko-fi",
),
"es": dict(
    title="Política de privacidad — TripSweep",
    nav_home="Inicio",
    h1="Política de privacidad",
    updated="Última actualización: 16 de septiembre de 2026",
    intro='TripSweep («la aplicación») está desarrollada por Jeffrey Brignoli. Esta página explica qué datos utiliza la aplicación, adónde van y por qué. El principio rector del proyecto es simple: <strong>nada sale nunca de tu iPhone</strong>.',
    s1_h="Lo que la aplicación no hace",
    s1_items=[
        "No recopila, envía ni comparte tus fotos, vídeos o metadatos con nadie.",
        "No crea ninguna cuenta de usuario ni solicita ninguna información personal (nombre, email...).",
        "No contiene ningún SDK publicitario ni de seguimiento (tracking) entre aplicaciones.",
        "No funciona con ningún servidor: el reconocimiento de lugares (ciudad/país) se realiza completamente sin conexión, a partir de datos integrados en la aplicación (GeoNames.org, licencia CC BY 4.0), sin consultar nunca un servicio en línea.",
    ],
    s2_h="Acceso a tu biblioteca de fotos",
    s2_p1="La aplicación solicita acceso completo a tu biblioteca de fotos (Fotos) por dos motivos:",
    s2_items=[
        "Analizar tus fotos y vídeos para agruparlos por estancia y calcular el espacio ocupado — este procesamiento se realiza completamente en tu dispositivo.",
        "Eliminar las fotos que elijas explícitamente eliminar — la eliminación siempre pasa por «Eliminados recientemente» (30 días), nunca una eliminación definitiva inmediata.",
    ],
    s2_p2="Ninguna foto, miniatura o metadato extraído de tu biblioteca de fotos se transmite nunca fuera de tu dispositivo.",
    s3_h="Acceso a tu ubicación",
    s3_p="La aplicación solicita acceso a tu ubicación únicamente cuando eliges añadir manualmente un «lugar» (por ejemplo «Casa» o «Trabajo») en la función de gestión de lugares. Esta ubicación se guarda localmente en tu dispositivo y nunca se transmite a otro sitio. Se utiliza solo para comparar la distancia con las estancias detectadas, para que puedas excluirlas de la lista si lo deseas.",
    s4_h="Sincronización con la app de Mac",
    s4_p1="Si también utilizas ",
    s4_p_link="PhotoCull",
    s4_p2=" en tu Mac, la app complementaria puede intercambiar información con ella mediante una conexión USB/Wi-Fi local directa entre tus dos dispositivos Apple (protocolo estándar utilizado para la sincronización de dispositivos iOS) — nunca a través de Internet ni de un servidor de terceros.",
    s5_h="Compras dentro de la app",
    s5_p="La aplicación ofrece una función de pago opcional («Pro», compra única) gestionada exclusivamente por Apple mediante StoreKit. El desarrollador no recopila, almacena ni puede ver ninguna información de pago: Apple gestiona toda la transacción conforme a su propia política de privacidad.",
    s6_h="Estadísticas y diagnósticos",
    s6_p="A día de hoy, la aplicación no integra ninguna herramienta de análisis o seguimiento de terceros. Si has activado el uso compartido de datos de análisis con los desarrolladores de aplicaciones (Ajustes de iOS > Privacidad y seguridad > Análisis y mejoras), Apple puede enviar informes de fallos anonimizados — esta función la gestiona Apple por completo, de forma independiente a la aplicación.",
    s7_h="Tus derechos",
    s7_p="Dado que el desarrollador no recopila ni almacena ningún dato personal fuera de tu dispositivo, no existe ninguna base de datos externa que consultar, corregir o eliminar. Mantienes en todo momento el control total sobre los permisos concedidos a la aplicación a través de los Ajustes de iOS.",
    s8_h="Contacto",
    s8_p1="Para cualquier pregunta relacionada con esta política de privacidad, puedes contactar con el desarrollador a través de ",
    s8_p2=".",
    footer_copy="© 2026 TripSweep. Desarrollado por Jeffrey Brignoli.",
    footer_home="Inicio", footer_kofi="Ko-fi",
),
}

print("privacy dict loaded ok", len(PRIVACY))
print("desktop dict loaded ok", len(DESKTOP))
print("dict loaded ok", len(INDEX))

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

def render_index(lang):
    d = INDEX[lang]
    a = lambda rel: asset_path(lang, rel)
    features_html = "\n".join(
        f'''        <div class="feature-card">
          <span class="icon">{icon}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </div>''' for icon, title, text in d["features"]
    )
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}" />
  <link rel="icon" type="image/png" href="{a('assets/img/favicon-tripsweep.png')}" />
{hreflang_links('index.html')}
  <link rel="stylesheet" href="{a('assets/style.css')}" />
</head>
<body>
  <div class="wrap">
    <header class="nav">
      <a class="brand" href="{path_for(lang, 'index.html', lang)}">
        <img class="logo-img" src="{a('assets/img/tripsweep-icon.png')}" alt="" />
        TripSweep
      </a>
      <nav class="links">
        <a href="{path_for(lang, 'desktop.html', lang)}">{d['nav_desktop']}</a>
        <a href="#fonctionnalites">{d['nav_features']}</a>
        <a href="#confidentialite">{d['nav_privacy_anchor']}</a>
        <a href="{path_for(lang, 'privacy.html', lang)}">{d['nav_privacy']}</a>
        {lang_switcher(lang, 'index.html')}
      </nav>
    </header>

    <section class="hero">
      <span class="badge">{d['badge']}</span>
      <h1>{d['h1']}</h1>
      <p class="subtitle">
        {d['subtitle']}
      </p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#" aria-disabled="true">{d['cta_store']}</a>
        <a class="btn btn-kofi" href="https://ko-fi.com/jeffreybrignoli" target="_blank" rel="noopener">{d['cta_kofi']}</a>
      </div>
      <p style="margin-top:20px; font-size:14px;">
        <a href="{path_for(lang, 'desktop.html', lang)}">{d['cta_desktop_link']}</a>
      </p>

      <div class="phone-frame">
        <img src="{a(f'assets/screenshots/tripsweep-mytrips-{lang}.jpg')}" alt="{d['hero_alt']}" />
      </div>
    </section>

    <section id="apercu">
      <h2>{d['preview_h2']}</h2>
      <div class="screens-row">
        <div class="phone-frame phone-frame-small">
          <img src="{a(f'assets/screenshots/tripsweep-mytrips-{lang}.jpg')}" alt="{d['preview_alt1']}" />
        </div>
        <div class="phone-frame phone-frame-small">
          <img src="{a(f'assets/screenshots/tripsweep-about-{lang}.jpg')}" alt="{d['preview_alt2']}" />
        </div>
      </div>
    </section>

    <section id="fonctionnalites">
      <h2>{d['features_h2']}</h2>
      <div class="features">
{features_html}
      </div>
    </section>

    <section id="confidentialite">
      <div class="privacy-strip">
        <h2>{d['privacy_h2']}</h2>
        <p>
          {d['privacy_p']}
        </p>
        <a class="btn btn-secondary" href="{path_for(lang, 'privacy.html', lang)}">{d['privacy_btn']}</a>
      </div>
    </section>

    <footer>
      <div>{d['footer_copy']}</div>
      <div class="footer-links">
        <a href="{path_for(lang, 'desktop.html', lang)}">{d['footer_desktop']}</a>
        <a href="{path_for(lang, 'privacy.html', lang)}">{d['footer_privacy']}</a>
        <a href="https://ko-fi.com/jeffreybrignoli" target="_blank" rel="noopener">{d['footer_kofi']}</a>
        <a href="https://github.com/brignolij/TripSweepSite" target="_blank" rel="noopener">{d['footer_github']}</a>
      </div>
    </footer>
  </div>
</body>
</html>
'''

def render_desktop(lang):
    d = DESKTOP[lang]
    a = lambda rel: asset_path(lang, rel)
    features_html = "\n".join(
        f'''        <div class="feature-card">
          <span class="icon">{icon}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </div>''' for icon, title, text in d["features"]
    )
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}" />
  <link rel="icon" type="image/png" href="{a('assets/img/favicon-photocull.png')}" />
{hreflang_links('desktop.html')}
  <link rel="stylesheet" href="{a('assets/style.css')}" />
</head>
<body>
  <div class="wrap">
    <header class="nav">
      <a class="brand" href="{path_for(lang, 'index.html', lang)}">
        <img class="logo-img" src="{a('assets/img/photocull-icon.png')}" alt="" />
        PhotoCull
      </a>
      <nav class="links">
        <a href="{path_for(lang, 'index.html', lang)}">{d['nav_ios']}</a>
        <a href="#fonctionnalites">{d['nav_features']}</a>
        <a href="{path_for(lang, 'privacy.html', lang)}">{d['nav_privacy']}</a>
        {lang_switcher(lang, 'desktop.html')}
      </nav>
    </header>

    <section class="hero">
      <span class="badge">{d['badge']}</span>
      <h1>{d['h1']}</h1>
      <p class="subtitle">
        {d['subtitle']}
      </p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#" aria-disabled="true">{d['cta_download']}</a>
        <a class="btn btn-kofi" href="https://ko-fi.com/jeffreybrignoli" target="_blank" rel="noopener">{d['cta_kofi']}</a>
      </div>

      <div class="phone-mock" style="width: 420px; height: 280px; border-radius: 16px;" aria-hidden="true">
        <div class="screen" style="border-radius: 10px; flex-direction: row; flex-wrap: wrap; gap: 6px;">
          <span class="thumb" style="width: 90px; height: 90px;"></span>
          <span class="thumb" style="width: 90px; height: 90px;"></span>
          <span class="thumb" style="width: 90px; height: 90px;"></span>
          <span class="thumb" style="width: 90px; height: 90px;"></span>
          <span class="thumb" style="width: 90px; height: 90px;"></span>
          <span class="thumb" style="width: 90px; height: 90px;"></span>
          <span class="thumb" style="width: 90px; height: 90px;"></span>
          <span class="thumb" style="width: 90px; height: 90px;"></span>
        </div>
      </div>
    </section>

    <section id="fonctionnalites">
      <h2>{d['features_h2']}</h2>
      <div class="features">
{features_html}
      </div>
    </section>

    <section>
      <div class="privacy-strip">
        <h2>{d['strip_h2']}</h2>
        <p>
          {d['strip_p_before']}
          <a href="{path_for(lang, 'index.html', lang)}">{d['strip_p_link']}</a>{d['strip_p_after']}
        </p>
      </div>
    </section>

    <footer>
      <div>{d['footer_copy']}</div>
      <div class="footer-links">
        <a href="{path_for(lang, 'index.html', lang)}">{d['footer_ios']}</a>
        <a href="{path_for(lang, 'privacy.html', lang)}">{d['footer_privacy']}</a>
        <a href="https://ko-fi.com/jeffreybrignoli" target="_blank" rel="noopener">{d['footer_kofi']}</a>
        <a href="https://github.com/brignolij/TripSweepSite" target="_blank" rel="noopener">{d['footer_github']}</a>
      </div>
    </footer>
  </div>
</body>
</html>
'''

def render_privacy(lang):
    d = PRIVACY[lang]
    a = lambda rel: asset_path(lang, rel)
    s1_items = "\n".join(f"        <li>{item}</li>" for item in d["s1_items"])
    s2_items = "\n".join(f"        <li>{item}</li>" for item in d["s2_items"])
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{d['title']}</title>
  <link rel="icon" type="image/png" href="{a('assets/img/favicon-tripsweep.png')}" />
{hreflang_links('privacy.html')}
  <link rel="stylesheet" href="{a('assets/style.css')}" />
</head>
<body>
  <div class="wrap">
    <header class="nav">
      <a class="brand" href="{path_for(lang, 'index.html', lang)}">
        <img class="logo-img" src="{a('assets/img/tripsweep-icon.png')}" alt="" />
        TripSweep
      </a>
      <nav class="links">
        <a href="{path_for(lang, 'index.html', lang)}">{d['nav_home']}</a>
        {lang_switcher(lang, 'privacy.html')}
      </nav>
    </header>

    <div class="legal">
      <h1>{d['h1']}</h1>
      <p><em>{d['updated']}</em></p>

      <p>
        {d['intro']}
      </p>

      <h2>{d['s1_h']}</h2>
      <ul>
{s1_items}
      </ul>

      <h2>{d['s2_h']}</h2>
      <p>
        {d['s2_p1']}
      </p>
      <ul>
{s2_items}
      </ul>
      <p>
        {d['s2_p2']}
      </p>

      <h2>{d['s3_h']}</h2>
      <p>
        {d['s3_p']}
      </p>

      <h2>{d['s4_h']}</h2>
      <p>
        {d['s4_p1']}<a href="{path_for(lang, 'desktop.html', lang)}">{d['s4_p_link']}</a>{d['s4_p2']}
      </p>

      <h2>{d['s5_h']}</h2>
      <p>
        {d['s5_p']}
      </p>

      <h2>{d['s6_h']}</h2>
      <p>
        {d['s6_p']}
      </p>

      <h2>{d['s7_h']}</h2>
      <p>
        {d['s7_p']}
      </p>

      <h2>{d['s8_h']}</h2>
      <p>
        {d['s8_p1']}<a href="https://ko-fi.com/jeffreybrignoli" target="_blank" rel="noopener">Ko-fi</a>{d['s8_p2']}
      </p>
    </div>

    <footer>
      <div>{d['footer_copy']}</div>
      <div class="footer-links">
        <a href="{path_for(lang, 'index.html', lang)}">{d['footer_home']}</a>
        <a href="https://ko-fi.com/jeffreybrignoli" target="_blank" rel="noopener">{d['footer_kofi']}</a>
      </div>
    </footer>
  </div>
</body>
</html>
'''

# ---------------------------------------------------------------------------
# Write files
# ---------------------------------------------------------------------------

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

for lang in LANGS:
    prefix = "" if lang == "en" else f"{lang}/"
    write(f"{prefix}index.html", render_index(lang))
    write(f"{prefix}desktop.html", render_desktop(lang))
    write(f"{prefix}privacy.html", render_privacy(lang))

print("ALL DONE")
