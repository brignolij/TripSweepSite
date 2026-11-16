# -*- coding: utf-8 -*-
# Spanish translation of the FAQ and blog of the TripSweep site. Tokens in answers/articles: {ts} {pc} {store} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacidad", more="Sigue leyendo",
    cta_store="📱 Descarga TripSweep en la App Store",
    cta_play="🤖 Descarga TripSweep en Google Play",
    cross_label={"tripsweep": "App de escritorio", "photocull": "App móvil"},
    twin_android="¿Usas un móvil Android? Lee la guía para Android:",
    twin_iphone="¿Usas un iPhone? Lee la guía para iPhone:",
    index={
        "tripsweep": dict(
            title="Blog de TripSweep: espacio en el iPhone y fotos duplicadas",
            desc="Guías prácticas para liberar espacio en el iPhone, eliminar fotos duplicadas y parecidas y limpiar viajes antiguos, sin iCloud y sin enviar tus fotos.",
            h1="Guías para limpiar las fotos de tu iPhone",
            intro="Guías breves y prácticas para liberar espacio en tu iPhone, borrar duplicados y quedarte solo con las mejores fotos."),
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
     "Sí, con <a href=\"{pc}\">PhotoCull</a> en un Mac o un PC con Windows. Marcas las fotos en la pantalla grande y, con un iPhone, PhotoCull las borra directamente por el cable USB: sin límite diario, sin nada que comprar y sin TripSweep. Hace falta que Fotos en iCloud esté desactivado en el iPhone y, en un Mac, macOS 27 o posterior (también funciona en Windows). El borrado es definitivo en el iPhone, las fotos no pasan por « Eliminados recientemente », pero PhotoCull guarda por defecto una copia en tu ordenador durante 30 días. TripSweep sigue siendo una opción: borra a través de « Eliminados recientemente » (30 días) y es el camino cuando Fotos en iCloud está activado o con macOS 26 o anterior. Los borrados pedidos desde el ordenador a través de TripSweep, que es también como funciona un teléfono Android, están limitados a 6 fotos al día gratis y 15 con Pro."),
    ("¿Qué iPhone y qué versiones de iOS admite TripSweep?",
     "TripSweep requiere iOS 18 o posterior. El análisis de fotos parecidas usa el framework Vision de Apple y es más rápido en los iPhone recientes, pero funciona en todos los modelos compatibles. En Android requiere Android 11 o posterior y está disponible en <a href=\"{play}\">Google Play</a>."),
]

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
}
