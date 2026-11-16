# TripSweep

A photo cleanup app for iPhone and Android that runs 100% on your device: no account, no cloud, no upload.

**Website: [tripsweep.idealy.ch](https://tripsweep.idealy.ch/)** · [Français](https://tripsweep.idealy.ch/fr/) · [Italiano](https://tripsweep.idealy.ch/it/) · [Deutsch](https://tripsweep.idealy.ch/de/) · [Español](https://tripsweep.idealy.ch/es/)

## TripSweep for iPhone and Android

TripSweep groups your photos and videos by trip (or by event and month when they have no location), shows what takes up space, and finds identical copies, similar and blurry photos, screenshots and large videos, so you keep the best shot and delete the rest in a few taps.

- [Download TripSweep on the App Store](https://apps.apple.com/app/tripsweep/id6813028251) (iOS 18+)
- [Get TripSweep on Google Play](https://play.google.com/store/apps/details?id=com.tripsweep.app) (Android 11+)
- [TripSweep website](https://tripsweep.idealy.ch/) · [FAQ](https://tripsweep.idealy.ch/faq.html)

## PhotoCull for Mac and Windows

PhotoCull, the desktop app that sorts your iPhone or Android photos on a computer, has its own website and repository:
**[photocull.idealy.ch](https://photocull.idealy.ch/)** ([brignolij/PhotoCullSite](https://github.com/brignolij/PhotoCullSite)).

## Guides

- [How to free up iPhone storage without paying for iCloud](https://tripsweep.idealy.ch/blog-free-up-iphone-storage.html)
- [How to delete duplicate and similar photos on your iPhone](https://tripsweep.idealy.ch/blog-delete-duplicate-photos-iphone.html)
- [How to free up Android storage without paying for Google One](https://tripsweep.idealy.ch/blog-free-up-android-storage.html)
- All guides: [TripSweep blog](https://tripsweep.idealy.ch/blog.html), in five languages. Guides to sort photos on a Mac or PC: [PhotoCull blog](https://photocull.idealy.ch/blog.html).

## Privacy

Your photos, videos and locations never leave your devices. The app only sends optional anonymous usage statistics, which you can turn off. Details in the [privacy policy](https://tripsweep.idealy.ch/privacy.html).

## About this repository

This repository holds the TripSweep website (published by GitHub Pages) and the older [PhotoCull releases](https://github.com/brignolij/TripSweepSite/releases) (new ones are on [PhotoCullSite](https://github.com/brignolij/PhotoCullSite/releases)). The apps' source code is not here.

---

## Maintenance du site

Site statique de TripSweep seul. PhotoCull a son propre site depuis novembre 2026 (dépôt `brignolij/PhotoCullSite`,
`photocull.idealy.ch`, dossier local `../photocull-website/`) ; les liens vers PhotoCull sont absolus.
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
python3 check_links.py https://photocull.idealy.ch=../photocull-website/sites/web   # vérifie aussi les liens vers PhotoCull
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
Android `UpdateChecker.kt`) **et** par les PhotoCull installés (`src/PhotoCull.Core/Updates/UpdateCheck.cs`) : il
reste ici, avec son schéma et son entrée `desktop`. Le site PhotoCull en publie une copie
(`https://photocull.idealy.ch/versions.json`, dépôt PhotoCullSite) pour les futures versions de PhotoCull. **Tant que
des versions anciennes de PhotoCull tournent, les deux copies doivent rester identiques** : toute modification se fait
dans les deux dépôts. Les releases PhotoCull de ce dépôt restent en place (`desktop.downloads` y renvoie).

### Anciennes adresses PhotoCull

Les pages PhotoCull (`desktop.html`, `desktop-faq.html`, `desktop-blog*.html`, dans les 5 langues) sont remplacées
par de petites pages de redirection (`meta refresh` + `canonical` + `noindex` + lien visible) générées par
`write_moved()` depuis la liste figée `PHOTOCULL_MOVED`. Elles ne sont ni dans `sitemap.xml` ni dans `llms.txt`.
Table complète ancienne → nouvelle adresse : `README.md` du dépôt PhotoCullSite. En bref : `/desktop.html` →
`https://photocull.idealy.ch/`, `/desktop-faq.html` → `/faq.html`, `/desktop-blog.html` → `/blog.html`,
`/desktop-blog-<slug>.html` → `/blog-<slug>.html` (et pareil sous `/fr/ /it/ /de/ /es/`).

`privacy.html` n'est pas redirigée : c'est la politique de TripSweep, qui décrit encore PhotoCull (les PhotoCull
installés et la fiche Microsoft Store y renvoient). PhotoCull a la sienne sur `https://photocull.idealy.ch/privacy.html`.
