# Debian Unstable/es
[Debian Inestable](https://wiki.debian.org/DebianUnstable) es una distribución rodante utilizada para [Desarrollo de Debian](Debian_development/es.md) y recomendada para usuarios avanzados en el desarrollo y empaquetado de FreeCAD. Los nuevos paquetes están listos tan pronto como se suben y se construyen, a menos que quien los suba los haya marcado para [Debian Experimental](https://wiki.debian.org/DebianExperimental), lo que requiere una instalación explícita (después de alguna configuración para habilitar la distribución extra) mediante sudo apt install -t experimental .

Frecuentemente, la gente que usa Debian Testing debería en realidad usar Debian Inestable; Debian Testing sólo debería considerarse un \"bolsillo de la versión de control de calidad\", ya que, aunque pueda parecer más estable que Unstable, en realidad hay un inconveniente. Los nuevos paquetes se suben a Debian Inestable y migran a Pruebas después de un tiempo, por lo que las correcciones de seguridad y los cambios importantes en el empaquetado pueden retrasarse de forma inapropiada.

Hay dos cosas clave para una buena experiencia de usuario en Unstable. La primera es no ejecutar nunca a ciegas sudo apt full-upgrade o sus equivalentes sin comprobar primero los resultados de la operación. Si dice que liberará cientos de MB de espacio, hay una transición de paquetes en marcha que eliminará una buena parte de su sistema. En su lugar, se puede ejecutar con seguridad sudo apt upgrade y obtener nuevos paquetes. A veces, esto resultará en paquetes retenidos, lo que significa que puede ser apropiado ejecutar full-upgrade ya que la desinstalación de paquetes puede ser realmente necesaria.

La segunda clave es aceptar que está participando en el desarrollo de Debian, y utilizar las herramientas y métodos apropiados. Por ejemplo, esto puede significar la instalación de paquetes como apt-listbugs o apt-listchanges o la suscripción a listas de correo de Debian como [debian-devel-announce@lists.debian.org](https://lists.debian.org/debian-devel-announce/).

Mientras que Debian Inestable es perfectamente adecuado como conductor diario a largo plazo, también es muy fácil de ejecutar en una máquina virtual, donde las roturas no serán un gran problema. Simplemente descargue una ISO de pruebas de Debian, instálela en una máquina virtual y actualícela, y luego edite /etc/apt/sources.list para que contenga algo como:

deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
deb [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
# deb-src [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free

Si quieres habilitar los paquetes de Experimental, pon esto en /etc/apt/sources.list.d/experimental.list:

deb [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free
# deb-src [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > Debian Unstable/es
