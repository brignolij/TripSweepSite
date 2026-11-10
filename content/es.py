# -*- coding: utf-8 -*-
# Spanish translation of the FAQ and blog of both sites. Tokens in answers/articles: {ts} {pc} {store} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacidad", more="Sigue leyendo",
    cta_store="📱 Descarga TripSweep en la App Store",
    cta_play="🤖 Descarga TripSweep en Google Play",
    cta_mac="💻 Descarga PhotoCull para Mac", cta_win="🪟 Descarga PhotoCull para Windows",
    cross_label={"tripsweep": "App de escritorio", "photocull": "App móvil"},
    twin_android="¿Usas un móvil Android? Lee la guía para Android:",
    twin_iphone="¿Usas un iPhone? Lee la guía para iPhone:",
    index={
        "tripsweep": dict(
            title="Blog de TripSweep: espacio en el iPhone y fotos duplicadas",
            desc="Guías prácticas para liberar espacio en el iPhone, eliminar fotos duplicadas y parecidas y limpiar viajes antiguos, sin iCloud y sin enviar tus fotos.",
            h1="Guías para limpiar las fotos de tu iPhone",
            intro="Guías breves y prácticas para liberar espacio en tu iPhone, borrar duplicados y quedarte solo con las mejores fotos."),
        "photocull": dict(
            title="Blog de PhotoCull: ordena fotos en Mac o PC y libera tu iPhone",
            desc="Guías para ordenar miles de fotos más rápido en una pantalla grande, comparar fotos parecidas y liberar un iPhone o un móvil Android desde un Mac o un PC.",
            h1="Guías para ordenar tus fotos en el ordenador",
            intro="Por qué una pantalla grande cambia la rapidez con la que ordenas fotos, y cómo aprovecharla para liberar espacio en tu iPhone o móvil Android."),
    },
)

FAQ_TRIPSWEEP_EXTRA = [
    ("¿Cuál es la diferencia entre fotos duplicadas y fotos parecidas?",
     "Las duplicadas son copias idénticas del mismo archivo. Las parecidas son tomas distintas de la misma escena: una ráfaga, cinco intentos del mismo atardecer, dos selfis casi iguales. Las duplicadas son fáciles de detectar; las fotos parecidas son donde se esconde la mayor parte del espacio desperdiciado, y TripSweep agrupa ambas para que conserves una y borres el resto."),
    ("¿Cómo elige TripSweep la mejor foto de un grupo?",
     "Analiza la nitidez, la puntuación estética de Apple y los rostros, y propone una toma por grupo. La sugerencia es solo un punto de partida: puedes conservar otra foto, conservar varias u omitir el grupo. El análisis se hace en tu iPhone con el framework Vision de Apple."),
    ("¿Qué encuentra la pestaña Limpieza?",
     "Copias idénticas, fotos parecidas, fotos borrosas, capturas de pantalla y vídeos grandes, cada uno en su propia categoría con el espacio que ocupa. Empiezas por la categoría que más espacio libera y la ordenas en unos pocos toques."),
    ("¿TripSweep me sugerirá borrar mis fotos favoritas?",
     "No. Las fotos que marcaste como favoritas nunca se sugieren para borrar, y no se elimina nada hasta que lo confirmes."),
    ("¿Funciona TripSweep con fotos que no tienen ubicación GPS?",
     "Sí. Las fotos sin ubicación se agrupan por evento y mes en lugar de por viaje, así que también se ordenan las capturas de pantalla, las imágenes guardadas y las fotos hechas con la localización desactivada."),
    ("¿Puedo ocultar mi casa y mi lugar de trabajo de mis viajes?",
     "Sí. Añade tu casa, tu trabajo o cualquier lugar por el que pases a diario como lugar excluido, para que el día a día no aparezca como un viaje y tus viajes de verdad destaquen. Pro permite lugares personalizados ilimitados."),
    ("¿Puedo hacer una copia de seguridad de un viaje o compartirlo antes de borrarlo?",
     "Sí. Puedes exportar un viaje completo a tu Mac o a la app Archivos, o compartirlo con las personas que estuvieron allí, y después borrarlo de tu iPhone cuando esté a salvo en otro sitio."),
    ("¿Necesito conexión a internet o una cuenta?",
     "No. TripSweep no necesita cuenta y funciona sin conexión. Los nombres de los lugares se reconocen en tu iPhone, y ninguna foto, vídeo ni ubicación se envía jamás a un servidor. Solo se pueden enviar estadísticas de uso anónimas y desactivables. Puedes desactivarlas en la pestaña Acerca de."),
    ("¿Borrar en TripSweep también borra mis fotos de iCloud?",
     "Si Fotos de iCloud está activado, borrar una foto en el iPhone la elimina de todos tus dispositivos, porque así funciona Fotos de iCloud. TripSweep borra a través de « Eliminados recientemente », así que tienes 30 días para arrepentirte, y el espacio de iCloud se libera cuando vacías ese álbum."),
    ("¿Puedo revisar las fotos de mi iPhone en una pantalla grande en lugar del móvil?",
     "Sí. <a href=\"{pc}\">PhotoCull</a> es la app de escritorio gratuita que acompaña a TripSweep, para Mac y Windows: muestra el carrete de tu iPhone agrupado por viaje, compara fotos parecidas lado a lado y te permite marcar cientos de fotos con unos pocos clics. <a href=\"{pc}\">Más información sobre PhotoCull</a>."),
    ("¿Puedo borrar fotos en bloque desde el ordenador en vez de tocar la pantalla del móvil?",
     "Sí, con <a href=\"{pc}\">PhotoCull</a> en un Mac o un PC con Windows. Marcas las fotos en la pantalla grande y TripSweep aplica el borrado en tu iPhone a través de « Eliminados recientemente ». La versión gratuita permite 6 fotos al día desde el Mac (consulta los planes en la página de TripSweep), Pro 15, y Pro + Desktop elimina el límite."),
    ("¿Qué iPhone y qué versiones de iOS admite TripSweep?",
     "TripSweep requiere iOS 18 o posterior. El análisis de fotos parecidas usa el framework Vision de Apple y es más rápido en los iPhone recientes, pero funciona en todos los modelos compatibles. En Android requiere Android 11 o posterior y está disponible en <a href=\"{play}\">Google Play</a>."),
]

