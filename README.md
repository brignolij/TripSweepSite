# TripSweep

A photo cleanup app for iPhone and Android that runs 100% on your device: no account, no cloud, no upload.

**Website: [tripsweep.idealy.ch](https://tripsweep.idealy.ch/)** · [Français](https://tripsweep.idealy.ch/fr/) · [Italiano](https://tripsweep.idealy.ch/it/) · [Deutsch](https://tripsweep.idealy.ch/de/) · [Español](https://tripsweep.idealy.ch/es/)

## TripSweep for iPhone and Android

TripSweep groups your photos and videos by trip (or by event and month when they have no location), shows what takes up space, and finds identical copies, similar and blurry photos, screenshots and large videos, so you keep the best shot and delete the rest in a few taps.

- [Download TripSweep on the App Store](https://apps.apple.com/app/tripsweep/id6813028251) (iOS 18+)
- [Get TripSweep on Google Play](https://play.google.com/store/apps/details?id=com.tripsweep.app) (Android 11+)
- [TripSweep website](https://tripsweep.idealy.ch/) · [FAQ](https://tripsweep.idealy.ch/faq.html)

## PixCuller for Mac and Windows

PixCuller, the desktop app that sorts your iPhone or Android photos on a computer, has its own website and repository:
**[pixculler.idealy.ch](https://pixculler.idealy.ch/)** ([brignolij/PixCullerSite](https://github.com/brignolij/PixCullerSite)).

## Guides

- [How to free up iPhone storage without paying for iCloud](https://tripsweep.idealy.ch/blog-free-up-iphone-storage.html)
- [How to delete duplicate and similar photos on your iPhone](https://tripsweep.idealy.ch/blog-delete-duplicate-photos-iphone.html)
- [How to free up Android storage without paying for Google One](https://tripsweep.idealy.ch/blog-free-up-android-storage.html)
- All guides: [TripSweep blog](https://tripsweep.idealy.ch/blog.html), in five languages. Guides to sort photos on a Mac or PC: [PixCuller blog](https://pixculler.idealy.ch/blog.html).

## Privacy

Your photos, videos and locations never leave your devices. The app only sends optional anonymous usage statistics, which you can turn off. Details in the [privacy policy](https://tripsweep.idealy.ch/privacy.html).

## About this repository

This repository holds the TripSweep website (published by GitHub Pages) and the older [PixCuller releases](https://github.com/brignolij/TripSweepSite/releases) (new ones are on [PixCullerSite](https://github.com/brignolij/PixCullerSite/releases)). The apps' source code is not here.

---

## Maintenance du site

Site statique de TripSweep seul. PixCuller a son propre site depuis novembre 2026 (dépôt `brignolij/PixCullerSite`,
`pixculler.idealy.ch`, dossier local `../pixculler-website/`) ; les liens vers PixCuller sont absolus.
Domaine géré chez Infomaniak, voir `DEPLOY.md`.

Tout est généré par `generate.py` dans `sites/web/`, que le workflow `.github/workflows/pages.yml` publie à
chaque push sur `main`. Seule dépendance : `cwebp` (`brew install webp`) pour les captures en WebP.

```
generate.py                   # génère sites/web/ (en = racine, /fr/ /it/ /de/ /es/)
content/{en,fr,it,de,es}.py   # FAQ et articles de blog, par langue
assets/                       # style.css, logos, captures d'écran (une par langue)
versions.json                 # lu par les apps pour l'avertissement de mise à jour, copié dans sites/web/
check_links.py                # vérifie liens internes, redirections, sitemap, longueur des titres et descriptions
indexnow.py                   # prévient Bing (IndexNow) après une mise en ligne
sites/web/                    # sortie générée et publiée : ne pas éditer à la main
```

Chaque page a ses hreflang, son canonical et ses données JSON-LD ; `sitemap.xml`, `robots.txt`, `llms.txt`,
`404.html` et les fichiers de vérification (Bing, IndexNow) sont générés aussi. Un nouvel article prend ses
dates dans `POST_DATES` ; titres ≤ 60 caractères, descriptions ≤ 160.

### Mettre à jour

```bash
python3 generate.py
python3 check_links.py https://pixculler.idealy.ch=../pixculler-website/sites/web   # vérifie aussi les liens vers PixCuller
```

```bash
git add -A && git commit && git push
```

Une fois le déploiement Pages terminé :

```bash
python3 indexnow.py
```

### Captures d'écran

Générées par `companion-app/TripSweepUITests/MarketingScreenshotsUITests.swift` (la commande est dans le
commentaire du fichier), sur un simulateur dédié sans photos personnelles, puis réduites :
`magick <png> -resize 500x -quality 82 <jpg>`. Les versions WebP sont produites par `generate.py`.

### Prévisualiser

```bash
python3 -m http.server 8000 -d sites/web
```

### versions.json : ne jamais le déplacer

`https://tripsweep.idealy.ch/versions.json` est lu par les apps TripSweep installées (iOS `UpdateChecker.swift`,
Android `UpdateChecker.kt`) **et** par les PixCuller installés (`src/PixCuller.Core/Updates/UpdateCheck.cs`) : il
reste ici, avec son schéma et son entrée `desktop`. Le site PixCuller en publie une copie
(`https://pixculler.idealy.ch/versions.json`, dépôt PixCullerSite) pour les futures versions de PixCuller. **Tant que
des versions anciennes de PixCuller tournent, les deux copies doivent rester identiques** : toute modification se fait
dans les deux dépôts. Les releases PixCuller de ce dépôt restent en place (`desktop.downloads` y renvoie).

### Anciennes adresses PixCuller

Les pages PixCuller (`desktop.html`, `desktop-faq.html`, `desktop-blog*.html`, dans les 5 langues) sont remplacées
par de petites pages de redirection (`meta refresh` + `canonical` + `noindex` + lien visible) générées par
`write_moved()` depuis la liste figée `PIXCULLER_MOVED`. Elles ne sont ni dans `sitemap.xml` ni dans `llms.txt`.
Table complète ancienne → nouvelle adresse : `README.md` du dépôt PixCullerSite. En bref : `/desktop.html` →
`https://pixculler.idealy.ch/`, `/desktop-faq.html` → `/faq.html`, `/desktop-blog.html` → `/blog.html`,
`/desktop-blog-<slug>.html` → `/blog-<slug>.html` (et pareil sous `/fr/ /it/ /de/ /es/`).

`privacy.html` n'est pas redirigée : c'est la politique de TripSweep, qui décrit encore PixCuller (les PixCuller
installés et la fiche Microsoft Store y renvoient). PixCuller a la sienne sur `https://pixculler.idealy.ch/privacy.html`.
