# -*- coding: utf-8 -*-
# French version of the FAQ and blog of both sites. Tokens in answers/articles: {ts} {pc} {store} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Confidentialité", more="À lire aussi",
    cta_store="📱 Télécharger TripSweep sur l'App Store",
    cta_play="🤖 Télécharger TripSweep sur Google Play",
    cta_mac="💻 Télécharger PhotoCull pour Mac", cta_win="🪟 Télécharger PhotoCull pour Windows",
    cross_label={"tripsweep": "Application de bureau", "photocull": "Application iOS"},
    index={
        "tripsweep": dict(
            title="Blog TripSweep : libérer de l'espace sur iPhone, photos en double",
            desc="Guides pratiques pour libérer de l'espace sur iPhone, supprimer doublons et photos similaires et trier vos anciens voyages, sans iCloud ni envoi de photos.",
            h1="Guides pour faire le ménage dans vos photos iPhone",
            intro="Des guides courts et pratiques pour libérer de l'espace sur votre iPhone, supprimer les doublons et ne garder que les meilleures photos."),
        "photocull": dict(
            title="Blog PhotoCull : trier ses photos sur Mac ou PC, vider son iPhone",
            desc="Guides pour trier des milliers de photos plus vite sur grand écran, comparer les photos similaires et vider votre iPhone depuis un Mac ou un PC.",
            h1="Guides pour trier vos photos sur ordinateur",
            intro="Pourquoi un grand écran change la vitesse à laquelle vous triez vos photos, et comment s'en servir pour vider votre iPhone."),
    },
)

FAQ_TRIPSWEEP_EXTRA = [
    ("Quelle est la différence entre photos en double et photos similaires ?",
     "Les doublons sont des copies identiques d'un même fichier. Les photos similaires sont des prises de vue différentes d'une même scène : une rafale, cinq essais du même coucher de soleil, deux selfies presque identiques. Les doublons sont faciles à repérer ; c'est dans les photos similaires que se cache l'essentiel de l'espace gaspillé, et TripSweep regroupe les deux pour que vous en gardiez une et supprimiez les autres."),
    ("Comment TripSweep choisit-il la meilleure photo d'un groupe ?",
     "Il évalue la netteté, le score esthétique d'Apple et les visages, puis propose une photo par groupe. Cette suggestion n'est qu'un point de départ : vous pouvez garder une autre photo, en garder plusieurs ou passer le groupe. L'analyse s'effectue sur votre iPhone avec le framework Vision d'Apple."),
    ("Que trouve l'onglet Nettoyage ?",
     "Les copies identiques, les photos similaires, les photos floues, les captures d'écran et les vidéos volumineuses, chacune dans sa propre catégorie avec l'espace qu'elle occupe. Vous commencez par la catégorie qui libère le plus de place et la triez en quelques touches."),
    ("TripSweep va-t-il me proposer de supprimer mes photos favorites ?",
     "Non. Les photos que vous avez ajoutées aux favoris ne sont jamais proposées à la suppression, et rien n'est supprimé tant que vous n'avez pas confirmé."),
    ("TripSweep fonctionne-t-il avec des photos sans position GPS ?",
     "Oui. Les photos sans localisation sont regroupées par événement et par mois plutôt que par voyage : les captures d'écran, les images enregistrées et les photos prises avec la localisation désactivée sont donc triées elles aussi."),
    ("Puis-je masquer mon domicile et mon lieu de travail de mes voyages ?",
     "Oui. Ajoutez votre domicile, votre travail ou tout endroit où vous passez chaque jour comme lieu exclu : le quotidien n'apparaît plus comme un voyage et vos vrais voyages ressortent. Pro rend les lieux personnalisés illimités."),
    ("Puis-je sauvegarder ou partager un voyage avant de le supprimer ?",
     "Oui. Vous pouvez exporter un voyage entier vers votre Mac ou vers l'app Fichiers, ou le partager avec les personnes qui y étaient, puis le supprimer de votre iPhone une fois qu'il est en sécurité ailleurs."),
    ("Faut-il une connexion internet ou un compte ?",
     "Non. TripSweep ne demande aucun compte et fonctionne hors ligne. Les noms de lieux sont reconnus sur votre iPhone, et aucune photo, vidéo ni position n'est jamais envoyée à un serveur. Seules des statistiques d'usage anonymes, désactivables, peuvent être envoyées. Vous pouvez les désactiver dans l'onglet À propos."),
    ("Supprimer dans TripSweep supprime-t-il aussi mes photos d'iCloud ?",
     "Si Photos iCloud est activé, supprimer une photo sur votre iPhone la retire de tous vos appareils, car c'est ainsi que fonctionne Photos iCloud. TripSweep supprime via l'album « Supprimés récemment » : vous avez 30 jours pour changer d'avis, et l'espace iCloud est libéré une fois cet album vidé."),
    ("Puis-je passer en revue les photos de mon iPhone sur grand écran plutôt que sur le téléphone ?",
     "Oui. <a href=\"{pc}\">PhotoCull</a> est l'application de bureau gratuite pour Mac et Windows : elle affiche la pellicule de votre iPhone regroupée par voyage, compare les photos similaires côte à côte et vous permet de sélectionner des centaines de photos en quelques clics. <a href=\"{pc}\">En savoir plus sur PhotoCull</a>."),
    ("Puis-je supprimer des photos en masse depuis mon ordinateur plutôt qu'en tapotant sur le téléphone ?",
     "Oui, avec <a href=\"{pc}\">PhotoCull</a> sur un Mac ou un PC Windows. Vous sélectionnez les photos sur grand écran, et la suppression est appliquée sur votre iPhone par TripSweep via « Supprimés récemment ». La version gratuite permet 6 photos par jour depuis le Mac (voir les offres sur la page TripSweep), Pro 15, et Pro + Desktop supprime la limite."),
    ("Quels iPhone et quelles versions d'iOS TripSweep prend-il en charge ?",
     "TripSweep nécessite iOS 18 ou une version ultérieure. L'analyse des photos similaires utilise le framework Vision d'Apple et va plus vite sur les iPhone récents, mais fonctionne sur tous les modèles pris en charge. Sur Android, elle nécessite Android 11 ou une version ultérieure et se télécharge sur <a href=\"{play}\">Google Play</a>."),
]

