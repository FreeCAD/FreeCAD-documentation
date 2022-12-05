# Debian Unstable/fr
[Debian Unstable](https://wiki.debian.org/DebianUnstable) est une distribution continue utilisée pour [Développement de Debian](Debian_development/fr.md) et recommandée pour les utilisateurs avancés dans le développement et l\'empaquetage FreeCAD. Les nouveaux paquets sont prêts dès qu\'ils sont téléchargés et construits, à moins que le téléchargeur ne les ait marqués pour [Debian Experimental](https://wiki.debian.org/DebianExperimental) ce qui nécessite une installation explicite (après une configuration pour activer la distribution supplémentaire) via .

Souvent, les personnes utilisant les Debian Testing devraient en fait utiliser Debian Unstable; Les Debian Testing ne devraient être considérés que comme une «entrée/sortie de Questions/réponses», car, même s\'il peut sembler plus stable que l\'Unstable, il y a en fait un inconvénient. Les nouveaux paquets sont téléchargés sur Debian Unstable et migrent vers Testing après un certain temps, ainsi les correctifs de sécurité et les modifications importantes de l\'empaquetage peuvent être retardés de manière inappropriée.

Il existe deux éléments clés pour une bonne expérience utilisateur dans Unstable. La première consiste à ne jamais exécuter aveuglément sudo apt full-upgrade ou ses équivalents sans d\'abord vérifier les résultats de l\'opération. Si cela signifie que vous allez libérer des centaines de Mo d\'espace, il y a une transition de package en cours qui supprimera une bonne partie de votre système. Au lieu de cela, on peut exécuter en toute sécurité sudo apt upgrade et obtenir de nouveaux packages. Parfois, cela entraînera la rétention des packages, ce qui signifie qu\'il peut être approprié d\'exécuter la full-upgrade car la désinstallation des packages peut être nécessaire.

La deuxième point consiste à comprendre que vous participez au développement Debian et à utiliser les outils et méthodes appropriés. Par exemple, cela peut signifier l\'installation de paquets comme apt-listbugs ou apt-listchanges ou l\'abonnement à des listes de diffusion Debian comme [debian-devel-announce@lists.debian.org](https://lists.debian.org/debian-devel-announce/).

Bien que Debian Unstable soit parfaitement adapté en tant que pilote quotidien à long terme, il est également très facile à exécuter sur une machine virtuelle, où les ruptures ne seront pas si importantes. Téléchargez simplement une ISO de test Debian, installez-la sur une machine virtuelle et mettez-la à jour, puis éditez /etc/apt/sources.list pour qu\'elle contienne quelque chose comme:

deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
deb [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
# deb-src [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free

Si vous souhaitez activer les packages d\'Experimental, mettez-les dans /etc/apt/sources.list.d/experimental.list:

deb [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free
# deb-src [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > Debian Unstable/fr
