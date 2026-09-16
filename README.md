# PhotosManager Companion — site vitrine

Site statique (HTML/CSS pur, aucune dépendance de build) présentant l'app compagnon
iOS de [PhotosManager](https://github.com/) : page d'accueil + politique de
confidentialité (requise par App Store Connect).

## Structure

```
website/
├── index.html       # Page d'accueil
├── privacy.html      # Politique de confidentialité
├── assets/
│   └── style.css      # Feuille de style partagée
└── README.md
```

## Prévisualiser en local

Aucun outil requis — ouvrez simplement `index.html` dans un navigateur, ou servez le
dossier avec n'importe quel serveur statique :

```bash
python3 -m http.server 8000
```

Puis ouvrez `http://localhost:8000`.

## Publier sur GitHub Pages

Ce dossier est pensé pour vivre dans **son propre dépôt GitHub dédié**, distinct du
dépôt principal de l'application (`PhotosManager`), afin de pouvoir être public et
publié via GitHub Pages sans exposer le code de l'app.

1. Créer un nouveau dépôt GitHub **public**, par exemple `photosmanager-companion-site`.
2. Pousser le contenu de ce dossier à la racine du dépôt (branche `main`).
3. Dans les réglages du dépôt : **Settings > Pages > Source** → sélectionner la branche
   `main` et le dossier `/ (root)`.
4. Le site est publié à `https://<ton-pseudo-github>.github.io/<nom-du-dépôt>/`.
5. Mettre à jour `AppLinks.websiteURL` dans l'app iOS
   (`companion-app/PhotosManagerCompanion/AppLinks.swift`) avec cette URL définitive.
6. Renseigner cette même URL comme lien "Politique de confidentialité" dans
   App Store Connect (`.../privacy.html`).

## À faire avant publication

- [ ] Remplacer le lien GitHub factice du pied de page par le vrai dépôt.
- [ ] Remplacer le mockup CSS du téléphone par de vraies captures d'écran de l'app
      (dossier `assets/screenshots/` à créer).
- [ ] Remplacer le bouton "Bientôt sur l'App Store" par le vrai lien une fois l'app publiée.
- [ ] Ajouter une favicon (`assets/favicon.svg` ou `.ico`) une fois le logo généré
      (voir `../companion-app/marketing/gemini-logo-prompt.md`).
