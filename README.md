# TripSweep & PhotoCull — site

Un seul site statique pour les deux apps, publié sur **https://tripsweep.idealy.ch** par GitHub Pages
(domaine géré chez Infomaniak, voir `DEPLOY.md`). TripSweep (iOS/Android) est à la racine, PhotoCull
(Mac/Windows) sous `desktop*.html`. `photocull.idealy.ch` redirige vers `desktop.html`.

Tout est généré par `generate.py` (Python standard, aucune dépendance) dans `sites/web/`, que le workflow
`.github/workflows/pages.yml` publie à chaque push sur `main`.

## Structure

```
generate.py          # génère sites/web/ (en = racine, /fr/ /it/ /de/ /es/)
content/{en,fr,it,de,es}.py   # FAQ et articles de blog, par langue
assets/              # style.css, logos, captures d'écran (une par langue)
versions.json        # lu par les apps pour l'avertissement de mise à jour, copié dans sites/web/
sites/web/           # sortie générée et publiée : ne pas éditer à la main
```

Pages par langue : `index`, `faq`, `blog` + 3 articles, `privacy` (TripSweep) et `desktop`, `desktop-faq`,
`desktop-blog` + 3 articles (PhotoCull). Chaque page a ses hreflang, son canonical, ses données JSON-LD ;
`sitemap.xml`, `robots.txt` et `llms.txt` sont générés aussi.

## Mettre à jour

Le texte vit dans `generate.py` (pages, confidentialité, tarifs) et `content/` (FAQ, blog). Puis :

```bash
python3 generate.py   # réécrit sites/web/
git add -A && git commit && git push   # Pages republie
```

## Captures d'écran

Générées par `companion-app/TripSweepUITests/MarketingScreenshotsUITests.swift` (la commande est dans le
commentaire du fichier), sur un simulateur dédié sans photos personnelles, puis réduites :
`magick <png> -resize 500x -quality 82 <jpg>`.

## Prévisualiser

```bash
python3 -m http.server 8000 -d sites/web
```