FAQ_PHOTOCULL = dict(
    title="FAQ de PhotoCull: ordena y borra fotos desde un Mac o un PC",
    desc="Cómo ordenar miles de fotos en el ordenador, comparar fotos parecidas, liberar un iPhone o un móvil Android desde un Mac o PC: respuestas sobre PhotoCull.",
    nav_home="PhotoCull", nav_desktop="App móvil",
    h1="Preguntas y respuestas",
    intro="Cómo ordenar tus fotos más rápido desde un ordenador, liberar espacio en tu iPhone o móvil Android desde un Mac o PC, y qué hace (y qué nunca hace) PhotoCull con tus fotos.",
    qa=[
        ('¿Cómo ordeno las fotos del iPhone en el ordenador, Mac o PC?',
         "Conecta el iPhone al ordenador con un cable USB, desbloquéalo y toca Confiar, y abre <a href=\"{pc}\">PhotoCull</a>: agrupa el carrete por viaje, compara las fotos parecidas lado a lado y marca cientos de fotos en pocos clics. Guías paso a paso: <a href=\"{post:sort-iphone-photos-on-mac}\">en el Mac</a> y <a href=\"{post:sort-iphone-photos-on-pc}\">en un PC con Windows</a>."),
        ("¿Por qué ordenar las fotos en el ordenador en lugar de en el iPhone?",
         "Una pantalla grande muestra más fotos a la vez, un ratón y un teclado seleccionan cientos en segundos, y comparar tomas lado a lado es más fácil que ir pasando de una a otra. Ordenar un carrete de miles de fotos son varias sesiones en el móvil y una sesión mucho más corta en un Mac o un PC."),
        ("¿Qué es PhotoCull?",
         "PhotoCull es una app de escritorio gratuita para Mac y Windows que agrupa tus fotos por viaje, compara tomas parecidas lado a lado y borra en bloque lo que no merece la pena conservar. Lee el carrete de tu iPhone por USB, o cualquier carpeta de fotos de tu ordenador, y funciona 100 % en el dispositivo."),
        ("¿Cómo ordeno miles de fotos rápidamente?",
         "Abre la vista Viajes: tu biblioteca aparece agrupada por viaje con el espacio que ocupa cada uno, así que empiezas por el más pesado. Dentro de un viaje, marca fotos en bloque, compara las parecidas lado a lado y conserva la mejor toma de cada grupo. Los mismos filtros que en la app para iOS (viajes de un solo día, lugares excluidos como casa o trabajo, tamaño) te ayudan a acotar."),
        ("¿Cómo libero espacio en el iPhone desde un Mac o un PC?",
         "Conecta tu iPhone por USB, abre PhotoCull, marca los viajes y las fotos que ya no necesitas y confirma. El borrado se aplica en el iPhone mediante la <a href=\"{ts}\">app TripSweep</a>, gratuita, a través de « Eliminados recientemente », así que el espacio se libera en cuanto vacías ese álbum."),
        ("¿Puedo borrar fotos del iPhone directamente desde el ordenador?",
         "Sí, desde un Mac o un PC con Windows, con la <a href=\"{ts}\">app TripSweep</a> instalada en el iPhone. Desde un Mac, la versión gratuita permite 6 fotos al día, Pro 15 y Pro + Desktop elimina el límite."),
        ("¿Borrar desde PhotoCull es permanente?",
         "No. Los borrados en el iPhone pasan siempre por el álbum « Eliminados recientemente » de la app Fotos, donde las fotos permanecen 30 días y se pueden recuperar. PhotoCull nunca hace un borrado permanente inmediato."),
        ("¿Cómo conecto mi iPhone a PhotoCull?",
         "Usa un cable USB, desbloquea el iPhone y toca « Confiar » cuando te lo pida. En un Mac no hace falta nada más. En Windows, instala la app gratuita Apple Devices desde Microsoft Store, que incluye el controlador que permite a PhotoCull leer el iPhone."),
        ("¿Puedo ordenar las fotos de un móvil Android en mi Mac o PC?",
         "Sí. PhotoCull se conecta a un móvil Android por wifi en un Mac o en un PC con Windows, o por USB en Windows. Tienes la misma vista Viajes, la misma comparación lado a lado y el mismo borrado en bloque que con un iPhone. El móvil necesita la <a href=\"{play}\">app TripSweep</a> gratuita (Android 11 o posterior), abierta en su pestaña Eliminación."),
        ("¿Cómo conecto mi móvil Android por wifi?",
         "Pon el móvil y el ordenador en la misma red wifi y abre la pestaña Eliminación de TripSweep en el móvil. En PhotoCull, haz clic en « Teléfono Android » y elige tu móvil; después autoriza el ordenador en el móvil: el mismo código de 4 dígitos aparece en las dos pantallas. Esto se hace una sola vez; la próxima vez se reconecta solo. <a href=\"{post:sort-android-photos-on-mac}\">Guía paso a paso para Mac</a>."),
        ("¿Por qué mi Mac no ve mi móvil Android por USB?",
         "macOS no admite de serie la forma en que los móviles Android comparten archivos por USB (MTP), así que normalmente el Mac no los ve. Usa la conexión por wifi: funciona en todos los Mac, sin instalar ningún controlador. En Windows funcionan tanto el USB como el wifi."),
        ("¿Es segura la conexión wifi con mi móvil?",
         "Sí. El móvil y el ordenador se comunican solo dentro de tu red local, con una conexión cifrada, y únicamente después de que hayas autorizado ese ordenador en el móvil con un código que coincide en ambos. Nada pasa por internet, y puedes revocar un ordenador desde TripSweep cuando quieras."),
        ("¿Qué pasa con las fotos que borro en un móvil Android?",
         "Confirmas el borrado en el móvil, en TripSweep, y las fotos van a la papelera del móvil, donde permanecen 30 días y se pueden recuperar. PhotoCull nunca borra nada de forma permanente por su cuenta."),
        ("¿Necesito la app TripSweep para iOS?",
         "No para explorar, comparar y ordenar un iPhone. Solo la necesitas para borrar fotos del iPhone, porque el borrado se aplica en el móvil. Un móvil Android necesita la app TripSweep para Android para poder conectarse. Las carpetas de tu ordenador se pueden ordenar sin ninguna de las dos."),
        ("¿Cómo busco fotos duplicadas en una carpeta de mi Mac o PC?",
         "Abre la carpeta en PhotoCull (« Abrir carpeta », o arrástrala a la ventana). Recorre las subcarpetas, compara lo que muestran las fotos y pone la misma insignia «≈ N» a las copias exactas, las ráfagas y las tomas casi idénticas. Conserva la mejor de cada grupo y manda el resto a la Papelera (Mac) o a la Papelera de reciclaje (Windows). Guías: <a href=\"{post:find-duplicate-photos-on-mac}\">en el Mac</a> y <a href=\"{post:find-duplicate-photos-on-windows}\">en Windows</a>."),
        ("¿Puedo usar PhotoCull con fotos guardadas en mi ordenador, no en un iPhone?",
         "Sí. Abre cualquier carpeta: PhotoCull encuentra las fotos parecidas, muestra las insignias en ellas y te permite comparar y borrar sin límite diario."),
        ("¿Cómo encuentra PhotoCull las fotos parecidas?",
         "Compara el contenido de tus fotos, no el nombre de los archivos, así que las ráfagas, las tomas casi idénticas y la misma escena fotografiada varias veces acaban en el mismo grupo. Puedes comparar hasta 6 fotos lado a lado y quedarte con la más nítida y mejor encuadrada."),
        ("¿Cómo comparo fotos parecidas lado a lado?",
         "Selecciona un grupo de fotos parecidas y abre la comparación: se muestran hasta 6 fotos del mismo tamaño para que puedas juzgar el enfoque, las expresiones y el encuadre. Conserva la mejor y marca el resto."),
        ("¿Funciona PhotoCull en Windows?",
         "Sí: Windows 10 y 11 (64 bits). Para leer un iPhone hace falta la app gratuita Apple Devices de Microsoft Store. La app todavía no está firmada digitalmente, así que Windows SmartScreen puede mostrar una advertencia la primera vez que la abras: elige « Más información » y luego « Ejecutar de todas formas »."),
        ("¿Qué Mac admite PhotoCull?",
         "Mac con Apple Silicon y macOS 11 o posterior. La app está firmada y notarizada por Apple, así que se abre sin ninguna advertencia de seguridad."),
        ("¿PhotoCull es gratis? ¿Hay suscripción?",
         "PhotoCull se descarga gratis y no hay suscripción. Explorar, comparar y ordenar es gratis, y ordenar una carpeta de tu ordenador nunca tiene límite. Borrar fotos de un iPhone desde un Mac está limitado a 6 al día en la versión gratuita, 15 con TripSweep Pro e ilimitado con Pro + Desktop (compras únicas que se hacen en la app TripSweep para iOS)."),
        ("¿PhotoCull envía mis fotos a un servidor o a la nube?",
         "No. PhotoCull funciona 100 % en el dispositivo: sin cuenta, sin nube, y ninguna foto, vídeo ni ubicación se envía a ningún sitio. El reconocimiento de lugares y la detección de fotos parecidas se ejecutan en tu ordenador. Solo se pueden enviar estadísticas de uso anónimas y desactivables."),
        ("¿PhotoCull cambiará o modificará mis fotos originales?",
         "No. PhotoCull solo lee tus fotos para mostrarlas y compararlas. El único cambio que hace es el borrado que tú confirmas."),
        ("¿Cómo oculto mi casa y mi lugar de trabajo de la vista de viajes?",
         "Añádelos como lugares excluidos: así el día a día deja de aparecer como un viaje y tus viajes de verdad destacan. El ajuste es el mismo que en la app para iOS."),
        ("¿Puedo hacer limpieza tras las vacaciones desde el ordenador?",
         "Sí, es el uso más habitual. Después de un viaje, conecta el iPhone, abre ese viaje en PhotoCull, compara las tomas parecidas, conserva la mejor de cada una y borra el resto. La <a href=\"{ts}\">app TripSweep</a> también puede exportar el viaje completo antes de que borres nada."),
        ("¿Puedo usar PhotoCull para preparar un álbum de fotos o una copia de seguridad?",
         "PhotoCull te ayuda a decidir qué merece la pena conservar: ordena el viaje, elimina los duplicados y las tomas casi idénticas, y después haz una copia de seguridad o comparte lo que quede. La <a href=\"{ts}\">app TripSweep</a> puede exportar o compartir un viaje completo."),
    ],
    footer_copy="© 2026 PhotoCull. Desarrollado por Jeffrey Brignoli.",
    footer_privacy="Privacidad", footer_kofi="Ko-fi",
)