FAQ_PHOTOCULL = dict(
    title="FAQ PhotoCull : trier et supprimer ses photos sur Mac ou PC",
    desc="Trier des milliers de photos sur ordinateur, comparer les similaires, libérer votre iPhone depuis un Mac ou un PC : les réponses sur PhotoCull.",
    nav_home="PhotoCull", nav_desktop="Application iOS",
    h1="Questions et réponses",
    intro="Comment trier vos photos plus vite depuis un ordinateur, vider votre iPhone depuis un Mac ou un PC, et ce que PhotoCull fait (et ne fait jamais) avec vos photos.",
    qa=[
        ('Comment trier les photos de mon iPhone sur ordinateur, Mac ou PC ?',
         "Branchez l'iPhone à l'ordinateur avec un câble USB, déverrouillez-le et touchez « Se fier », puis ouvrez <a href=\"{pc}\">PhotoCull</a> : il regroupe votre pellicule par voyage, compare les photos similaires côte à côte et marque des centaines de photos en quelques clics. Guides pas à pas : <a href=\"{post:sort-iphone-photos-on-mac}\">sur Mac</a> et <a href=\"{post:sort-iphone-photos-on-pc}\">sur PC Windows</a>."),
        ("Pourquoi trier ses photos sur ordinateur plutôt que sur l'iPhone ?",
         "Un grand écran affiche plus de photos à la fois, une souris et un clavier en sélectionnent des centaines en quelques secondes, et comparer des photos côte à côte est plus facile que de faire des allers-retours. Trier une pellicule de plusieurs milliers de photos représente plusieurs séances sur un téléphone, et une session bien plus courte sur un Mac ou un PC."),
        ("Qu'est-ce que PhotoCull ?",
         "PhotoCull est une application de bureau gratuite pour Mac et Windows qui regroupe vos photos par voyage, compare les photos similaires côte à côte et supprime en masse ce qui ne mérite pas d'être gardé. Elle lit la pellicule de votre iPhone par USB, ou n'importe quel dossier de photos de votre ordinateur, et fonctionne 100 % sur l'appareil."),
        ("Comment trier rapidement des milliers de photos ?",
         "Ouvrez la vue Voyages : votre photothèque est regroupée par voyage avec l'espace occupé par chacun, vous commencez donc par le plus lourd. Dans un voyage, sélectionnez les photos en masse, comparez les photos similaires côte à côte et gardez la meilleure de chaque groupe. Les mêmes filtres que dans l'app iOS (voyages d'une seule journée, lieux exclus comme le domicile ou le travail, taille) permettent d'affiner."),
        ("Comment libérer de l'espace sur mon iPhone depuis un Mac ou un PC ?",
         "Branchez votre iPhone en USB, ouvrez PhotoCull, sélectionnez les voyages et les photos dont vous n'avez plus besoin, puis confirmez. La suppression est appliquée sur l'iPhone par l'<a href=\"{ts}\">app TripSweep</a> gratuite via « Supprimés récemment » : l'espace est donc libéré dès que vous videz cet album."),
        ("Puis-je supprimer des photos de mon iPhone directement depuis mon ordinateur ?",
         "Oui, depuis un Mac ou un PC Windows, avec l'<a href=\"{ts}\">app TripSweep</a> installée sur l'iPhone. Depuis un Mac, la version gratuite permet 6 photos par jour, Pro 15, et Pro + Desktop supprime la limite."),
        ("La suppression depuis PhotoCull est-elle définitive ?",
         "Non. Les suppressions sur l'iPhone passent toujours par l'album « Supprimés récemment » de l'app Photos, où les photos restent 30 jours et peuvent être restaurées. PhotoCull n'effectue jamais de suppression définitive immédiate."),
        ("Comment connecter mon iPhone à PhotoCull ?",
         "Utilisez un câble USB, déverrouillez l'iPhone et touchez « Se fier à cet ordinateur » quand on vous le demande. Sur Mac, rien d'autre n'est nécessaire. Sur Windows, installez l'app gratuite Apple Devices depuis le Microsoft Store, qui fournit le pilote permettant à PhotoCull de lire l'iPhone."),
        ("Ai-je besoin de l'app iOS TripSweep ?",
         "Pas pour parcourir, comparer et trier. Vous en avez besoin uniquement pour supprimer des photos de l'iPhone, car la suppression est appliquée sur le téléphone. Les dossiers de votre ordinateur peuvent être triés sans elle."),
        ("Comment trouver les photos en double dans un dossier sur mon Mac ou mon PC ?",
         "Ouvrez le dossier dans PhotoCull (« Ouvrir un dossier », ou glissez-le sur la fenêtre). Il parcourt les sous-dossiers, compare ce que montrent les photos et appose le même badge « ≈ N » sur les copies exactes, les rafales et les prises quasi identiques. Gardez la meilleure de chaque groupe et envoyez le reste à la Corbeille. Guides : <a href=\"{post:find-duplicate-photos-on-mac}\">sur Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">sur Windows</a>."),
        ("Puis-je utiliser PhotoCull sur des photos stockées sur mon ordinateur, et non sur un iPhone ?",
         "Oui. Ouvrez n'importe quel dossier : PhotoCull y repère les photos similaires, affiche les badges sur celles-ci et vous laisse comparer et supprimer sans limite quotidienne."),
        ("Comment PhotoCull détecte-t-il les photos similaires ?",
         "Il compare le contenu de vos photos, pas leurs noms de fichiers : les rafales, les prises presque identiques et la même scène photographiée plusieurs fois se retrouvent dans le même groupe. Vous pouvez comparer jusqu'à 6 photos côte à côte et garder la plus nette, la mieux cadrée."),
        ("Comment comparer des photos similaires côte à côte ?",
         "Sélectionnez un groupe de photos similaires et ouvrez la comparaison : jusqu'à 6 photos s'affichent à la même taille pour juger la mise au point, les expressions et le cadrage. Gardez la meilleure et sélectionnez les autres."),
        ("PhotoCull fonctionne-t-il sous Windows ?",
         "Oui : Windows 10 et 11 (64 bits). La lecture d'un iPhone nécessite l'app gratuite Apple Devices du Microsoft Store. L'application n'est pas encore signée numériquement, donc Windows SmartScreen peut afficher un avertissement au premier lancement : choisissez « Informations complémentaires » puis « Exécuter quand même »."),
        ("Quels Mac PhotoCull prend-il en charge ?",
         "Les Mac avec puce Apple Silicon sous macOS 11 ou version ultérieure. L'application est signée et notarisée par Apple, elle s'ouvre donc sans avertissement de sécurité."),
        ("PhotoCull est-il gratuit ? Y a-t-il un abonnement ?",
         "PhotoCull est gratuit à télécharger et il n'y a aucun abonnement. Parcourir, comparer et trier est gratuit, et le tri d'un dossier sur votre ordinateur n'est jamais limité. La suppression de photos d'un iPhone depuis un Mac est limitée à 6 par jour en version gratuite, 15 avec TripSweep Pro et illimitée avec Pro + Desktop (achats uniques effectués dans l'app iOS TripSweep)."),
        ("PhotoCull envoie-t-il mes photos vers un serveur ou le cloud ?",
         "Non. PhotoCull fonctionne 100 % sur l'appareil : pas de compte, pas de cloud, aucune photo, vidéo ni position n'est jamais envoyée où que ce soit. La reconnaissance des lieux et la détection des photos similaires s'exécutent sur votre ordinateur. Seules des statistiques d'usage anonymes, désactivables, peuvent être envoyées."),
        ("PhotoCull modifie-t-il mes photos originales ?",
         "Non. PhotoCull ne fait que lire vos photos pour les afficher et les comparer. La seule modification qu'il effectue est la suppression que vous confirmez."),
        ("Comment masquer mon domicile et mon lieu de travail dans la vue Voyages ?",
         "Ajoutez-les comme lieux exclus : le quotidien cesse alors d'apparaître comme un voyage et vos vrais voyages ressortent. Le réglage est le même que dans l'app iOS."),
        ("Puis-je faire le tri après des vacances depuis mon ordinateur ?",
         "Oui, c'est l'usage typique. Après un voyage, branchez l'iPhone, ouvrez ce voyage dans PhotoCull, comparez les photos similaires, gardez la meilleure de chaque groupe et supprimez le reste. L'<a href=\"{ts}\">app TripSweep</a> peut aussi exporter tout le voyage avant que vous ne supprimiez quoi que ce soit."),
        ("Puis-je utiliser PhotoCull pour préparer un album photo ou une sauvegarde ?",
         "PhotoCull vous aide à décider ce qui mérite d'être gardé : triez le voyage, supprimez les doublons et les photos quasi identiques, puis sauvegardez ou partagez ce qui reste. L'<a href=\"{ts}\">app TripSweep</a> peut exporter ou partager un voyage entier."),
    ],
    footer_copy="© 2026 PhotoCull. Développé par Jeffrey Brignoli.",
    footer_privacy="Confidentialité", footer_kofi="Ko-fi",
)

BLOG = {
"tripsweep": [
dict(slug="free-up-iphone-storage",
     title="Libérer de l'espace sur iPhone sans iCloud : le guide pratique",
     desc="Où part vraiment le stockage de votre iPhone et les moyens les plus rapides de libérer des gigaoctets de photos et de vidéos sans payer plus d'iCloud.",
     h1="Comment libérer de l'espace sur iPhone sans payer pour iCloud",
     body="""      <p>« Stockage iPhone saturé » signifie presque toujours la même chose : l'app Photos. Les photos et les vidéos sont généralement le poste le plus lourd dans Réglages → Général → Stockage iPhone, et la plus grande partie de cet espace est du gaspillage que vous pouvez supprimer sans perdre le moindre souvenir.</p>

      <h2>1. Commencez par ce qui pèse le plus</h2>
      <p>Les grosses vidéos sont le gain le plus rapide : quelques minutes de vidéo 4K occupent autant de place que des centaines de photos. Triez vos vidéos par taille, regardez les premières secondes et supprimez celles que vous n'ouvrirez plus jamais. Les enregistrements d'écran et les vidéos reçues par les messageries sont des coupables fréquents.</p>

      <h2>2. Supprimez les photos similaires, pas seulement les doublons</h2>
      <p>L'app Photos sait trouver les doublons exacts, mais le vrai gaspillage vient des prises quasi identiques : la rafale de dix images, cinq essais de la même photo de groupe, trois selfies à la suite. Gardez la meilleure de chaque groupe et supprimez le reste. C'est là que la plupart des gens récupèrent le plus d'espace, et c'est la partie la plus pénible à faire à la main.</p>

      <h2>3. Faites le ménage dans les captures d'écran et les photos floues</h2>
      <p>Les captures d'écran s'accumulent sans qu'on s'en aperçoive : billets, plans, conversations dont vous n'avez plus besoin. Il en va de même des photos floues et des clichés accidentels. Elles méritent rarement de rester, et on les passe vite en revue d'un seul bloc.</p>

      <h2>4. Videz « Supprimés récemment »</h2>
      <p>Les photos supprimées restent 30 jours dans l'album Supprimés récemment et continuent d'occuper de la place. Une fois satisfait de vos choix, videz-le pour récupérer vraiment l'espace.</p>

      <h2>5. Triez vos anciens voyages, un par un</h2>
      <p>Les anciennes vacances forment le plus gros bloc de photos que vous ne regardez jamais. Avancer voyage par voyage est plus facile que de faire défiler une photothèque de milliers de photos : choisissez le voyage le plus lourd, gardez les meilleurs moments, supprimez le reste.</p>

      <h2>Comment TripSweep accélère tout ça</h2>
      <p><a href="{ts}">TripSweep</a> fait ces étapes à votre place sur l'iPhone. Son onglet Nettoyage liste les copies identiques, les photos similaires, les photos floues, les captures d'écran et les vidéos volumineuses, chacune avec l'espace qu'elle occupe. Vos voyages sont regroupés par lieu et par date et classés par taille, et un bouton « Garder 1 par groupe » traite toute une catégorie d'une seule touche. Les favoris ne sont jamais proposés à la suppression, les suppressions passent par « Supprimés récemment » et rien ne quitte jamais votre téléphone : pas de compte, pas de cloud. Seules des statistiques d'usage anonymes, désactivables, peuvent être envoyées.</p>
      <p>Si vous préférez un grand écran, <a href="{pc}">PhotoCull</a> fait le même tri sur un Mac ou un PC Windows.</p>

      <h2>Ai-je besoin d'iCloud ?</h2>
      <p>iCloud est une bonne sauvegarde, mais ce n'est pas un outil de nettoyage : il stocke tout, doublons compris. Faire le ménage d'abord, c'est avoir besoin de moins de stockage, où qu'il soit.</p>"""),
dict(slug="delete-duplicate-photos-iphone",
     title="Supprimer les photos en double et similaires sur iPhone",
     desc="Repérez les doublons exacts, les rafales et les photos quasi identiques sur votre iPhone, gardez la meilleure et supprimez le reste en toute sécurité.",
     h1="Comment supprimer les photos en double et similaires sur votre iPhone",
     body="""      <p>Les doublons grignotent discrètement le stockage de l'iPhone. Certains sont des copies exactes, mais la plupart sont des prises quasi identiques d'un même moment. Voici comment trouver les uns et les autres et les supprimer en toute sécurité.</p>

      <h2>Doublons et photos similaires, ce n'est pas la même chose</h2>
      <p>Un doublon exact est le même fichier enregistré deux fois, par exemple après un import ou un téléchargement. Une photo similaire est une prise de vue différente de la même scène : une rafale, plusieurs essais d'une photo de groupe, un selfie refait jusqu'à ce que vous soyez content. Les doublons exacts sont faciles à détecter ; les photos similaires sont plus fréquentes et prennent bien plus de place.</p>

      <h2>La méthode intégrée</h2>
      <p>Les versions récentes d'iOS incluent un album Doublons dans l'app Photos (sous Utilitaires). Il fusionne les copies exactes et constitue un bon premier passage. Il ne regroupe pas les photos similaires : les rafales et les photos quasi identiques restent donc dans votre photothèque.</p>

      <h2>Supprimer les photos similaires</h2>
      <p>Pour les photos similaires, il faut comparer et choisir. Ouvrez le groupe, regardez la netteté, les expressions et le cadrage, gardez la meilleure photo et supprimez les autres. Le faire à la main sur des milliers de photos est long, ce qui explique pourquoi la plupart des gens ne vont jamais au bout.</p>

      <h2>Allez plus vite avec TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> trouve les copies identiques et les photos similaires dans toute votre photothèque et affiche chaque groupe côte à côte, sans recadrage. Il suggère la meilleure prise grâce à la netteté, au score esthétique d'Apple et aux visages, et le bouton « Garder 1 par groupe » de l'onglet Nettoyage trie toute une catégorie d'une seule touche. Vos favoris ne sont jamais proposés à la suppression.</p>

      <h2>Supprimer en toute sécurité</h2>
      <ul>
        <li>Supprimez via l'app Photos : les photos supprimées vont dans « Supprimés récemment » pendant 30 jours, une erreur est donc réversible.</li>
        <li>Gardez vos favoris : marquez les photos que vous aimez avant de faire le ménage.</li>
        <li>Vérifiez Photos iCloud : s'il est activé, supprimer sur l'iPhone supprime partout.</li>
        <li>Videz « Supprimés récemment » à la fin pour récupérer l'espace.</li>
      </ul>

      <h2>Vous préférez un grand écran ?</h2>
      <p>Avec <a href="{pc}">PhotoCull</a> sur un Mac ou un PC Windows, vous pouvez comparer jusqu'à six photos similaires côte à côte et en sélectionner des centaines en quelques clics.</p>"""),
dict(slug="clean-up-vacation-photos",
     title="Trier ses photos de vacances et ne garder que les meilleures",
     desc="Transformez mille photos de vacances en album à conserver : regroupez par voyage, supprimez les photos quasi identiques, gardez les meilleurs moments.",
     h1="Comment trier vos anciennes photos de vacances et garder les meilleures",
     body="""      <p>Un voyage d'une semaine produit facilement mille photos et vidéos, dont la plupart sont des quasi-copies de quelques bonnes prises. Les trier quand le voyage est tout frais est facile ; les trier un an plus tard est une corvée. Cette méthode marche dans les deux cas.</p>

      <h2>1. Travaillez voyage par voyage</h2>
      <p>Une photothèque de 20 000 photos est décourageante ; un voyage de 800 photos, beaucoup moins. Regroupez vos photos par voyage grâce à leur date et à leur lieu, et traitez un voyage à la fois, en commençant par le plus lourd.</p>

      <h2>2. Supprimez d'abord les photos quasi identiques</h2>
      <p>L'essentiel d'un voyage, ce sont des variations de la même scène. Pour chaque groupe, gardez la photo la plus nette, avec les meilleures expressions, et supprimez les autres. Cela suffit souvent à diviser par deux la taille d'un voyage.</p>

      <h2>3. Passez en revue le reste : captures d'écran, photos floues, grosses vidéos</h2>
      <p>Les billets, les plans, les photos accidentelles et les longues vidéos que vous ne revoyez jamais sont faciles à supprimer une fois qu'elles sont listées ensemble.</p>

      <h2>4. Sauvegardez ou partagez avant de supprimer</h2>
      <p>Exportez les photos à garder vers votre ordinateur ou partagez-les avec les amis qui étaient là. Ensuite seulement, supprimez le voyage de votre téléphone. Les suppressions vont dans « Supprimés récemment », ce qui vous laisse 30 jours pour changer d'avis.</p>

      <h2>5. Les photos sans GPS</h2>
      <p>Les photos prises avec la localisation désactivée ou enregistrées depuis des messages n'ont pas de lieu. Regroupez-les plutôt par événement et par mois, pour qu'elles soient triées elles aussi.</p>

      <h2>Comment TripSweep vous aide</h2>
      <p><a href="{ts}">TripSweep</a> regroupe vos photos et vidéos par voyage (ou par événement et par mois quand il n'y a pas de GPS), indique combien de gigaoctets de photos similaires contient chaque voyage, suggère la meilleure prise de chaque groupe et exporte ou partage un voyage entier. Vous pouvez exclure le domicile et le travail pour que le quotidien ne ressemble pas à un voyage. Tout s'exécute sur votre iPhone, hors ligne.</p>
      <p>Pour faire de même sur grand écran, <a href="{pc}">PhotoCull</a> affiche les voyages de votre iPhone sur un Mac ou un PC Windows.</p>"""),
],
"photocull": [
dict(slug="sort-iphone-photos-on-mac",
     title="Comment trier les photos de son iPhone sur Mac",
     desc="Triez des milliers de photos d'iPhone sur votre Mac : ce que Photos et Transfert d'images savent faire, et une méthode plus rapide pour trier.",
     h1="Comment trier les photos de son iPhone sur Mac",
     body="""      <p>Trier une pellicule pleine sur l'iPhone, ce sont des heures de tapotements. Sur un Mac, vous voyez bien plus de photos à la fois, vous sélectionnez à la souris et vous comparez sur grand écran. Voici comment faire, avec les outils de macOS et avec une application dédiée.</p>

      <h2>Avec les outils intégrés à macOS</h2>
      <ul>
        <li><strong>Photos :</strong> importe une copie des photos de l'iPhone sur le Mac. Pratique comme sauvegarde, mais il ne vous dit pas quoi supprimer sur l'iPhone.</li>
        <li><strong>Transfert d'images :</strong> liste les photos de l'iPhone comme de simples fichiers, sans regroupement par voyage ni comparaison des photos similaires.</li>
      </ul>
      <p>Les deux fonctionnent, mais avec des milliers de photos, vous faites toujours défiler une seule longue liste.</p>

      <h2>Avec PhotoCull, étape par étape</h2>
      <p><strong>1. Installez PhotoCull.</strong> <a href="{mac}">Téléchargez-le gratuitement</a> : macOS 11 ou ultérieur sur Apple Silicon, signé et notarisé par Apple.</p>
      <p><strong>2. Branchez l'iPhone.</strong> Connectez-le avec un câble USB, déverrouillez-le et touchez « Se fier ».</p>
      <p><strong>3. Triez voyage par voyage.</strong> La vue Voyages regroupe votre pellicule par date et par lieu et indique la place prise par chaque voyage. Commencez par le plus lourd.</p>
      <p><strong>4. Comparez et marquez.</strong> Les photos similaires portent un badge : ouvrez-en jusqu'à six côte à côte, gardez la meilleure et marquez les autres, ainsi que les captures d'écran et les grosses vidéos inutiles.</p>
      <p><strong>5. Supprimez sans risque.</strong> La suppression est appliquée sur l'iPhone par l'<a href="{ts}">app TripSweep</a>, gratuite, via « Supprimés récemment » : vous avez 30 jours pour changer d'avis.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Tout reste sur votre Mac et votre iPhone : pas de compte, pas de cloud, aucun envoi.</li>
        <li>PhotoCull ne modifie jamais vos originaux et ne supprime que ce que vous confirmez.</li>
        <li>Depuis un Mac, la version gratuite permet 6 suppressions par jour, TripSweep Pro 15, et Pro + Desktop est illimité. Parcourir et trier est gratuit, et trier un dossier de photos sur le Mac n'est jamais limité.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="Comment trier les photos de son iPhone sur PC Windows",
     desc="Triez des milliers de photos d'iPhone sur Windows 10 ou 11 : ce que montrent l'app Photos et l'Explorateur, et une méthode plus rapide pour trier.",
     h1="Comment trier les photos de son iPhone sur PC Windows",
     body="""      <p>Un iPhone et un ordinateur Windows ? Vous pouvez quand même trier vos photos sur grand écran plutôt que sur le téléphone. Voici ce que Windows sait faire seul, et une méthode plus rapide.</p>

      <h2>Avec les outils intégrés à Windows</h2>
      <ul>
        <li><strong>App Photos :</strong> importe une copie des photos de l'iPhone sur le PC. Bien pour une sauvegarde, mais elle ne vous aide pas à choisir quoi supprimer.</li>
        <li><strong>Explorateur de fichiers :</strong> affiche les photos de l'iPhone dans des dossiers comme 100APPLE, nommées IMG_0001 et ainsi de suite, sans voyages ni comparaison des photos similaires.</li>
      </ul>

      <h2>Avec PhotoCull, étape par étape</h2>
      <p><strong>1. Installez Apple Devices.</strong> Installez l'app gratuite Apple Devices depuis le Microsoft Store : Windows en a besoin pour lire un iPhone.</p>
      <p><strong>2. Installez PhotoCull.</strong> Depuis le Microsoft Store ou en <a href="{win}">le téléchargeant gratuitement</a> (Windows 10/11, 64 bits). Le téléchargement n'est pas encore signé, SmartScreen peut donc afficher un avertissement au premier lancement.</p>
      <p><strong>3. Branchez l'iPhone.</strong> Connectez-le avec un câble USB, déverrouillez-le et touchez « Se fier ».</p>
      <p><strong>4. Triez voyage par voyage.</strong> La vue Voyages regroupe votre pellicule par date et par lieu et indique la place prise par chaque voyage. Commencez par le plus lourd.</p>
      <p><strong>5. Comparez, marquez, supprimez.</strong> Les photos similaires portent un badge : comparez-en jusqu'à six côte à côte, gardez la meilleure et marquez les autres. La suppression est appliquée sur l'iPhone par l'<a href="{ts}">app TripSweep</a>, gratuite, via « Supprimés récemment » : vous avez 30 jours pour changer d'avis.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Tout reste sur votre PC et votre iPhone : pas de compte, pas de cloud, aucun envoi.</li>
        <li>PhotoCull ne modifie jamais vos originaux et ne supprime que ce que vous confirmez.</li>
        <li>Parcourir et trier est gratuit, et trier un dossier de photos déjà sur le PC n'est jamais limité.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Trier des milliers de photos plus vite sur Mac ou PC Windows",
     desc="Pourquoi trier ses photos sur grand écran va bien plus vite que sur un téléphone, et une méthode simple pour en trier des milliers en une séance.",
     h1="Comment trier des milliers de photos plus vite sur Mac ou PC",
     body="""      <p>Si votre pellicule contient dix mille photos, la trier sur l'écran d'un téléphone est un chantier que vous ne finirez jamais. Sur un ordinateur, ça peut tenir en une soirée. Voici pourquoi, et une méthode qui marche.</p>

      <h2>Pourquoi un ordinateur est plus rapide</h2>
      <ul>
        <li><strong>Plus à l'écran :</strong> des dizaines de photos à la fois au lieu de quelques-unes.</li>
        <li><strong>Sélection précise :</strong> une souris et un clavier sélectionnent des centaines de photos en quelques secondes.</li>
        <li><strong>Vraie comparaison :</strong> les photos similaires côte à côte, à une taille où l'on voit la netteté et les expressions.</li>
      </ul>

      <h2>Une méthode qui marche</h2>
      <p><strong>1. Regroupez par voyage.</strong> Trier par date et par lieu découpe la photothèque en morceaux gérables. Commencez par le voyage qui prend le plus de place.</p>
      <p><strong>2. Supprimez les quasi-copies.</strong> Comparez chaque groupe de photos similaires, gardez la meilleure et sélectionnez les autres.</p>
      <p><strong>3. Filtrez le bruit.</strong> Masquez les lieux qui ne vous intéressent pas (domicile, travail) pour que les vrais voyages ressortent, et filtrez par taille pour trouver les fichiers lourds.</p>
      <p><strong>4. Supprimez d'un coup.</strong> Sélectionnez des centaines de photos et confirmez une seule fois.</p>

      <h2>PhotoCull fait exactement ça</h2>
      <p><a href="{pc}">PhotoCull</a> est une application de bureau gratuite pour Mac et Windows. Sa vue Voyages regroupe la photothèque par voyage et indique l'espace occupé par chacun, les photos similaires portent un badge, et vous pouvez en comparer jusqu'à six côte à côte. Elle lit un iPhone par USB ou n'importe quel dossier de votre ordinateur, fonctionne 100 % sur l'appareil et ne modifie jamais vos originaux.</p>
      <p>Les suppressions sur un iPhone passent par l'<a href="{ts}">app TripSweep</a> gratuite et « Supprimés récemment » : une erreur peut donc être annulée pendant 30 jours. Le tri d'un dossier sur votre ordinateur n'est jamais limité.</p>

      <h2>Conseils pour une longue séance</h2>
      <ul>
        <li>Travaillez voyage par voyage, plutôt qu'en faisant défiler toute la photothèque.</li>
        <li>Décidez vite : si deux photos se ressemblent, gardez-en une.</li>
        <li>Supprimez à la fin de chaque voyage, pour voir votre progression.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="Libérer de l'espace sur iPhone depuis un Mac ou un PC Windows",
     desc="Branchez votre iPhone, triez vos photos sur grand écran et supprimez ce dont vous n'avez pas besoin, sans iCloud et sans rien envoyer en ligne.",
     h1="Comment libérer de l'espace sur votre iPhone depuis un Mac ou un PC Windows",
     body="""      <p>Faire le ménage dans un iPhone plein, directement sur l'iPhone, est fastidieux. Depuis un ordinateur, vous voyez bien plus de photos à la fois et décidez plus vite. Voici toute la démarche.</p>

      <h2>Ce qu'il vous faut</h2>
      <ul>
        <li>Un Mac (Apple Silicon, macOS 11 ou ultérieur) ou un PC Windows 10/11.</li>
        <li>Un câble USB. Sous Windows, aussi l'app gratuite Apple Devices du Microsoft Store.</li>
        <li><a href="{pc}">PhotoCull</a>, gratuit sur les deux systèmes.</li>
        <li>Pour supprimer depuis l'iPhone : l'<a href="{ts}">app TripSweep</a> gratuite sur l'iPhone.</li>
      </ul>

      <h2>Pas à pas</h2>
      <p><strong>1. Branchez et faites confiance.</strong> Connectez l'iPhone, déverrouillez-le et touchez « Se fier ».</p>
      <p><strong>2. Ouvrez la vue Voyages.</strong> PhotoCull regroupe votre pellicule par voyage et indique l'espace occupé par chacun.</p>
      <p><strong>3. Triez les voyages les plus lourds.</strong> Comparez les photos similaires, gardez la meilleure et sélectionnez le reste, ainsi que les captures d'écran et les grosses vidéos dont vous n'avez pas besoin.</p>
      <p><strong>4. Confirmez la suppression.</strong> Depuis un Mac, la suppression est appliquée sur l'iPhone par TripSweep via « Supprimés récemment », et sous Windows aussi. Rien n'est effacé définitivement sur le coup.</p>
      <p><strong>5. Videz « Supprimés récemment ».</strong> L'espace de stockage revient une fois l'album vidé.</p>

      <h2>Est-ce sûr ?</h2>
      <p>Oui : vos photos restent sur vos appareils, sans compte, sans cloud et sans envoi. Les photos supprimées restent 30 jours dans « Supprimés récemment », et PhotoCull ne fait que lire vos photos tant que vous n'avez pas confirmé.</p>

      <h2>Combien de photos puis-je supprimer par jour ?</h2>
      <p>Depuis un Mac, la version gratuite permet 6 photos par jour, TripSweep Pro 15 et Pro + Desktop est illimité (voir les offres sur la page TripSweep). Ce sont tous des achats uniques, sans abonnement. Parcourir, comparer et trier est gratuit, et le tri d'un dossier sur votre ordinateur n'est jamais limité.</p>

      <h2>Sous Windows</h2>
      <p>Les étapes sont les mêmes sous Windows 10 et 11. Installez d'abord l'app gratuite Apple Devices du Microsoft Store, pour que PhotoCull puisse lire l'iPhone. L'application n'est pas encore signée numériquement, donc SmartScreen peut afficher un avertissement au premier lancement.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Comparer des photos similaires côte à côte et garder la meilleure",
     desc="Une routine simple pour choisir la meilleure prise parmi des photos quasi identiques : ce qu'il faut regarder, et comment aller vite sur grand écran.",
     h1="Comment comparer des photos similaires et garder la meilleure",
     body="""      <p>Vous avez pris six photos du même moment et elles ont toutes l'air bien. Choisir la meilleure prend quelques secondes avec la bonne méthode, et plusieurs minutes avec la mauvaise.</p>

      <h2>Ce qu'il faut vérifier, dans cet ordre</h2>
      <ol>
        <li><strong>La netteté.</strong> Zoomez sur les yeux ou sur le sujet principal. Un sujet flou est éliminatoire.</li>
        <li><strong>Les expressions.</strong> Yeux ouverts, sourires naturels, personne en plein clignement.</li>
        <li><strong>Le cadrage.</strong> Rien de coupé, un arrière-plan propre, l'horizon droit.</li>
        <li><strong>Le moment.</strong> Si deux photos se valent, gardez celle qui paraît la plus vivante.</li>
      </ol>

      <h2>Pourquoi le côte à côte compte</h2>
      <p>Passer d'une photo à l'autre rend les petites différences difficiles à voir. Les voir l'une à côté de l'autre, à la même taille, rend évidente la plus nette ou la mieux cadrée. Un écran d'ordinateur en affiche jusqu'à six à la fois, là où un téléphone en montre une.</p>

      <h2>Une routine plus rapide</h2>
      <p>Regroupez d'abord les photos similaires, pour ne jamais avoir à les chercher dans la photothèque. Pour chaque groupe, ouvrez la comparaison, choisissez-en une et sélectionnez les autres. Vous décidez en quelques secondes, pas en minutes.</p>

      <h2>Faites-le avec PhotoCull</h2>
      <p><a href="{pc}">PhotoCull</a> affiche un badge sur les photos similaires, en ouvre jusqu'à six côte à côte et vous laisse sélectionner les autres en un clic. Il fonctionne avec un iPhone connecté en USB ou avec n'importe quel dossier de votre Mac ou PC, hors ligne, et ne modifie jamais vos originaux.</p>
      <p>Sur le téléphone lui-même, l'<a href="{ts}">app TripSweep</a> suggère la meilleure prise de chaque groupe grâce à la netteté, au score esthétique d'Apple et aux visages, et son bouton « Garder 1 par groupe » traite toute une catégorie d'un coup.</p>

      <h2>Gardez, sans regret</h2>
      <p>Quand vous hésitez, gardez-en deux. Les suppressions sur un iPhone passent par « Supprimés récemment » pendant 30 jours, vous pouvez donc encore changer d'avis.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="Trouver les photos en double et similaires sur Mac",
     desc="Trouvez copies exactes, rafales et prises quasi identiques dans vos dossiers photos ou sur un disque externe, gardez la meilleure et supprimez le reste.",
     h1="Comment trouver les photos en double et similaires sur Mac",
     body="""      <p>Des années d'imports, de cartes mémoire et de sauvegardes laissent les mêmes photos éparpillées dans des dossiers sur un Mac. Certaines sont des copies exactes ; la plupart sont des prises quasi identiques du même instant. Voici comment trouver les deux, garder la meilleure et libérer de la place, sans toucher à votre photothèque Photos.</p>

      <h2>Ce que propose macOS</h2>
      <ul>
        <li><strong>Finder :</strong> trier un dossier par nom ou par taille aide à repérer les copies évidentes comme « IMG_1234 copie.jpg », mais pas deux prises différentes de la même scène.</li>
        <li><strong>Photos :</strong> son album Doublons ne couvre que les photos déjà présentes dans la photothèque Photos, pas vos autres dossiers ni vos disques.</li>
      </ul>

      <h2>Avec PhotoCull, étape par étape</h2>
      <p><strong>1. Installez PhotoCull.</strong> <a href="{mac}">Téléchargez-le gratuitement</a> : macOS 11 ou ultérieur sur Apple Silicon, signé et notarisé par Apple.</p>
      <p><strong>2. Ouvrez le dossier.</strong> Cliquez sur « Ouvrir un dossier », ou glissez un dossier sur la fenêtre. Les sous-dossiers sont inclus, les disques externes aussi.</p>
      <p><strong>3. Regardez les badges.</strong> PhotoCull compare le contenu des photos, pas leurs noms : les copies exactes, les rafales et les prises quasi identiques portent le même badge « ≈ N ».</p>
      <p><strong>4. Gardez la meilleure.</strong> Ouvrez un groupe pour comparer jusqu'à six photos côte à côte, gardez la plus nette et marquez les autres.</p>
      <p><strong>5. Supprimez sans risque.</strong> Les fichiers marqués vont dans la Corbeille du Mac, où « Remettre » les restaure si vous changez d'avis.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Les fichiers JPEG, HEIC, PNG, TIFF, WebP et RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sont pris en charge, ainsi que les vidéos MOV et MP4.</li>
        <li>Les photos sont datées d'après leurs données EXIF : des dossiers copiés restent classés selon le jour de la prise de vue.</li>
        <li>Trier un dossier est gratuit et jamais limité. Tout se passe sur votre Mac : pas de compte, aucun envoi.</li>
        <li>Les photothèques Photos et les paquets d'applications présents dans le dossier sont ignorés : PhotoCull ne fouille jamais les fichiers d'une autre application.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Trouver les photos en double et similaires sur Windows",
     desc="Trouvez copies exactes, rafales et prises quasi identiques dans vos dossiers photos ou sur un disque externe, gardez la meilleure et supprimez le reste.",
     h1="Comment trouver les photos en double et similaires sur Windows 10 ou 11",
     body="""      <p>Sauvegardes de téléphone, cartes mémoire et anciennes copies laissent les mêmes photos dans plusieurs dossiers d'un PC. Certaines sont de vrais doublons, la plupart sont des prises quasi identiques. Voici comment trouver les deux et faire le ménage sans risque.</p>

      <h2>Ce que propose Windows</h2>
      <ul>
        <li><strong>Explorateur de fichiers :</strong> trier par nom, taille ou date aide pour les copies évidentes, mais il ne sait pas que deux fichiers différents montrent la même scène.</li>
        <li><strong>L'app Photos :</strong> pratique pour afficher et importer, mais sans outil pour repérer les prises similaires et choisir la meilleure.</li>
      </ul>

      <h2>Avec PhotoCull, étape par étape</h2>
      <p><strong>1. Installez PhotoCull.</strong> Obtenez-le gratuitement <a href="{win}">pour Windows 10 ou 11</a> (64 bits), ou depuis le Microsoft Store.</p>
      <p><strong>2. Ouvrez le dossier.</strong> Cliquez sur « Ouvrir un dossier », ou glissez un dossier sur la fenêtre. Les sous-dossiers et les disques externes sont inclus.</p>
      <p><strong>3. Regardez les badges.</strong> PhotoCull compare ce que montrent les photos, pas leurs noms de fichiers : les copies exactes, les rafales et les prises quasi identiques portent le même badge « ≈ N ».</p>
      <p><strong>4. Gardez la meilleure.</strong> Comparez jusqu'à six photos côte à côte, gardez la plus nette, marquez les autres.</p>
      <p><strong>5. Supprimez sans risque.</strong> Les fichiers marqués vont dans la Corbeille de Windows : vous pouvez les restaurer.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Les fichiers JPEG, HEIC, PNG, TIFF, WebP et RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sont pris en charge, ainsi que les vidéos MOV et MP4. Les miniatures HEIC nécessitent l'extension gratuite Extensions d'image HEIF de Microsoft.</li>
        <li>Les photos sont datées d'après leurs données EXIF : des dossiers copiés restent classés selon le jour de la prise de vue.</li>
        <li>Trier un dossier est gratuit et jamais limité. Tout se passe sur votre PC : pas de compte, aucun envoi.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Trier un gros dossier de photos ou un disque dur externe",
     desc="Vieilles sauvegardes, cartes mémoire, disque externe plein de photos : une méthode simple pour trier des milliers de fichiers par voyage et garder le meilleur.",
     h1="Comment trier un gros dossier de photos, ou tout un disque dur externe",
     body="""      <p>Tout le monde en a un : un dossier « Photos à trier », une vieille sauvegarde de téléphone, un disque externe rempli en dix ans. Des milliers de fichiers, aucun ordre, beaucoup de quasi-doublons. Voici une méthode pour en venir à bout en une seule séance.</p>

      <h2>1. Ouvrez tout le dossier d'un coup</h2>
      <p>N'avancez pas dossier par dossier. Ouvrez le dossier racine dans <a href="{pc}">PhotoCull</a> (« Ouvrir un dossier », ou glissez-le sur la fenêtre) : les sous-dossiers sont inclus, et chaque photo est datée d'après ses données EXIF plutôt que d'après le jour où elle a été copiée.</p>

      <h2>2. Laissez les voyages apparaître</h2>
      <p>La vue Voyages regroupe les photos par date et par lieu et indique la place prise par chaque groupe. Dix ans de fichiers deviennent une liste de voyages et d'événements, et vous commencez par les plus lourds.</p>

      <h2>3. Réduisez les quasi-doublons</h2>
      <p>Les rafales, les prises répétées et les copies d'une même photo portent un badge « ≈ N ». Comparez-en jusqu'à six côte à côte, gardez la meilleure, marquez les autres. Cette étape seule supprime souvent une grande partie des fichiers.</p>

      <h2>4. Marquez les restes évidents</h2>
      <p>Captures d'écran, photos floues, vidéos accidentelles : marquez-les au passage. Rien n'est supprimé tant que vous n'avez pas confirmé.</p>

      <h2>5. Supprimez sans risque</h2>
      <p>Les fichiers confirmés vont dans la Corbeille sur Mac ou dans la Corbeille de Windows, une erreur peut donc être rattrapée. Videz-la quand vous êtes sûr de vous.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Les fichiers RAW d'appareils photo (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sont pris en charge, comme les JPEG, HEIC, PNG et les vidéos.</li>
        <li>Trier des dossiers est gratuit et jamais limité, sur Mac (<a href="{mac}">télécharger</a>) comme sous Windows (<a href="{win}">télécharger</a>).</li>
        <li>Vos originaux ne sont jamais modifiés : la seule modification de PhotoCull est la suppression que vous confirmez.</li>
      </ul>"""),
],
}
