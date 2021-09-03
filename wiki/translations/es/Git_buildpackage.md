

Los flujos de trabajo de desarrollo de Debian modernos implican [empaquetar con Git](https://wiki.debian.org/PackagingWithGit) y la herramienta principal para hacerlo es [git-buildpackage](http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html). git-buildpackage proporciona un comando gbp con varias opciones similares al propio comando git. Muchos de estos comandos son en sí mismos sólo una envoltura de herramientas de Debian de nivel inferior, por lo que la complejidad para aprender a empaquetar puede ser bastante alta.

Para evitar esto, aquí están los pasos cortos y simples para empezar con git-buildpackage. Esto debería funcionar en casi cualquier distribución basada en Debian, pero recomiendo trabajar en esto en un entorno limpio y separado una máquina virtual [Debian Inestable](Debian_Unstable/es.md).

1.  Instálalo con sudo apt install git-buildpackage
2.  Coge los dotfiles al final de esta página. Necesitarás: ~/.gbp.conf, ~/.pbuilderrc, y ~/.quiltrc
3.  La construcción del paquete se producirá en un entorno limpio. Créalo con sudo git-pbuilder create.
4.  Encuentre la URL de un paquete que quiera construir en <https://salsa.debian.org>, la instancia de GitLab autoalojada del proyecto Debian.
5.  Cree un clon del mismo con 
6.  Entre en el directorio del repo clonado con cd
7.  Ejecute la construcción con gbp buildpackage -us -uc
8.  Cuando termine, sus paquetes estarán en ../build-area/.

##### gbp.conf

Ubicación: ~/.gbp.conf

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.gbp.conf>

##### pbuilderrc

Ubicación: ~/.pbuilderrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.pbuilderrc>

##### quiltrc

Ubicación: ~/.quiltrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.quiltrc>


 

[Category:Packaging{{\#translation:}}](Category:Packaging.md) [Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
