# TripSweep & PhotoCull

Two photo cleanup apps that run 100% on your devices: no account, no cloud, no upload.

**Website: [tripsweep.idealy.ch](https://tripsweep.idealy.ch/)** · [Français](https://tripsweep.idealy.ch/fr/) · [Italiano](https://tripsweep.idealy.ch/it/) · [Deutsch](https://tripsweep.idealy.ch/de/) · [Español](https://tripsweep.idealy.ch/es/)

## TripSweep for iPhone

TripSweep groups your photos and videos by trip (or by event and month when they have no location), shows what takes up space, and finds identical copies, similar and blurry photos, screenshots and large videos, so you keep the best shot and delete the rest in a few taps.

- [Download TripSweep on the App Store](https://apps.apple.com/app/tripsweep/id6813028251) (iOS 18+)
- [TripSweep website](https://tripsweep.idealy.ch/) · [FAQ](https://tripsweep.idealy.ch/faq.html)

## PhotoCull for Mac and Windows

PhotoCull sorts your iPhone photos on a computer: your camera roll grouped by trip, similar shots compared side by side (up to six at once) and hundreds of photos deleted in a few clicks. It also sorts any folder of photos on your computer, and never modifies your originals.

- **Mac:** [download PhotoCull for Mac](https://github.com/brignolij/TripSweepSite/releases/latest/download/PhotoCull-Desktop.zip). Free, macOS 11+ on Apple Silicon, signed and notarized by Apple.
- **Windows:** [get it from the Microsoft Store](https://apps.microsoft.com/detail/9n6wv393b3pl) or [download the zip](https://github.com/brignolij/TripSweepSite/releases/latest/download/PhotoCull-Windows-x64.zip). Free, Windows 10/11 (64-bit). Reading an iPhone needs the free Apple Devices app from the Microsoft Store. The zip is not code-signed yet, so SmartScreen may warn on first launch.
- [PhotoCull website](https://tripsweep.idealy.ch/desktop.html) · [FAQ](https://tripsweep.idealy.ch/desktop-faq.html)

## Guides

- [How to sort your iPhone photos on a Mac](https://tripsweep.idealy.ch/desktop-blog-sort-iphone-photos-on-mac.html)
- [How to sort your iPhone photos on a Windows PC](https://tripsweep.idealy.ch/desktop-blog-sort-iphone-photos-on-pc.html)
- [How to free up iPhone storage without paying for iCloud](https://tripsweep.idealy.ch/blog-free-up-iphone-storage.html)
- [How to delete duplicate and similar photos on your iPhone](https://tripsweep.idealy.ch/blog-delete-duplicate-photos-iphone.html)
- All guides: [TripSweep blog](https://tripsweep.idealy.ch/blog.html) · [PhotoCull blog](https://tripsweep.idealy.ch/desktop-blog.html), each in five languages.

## Privacy

Your photos, videos and locations never leave your devices. The apps only send optional anonymous usage statistics, which you can turn off. Details in the [privacy policy](https://tripsweep.idealy.ch/privacy.html).

## About this repository

This repository holds the website (published by GitHub Pages) and the [PhotoCull releases](https://github.com/brignolij/TripSweepSite/releases). The apps' source code is not here.

---

## Maintenance du site

Un seul site statique pour les deux apps : TripSweep à la racine, PhotoCull sous `desktop*.html`.
`photocull.idealy.ch` redirige vers `desktop.html`. Domaine géré chez Infomaniak, voir `DEPLOY.md`.

Tout est généré par `generate.py` dans `sites/web/`, que le workflow `.github/workflows/pages.yml` publie à
chaque push sur `main`. Seule dépendance : `cwebp` (`brew install webp`) pour les captures en WebP.

```
generate.py                   # génère sites/web/ (en = racine, /fr/ /it/ /de/ /es/)
content/{en,fr,it,de,es}.py   # FAQ et articles de blog, par langue
assets/                       # style.css, logos, captures d'écran (une par langue)
versions.json                 # lu par les apps pour l'avertissement de mise à jour, copié dans sites/web/
indexnow.py                   # prévient Bing (IndexNow) après une mise en ligne
sites/web/                    # sortie générée et publiée : ne pas éditer à la main
```

Chaque page a ses hreflang, son canonical et ses données JSON-LD ; `sitemap.xml`, `robots.txt`, `llms.txt`,
`404.html` et les fichiers de vérification (Bing, IndexNow) sont générés aussi. Un nouvel article prend ses
dates dans `POST_DATES` ; titres ≤ 60 caractères, descriptions ≤ 160.

### Mettre à jour

```bash
python3 generate.py
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