BLOG = {
"tripsweep": [
dict(slug="free-up-iphone-storage",
     title="Cómo liberar espacio en el iPhone sin iCloud: guía práctica",
     desc="Dónde se va realmente el almacenamiento de tu iPhone y las formas más rápidas de liberar gigas de fotos y vídeos sin pagar más por iCloud.",
     h1="Cómo liberar espacio en el iPhone sin pagar por iCloud",
     body="""      <p>« Almacenamiento del iPhone lleno » casi siempre significa una sola cosa: la app Fotos. Las fotos y los vídeos suelen ser lo que más ocupa en Ajustes → General → Almacenamiento del iPhone, y la mayor parte de ese espacio es basura que puedes eliminar sin perder ni un solo recuerdo.</p>

      <h2>1. Empieza por lo que más pesa</h2>
      <p>Los vídeos grandes son la victoria más rápida: unos minutos de vídeo en 4K ocupan tanto como cientos de fotos. Ordena tus vídeos por tamaño, mira los primeros segundos y borra los que no vas a volver a abrir. Las grabaciones de pantalla y los vídeos que te llegan por aplicaciones de mensajería suelen ser los principales culpables.</p>

      <h2>2. Borra las fotos parecidas, no solo las duplicadas</h2>
      <p>La app Fotos puede encontrar duplicados exactos, pero el verdadero desperdicio está en las tomas casi idénticas: la ráfaga de diez fotogramas, cinco intentos de la misma foto de grupo, tres selfis seguidos. Conserva la mejor de cada grupo y borra el resto. Aquí es donde la mayoría de la gente recupera más espacio, y es lo más difícil de hacer a mano.</p>

      <h2>3. Elimina capturas de pantalla y fotos borrosas</h2>
      <p>Las capturas de pantalla se acumulan sin que te des cuenta: entradas, mapas, conversaciones que ya no necesitas. Con las fotos borrosas y las tomas accidentales pasa lo mismo. Rara vez merecen quedarse y se revisan rápido todas juntas.</p>

      <h2>4. Vacía « Eliminados recientemente »</h2>
      <p>Las fotos borradas permanecen 30 días en el álbum Eliminados recientemente y siguen ocupando espacio. Cuando estés conforme con tus decisiones, vacíalo para recuperar de verdad el almacenamiento.</p>

      <h2>5. Limpia los viajes antiguos, uno por uno</h2>
      <p>Las vacaciones antiguas son el mayor bloque de fotos que nunca miras. Ir viaje por viaje es más fácil que desplazarse por una biblioteca de miles de fotos: elige el viaje más pesado, conserva lo mejor y borra lo que sobra.</p>

      <h2>Cómo te lo hace más rápido TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> hace estos pasos por ti en el iPhone. Su pestaña Limpieza enumera las copias idénticas, las fotos parecidas, las fotos borrosas, las capturas de pantalla y los vídeos grandes, cada uno con el espacio que ocupa. Tus viajes se agrupan por lugar y fecha y se ordenan por tamaño, y un botón « Conservar 1 por grupo » resuelve una categoría entera con un solo toque. Los favoritos nunca se sugieren para borrar, los borrados pasan por « Eliminados recientemente » y nada sale jamás de tu móvil: sin cuenta, sin nube. Solo se pueden enviar estadísticas de uso anónimas y desactivables.</p>
      <p>Si prefieres una pantalla grande, <a href="{pc}">PhotoCull</a> hace el mismo trabajo de ordenación en un Mac o un PC con Windows.</p>

      <h2>¿Necesito iCloud?</h2>
      <p>iCloud es una buena copia de seguridad, pero no es una herramienta de limpieza: guarda todo, duplicados incluidos. Limpiar primero significa que necesitas menos almacenamiento, esté donde esté.</p>"""),
dict(slug="delete-duplicate-photos-iphone",
     title="Cómo borrar fotos duplicadas y parecidas en el iPhone",
     desc="Encuentra duplicados exactos, ráfagas y tomas casi idénticas en tu iPhone, conserva la mejor y borra el resto con seguridad.",
     h1="Cómo borrar fotos duplicadas y parecidas en tu iPhone",
     body="""      <p>Los duplicados consumen almacenamiento del iPhone en silencio. Algunos son copias exactas, pero la mayoría son tomas casi idénticas del mismo momento. Así puedes encontrar ambos y limpiarlos con seguridad.</p>

      <h2>Duplicadas y parecidas no son lo mismo</h2>
      <p>Un duplicado exacto es el mismo archivo guardado dos veces, por ejemplo tras una importación o una descarga. Una foto parecida es una toma distinta de la misma escena: una ráfaga, varias tomas de una foto de grupo, un selfi repetido hasta que quedaste contento. Los duplicados exactos son fáciles de detectar; las fotos parecidas son más comunes y ocupan mucho más espacio.</p>

      <h2>La forma integrada en iOS</h2>
      <p>Las versiones recientes de iOS incluyen un álbum Duplicados en la app Fotos (en Utilidades). Fusiona las copias exactas y es un buen primer paso. No agrupa las fotos parecidas, así que las ráfagas y las tomas casi idénticas siguen en tu biblioteca.</p>

      <h2>Cómo eliminar fotos parecidas</h2>
      <p>Con las tomas parecidas hay que comparar y elegir. Abre el grupo, fíjate en la nitidez, las expresiones y el encuadre, conserva la mejor foto y borra las demás. Hacerlo a mano con miles de fotos es lento, y por eso la mayoría de la gente nunca lo termina.</p>

      <h2>Hazlo más rápido con TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> encuentra copias idénticas y fotos parecidas en cualquier parte de tu biblioteca y muestra cada grupo lado a lado sin recortar. Sugiere la mejor toma según la nitidez, la puntuación estética de Apple y los rostros, y el botón « Conservar 1 por grupo » de la pestaña Limpieza ordena una categoría entera con un solo toque. Tus favoritos nunca se sugieren para borrar.</p>

      <h2>Borra con seguridad</h2>
      <ul>
        <li>Borra a través de la app Fotos: las fotos borradas van a « Eliminados recientemente » durante 30 días, así que un error tiene arreglo.</li>
        <li>Conserva los favoritos: marca las fotos que quieres antes de limpiar.</li>
        <li>Revisa Fotos de iCloud: si está activado, borrar en el iPhone borra en todas partes.</li>
        <li>Vacía « Eliminados recientemente » al final para recuperar el espacio.</li>
      </ul>

      <h2>¿Prefieres una pantalla grande?</h2>
      <p>Con <a href="{pc}">PhotoCull</a> en un Mac o un PC con Windows puedes comparar hasta seis fotos parecidas lado a lado y marcar cientos con unos pocos clics.</p>"""),
dict(slug="clean-up-vacation-photos",
     title="Cómo limpiar fotos de vacaciones y quedarte con las mejores",
     desc="Convierte mil fotos de vacaciones en un álbum para guardar: agrupa por viaje, elimina las tomas casi idénticas y conserva lo mejor.",
     h1="Cómo limpiar fotos de vacaciones antiguas y quedarte con las mejores",
     body="""      <p>Un viaje de una semana produce fácilmente mil fotos y vídeos, y la mayoría son casi copias de unas pocas buenas tomas. Ordenarlas con el viaje reciente es fácil; ordenarlas un año después es un rollo. Este método sirve para ambos casos.</p>

      <h2>1. Trabaja viaje por viaje</h2>
      <p>Una biblioteca de 20 000 fotos abruma; un viaje de 800 fotos, no. Agrupa tus fotos por viaje según su fecha y ubicación, y ocúpate de un viaje cada vez, empezando por el más pesado.</p>

      <h2>2. Elimina primero las tomas casi idénticas</h2>
      <p>Buena parte de un viaje son variaciones de la misma escena. En cada grupo, conserva la más nítida y con mejores expresiones, y borra las demás. Solo con esto, el tamaño de un viaje suele reducirse a la mitad.</p>

      <h2>3. Revisa lo que queda: capturas de pantalla, fotos borrosas, vídeos grandes</h2>
      <p>Entradas, mapas, fotos accidentales y vídeos largos que nunca vuelves a ver son fáciles de eliminar cuando aparecen todos juntos.</p>

      <h2>4. Haz una copia o comparte antes de borrar</h2>
      <p>Exporta las fotos que te quedas a tu ordenador o compártelas con los amigos que estuvieron allí. Solo entonces borra el viaje de tu móvil. Los borrados van a « Eliminados recientemente », que te da 30 días para arrepentirte.</p>

      <h2>5. Fotos sin GPS</h2>
      <p>Las fotos hechas con la localización desactivada o guardadas desde mensajes no tienen lugar. Agrúpalas por evento y mes, para que también se ordenen.</p>

      <h2>Cómo ayuda TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> agrupa tus fotos y vídeos por viaje (o por evento y mes cuando no hay GPS), muestra cuántos gigas de fotos parecidas contiene cada viaje, sugiere la mejor toma de cada grupo y exporta o comparte un viaje completo. Puedes excluir tu casa y tu trabajo para que el día a día no parezca un viaje. Todo se ejecuta en tu iPhone, sin conexión.</p>
      <p>Para hacer lo mismo en una pantalla grande, <a href="{pc}">PhotoCull</a> muestra los viajes de tu iPhone en un Mac o un PC con Windows.</p>"""),
dict(slug="free-up-android-storage",
     title="Cómo liberar espacio en Android sin Google One",
     desc="Dónde se va realmente el almacenamiento de tu Android y las formas más rápidas de liberar gigas de fotos y vídeos sin pagar más por la nube.",
     h1="Cómo liberar espacio en Android sin pagar por Google One",
     body="""      <p>« Almacenamiento lleno » en un móvil Android casi siempre significa fotos y vídeos. Ajustes → Almacenamiento lo muestra con claridad, y la mayor parte de ese espacio son fotos que no vas a volver a mirar. Así se recupera sin comprar más almacenamiento en la nube.</p>

      <h2>1. Empieza por lo que más pesa</h2>
      <p>Los vídeos largos son la victoria más rápida: unos minutos de vídeo en 4K ocupan tanto como cientos de fotos. Ordénalos por tamaño, mira los primeros segundos y borra los que no vas a volver a abrir.</p>

      <h2>2. Borra las fotos parecidas, no solo las duplicadas</h2>
      <p>Las apps de limpieza encuentran copias exactas, pero el verdadero desperdicio está en las tomas casi idénticas: ráfagas, cinco intentos de la misma foto de grupo, tres selfis seguidos. Conserva la mejor de cada grupo y borra el resto.</p>

      <h2>3. Elimina capturas de pantalla y fotos borrosas</h2>
      <p>Las capturas de pantalla de entradas, mapas y conversaciones se acumulan sin que te des cuenta, igual que las fotos accidentales o borrosas. Se revisan rápido todas juntas.</p>

      <h2>4. Vacía la papelera</h2>
      <p>Las fotos borradas suelen esperar 30 días en la papelera y siguen ocupando espacio. Cuando estés conforme con tus decisiones, vacíala para recuperar de verdad el almacenamiento.</p>

      <h2>5. Limpia los viajes antiguos, uno por uno</h2>
      <p>Las vacaciones antiguas son el mayor bloque de fotos que nunca miras. Ir viaje por viaje es más fácil que desplazarse por miles de fotos: elige el viaje más pesado, conserva lo mejor y borra lo que sobra.</p>

      <h2>Cómo te lo facilita TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> hace estos pasos por ti en el móvil. Su pestaña Limpieza lista las copias idénticas, las fotos parecidas, las fotos borrosas, las capturas de pantalla y los vídeos grandes, cada uno con el espacio que ocupa, y tus viajes se agrupan automáticamente. Es gratuita en <a href="{play}">Google Play</a> (Android 11 o posterior) y funciona 100 % en el móvil.</p>
      <p>Si prefieres una pantalla grande, <a href="{pc}">PhotoCull</a> hace la misma clasificación en un Mac o un PC con Windows, conectado por wifi.</p>

      <h2>¿Necesito Google One?</h2>
      <p>El almacenamiento en la nube es una buena copia de seguridad, pero no es una herramienta de limpieza: guarda todo, duplicados incluidos. Limpiar primero significa que necesitas menos espacio, estés donde estés.</p>"""),
dict(slug="delete-duplicate-photos-android",
     title="Cómo borrar fotos duplicadas y parecidas en Android",
     desc="Encuentra duplicados exactos, ráfagas y tomas casi idénticas en tu móvil Android, conserva la mejor y borra el resto con seguridad.",
     h1="Cómo borrar fotos duplicadas y parecidas en tu móvil Android",
     body="""      <p>Los duplicados se comen en silencio el almacenamiento de un móvil Android. Algunos son copias exactas, pero la mayoría son tomas casi idénticas del mismo momento. Así se encuentran ambos tipos y se limpian con seguridad.</p>

      <h2>Duplicadas y parecidas no son lo mismo</h2>
      <p>Una foto duplicada es el mismo archivo guardado dos veces, por ejemplo tras una descarga, una app de mensajería o una restauración. Una foto parecida es otra toma de la misma escena: una ráfaga, varios intentos de una foto de grupo, un selfi repetido hasta que salió bien. Los limpiadores de archivos detectan el primer tipo; el segundo ocupa mucho más espacio.</p>

      <h2>Qué ofrece Android</h2>
      <p>Las apps de gestión de archivos pueden listar archivos duplicados exactos, y tu galería muestra las ráfagas. Ninguna compara por ti las tomas casi idénticas ni te ayuda a elegir la mejor, así que acabas pasando de una foto a otra una por una.</p>

      <h2>Una forma más rápida</h2>
      <p><strong>1. Agrupa por escena.</strong> <a href="{ts}">TripSweep</a> compara el contenido de tus fotos, no sus nombres, y agrupa las tomas de la misma escena: una ráfaga de diez pasa a ser una sola decisión.</p>
      <p><strong>2. Conserva la mejor.</strong> Propone una toma por grupo; puedes conservar otra, conservar varias u omitir el grupo.</p>
      <p><strong>3. Borra con seguridad.</strong> Las fotos borradas van a la papelera del móvil durante 30 días, así que un error se puede deshacer.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se ejecuta en el móvil: sin cuenta, sin envíos. TripSweep es gratuita en <a href="{play}">Google Play</a> (Android 11 o posterior).</li>
        <li>Para un carrete entero, comparar en una pantalla grande con <a href="{pc}">PhotoCull</a> en un Mac o un PC es todavía más rápido.</li>
      </ul>"""),
],
"photocull": [
dict(slug="sort-iphone-photos-on-mac",
     title="Cómo ordenar las fotos del iPhone en el Mac",
     desc="Ordena miles de fotos del iPhone en tu Mac: qué hacen Fotos y Captura de Imagen, y una forma más rápida de agrupar, comparar y borrar.",
     h1="Cómo ordenar las fotos del iPhone en el Mac",
     body="""      <p>Ordenar un carrete lleno en el iPhone son horas de toques. En un Mac ves muchas más fotos a la vez, seleccionas con el ratón y comparas en una pantalla grande. Así se hace, con las herramientas de macOS y con una app dedicada.</p>

      <h2>Con las herramientas de macOS</h2>
      <ul>
        <li><strong>Fotos:</strong> importa una copia de las fotos del iPhone al Mac. Útil como copia de seguridad, pero no te dice qué borrar en el iPhone.</li>
        <li><strong>Captura de Imagen:</strong> muestra las fotos del iPhone como simples archivos, sin agruparlas por viaje ni comparar las fotos parecidas.</li>
      </ul>
      <p>Las dos funcionan, pero con miles de fotos sigues desplazándote por una única lista larga.</p>

      <h2>Con PhotoCull, paso a paso</h2>
      <p><strong>1. Instala PhotoCull.</strong> <a href="{mac}">Descárgalo gratis</a>: macOS 11 o posterior en Apple Silicon, firmado y notarizado por Apple.</p>
      <p><strong>2. Conecta el iPhone.</strong> Conéctalo con un cable USB, desbloquéalo y toca Confiar.</p>
      <p><strong>3. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar y muestra el espacio que ocupa cada viaje. Empieza por el más pesado.</p>
      <p><strong>4. Compara y marca.</strong> Las fotos parecidas llevan una insignia: abre hasta seis lado a lado, quédate con la mejor y marca el resto, junto con capturas de pantalla y vídeos grandes que no necesites.</p>
      <p><strong>5. Borra con seguridad.</strong> El borrado lo aplica en el iPhone la <a href="{ts}">app TripSweep</a>, gratuita, a través de « Eliminados recientemente »: tienes 30 días para cambiar de opinión.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se queda en tu Mac y tu iPhone: sin cuenta, sin nube, sin envíos.</li>
        <li>PhotoCull nunca modifica tus originales y solo borra lo que confirmas.</li>
        <li>Desde un Mac, la versión gratuita permite 6 borrados al día, TripSweep Pro 15, y Pro + Desktop no tiene límite. Explorar y ordenar es gratis, y ordenar una carpeta de fotos en el Mac nunca tiene límite.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="Cómo ordenar las fotos del iPhone en un PC con Windows",
     desc="Ordena miles de fotos del iPhone en Windows 10 u 11: qué muestran la app Fotos y el Explorador, y una forma más rápida de ordenar y borrar.",
     h1="Cómo ordenar las fotos del iPhone en un PC con Windows",
     body="""      <p>¿iPhone pero ordenador con Windows? Puedes ordenar tus fotos en una pantalla grande en lugar del teléfono. Esto es lo que Windows hace por sí solo, y un método más rápido.</p>

      <h2>Con las herramientas de Windows</h2>
      <ul>
        <li><strong>App Fotos:</strong> importa una copia de las fotos del iPhone al PC. Sirve como copia de seguridad, pero no te ayuda a elegir qué borrar.</li>
        <li><strong>Explorador de archivos:</strong> muestra las fotos del iPhone en carpetas como 100APPLE, con nombres como IMG_0001, sin viajes ni comparación de fotos parecidas.</li>
      </ul>

      <h2>Con PhotoCull, paso a paso</h2>
      <p><strong>1. Instala Apple Devices.</strong> Instala la app gratuita Apple Devices de Microsoft Store: Windows la necesita para leer un iPhone.</p>
      <p><strong>2. Instala PhotoCull.</strong> Desde Microsoft Store o <a href="{win}">descargándolo gratis</a> (Windows 10/11, 64 bits). La descarga aún no está firmada, así que SmartScreen puede avisar en el primer inicio.</p>
      <p><strong>3. Conecta el iPhone.</strong> Conéctalo con un cable USB, desbloquéalo y toca Confiar.</p>
      <p><strong>4. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar y muestra el espacio que ocupa cada viaje. Empieza por el más pesado.</p>
      <p><strong>5. Compara, marca, borra.</strong> Las fotos parecidas llevan una insignia: compara hasta seis lado a lado, quédate con la mejor y marca el resto. El borrado lo aplica en el iPhone la <a href="{ts}">app TripSweep</a>, gratuita, a través de « Eliminados recientemente »: tienes 30 días para cambiar de opinión.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se queda en tu PC y tu iPhone: sin cuenta, sin nube, sin envíos.</li>
        <li>PhotoCull nunca modifica tus originales y solo borra lo que confirmas.</li>
        <li>Explorar y ordenar es gratis, y ordenar una carpeta de fotos que ya está en el PC nunca tiene límite.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Cómo ordenar miles de fotos más rápido en un Mac o PC",
     desc="Por qué ordenar fotos en una pantalla grande es mucho más rápido que en el móvil, y un método sencillo para repasar miles de fotos en una sola sesión.",
     h1="Cómo ordenar miles de fotos más rápido en un Mac o un PC",
     body="""      <p>Si tu carrete tiene diez mil fotos, ordenarlas en la pantalla del móvil es un proyecto que nunca acabarás. En un ordenador puede ser cosa de una tarde. Aquí te explico por qué y un método que funciona.</p>

      <h2>Por qué un ordenador es más rápido</h2>
      <ul>
        <li><strong>Más en pantalla:</strong> decenas de fotos a la vez en lugar de un puñado.</li>
        <li><strong>Selección precisa:</strong> un ratón y un teclado seleccionan cientos de fotos en segundos.</li>
        <li><strong>Comparación de verdad:</strong> fotos parecidas una junto a otra, a un tamaño en el que se ven el enfoque y las expresiones.</li>
      </ul>

      <h2>Un método que funciona</h2>
      <p><strong>1. Agrupa por viaje.</strong> Ordenar por fecha y lugar divide la biblioteca en partes manejables. Empieza por el viaje que más espacio ocupa.</p>
      <p><strong>2. Elimina las casi copias.</strong> Compara cada grupo de tomas parecidas, conserva la mejor y marca el resto.</p>
      <p><strong>3. Filtra el ruido.</strong> Oculta los lugares que no te interesan (casa, trabajo) para que los viajes de verdad destaquen, y filtra por tamaño para encontrar los archivos pesados.</p>
      <p><strong>4. Borra de una vez.</strong> Marca cientos de fotos y confirma una sola vez.</p>

      <h2>PhotoCull hace justo esto</h2>
      <p><a href="{pc}">PhotoCull</a> es una app de escritorio gratuita para Mac y Windows. Su vista Viajes agrupa la biblioteca por viaje y muestra el espacio que ocupa cada uno, las fotos parecidas llevan una insignia y puedes comparar hasta seis lado a lado. Lee un iPhone por USB o cualquier carpeta de tu ordenador, funciona 100 % en el dispositivo y nunca modifica tus originales.</p>
      <p>Los borrados en un iPhone pasan por la <a href="{ts}">app TripSweep</a>, gratuita, y por « Eliminados recientemente », así que un error se puede deshacer durante 30 días. Ordenar una carpeta de tu ordenador nunca tiene límite.</p>

      <h2>Consejos para una sesión larga</h2>
      <ul>
        <li>Trabaja viaje por viaje, sin recorrer toda la biblioteca.</li>
        <li>Decide rápido: si dos tomas se parecen, conserva una.</li>
        <li>Borra al final de cada viaje, para que se note el avance.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="Cómo liberar espacio en el iPhone desde un Mac o PC",
     desc="Conecta tu iPhone, ordena fotos en una pantalla grande y borra lo que no necesitas, sin iCloud y sin enviar nada a internet.",
     h1="Cómo liberar espacio en el iPhone desde un Mac o un PC con Windows",
     body="""      <p>Limpiar un iPhone lleno desde el propio iPhone es tedioso. Desde un ordenador ves muchas más fotos a la vez y decides más rápido. Este es el proceso completo.</p>

      <h2>Qué necesitas</h2>
      <ul>
        <li>Un Mac (Apple Silicon, macOS 11 o posterior) o un PC con Windows 10/11.</li>
        <li>Un cable USB. En Windows, además, la app gratuita Apple Devices de Microsoft Store.</li>
        <li><a href="{pc}">PhotoCull</a>, gratuito para ambos sistemas.</li>
        <li>Para borrar desde el iPhone: la <a href="{ts}">app TripSweep</a>, gratuita, en el iPhone.</li>
      </ul>

      <h2>Paso a paso</h2>
      <p><strong>1. Conecta y confía.</strong> Conecta el iPhone, desbloquéalo y toca Confiar.</p>
      <p><strong>2. Abre la vista Viajes.</strong> PhotoCull agrupa tu carrete por viaje y muestra el espacio que ocupa cada uno.</p>
      <p><strong>3. Ordena los viajes más pesados.</strong> Compara las tomas parecidas, conserva la mejor y marca el resto, además de las capturas de pantalla y los vídeos grandes que no necesites.</p>
      <p><strong>4. Confirma el borrado.</strong> Desde un Mac, TripSweep aplica el borrado en el iPhone a través de « Eliminados recientemente », y en Windows también. Nada se borra de forma permanente al instante.</p>
      <p><strong>5. Vacía « Eliminados recientemente ».</strong> El espacio se recupera cuando se vacía el álbum.</p>

      <h2>¿Es seguro?</h2>
      <p>Sí: tus fotos se quedan en tus dispositivos, sin cuenta, sin nube y sin subir nada. Las fotos borradas permanecen 30 días en « Eliminados recientemente », y PhotoCull solo lee tus fotos hasta que tú confirmas.</p>

      <h2>¿Cuántas fotos puedo borrar al día?</h2>
      <p>Desde un Mac, la versión gratuita permite 6 fotos al día, TripSweep Pro 15 y Pro + Desktop es ilimitado (consulta los planes en la página de TripSweep). Todas son compras únicas, sin suscripción. Explorar, comparar y ordenar es gratis, y ordenar una carpeta de tu ordenador nunca tiene límite.</p>

      <h2>En Windows</h2>
      <p>Los pasos son los mismos en Windows 10 y 11. Instala primero la app gratuita Apple Devices de Microsoft Store, para que PhotoCull pueda leer el iPhone. La app todavía no está firmada digitalmente, así que SmartScreen puede mostrar una advertencia la primera vez que la abras.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Cómo comparar fotos parecidas lado a lado y quedarte con la mejor",
     desc="Una rutina sencilla para elegir la mejor toma entre fotos casi idénticas: en qué fijarte y cómo hacerlo rápido en una pantalla grande.",
     h1="Cómo comparar fotos parecidas y quedarte con la mejor",
     body="""      <p>Hiciste seis fotos del mismo momento y todas se ven bien. Elegir la mejor lleva segundos con el método adecuado, y varios minutos con el equivocado.</p>

      <h2>Qué revisar, en este orden</h2>
      <ol>
        <li><strong>Enfoque.</strong> Haz zoom en los ojos o en el sujeto principal. Un sujeto borroso queda descartado.</li>
        <li><strong>Expresiones.</strong> Ojos abiertos, sonrisas naturales, nadie parpadeando.</li>
        <li><strong>Encuadre.</strong> Nada cortado, un fondo limpio, el horizonte recto.</li>
        <li><strong>Momento.</strong> Si dos tomas están igual, quédate con la que transmita más vida.</li>
      </ol>

      <h2>Por qué importa verlas lado a lado</h2>
      <p>Pasar de una foto a otra hace difícil ver las pequeñas diferencias. Verlas una junto a otra, al mismo tamaño, hace evidente cuál es la más nítida o la mejor encuadrada. La pantalla de un ordenador muestra hasta seis a la vez, mientras que el móvil muestra una.</p>

      <h2>Una rutina más rápida</h2>
      <p>Agrupa primero las fotos parecidas, para no tener que buscarlas en la biblioteca. En cada grupo, abre la comparación, elige una y marca las demás. Decides en segundos, no en minutos.</p>

      <h2>Hazlo con PhotoCull</h2>
      <p><a href="{pc}">PhotoCull</a> muestra una insignia en las fotos parecidas, abre hasta seis lado a lado y te deja marcar el resto con un clic. Funciona con un iPhone conectado por USB o con cualquier carpeta de tu Mac o PC, sin conexión, y nunca modifica tus originales.</p>
      <p>En el propio móvil, la <a href="{ts}">app TripSweep</a> sugiere la mejor toma de cada grupo según la nitidez, la puntuación estética de Apple y los rostros, y su botón « Conservar 1 por grupo » resuelve una categoría entera de una vez.</p>

      <h2>Conserva sin arrepentirte</h2>
      <p>Cuando dudes, quédate con dos. Los borrados en un iPhone pasan por « Eliminados recientemente » durante 30 días, así que aún puedes cambiar de opinión.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="Cómo buscar fotos duplicadas y parecidas en un Mac",
     desc="Encuentra copias exactas, ráfagas y tomas casi idénticas en las carpetas de tu Mac o en un disco externo, conserva la mejor y manda el resto a la Papelera.",
     h1="Cómo buscar fotos duplicadas y parecidas en un Mac",
     body="""      <p>Años de importaciones, tarjetas de cámara y copias de seguridad dejan las mismas fotos repartidas por las carpetas de un Mac. Algunas son copias exactas; la mayoría son tomas casi idénticas del mismo momento. Así se encuentran las dos, te quedas con la mejor y recuperas espacio, sin tocar tu biblioteca de Fotos.</p>

      <h2>Qué ofrece macOS</h2>
      <ul>
        <li><strong>Finder:</strong> ordenar una carpeta por nombre o tamaño ayuda a detectar copias evidentes como «IMG_1234 copia.jpg», pero no dos tomas distintas de la misma escena.</li>
        <li><strong>Fotos:</strong> su álbum Duplicados solo abarca las fotos que ya están en la biblioteca de Fotos, no tus otras carpetas ni discos.</li>
      </ul>

      <h2>Con PhotoCull, paso a paso</h2>
      <p><strong>1. Instala PhotoCull.</strong> <a href="{mac}">Descárgalo gratis</a>: macOS 11 o posterior en Apple Silicon, firmado y notarizado por Apple.</p>
      <p><strong>2. Abre la carpeta.</strong> Pulsa « Abrir carpeta » o arrastra una carpeta a la ventana. Se incluyen las subcarpetas y también los discos externos.</p>
      <p><strong>3. Mira las insignias.</strong> PhotoCull compara el contenido de las fotos, no sus nombres: las copias exactas, las ráfagas y las tomas casi idénticas llevan la misma insignia «≈ N».</p>
      <p><strong>4. Quédate con la mejor.</strong> Abre un grupo para comparar hasta seis fotos lado a lado, conserva la más nítida y marca el resto.</p>
      <p><strong>5. Borra con seguridad.</strong> Los archivos marcados van a la Papelera del Mac, donde « Recuperar » los devuelve si cambias de opinión.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Admite JPEG, HEIC, PNG, TIFF, WebP y archivos RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), además de vídeos MOV y MP4.</li>
        <li>Las fotos se fechan con sus datos EXIF, así que las carpetas copiadas se siguen ordenando por el día en que se hicieron.</li>
        <li>Ordenar una carpeta es gratis y nunca tiene límite. Todo se ejecuta en tu Mac: sin cuenta, sin envíos.</li>
        <li>Las bibliotecas de Fotos y los paquetes de apps que haya dentro de la carpeta se omiten, así que PhotoCull nunca husmea en los archivos de otra app.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Cómo buscar fotos duplicadas y parecidas en Windows",
     desc="Encuentra copias exactas, ráfagas y tomas casi idénticas en tu PC o en un disco externo, conserva la mejor y manda el resto a la Papelera de reciclaje.",
     h1="Cómo buscar fotos duplicadas y parecidas en Windows 10 u 11",
     body="""      <p>Las copias de seguridad del móvil, las tarjetas de cámara y las copias antiguas dejan las mismas fotos en varias carpetas de un PC. Algunas son duplicados exactos, la mayoría son tomas casi idénticas. Así se encuentran las dos y se limpia todo con seguridad.</p>

      <h2>Qué ofrece Windows</h2>
      <ul>
        <li><strong>Explorador de archivos:</strong> ordenar por nombre, tamaño o fecha ayuda con las copias evidentes, pero no sabe que dos archivos distintos muestran la misma escena.</li>
        <li><strong>La app Fotos:</strong> buena para ver e importar, pero sin ninguna herramienta para encontrar tomas parecidas y elegir la mejor.</li>
      </ul>

      <h2>Con PhotoCull, paso a paso</h2>
      <p><strong>1. Instala PhotoCull.</strong> Consíguelo gratis <a href="{win}">para Windows 10 u 11</a> (64 bits), o en Microsoft Store.</p>
      <p><strong>2. Abre la carpeta.</strong> Pulsa « Abrir carpeta » o arrastra una carpeta a la ventana. Se incluyen las subcarpetas y los discos externos.</p>
      <p><strong>3. Mira las insignias.</strong> PhotoCull compara lo que muestran las fotos, no los nombres de archivo: las copias exactas, las ráfagas y las tomas casi idénticas llevan la misma insignia «≈ N».</p>
      <p><strong>4. Quédate con la mejor.</strong> Compara hasta seis fotos lado a lado, conserva la más nítida y marca el resto.</p>
      <p><strong>5. Borra con seguridad.</strong> Los archivos marcados van a la Papelera de reciclaje, así que puedes restaurarlos.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Admite JPEG, HEIC, PNG, TIFF, WebP y archivos RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), además de vídeos MOV y MP4. Las miniaturas HEIC requieren las Extensiones de imagen HEIF gratuitas de Microsoft.</li>
        <li>Las fotos se fechan con sus datos EXIF, así que las carpetas copiadas se siguen ordenando por el día en que se hicieron.</li>
        <li>Ordenar una carpeta es gratis y nunca tiene límite. Todo se ejecuta en tu PC: sin cuenta, sin envíos.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Cómo ordenar una carpeta enorme de fotos en un Mac o PC",
     desc="Copias antiguas, tarjetas de cámara, un disco externo lleno: un método sencillo para ordenar miles de fotos por viaje, quitar casi copias y conservar lo mejor.",
     h1="Cómo ordenar una carpeta enorme de fotos, o un disco externo entero",
     body="""      <p>Todos tenemos una: una carpeta llamada «Fotos por ordenar», una copia antigua del móvil, un disco externo que se ha ido llenando durante diez años. Miles de archivos, sin orden y con muchas casi copias. Este es un método para despacharlo en una sola sesión.</p>

      <h2>1. Abre toda la carpeta de una vez</h2>
      <p>No vayas carpeta por carpeta. Abre la carpeta principal en <a href="{pc}">PhotoCull</a> (« Abrir carpeta », o arrástrala a la ventana): se incluyen las subcarpetas y cada foto se fecha con sus datos EXIF, no por el día en que se copió.</p>

      <h2>2. Deja que aparezcan los viajes</h2>
      <p>La vista Viajes agrupa las fotos por fecha y lugar y muestra el espacio que ocupa cada grupo. Diez años de archivos se convierten en una lista de viajes y eventos, y empiezas por el más pesado.</p>

      <h2>3. Reduce las casi copias</h2>
      <p>Las ráfagas, las tomas repetidas y las copias de una misma foto llevan una insignia «≈ N». Compara hasta seis lado a lado, conserva la mejor y marca el resto. Solo con este paso suele desaparecer buena parte de los archivos.</p>

      <h2>4. Marca lo que sobra a simple vista</h2>
      <p>Capturas de pantalla, fotos movidas, vídeos accidentales: márcalos sobre la marcha. No se borra nada hasta que confirmes.</p>

      <h2>5. Borra con seguridad</h2>
      <p>Los archivos confirmados van a la Papelera en un Mac o a la Papelera de reciclaje en Windows, así que un error se puede deshacer. Vacíala cuando estés seguro.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Se admiten los archivos RAW de cámara (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) junto con JPEG, HEIC, PNG y vídeos.</li>
        <li>Ordenar carpetas es gratis y nunca tiene límite, en Mac (<a href="{mac}">descarga</a>) y en Windows (<a href="{win}">descarga</a>).</li>
        <li>Tus originales no se modifican nunca: el único cambio que hace PhotoCull es el borrado que confirmas.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="Cómo ordenar las fotos de Android en un Mac",
     desc="Un Mac no lee los móviles Android por USB. Cómo ordenar miles de fotos de Android en el Mac por wifi y borrar lo que no necesitas.",
     h1="Cómo ordenar las fotos de Android en un Mac",
     body="""      <p>Conecta un móvil Android a un Mac y, casi siempre, no pasa nada: macOS no lee los móviles Android por USB como lo hace Windows. Y sin embargo un Mac es el mejor sitio para ordenar un carrete grande, con una pantalla amplia, un ratón y comparación lado a lado. Esto es lo que funciona.</p>

      <h2>Lo que macOS puede hacer por sí solo</h2>
      <ul>
        <li><strong>Captura de Imagen:</strong> puede ver el móvil si eliges « Transferir fotos » (PTP) en la notificación USB, pero solo como una lista plana de archivos, sin agrupar y sin forma de comparar fotos parecidas.</li>
        <li><strong>Android File Transfer de Google:</strong> ya no tiene mantenimiento y, de todos modos, solo copia archivos.</li>
        <li><strong>Subir a la nube:</strong> enviarlo todo a un servicio online solo para ordenarlo es lento, gasta tus datos y deja tus fotos en el servidor de otra persona.</li>
      </ul>

      <h2>Con PhotoCull, por wifi, paso a paso</h2>
      <p><strong>1. Instala las dos apps.</strong> <a href="{mac}">Descarga PhotoCull para Mac</a> gratis (macOS 11 o posterior en Apple Silicon) e instala en el móvil la <a href="{play}">app TripSweep de Google Play</a>, gratuita (Android 11 o posterior).</p>
      <p><strong>2. La misma red wifi.</strong> Conecta el móvil a la misma red wifi que el Mac y abre la pestaña Eliminación de TripSweep.</p>
      <p><strong>3. Conéctate una vez.</strong> En PhotoCull, haz clic en « Teléfono Android » y elige tu móvil. Autoriza el Mac en el móvil: el mismo código de 4 dígitos aparece en las dos pantallas. La próxima vez se reconecta solo.</p>
      <p><strong>4. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar, con el espacio que ocupa cada viaje. Las fotos parecidas llevan una insignia: compara hasta seis lado a lado, quédate con la mejor y marca el resto.</p>
      <p><strong>5. Borra con seguridad.</strong> Haz clic en Borrar y confirma en el móvil, en TripSweep. Las fotos van a la papelera del móvil durante 30 días, así que un error se puede deshacer.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>La conexión no sale de tu red local y está cifrada; nada pasa por internet.</li>
        <li>PhotoCull nunca modifica tus originales y solo borra lo que confirmas en el móvil.</li>
        <li>Desde el ordenador, la versión gratuita permite 6 borrados al día, TripSweep Pro 15, y Pro + Desktop es ilimitado. Explorar y ordenar es siempre gratis.</li>
        <li>¿Tienes también un iPhone? Se conecta al Mac con un cable USB.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="Cómo ordenar las fotos de Android en un PC con Windows",
     desc="Ordena miles de fotos de Android en Windows 10 u 11: qué muestran el Explorador y la app Fotos, y una forma más rápida de agrupar y borrar.",
     h1="Cómo ordenar las fotos de Android en un PC con Windows",
     body="""      <p>Windows lee bien los móviles Android, pero leer no es ordenar. Con miles de fotos, las herramientas integradas te dejan desplazándote por una lista interminable de nombres de archivo. Esto es lo que hacen, y una forma más rápida de liberar el móvil desde tu PC.</p>

      <h2>Con las herramientas de Windows</h2>
      <ul>
        <li><strong>Explorador de archivos:</strong> tras elegir « Transferencia de archivos » en el móvil, su carpeta DCIM aparece como archivos. Puedes borrar desde ahí, pero sin agrupar y sin forma de comparar fotos parecidas.</li>
        <li><strong>App Fotos:</strong> importa una copia al PC. Una buena copia de seguridad, pero no te dice qué quitar del móvil.</li>
        <li><strong>Enlace Móvil:</strong> solo muestra las fotos recientes, de una en una.</li>
      </ul>

      <h2>Con PhotoCull, paso a paso</h2>
      <p><strong>1. Instala las dos apps.</strong> Consigue PhotoCull gratis <a href="{win}">para Windows 10 u 11</a> y la <a href="{play}">app TripSweep de Google Play</a>, gratuita, en el móvil (Android 11 o posterior).</p>
      <p><strong>2. Conecta por USB o wifi.</strong> Por USB: conecta el móvil y elige « Transferencia de archivos » en su notificación USB. Por wifi: pon ambos en la misma red. Después abre la pestaña Eliminación de TripSweep y haz clic en « Teléfono Android » en PhotoCull.</p>
      <p><strong>3. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar y muestra el espacio que ocupa cada viaje. Empieza por el más pesado.</p>
      <p><strong>4. Compara y marca.</strong> Las fotos parecidas llevan una insignia: abre hasta seis lado a lado, quédate con la mejor y marca el resto, junto con capturas de pantalla y vídeos grandes.</p>
      <p><strong>5. Borra con seguridad.</strong> Confirma en el móvil, en TripSweep: las fotos van a la papelera del móvil durante 30 días.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se queda en tu PC y tu móvil: sin cuenta, sin nube, sin envíos.</li>
        <li>Borrar desde el Explorador de archivos es inmediato y permanente; hacerlo con TripSweep conserva la red de seguridad de 30 días.</li>
        <li>Desde el PC, la versión gratuita permite 6 borrados al día, TripSweep Pro 15, y Pro + Desktop es ilimitado. Ordenar una carpeta del PC nunca tiene límite.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="Cómo liberar espacio en Android desde un Mac o un PC",
     desc="Conecta tu móvil Android, ordena las fotos en una pantalla grande y borra lo que no necesitas, sin pagar Google One y sin subir nada.",
     h1="Cómo liberar espacio en tu móvil Android desde un Mac o un PC",
     body="""      <p>Cuando un móvil Android se queda sin espacio, casi siempre la causa son las fotos y los vídeos. Limpiarlos en una pantalla pequeña es lento. Desde un ordenador ves más a la vez y decides más rápido, sin comprar más almacenamiento en la nube.</p>

      <h2>Por qué ayuda un ordenador</h2>
      <p>Una pantalla grande muestra decenas de fotos a la vez, un ratón selecciona cientos en segundos y comparar tomas casi idénticas lado a lado es mucho más fácil que ir deslizando de una a otra. Un carrete que en el móvil te llevaría una tarde, se despacha en minutos.</p>

      <h2>El método</h2>
      <p><strong>1. Conecta el móvil.</strong> Instala <a href="{pc}">PhotoCull</a> en tu Mac o PC y la <a href="{play}">app TripSweep</a>, gratuita, en el móvil. Conéctate por wifi (Mac y Windows) o por USB (Windows), con TripSweep abierta en la pestaña Eliminación.</p>
      <p><strong>2. Empieza por lo que más pesa.</strong> La vista Viajes muestra el espacio que ocupa cada viaje; los vídeos largos y las vacaciones antiguas suelen liberar más.</p>
      <p><strong>3. Elimina las tomas casi idénticas.</strong> Las ráfagas y las tomas repetidas de la misma escena llevan una insignia. Compáralas lado a lado, quédate con la mejor y marca el resto.</p>
      <p><strong>4. Limpia capturas de pantalla y fotos borrosas.</strong> Rara vez merecen quedarse y se marcan rápido todas juntas.</p>
      <p><strong>5. Confirma en el móvil.</strong> TripSweep aplica el borrado y envía las fotos a la papelera del móvil, donde permanecen 30 días. Vacía la papelera cuando estés seguro para recuperar el espacio.</p>

      <h2>¿Necesito Google One?</h2>
      <p>El almacenamiento en la nube es una buena copia de seguridad, pero lo guarda todo, duplicados incluidos. Limpiar primero significa que necesitas menos almacenamiento, en el móvil y en la nube.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Sin cuenta y sin envíos: el móvil y el ordenador se comunican por tu propia red o por cable.</li>
        <li>Desde el ordenador, la versión gratuita permite 6 borrados al día, Pro 15, y Pro + Desktop es ilimitado.</li>
      </ul>"""),
],
}
