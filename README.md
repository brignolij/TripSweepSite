# TripSweep & PhotoCull — site vitrine

Site statique (HTML/CSS pur, aucune dépendance de build) présentant les deux apps :
**TripSweep** (compagnon iOS) et **PhotoCull** (app de bureau macOS) — pages d'accueil +
politique de confidentialité (requise par App Store Connect).

Généré à partir d'un script Python (`generate.py`, gardé hors du dossier publié —
voir plus bas) pour garantir la cohérence du contenu sur les 5 langues.

## Multilingue

Le site est disponible en 5 langues, générées comme des pages HTML statiques
**indexables séparément** (pas de switch JS côté client) :

- **Anglais = langue par défaut**, servie à la racine (`/index.html`, `/desktop.html`,
  `/privacy.html`) — pas de redirection, c'est la version que Google indexe par défaut.
- Les 4 autres langues vivent dans un sous-dossier par code langue :
  `/fr/`, `/it/`, `/de/`, `/es/` (mêmes noms de fichiers à l'intérieur).
- Chaque page déclare ses 5 variantes via `<link rel="alternate" hreflang="...">`
  (+ `x-default` pointant vers l'anglais), pour que les moteurs de recherche proposent
  la bonne langue selon l'utilisateur.
- Un sélecteur de langue (`.lang-switch`) est présent dans la nav de chaque page.

## Structure

```
website/
├── generate.py                    # Génère les 15 pages HTML depuis les dicos de contenu
├── index.html, desktop.html, privacy.html   # Anglais (défaut)
├── fr/  index.html, desktop.html, privacy.html
├── it/  index.html, desktop.html, privacy.html
├── de/  index.html, desktop.html, privacy.html
├── es/  index.html, desktop.html, privacy.html
├── assets/
│   ├── style.css                 # Feuille de style partagée
│   ├── img/                      # Logos + favicons (TripSweep, PhotoCull)
│   └── screenshots/               # Captures d'écran, une par langue
│       (tripsweep-mytrips-<lang>.jpg, tripsweep-about-<lang>.jpg)
└── README.md
```

## Mettre à jour le contenu

Le contenu de chaque langue vit dans `generate.py`, à la racine de ce dossier, sous
forme de dictionnaires Python (`INDEX`, `DESKTOP`, `PRIVACY`). Modifier le texte là,
puis relancer :

```bash
python3 generate.py
```

Ça régénère les 15 fichiers HTML d'un coup, avec les bons chemins relatifs et les
bonnes balises hreflang selon la profondeur du dossier.

## Captures d'écran

Une capture par langue est nécessaire pour `tripsweep-mytrips-<lang>.jpg` et
`tripsweep-about-<lang>.jpg` (utilisées dans le hero + la section "Un aperçu de
l'app"). Générées via le simulateur iOS en mode démo (`-UseFakeTrips YES`, voir
`companion-app/TripSweep/FakeTripsProvider.swift`) avec la langue système changée
pour chaque capture (`xcrun simctl spawn <device> defaults write "Apple Global
Domain" AppleLanguages -array <lang>`, puis reboot du simulateur).

## Prévisualiser en local

```bash
python3 -m http.server 8000
```

Puis ouvrez `http://localhost:8000` (anglais) ou `http://localhost:8000/fr/` etc.

## Publier sur GitHub Pages

Ce dossier est pensé pour vivre dans **son propre dépôt GitHub dédié**, distinct du
dépôt principal de l'application (`PhotosManager`), afin de pouvoir être public et
publié via GitHub Pages sans exposer le code de l'app.

1. Créer un nouveau dépôt GitHub **public**, par exemple `tripsweep-site`.
2. Pousser le contenu de ce dossier à la racine du dépôt (branche `main`) — **sans**
   `generate.py` s'il contient des notes internes, ou en le gardant, au choix.
3. Dans les réglages du dépôt : **Settings > Pages > Source** → sélectionner la branche
   `main` et le dossier `/ (root)`.
4. Le site est publié à `https://<ton-pseudo-github>.github.io/<nom-du-dépôt>/`.
5. **Remplacer les URLs relatives `hreflang` par des URLs absolues** avec le domaine
   définitif (actuellement `/index.html`, `/fr/index.html`, etc. — fonctionnent en
   relatif mais Google recommande des URLs absolues).
6. Mettre à jour `AppLinks.websiteURL` dans l'app iOS
   (`companion-app/TripSweep/AppLinks.swift`) avec cette URL définitive.
7. Renseigner cette même URL comme lien "Politique de confidentialité" dans
   App Store Connect (`.../privacy.html`).

## À faire avant publication

- [ ] Remplacer le lien GitHub factice du pied de page par le vrai dépôt.
- [ ] Remplacer le bouton "Bientôt sur l'App Store" / "Télécharger pour Mac (bientôt)"
      par les vrais liens une fois les apps publiées.
- [ ] URLs hreflang absolues (voir ci-dessus) une fois le domaine définitif connu.
- [ ] Captures d'écran de l'app de bureau PhotoCull (le hero garde encore le mockup CSS).
