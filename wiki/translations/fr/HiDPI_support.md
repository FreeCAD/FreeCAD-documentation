# HiDPI support/fr
**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

![Rapport des pixels de l\'appareil. 100% = 1, 200% = 2, 150% = 1.5](images/HiDpiDevicePixelRatio.png )

Il s\'agit d\'un [projet](Development_roadmap/fr.md) dédié à la prise en charge des affichages haute résolution dans FreeCAD.

La prise en charge HiDPI fait référence au problème d\'affichage des images matricielles (polices, curseurs, images) et des éléments de l\'interface utilisateur (boutons, menus, poignées) sur des écrans haute résolution. C\'est aussi un terme introduit par Apple.

Le problème est que la taille physique d\'un écran reste la même (de 21 à 32 pouces) tandis que sa résolution augmente (FullHD, 4K, 8K).

Pour résoudre ce problème, Apple a introduit le \"HiDPI\", c\'est-à-dire la mise à l\'échelle de tous les éléments de l\'interface utilisateur en fonction de la taille de la police. La taille des polices est spécifiée en points, tandis que leur valeur en pixels est calculée à l\'aide de la DPI et du ratio de pixels du périphérique, qui est un facteur d\'échelle spécifié par un utilisateur dans les paramètres du système d\'exploitation. Dans le même temps, les images tramées sont rendues à leur taille réelle en pixels, de sorte que les pixels individuels sont moins visibles. Cela signifie que les images tramées sont fournies à une résolution plus élevée pour compenser leur taille sur un écran. Les graphiques vectoriels (éléments de l\'interface utilisateur) sont rendus en conséquence, à une résolution plus élevée.

## Plan directeur 

### Première partie 

Objectif: nous assurer que nous tirons le meilleur parti du support Qt.

-   En cours. Migrer la base d\'utilisateurs vers Qt\> 5.6 et définir AA\_EnableHighDpiScaling sur true.
-   Mettre à l\'échelle tous les curseurs et icônes (en les multipliant par devicePixelRatio) <https://github.com/FreeCAD/FreeCAD/pull/3712>.
-   Rendre tous les vecteurs graphiques de pixels ou disponibles à différentes densités de pixels .

### Deuxième partie 

Objectif: nous assurer que la police système est correctement déterminée.

-   Regrouper les plugins de thème QPA appropriés sur toutes les principales plates-formes (AppImage, etc.)
-   Trouver des moyens de détecter que la police du système est modifiée
-   Supprimer le paramètre de taille de la barre d\'outils/icône et définir la taille de la barre d\'outils par rapport à la police système
-   Ajouter un paramètre expérimental \"facteur d\'échelle\" qui dépendra du ratio de pixels de l\'appareil et/ou de la taille de la police du système
-   Redimensionner la taille de la barre d\'outils/de l\'icône en fonction du nouveau paramètre expérimental
-   Recueillir les commentaires des utilisateurs pour savoir si nous avons besoin de la taille de l\'icône de la barre d\'outils personnalisable

### Troisième partie 

Objectif: rendre la taille de tous les widgets de l\'interface utilisateur par rapport à la taille de la police

-   Dans tous les endroits appropriés, obtenir des métriques de police système pour déterminer la taille d\'un widget.
-   Aux endroits où la taille réelle est référencée, supposer la taille de la police comme mesure relative (72 points = 96 pixels virtuels = 1 pouce).
-   Choisir un appareil de référence par rapport auquel l\'interface utilisateur pourrait être mise à l\'échelle.
-   Les coordonnées 2D et les tailles doivent supposer des pixels indépendants de l\'appareil.
-   S\'assurer que les versions qreal des API sont utilisées.
-   Désactiver AA\_EnableHighDpiScaling.

### Quatrième partie 

Objectif: prendre en charge le redimensionnement lorsque la fenêtre est déplacée d\'un écran à un autre

-   Détecter que le rapport de pixels de l\'appareil a changé
-   Notifier tous les widgets en fonction du ratio de pixels de l\'appareil ou de la taille de la police

## Contexte

### Résolution d\'affichage 

<img alt="" src=images/Vector_Video_Standards8.svg  style="width:800px;">

### Ratio de pixels de l\'appareil 

C\'est un concept bien connu des développeurs Web et Android. Mais pas tant pour les développeurs de bureau.

Fondamentalement, c\'est le rapport entre les pixels physiques et les pixels indépendants de l\'appareil.

Tout d\'abord. Le positionnement et la taille de l\'interface utilisateur (x, y, largeur, hauteur) sont historiquement définis en pixels.

Mais comme une plus grande variété de résolutions d\'écrans devient disponible dans de nombreuses tailles physiques différentes, c\'est devenu un problème dont les développeurs de logiciels doivent être conscients.

Le développement de FreeCAD a commencé en 2002, bien avant qu\'un tel problème ne soit même prévu.

Ok, pourquoi ne pas simplement augmenter le DPI, demandez-vous. Eh bien, le problème est que vous souhaitez toujours bénéficier de l\'affichage haute résolution.

Tous les graphiques matriciels doivent contenir plus de pixels, tandis que les graphiques vectoriels (polices et icônes) doivent être de la même taille physique que celle visible à l\'écran.

Si vous changez simplement le DPI, vous redimensionneriez tout de haut en bas. Mais en fait, vous avez besoin que toutes les tailles de pixels restent les mêmes, tandis que les ressources (images) doivent être affichées dans une résolution plus élevée.

Ainsi, le concept de \"pixels indépendants du périphérique\" a été introduit. L\'idée était que les développeurs ne pouvaient continuer à se soucier de la taille physique d\'un écran et de concevoir des interfaces utilisateur en pixels virtuels.

Mais la réalité est que si vous utilisez des graphiques matriciels, ils deviennent pixélisés, flous ou aliasés lorsqu\'ils sont affichés dans une résolution non native. Les développeurs doivent donc désormais fournir plusieurs versions d\'images raster, pour chaque rapport de pixels de l\'appareil. Habituellement, ce sont des nombres entiers: 1, 2, 3, 4. Mais cela peut aussi être fractionnaire (125%, 150%, 175% = 1,25, 1,5, 1,75) ce qui signifie qu\'il y a encore une mise à l\'échelle impliquée, mais pas aussi apparente.

-   <https://stackoverflow.com/questions/8785643/what-exactly-is-device-pixel-ratio>
-   <https://stackoverflow.com/questions/13911786/what-is-device-pixel-ratio-for>

## Problème de test/démonstration 

### OS X 

1.  Ouvrez \"Affichage\"
2.  Choisissez \"Échelle\".
3.  Choisissez \"Texte plus grand\" - cela augmente le ratio de pixels de l\'appareil

Vidéo: <https://www.youtube.com/watch?v=4U3eh_fMo4o>

### Window X 

Commandes utiles:

    ~$ xrdb -query
    *customization: -color
    Xft.dpi:    192
    Xft.antialias:  1
    Xft.hinting:    1
    Xft.hintstyle:  hintslight
    Xft.rgba:   rgb
    Xcursor.size:   128
    Xcursor.theme:  DMZ-White

    ~$ xdpyinfo | grep -B 2 resolution
    screen #0:
      dimensions:    3840x2160 pixels (1016x572 millimeters)
      resolution:    96x96 dots per inch

### Ubuntu (Shell GNOME) 

1.  Ouvrez «Moniteurs» (Paramètres\> Périphériques\> Écrans)
2.  Sélectionnez la plus haute résolution disponible
3.  Sélectionnez une mise à l\'échelle supérieure à 100%

## Problèmes et solutions 

-   Images matricielles (curseurs, icônes)
-   Polices (définies en pixels plutôt qu\'en points)
-   Point chaud du curseur
-   Zoom/Rotation de l\'origine
-   Distance d\'accrochage
-   Distance de sélection (la zone chaude autour des objets sélectionnables)

### Taille de la police 

Les polices sont généralement vectorielles. Elles n\'ont donc pas besoin d\'une version de résolution plus élevée pour pouvoir être mis à l\'échelle (en pixels). Cependant, nous ne pouvons pas simplement augmenter chaque taille de police et l\'appeler un jour. Les gens sont habitués à la taille des polices en fonction de leur apparence sur papier. Et sur le papier, on sait que la police 72pt prend un pouce, et sur les écrans d\'autrefois, un pouce était égal à 96 pixels au niveau de zoom 1:1.

Ainsi, à mesure que les résolutions d\'affichage augmentent, les écrans peuvent contenir plus de lignes de texte de même taille. Donc, naturellement, comme la taille physique de l\'écran reste la même et que nos yeux ne parviennent pas à mieux discerner les petits détails, nous percevons la même taille de point de police comme plus petite sur des résolutions plus élevées.

Pour résoudre ce problème, le système d\'exploitation a mis en œuvre ce qu\'il a appelé la mise à l\'échelle DPI (ou les paramètres de police DPI dans les temps anciens) ou la mise à l\'échelle haute résolution des écrans 4K récents. Les utilisateurs pourraient changer le DPI et bénéficier de beaucoup plus d\'espace en termes de pixels tout en gardant une taille de police confortable à lire.

### Taille du curseur personnalisée 

La taille du curseur est un peu difficile. Qt recommande d\'utiliser une taille d\'image codée en dur de 32x32. À partir de 5.x, il ne fournit aucune fonctionnalité pour s\'intégrer au système d\'exploitation et interroger la taille du pointeur de la souris. C\'est dommage car cela signifie que vous ne pouvez pas bénéficier des paramètres d\'accessibilité, où la taille du curseur peut être définie sur une valeur arbitrairement grande.

Donc, jusqu\'à ce que Qt fournisse de meilleurs conseils sur la taille du curseur, utilisons une image avec un rapport de pixels de l\'appareil de 32\*.

Dans le système d\'exploitation, par exemple dans GNOME, la taille du curseur semble être fixe en termes de pixels virtuels. Autrement dit, il respecte le ratio de pixels de l\'appareil (conservez la même taille apparente). Mais il augmente lorsque vous modifiez la résolution d\'affichage (c\'est-à-dire qu\'il reste le même en pixels, mais augmente en taille apparente).

Par exemple, voici un paramètre par défaut pour les pixels virtuels dans GNOME:

    ~$ gsettings get org.gnome.desktop.interface cursor-size
    64

Compte tenu du facteur d\'échelle, cela signifie la taille de pixel physique de 128.

Qt ne fournit pas la fonctionnalité pour récupérer cette valeur. Nous devons donc le coder en dur ou fournir un paramètre utilisateur pour le modifier.

## Fils du forum 

-   [Améliorer la prise en charge des écrans haute résolution](https://forum.freecadweb.org/viewtopic.php?t=34916) - prise en charge générale de Qt
-   [Actualités: Qt 5.14 apporte un support HiDPI nettement meilleur](https://forum.freecadweb.org/viewtopic.php?t=39325) - support général de Qt
-   [Curseurs personnalisés et ppp élevé (testeurs Windows et MacOS nécessaires)](https://forum.freecadweb.org/viewtopic.php?&t=48719) - problème d\'image du curseur raster
-   [Assistance HiDPI en vue Sketcher](https://forum.freecadweb.org/viewtopic.php?t=34853) - problème de distance de sélection
-   [Améliorations de la résolution élevée](https://forum.freecadweb.org/viewtopic.php?t=10512) - PR «Corrections haute résolution» <https://github.com/FreeCAD/FreeCAD/pull/54>, mauvaise qualité, 2015
-   [High dpi](https://forum.freecadweb.org/viewtopic.php?t=12123) - version expérimentale avec PR \"High DPI Improvements\"
-   [Taille de la police GUI](https://forum.freecadweb.org/viewtopic.php?t=41656) - problème de taille de police et solution de contournement QT\_SCALE\_FACTOR
-   [BUG? Icônes recadrées](https://forum.freecadweb.org/viewtopic.php?t=28838) - problèmes avec HiDPI sur plusieurs écrans
-   [FreeCAD 0.17 sur macOS Update (Qt 5 builds now available)](https://forum.freecadweb.org/viewtopic.php?t=20977) - problèmes avec HiDPI sous OS X après la mise à niveau vers Qt5
-   [Ticket \# 3537 - Le mode Draft Edit ne fonctionne pas sous MacOS X (problème HiDPi)](https://forum.freecadweb.org/viewtopic.php?f=3&t=29743) - OS X + HiDPI, Qt5
-   [Menu déformé sur écran externe MAC](https://forum.freecadweb.org/viewtopic.php?t=39975) - OS X + HiDPI, écran externe
-   [plan et état macOS Qt5](https://forum.freecadweb.org/viewtopic.php?t=19724&start=60) - OS X a abandonné la prise en charge des problèmes Qt4 et HiDPI
-   <https://www.google.com/search?q=freecad+hidpi+site:forum.freecadweb.org>
-   [Une suggestion pour désactiver la mise à l\'échelle \"dump\" avant de s\'attaquer aux problèmes de taille de la police](https://forum.freecadweb.org/viewtopic.php?f=10&t=52307)
-   [Navigation cube scaling](https://forum.freecadweb.org/viewtopic.php?f=3&t=42835)
-   [Navigation cube scaling 2](https://forum.freecadweb.org/viewtopic.php?p=450061#p450061)

## Changements importants 

-    {{commit|a14b99e77}}
    

-    {{commit|2f2d50535}}
    

-    {{commit|bb6e4e6ad}}
    

-    {{commit|23ecb8eac}}
    

-    {{commit|ca7770b80}}
    

-    {{commit|51fcdd2c0}}
    

-    {{commit|805ccd8deb}}
    

-    {{commit|347156403}}
    

-    {{commit|094dda5900d}}
    

-    {{commit|925cffc1535}}
    

-    {{commit|7dfeb801a}}
    

## Problèmes de Bugtracker 

-   Tickets marqués avec [HiDPI](https://tracker.freecadweb.org/search.php?tag_string=HiDPI)

## Références externes 

-   <https://doc.qt.io/qt-5/highdpi.html>
-   <https://doc.qt.io/qt-5/scalability.html>
-   <https://docs.microsoft.com/en-us/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows>
-   <https://docs.microsoft.com/en-us/windows/win32/w8cookbook/high-dpi-for-desktop-apps-in-windows-8-1?redirectedfrom=MSDN>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > HiDPI support/fr
