# -*- coding: utf-8 -*-
# Spanish translation of the FAQ and blog of both sites. Tokens in answers/articles: {ts} {pc} {store} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacidad", more="Sigue leyendo",
    cta_store="📱 Descarga TripSweep en la App Store",
    cta_mac="💻 Descarga PhotoCull para Mac", cta_win="🪟 Descarga PhotoCull para Windows",
    cross_label={"tripsweep": "App de escritorio", "photocull": "App para iOS"},
    index={
        "tripsweep": dict(
            title="Blog de TripSweep: libera espacio en el iPhone y borra fotos duplicadas",
            desc="Guías prácticas para liberar espacio en el iPhone, eliminar fotos duplicadas y parecidas y limpiar viajes antiguos, sin iCloud y sin enviar tus fotos a ningún sitio.",
            h1="Guías para limpiar las fotos de tu iPhone",
            intro="Guías breves y prácticas para liberar espacio en tu iPhone, borrar duplicados y quedarte solo con las mejores fotos."),
        "photocull": dict(
            title="Blog de PhotoCull: ordena fotos en Mac o PC y libera tu iPhone",
            desc="Guías para ordenar miles de fotos más rápido en una pantalla grande, comparar fotos parecidas lado a lado y liberar espacio en el iPhone desde un Mac o un PC con Windows.",
            h1="Guías para ordenar tus fotos en el ordenador",
            intro="Por qué una pantalla grande cambia la rapidez con la que ordenas fotos, y cómo aprovecharla para liberar espacio en tu iPhone."),
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
     "No. TripSweep no necesita cuenta y funciona sin conexión. Los nombres de los lugares se reconocen en tu iPhone, y ninguna foto, vídeo ni ubicación se envía jamás a un servidor."),
    ("¿Borrar en TripSweep también borra mis fotos de iCloud?",
     "Si Fotos de iCloud está activado, borrar una foto en el iPhone la elimina de todos tus dispositivos, porque así funciona Fotos de iCloud. TripSweep borra a través de « Eliminados recientemente », así que tienes 30 días para arrepentirte, y el espacio de iCloud se libera cuando vacías ese álbum."),
    ("¿Puedo revisar las fotos de mi iPhone en una pantalla grande en lugar del móvil?",
     "Sí. <a href=\"{pc}\">PhotoCull</a> es la app de escritorio gratuita que acompaña a TripSweep, para Mac y Windows: muestra el carrete de tu iPhone agrupado por viaje, compara fotos parecidas lado a lado y te permite marcar cientos de fotos con unos pocos clics. <a href=\"{pc}\">Más información sobre PhotoCull</a>."),
    ("¿Puedo borrar fotos en bloque desde el ordenador en vez de tocar la pantalla del móvil?",
     "Sí, con <a href=\"{pc}\">PhotoCull</a> en un Mac o un PC con Windows. Marcas las fotos en la pantalla grande y TripSweep aplica el borrado en tu iPhone a través de « Eliminados recientemente ». La versión gratuita permite 6 fotos al día desde el Mac (consulta los planes en la página de TripSweep), Pro 15, y Pro + Desktop elimina el límite."),
    ("¿Qué iPhone y qué versiones de iOS admite TripSweep?",
     "TripSweep requiere iOS 18 o posterior. El análisis de fotos parecidas usa el framework Vision de Apple y es más rápido en los iPhone recientes, pero funciona en todos los modelos compatibles."),
]

FAQ_PHOTOCULL = dict(
    title="FAQ de PhotoCull: ordena y borra fotos desde un Mac o un PC",
    desc="Cómo ordenar miles de fotos en el ordenador, comparar fotos parecidas, liberar espacio en el iPhone desde un Mac o PC y borrar con seguridad: respuestas sobre PhotoCull, 100 % sin conexión.",
    nav_home="PhotoCull", nav_desktop="App para iOS",
    h1="Preguntas y respuestas",
    intro="Cómo ordenar tus fotos más rápido desde un ordenador, liberar espacio en tu iPhone desde un Mac o PC, y qué hace (y qué nunca hace) PhotoCull con tus fotos.",
    qa=[
        ("¿Por qué ordenar las fotos en el ordenador en lugar de en el iPhone?",
         "Una pantalla grande muestra más fotos a la vez, un ratón y un teclado seleccionan cientos en segundos, y comparar tomas lado a lado es más fácil que ir pasando de una a otra. Ordenar un carrete de miles de fotos son varias sesiones en el móvil y una sesión mucho más corta en un Mac o un PC."),
        ("¿Qué es PhotoCull?",
         "PhotoCull es una app de escritorio gratuita para Mac y Windows que agrupa tus fotos por viaje, compara tomas parecidas lado a lado y borra en bloque lo que no merece la pena conservar. Lee el carrete de tu iPhone por USB, o cualquier carpeta de fotos de tu ordenador, y funciona 100 % sin conexión."),
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
        ("¿Necesito la app TripSweep para iOS?",
         "No para explorar, comparar y ordenar. Solo la necesitas para borrar fotos del iPhone, porque el borrado se aplica en el móvil. Las carpetas de tu ordenador se pueden ordenar sin ella."),
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
         "No. PhotoCull funciona 100 % sin conexión: sin cuenta, sin nube, y ninguna foto, vídeo ni ubicación se envía a ningún sitio. El reconocimiento de lugares y la detección de fotos parecidas se ejecutan en tu ordenador."),
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
      <p><a href="{ts}">TripSweep</a> hace estos pasos por ti en el iPhone. Su pestaña Limpieza enumera las copias idénticas, las fotos parecidas, las fotos borrosas, las capturas de pantalla y los vídeos grandes, cada uno con el espacio que ocupa. Tus viajes se agrupan por lugar y fecha y se ordenan por tamaño, y un botón « Conservar 1 por grupo » resuelve una categoría entera con un solo toque. Los favoritos nunca se sugieren para borrar, los borrados pasan por « Eliminados recientemente » y nada sale jamás de tu móvil: sin cuenta, sin nube, sin servidor.</p>
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
     title="Cómo limpiar fotos de vacaciones antiguas y quedarte con las mejores",
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
],
"photocull": [
dict(slug="sort-photos-on-computer",
     title="Cómo ordenar miles de fotos más rápido en un Mac o un PC con Windows",
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
      <p><a href="{pc}">PhotoCull</a> es una app de escritorio gratuita para Mac y Windows. Su vista Viajes agrupa la biblioteca por viaje y muestra el espacio que ocupa cada uno, las fotos parecidas llevan una insignia y puedes comparar hasta seis lado a lado. Lee un iPhone por USB o cualquier carpeta de tu ordenador, funciona 100 % sin conexión y nunca modifica tus originales.</p>
      <p>Los borrados en un iPhone pasan por la <a href="{ts}">app TripSweep</a>, gratuita, y por « Eliminados recientemente », así que un error se puede deshacer durante 30 días. Ordenar una carpeta de tu ordenador nunca tiene límite.</p>

      <h2>Consejos para una sesión larga</h2>
      <ul>
        <li>Trabaja viaje por viaje, sin recorrer toda la biblioteca.</li>
        <li>Decide rápido: si dos tomas se parecen, conserva una.</li>
        <li>Borra al final de cada viaje, para que se note el avance.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="Cómo liberar espacio en el iPhone desde un Mac o un PC con Windows",
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
],
}
