# Mettre le site en ligne sur tripsweep.idealy.ch

Un seul site pour les deux apps : TripSweep à la racine, PhotoCull sur `desktop.html`
(`desktop-faq.html`, `desktop-blog*.html`). Hébergé par GitHub Pages, domaine géré chez Infomaniak.

Ordre à respecter : **DNS → GitHub → attendre le HTTPS → Search Console → mettre à jour les apps**.

## 1. DNS chez Infomaniak (5 min)

1. Manager Infomaniak → **Web & Domaine** → **Domaines** → cliquer sur `idealy.ch`.
2. Ouvrir **Zone DNS** (parfois « Gérer la zone DNS »).
3. **Ajouter un enregistrement** :

   | Champ | Valeur |
   |---|---|
   | Type | `CNAME` |
   | Source / Nom | `tripsweep` |
   | Cible | `brignolij.github.io.` (avec le point final si le formulaire le demande) |
   | TTL | 3600 (ou la valeur par défaut) |

4. Enregistrer. Ne touchez **à aucun** autre enregistrement (MX, SPF/TXT : ce sont vos e-mails).
5. Vérifier (la propagation prend de quelques minutes à 1 h) :

```bash
dig +short CNAME tripsweep.idealy.ch
```

Résultat attendu : `brignolij.github.io.`

Les noms exacts des menus Infomaniak peuvent varier légèrement ; l'important est le CNAME `tripsweep` → `brignolij.github.io`.

## 2. GitHub Pages

1. Pousser le dossier `website/` (dépôt `brignolij/TripSweepSite`) : il contient `sites/web/` et le workflow
   `.github/workflows/pages.yml` qui publie ce dossier.
2. Dépôt sur GitHub → **Settings → Pages** :
   - **Source** : `GitHub Actions`
   - **Custom domain** : `tripsweep.idealy.ch` → Save (GitHub vérifie le DNS)
3. Attendre que la coche verte apparaisse (jusqu'à ~1 h : GitHub crée le certificat), puis cocher
   **Enforce HTTPS**.
4. Tester : https://tripsweep.idealy.ch/ et https://tripsweep.idealy.ch/desktop.html

L'ancienne adresse `brignolij.github.io/TripSweepSite/` devrait ensuite rediriger (301) vers le nouveau domaine,
`versions.json` compris. À contrôler après la mise en ligne, car les apps déjà installées lisent ce fichier.

## 3. Google Search Console

1. https://search.google.com/search-console → **Ajouter une propriété** → **Préfixe d'URL** →
   `https://tripsweep.idealy.ch/`.
2. Vérification : la balise `google-site-verification` est déjà dans toutes les pages, choisir « Balise HTML ».
3. **Sitemaps** → ajouter `sitemap.xml`.
4. Optionnel, pour couvrir tous les sous-domaines : propriété « Domaine » `idealy.ch`, avec un enregistrement
   TXT à ajouter dans la même zone DNS Infomaniak.

## 4. Après le HTTPS : à mettre à jour (à demander à Claude)

Les anciennes URLs sont encore dans : `AppLinks.swift`, `UpdateChecker.swift` (iOS), `ReviewManager.kt`,
`UpdateChecker.kt` (Android), `UpdateCheck.cs` (desktop), et dans les fiches App Store Connect, Play Console et
Microsoft Store (URL marketing et politique de confidentialité : `https://tripsweep.idealy.ch/privacy.html`).

## 5. photocull.idealy.ch (fait)

Redirection web permanente (301) Infomaniak : `photocull.idealy.ch` → `https://tripsweep.idealy.ch/desktop.html`
(HTTP et HTTPS). Utile pour une carte ou une fiche de store.

## Régénérer le site

```bash
python3 generate.py   # écrit sites/web/, puis commit + push
```
