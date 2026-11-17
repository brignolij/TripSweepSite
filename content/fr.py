# -*- coding: utf-8 -*-
# French version of the FAQ and blog of the TripSweep site. Tokens in answers/articles: {ts} {pc} {store} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Confidentialité", more="À lire aussi",
    cta_store="📱 Télécharger TripSweep sur l'App Store",
    cta_play="🤖 Télécharger TripSweep sur Google Play",
    cross_label={"tripsweep": "Application de bureau", "pixculler": "Application mobile"},
    twin_android="Vous avez un téléphone Android ? Lisez le guide Android :",
    twin_iphone="Vous avez un iPhone ? Lisez le guide iPhone :",
    index={
        "tripsweep": dict(
            title="Blog TripSweep : libérer de l'espace sur iPhone, photos en double",
            desc="Guides pratiques pour libérer de l'espace sur iPhone, supprimer doublons et photos similaires et trier vos anciens voyages, sans iCloud ni envoi de photos.",
            h1="Guides pour faire le ménage dans vos photos iPhone",
            intro="Des guides courts et pratiques pour libérer de l'espace sur votre iPhone, supprimer les doublons et ne garder que les meilleures photos."),
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
     "Oui. <a href=\"{pc}\">PixCuller</a> est l'application de bureau gratuite pour Mac et Windows : elle affiche la pellicule de votre iPhone regroupée par voyage, compare les photos similaires côte à côte et vous permet de sélectionner des centaines de photos en quelques clics. <a href=\"{pc}\">En savoir plus sur PixCuller</a>."),
    ("Puis-je supprimer des photos en masse depuis mon ordinateur plutôt qu'en tapotant sur le téléphone ?",
     "Oui, avec <a href=\"{pc}\">PixCuller</a> sur un Mac ou un PC Windows. Vous sélectionnez les photos sur le grand écran et PixCuller les supprime directement par le câble USB, sans limite quotidienne et sans rien à acheter. Avec un iPhone, cela demande que Photos iCloud soit désactivé sur l'iPhone, et macOS 27 ou ultérieur sur un Mac (tout Windows 10 ou 11 convient). La suppression est définitive sur l'iPhone, les photos ne passent pas par « Supprimés récemment », mais PixCuller garde par défaut une copie sur votre ordinateur pendant 30 jours. Un téléphone Android se branche aussi par câble USB, en mode « Transfert de fichiers », sans rien à installer sur le téléphone (Windows 10 ou 11, ou un Mac avec macOS 27 ou ultérieur)."),
    ("Quels iPhone et quelles versions d'iOS TripSweep prend-il en charge ?",
     "TripSweep nécessite iOS 18 ou une version ultérieure. L'analyse des photos similaires utilise le framework Vision d'Apple et va plus vite sur les iPhone récents, mais fonctionne sur tous les modèles pris en charge. Sur Android, elle nécessite Android 11 ou une version ultérieure et se télécharge sur <a href=\"{play}\">Google Play</a>."),
]

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
      <p>Si vous préférez un grand écran, <a href="{pc}">PixCuller</a> fait le même tri sur un Mac ou un PC Windows.</p>

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
      <p>Avec <a href="{pc}">PixCuller</a> sur un Mac ou un PC Windows, vous pouvez comparer jusqu'à six photos similaires côte à côte et en sélectionner des centaines en quelques clics.</p>"""),
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
      <p>Pour faire de même sur grand écran, <a href="{pc}">PixCuller</a> affiche les voyages de votre iPhone sur un Mac ou un PC Windows.</p>"""),
dict(slug="free-up-android-storage",
     title="Libérer de l'espace sur Android sans payer Google One",
     desc="Où part vraiment le stockage de votre Android et les moyens les plus rapides de libérer des gigaoctets de photos et de vidéos sans payer plus de cloud.",
     h1="Comment libérer de l'espace sur Android sans payer pour Google One",
     body="""      <p>« Stockage saturé » sur un téléphone Android signifie presque toujours : photos et vidéos. Réglages → Stockage le montre clairement, et la plus grande partie de cet espace, ce sont des photos que vous ne regarderez plus jamais. Voici comment le récupérer sans acheter de stockage cloud supplémentaire.</p>

      <h2>1. Commencez par ce qui pèse le plus</h2>
      <p>Les grosses vidéos sont le gain le plus rapide : quelques minutes de vidéo 4K occupent autant de place que des centaines de photos. Triez vos vidéos par taille, regardez les premières secondes et supprimez celles que vous n'ouvrirez plus jamais.</p>

      <h2>2. Supprimez les photos similaires, pas seulement les doublons</h2>
      <p>Les applis de nettoyage trouvent les copies exactes, mais le vrai gaspillage vient des prises quasi identiques : les rafales, cinq essais de la même photo de groupe, trois selfies à la suite. Gardez la meilleure de chaque groupe et supprimez le reste.</p>

      <h2>3. Faites le ménage dans les captures d'écran et les photos floues</h2>
      <p>Les captures d'écran de billets, de plans et de conversations s'accumulent sans qu'on s'en aperçoive, tout comme les clichés accidentels ou flous. Elles se passent vite en revue d'un seul bloc.</p>

      <h2>4. Videz la corbeille</h2>
      <p>Les photos supprimées attendent généralement 30 jours dans la corbeille et continuent d'occuper de la place. Une fois satisfait de vos choix, videz-la pour récupérer vraiment l'espace.</p>

      <h2>5. Triez vos anciens voyages, un par un</h2>
      <p>Les anciennes vacances forment le plus gros bloc de photos que vous ne regardez jamais. Avancer voyage par voyage est plus facile que de faire défiler des milliers de photos : choisissez le voyage le plus lourd, gardez les meilleurs moments, supprimez le reste.</p>

      <h2>Comment TripSweep accélère tout ça</h2>
      <p><a href="{ts}">TripSweep</a> fait ces étapes à votre place sur le téléphone. Son onglet Nettoyage liste les copies identiques, les photos similaires, les photos floues, les captures d'écran et les vidéos volumineuses, chacune avec l'espace qu'elle occupe, et vos voyages sont regroupés automatiquement. Il est gratuit sur <a href="{play}">Google Play</a> (Android 11 ou ultérieur) et fonctionne 100 % sur le téléphone.</p>
      <p>Si vous préférez un grand écran, <a href="{pc}">PixCuller</a> fait le même tri sur un Mac ou un PC Windows, avec le téléphone branché par câble USB.</p>

      <h2>Ai-je besoin de Google One ?</h2>
      <p>Le stockage cloud est une bonne sauvegarde, mais ce n'est pas un outil de nettoyage : il stocke tout, doublons compris. Faire le ménage d'abord, c'est avoir besoin de moins de stockage, où qu'il soit.</p>"""),
dict(slug="delete-duplicate-photos-android",
     title="Supprimer les photos en double et similaires sur Android",
     desc="Repérez les doublons exacts, les rafales et les photos quasi identiques sur votre téléphone Android, gardez la meilleure et supprimez le reste en sécurité.",
     h1="Comment supprimer les photos en double et similaires sur votre téléphone Android",
     body="""      <p>Les doublons grignotent discrètement le stockage d'un téléphone Android. Certains sont des copies exactes, mais la plupart sont des prises quasi identiques d'un même moment. Voici comment trouver les uns et les autres et les supprimer en toute sécurité.</p>

      <h2>Doublons et photos similaires, ce n'est pas la même chose</h2>
      <p>Un doublon exact est le même fichier enregistré deux fois, par exemple après un téléchargement, une messagerie ou une restauration. Une photo similaire est une prise de vue différente de la même scène : une rafale, plusieurs essais d'une photo de groupe, un selfie refait jusqu'à ce que vous soyez content. Les outils de nettoyage de fichiers repèrent les premiers ; les secondes prennent bien plus de place.</p>

      <h2>Ce qu'offre Android</h2>
      <p>Les gestionnaires de fichiers peuvent lister les fichiers en double exacts, et votre galerie affiche les rafales. Ni l'un ni l'autre ne compare les prises quasi identiques ni ne vous aide à choisir la meilleure : vous finissez par passer d'une photo à l'autre une par une.</p>

      <h2>Une méthode plus rapide</h2>
      <p><strong>1. Regroupez par scène.</strong> <a href="{ts}">TripSweep</a> compare le contenu de vos photos, pas leurs noms, et regroupe les prises d'une même scène : une rafale de dix devient une seule décision.</p>
      <p><strong>2. Gardez la meilleure.</strong> Il suggère une prise par groupe ; vous pouvez en garder une autre, en garder plusieurs ou passer le groupe.</p>
      <p><strong>3. Supprimez sans risque.</strong> Les photos supprimées vont dans la corbeille du téléphone pendant 30 jours, une erreur est donc réversible.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Tout s'exécute sur le téléphone : pas de compte, aucun envoi. TripSweep est gratuit sur <a href="{play}">Google Play</a> (Android 11 ou ultérieur).</li>
        <li>Pour toute une pellicule, comparer sur grand écran avec <a href="{pc}">PixCuller</a> sur un Mac ou un PC est encore plus rapide.</li>
      </ul>"""),
],
}
