# Manual:Traditional 2D drafting/fr
{{Manual   *TOC/fr}}

Vous pouvez être intéressé par FreeCAD car vous avez déjà une expérience de dessin technique, par exemple avec un logiciel comme [AutoCAD](https   *//fr.wikipedia.org/wiki/AutoCAD). Ou vous savez déjà quelque chose dans le Design, ou vous préférez dessiner avant de construire. Dans les deux cas, FreeCAD propose un atelier avec des fonctionnalités plus traditionnelles, avec des outils que l'on trouve dans la plupart des applications CAO 2D    * l\'[atelier Draft](Draft_Workbench/fr.md).

L'atelier Draft, bien qu\'il adopte des façons de travailler hérité du dessin traditionnel 2D du monde de la CAO n\'est pas limité au royaume 2D. Tous ses outils fonctionnent dans l\'ensemble de l\'espace 3D et beaucoup de ses outils, par exemple <img alt="" src=images/Draft_Move.svg  style="width   *16px;"> [déplacement](Draft_Move/fr.md) ou <img alt="" src=images/Draft_Rotate.svg  style="width   *16px;"> [rotation](Draft_Rotate/fr.md), sont couramment utilisés partout dans FreeCAD car ils sont souvent plus intuitifs que changer les paramètres de placement manuellement.

Parmi les outils offerts par l'atelier Draft, vous trouverez des outils de dessin traditionnels comme <img alt="" src=images/Draft_Line.svg  style="width   *16px;"> [Ligne](Draft_Line/fr.md), <img alt="" src=images/Draft_Circle.svg  style="width   *16px;"> [Cercle](Draft_Circle/fr.md) ou <img alt="" src=images/Draft_Wire.svg  style="width   *16px;"> [Polyligne](Draft_Wire/fr.md), des outils de modification comme <img alt="" src=images/Draft_Move.svg  style="width   *16px;"> [Déplacer](Draft_Move/fr.md) de translation, <img alt="" src=images/Draft_Rotate.svg  style="width   *16px;"> [Pivoter](Draft_Rotate/fr.md) ou <img alt="" src=images/Draft_Offset.svg  style="width   *16px;"> [Décaler](Draft_Offset/fr.md), un système de [plan de travail/grille](Draft_SelectPlane/fr.md) qui vous permet de définir précisément dans quel plan vous travaillez, et un système d\'[aimantation](Draft_Snap/fr.md) complet qui permet de dessiner et de positionner précisément les éléments l\'un par rapport à l\'autre.

Pour montrer le travail et les possibilités de l\'ébauche de travail, nous réaliserons un exercice simple, dont le résultat sera ce petit dessin, montrant le plan d\'étage d\'une petite maison qui ne contient qu\'un dessus de cuisine (un plan d\'appartement très absurde, mais on peut faire ce que nous voulons ici, n\'est-ce pas?)    *

![](images/Exercise_cabin_01.jpg )

-   Rendez-vous dans l'**atelier Draft**
-   Comme dans toutes les applications de dessin technique, il est judicieux de configurer votre environnement correctement, cela vous épargnera beaucoup de temps. Configurez la [grille et plan de travail](Draft_SelectPlane/fr.md), le [texte](Draft_Text/fr.md) et les paramètres de [dimension](Draft_Dimension/fr.md) à votre convenance dans le menu **Édition → Préférences → Draft**. Dans cet exercice, cependant, nous agirons comme si ces paramètres de préférences étaient laissés à leurs valeurs par défaut.

![](images/Freecad_draft_options_01.jpg )

Une option peut nécessiter votre attention, difficile   * l'option \"**Remplir les objets avec des surfaces chaque fois que possible**\". Si cette option est marquée, les objets fermés tels que les rectangles ou les cercles seront remplis avec une surface par défaut, ce qui peut rendre difficile l\'accrochage aux objets sous-jacents. Vous pouvez désactiver cette option maintenant ou ultérieurement pour désactiver la propriété \"**Créer une face**\" de chaque objet afin de les empêcher de créer une face.

-   L'atelier Draft a également deux barres d\'outils spéciales    * L\'une avec les **paramètres visuels**, où vous pouvez changer le plan de travail en cours, activer/désactiver le [mode de construction](Draft_ToggleConstructionMode/fr.md), définir la couleur de la ligne, la couleur de la face, le poids de la ligne et la taille du texte à utiliser pour les nouveaux objets, et une autre avec les **emplacements d\'aimantation**. Là, vous pouvez activer/désactiver la grille et définir/désactiver des [emplacements d\'aimantation](Draft_Snap.md) individuels    *

![](images/Draft_toolbars.jpg )

L\'activation de tous les boutons d\'accrochage est pratique, mais ralentit également le dessin, car il faut effectuer davantage de calculs lorsque vous déplacez le curseur de la souris. Il est souvent préférable de ne garder que ceux que vous utiliserez réellement.

-   Commençons par passer en **mode construction**, ce qui nous permettra de dessiner des lignes directrices sur lesquelles nous allons dessiner notre géométrie finale.
-   Si vous le souhaitez, mettez le **plan de travail** sur **XY**. Si vous faites cela, le plan de travail ne changera pas, peu importe la vue actuelle. Si ce n\'est pas le cas, le plan de travail s\'adapte automatiquement à la vue actuelle, et vous devriez prendre soin de rester en vue de dessus lorsque vous souhaitez dessiner sur le plan XY (sol).
-   Ensuite, sélectionnez l\'outil <img alt="" src=images/Draft_Rectangle.svg  style="width   *16px;"> [Rectangle](Draft_Rectangle/fr.md) et tracez un rectangle, en commençant par le point (0,0,0), de 2 mètres par 2 mètres (laissez Z à zéro). Notez que la plupart des commandes Draft peuvent être entièrement exécutées à partir du clavier, sans toucher la souris, en utilisant leur raccourci à deux lettres. Notre premier rectangle 2x2m peut se faire comme ceci    * re 0 **Entrée** 0 Entrée 0 **Entrée** 2m **Entrée** 2m **Entrée** 0 **Entrée**.
-   Dupliquez ce rectangle de 15 cm à l\'intérieur, en utilisant l\'outil Décalage <img alt="" src=images/Draft_Offset.svg  style="width   *16px;"> [Décalage](Draft_Offset/fr.md), en activant son mode Copie et en lui donnant une distance de 15 cm    *

![](images/Exercise_cabin_02.jpg )

-   Nous pouvons ensuite dessiner quelques lignes verticales pour définir où nos portes et fenêtres seront placées, en utilisant l\'outil <img alt="" src=images/Draft_Line.svg  style="width   *16px;"> [Ligne](Draft_Line/fr.md) (notez que la case du mode \"relatif\" doit être décochée pour cette étape). L'intersection de ces lignes avec nos deux rectangles nous donnera des intersections utiles pour enrayer nos murs. Dessinez la première ligne du point (15cm, 1m, 0) au point (15cm, 3m, 0).
-   Dupliquez cette ligne 5 fois, en utilisant l\'outil <img alt="" src=images/Draft_Move.svg  style="width   *16px;"> [Déplacer](Draft_Move/fr.md) avec le mode Copy activé. Activez également le mode relatif, ce qui nous permettra de définir des déplacements selon des distances relatives, ce qui correspond à la position exacte de chaque ligne. Effectuer chaque opération de déplacement en série sur la ligne qui a été créée immédiatement avant. Donnez à chaque nouvelle copie un point de départ, vous pouvez le laisser à (0,0,0) par exemple, et les points finaux relatifs suivants    *
    -   line001   * x   * 10cm
    -   line002   * x   * 120cm
    -   line003   * x   * -55cm, y   * -2m
    -   line004   * x   * 80cm
    -   line005   * x   * 15cm

![](images/Exercise_cabin_03.jpg )

-   C\'est tout ce dont nous avons besoin maintenant, nous pouvons donc désactiver le mode de construction. Vérifiez que toute la géométrie de la construction a été placée dans un groupe \"Construction\", ce qui permet de le masquer tout à la fois ou même de le supprimer complètement plus tard.
-   Maintenant, dessinons nos deux morceaux de mur en utilisant l\'outil <img alt="" src=images/Draft_Wire.svg  style="width   *16px;"> [Polyligne](Draft_Wire/fr.md). Assurez-vous que l\'outil <img alt="" src=images/Draft_Snap_Intersection.svg  style="width   *16px;"> [Aimantation d\'intersection](Draft_Snap/fr.md) est activé, car nous aurons besoin de nous aimanter aux intersections de nos lignes et rectangles. Dessinez deux fils comme suit, en cliquant sur tous les points de leurs contours. Pour les fermer, cliquez à nouveau sur le premier point, ou appuyez sur le bouton *Fermer*    *

![](images/Exercise_cabin_04.jpg )

Nous pouvons changer leur couleur grise par défaut en un motif de hachures, en sélectionnant les deux murs, et en définissant leur propriété **Motif** à **Simple**, et leur **taille** à votre goût, par exemple **0,005**.

![](images/Exercise_cabin_05.jpg )

-   Nous pouvons maintenant cacher la géométrie de construction en cliquant avec le bouton droit sur le groupe Construction et en choisissant **Masquer la sélection**.
-   Dessinons maintenant les fenêtres et les portes. Assurez-vous que le filtre d'accrochage <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width   *16px;"> [Point Milieu](Draft_Snap/fr.md) est activé et tracez six lignes comme suit    *

![](images/Exercise_cabin_06.jpg )

-   Nous allons maintenant changer la ligne de porte pour créer un symbole de porte ouvert. Commencez par faire tourner la ligne à l\'aide de l\'outil <img alt="" src=images/Draft_Rotate.svg  style="width   *16px;"> [Rotation](Draft_Rotate/fr.md). Cliquez sur l\'extrémité de la ligne en tant que centre de rotation, lui donner un angle de départ de **0** et un angle d\'extrémité de **-90**.
-   Ensuite, créez l\'arc d\'ouverture avec l\'outil <img alt="" src=images/Draft_Arc.svg  style="width   *16px;"> [Arc](Draft_Arc/fr.md). Choisissez le même point que le centre de rotation que nous avons utilisé dans l\'étape précédente comme centre, cliquez sur l\'autre point de la ligne pour donner le rayon, puis les points de début et de fin comme suit    *

![](images/Exercise_cabin_07.jpg )

-   Nous pouvons maintenant placer des meubles. Pour commencer, placez un compteur en dessinant un rectangle du coin supérieur gauche et en lui donnant une largeur de 170cm et une hauteur de -60cm. Dans l\'image ci-dessous, la propriété **Transparence** du rectangle est configurée à 80%, pour lui donner un bon aspect des meubles.
-   Ensuite, ajoutons un lavabo et une table de cuisson. Dessiner ces types de symboles à la main peut être très fastidieux, et ils sont généralement faciles à trouver sur Internet, par exemple sur <http   *//www.cad-blocks.net>. Dans la section **Téléchargements** ci-dessous, pour plus de commodité, nous avons récupéré un évier et une table de cuisson sur ce site et les avons sauvegardés en tant que fichiers DXF. Vous pouvez télécharger ces deux fichiers en visitant les liens ci-dessous et en cliquant avec le bouton droit sur le bouton **Raw**, puis en sélectionnant **Enregistrer sous**.
-   L\'insertion d\'un fichier DXF dans un document FreeCAD ouvert peut être effectuée soit en choisissant l\'option du menu **Fichier → Importer**, soit en faisant glisser et déposer le fichier DXF depuis votre explorateur de fichiers dans la fenêtre FreeCAD. Le contenu des fichiers DXF peut ne pas apparaître directement au centre de votre vue actuelle, selon l\'endroit où ils se trouvaient dans le fichier DXF. Vous pouvez utiliser le menu **Affichage → Affichage standard → Afficher tout** pour faire un zoom arrière et trouver les objets importés. Insérez les deux fichiers DXF et déplacez-les à un emplacement approprié sur le dessus de la table    *

![](images/Exercise_cabin_08.jpg )

-   Nous pouvons maintenant placer quelques dimensions à l\'aide de l\'outil <img alt="" src=images/Draft_Dimension.svg  style="width   *16px;"> [Dimension](Draft_Dimension/fr.md). Les dimensions sont dessinées en cliquant sur 3 points   * le point de départ, un point final et un troisième point pour placer la ligne de cote. Pour obtenir des dimensions horizontales ou verticales, même si les deux premiers points ne sont pas alignés, appuyez sur Maj lorsque vous cliquez sur le deuxième point.
-   Vous pouvez modifier la position d\'un texte de cote en double-cliquant sur la dimension dans l\'arborescence. Un point de contrôle vous permettra de déplacer le texte graphiquement. Dans notre exercice, les textes \"0.15\" ont été déplacés pour une meilleure clarté.
-   Vous pouvez modifier le contenu du texte de cote en éditant leur propriété **Override**. Dans notre exemple, les textes des dimensions des portes et des fenêtres ont été édités pour indiquer leurs hauteurs    *

![](images/Exercise_cabin_09.jpg )

-   Ajoutons des textes de description à l\'aide de l\'outil <img alt="" src=images/Draft_Text.svg  style="width   *16px;"> [Texte](Draft_Text/fr.md). Cliquez sur un point pour positionner le texte, puis entrez les lignes de texte, en appuyant sur Entrée après chaque ligne. Pour terminer, appuyez deux fois sur Entrée.
-   Les lignes de repère (également appelées «leaders») qui relient les textes à l\'élément qu\'ils décrivent se font simplement avec l\'outil Polyligne. Dessinez les polylignes, à partir de la position du texte, jusqu'à l\'endroit décrit. Une fois que cela est fait, vous pouvez ajouter une bille ou une flèche à la fin des fils en définissant leur propriété **End Arrow** (extrémité de la flèche) sur **`True`**.

![](images/Exercise_cabin_10.jpg )

Notre dessin est maintenant terminé ! Puisqu\'il commence à y avoir un certain nombre d\'objets, il serait judicieux de faire du nettoyage et de placer tout dans une belle structure de groupes, pour rendre le fichier plus facile à comprendre à une autre personne    *

![](images/Exercise_cabin_11.jpg )

-   Nous pouvons maintenant imprimer notre travail en le plaçant sur une feuille de dessin, que nous allons montrer plus loin dans ce manuel, ou exporter directement notre dessin vers d\'autres applications de CAO en l\'exportant vers un fichier DXF. Il suffit de sélectionner notre groupe \"Floor Plan\", sélectionnez le menu **Fichier → Exporter**, et sélectionnez le format Autodesk DXF. Le fichier peut alors être ouvert dans n\'importe quelle autre application CAO 2D telle que [LibreCAD](http   *//www.librecad.org). Vous pouvez remarquer quelques différences selon les configurations de chaque application.

![](images/Exercise_cabin_12.jpg )

-   La chose la plus importante à propos de l'atelier Draft, c\'est que la géométrie que vous créez avec lui peut être utilisée comme base ou extrudée facilement dans des objets 3D, simplement en utilisant l\'outil Extrusion <img alt="" src=images/Part_Extrude.svg  style="width   *16px;"> [Part Extrusion](Part_Extrude/fr.md) de l'[atelier Part](Part_Workbench/fr.md) ou, pour rester dans Draft, l\'outil <img alt="" src=images/Draft_Trimex.svg  style="width   *16px;"> [Ajuster ou prolonger](Draft_Trimex/fr.md), qui sous le capot, exécute une extrusion de pièce, mais le fait \"à la manière de Draft\", c\'est-à-dire qu\'il vous permet d\'indiquer et de fixer graphiquement la longueur d\'extrusion. Essayez l\'extrusion de nos murs comme indiqué ci-dessous.
-   En appuyant sur le bouton Sélectionner le <img alt="" src=images/Draft_SelectPlane.svg  style="width   *16px;"> [plan de travail](Draft_SelectPlane/fr.md) après avoir sélectionné une face d\'un objet, vous pouvez également placer le plan de travail n\'importe où et, par conséquent, dessiner des objets Draft dans différents plans, par exemple sur le dessus des murs. Ceux-ci peuvent ensuite être extrudés pour former d\'autres solides 3D. Expérimentez le réglage du plan de travail sur l\'une des faces supérieures des murs, puis tracez des rectangles là-haut.

![](images/Exercise_cabin_13.jpg )

-   Toutes sortes d\'ouvertures peuvent également être faites aussi facilement en dessinant des objets Draft sur les faces des murs, puis en les extrudant, puis en utilisant les outils booléens de l'atelier Part pour les soustraire d\'un autre solide, comme nous l\'avons vu dans le chapitre précédent.

Fondamentalement, ce que fait l'atelier Draft, c\'est fournir des moyens graphiques pour créer des opérations partielles de base. Pendant que dans Part, vous positionnez généralement les objets en définissant leur propriété de placement à la main, dans Draft vous pouvez le faire à l\'écran. Il y a des moments où c'est mieux, d\'autres fois où l\'autre est préférable. N\'oubliez pas, vous pouvez créer des [outils personnalisés](Interface_Customization/fr.md) dans un de ces ateliers, ajouter les outils de l\'autre et obtenir le meilleur des deux mondes.

## Téléchargements

-   Le fichier créé lors de cet exercice   * <https   *//github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/cabin.FCStd>
-   Le fichier DXF de l\'évier   * <https   *//github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/sink.dxf>
-   Le fichier DXF de la table de cuisson   * <https   *//github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/cooktop.dxf>
-   Le fichier final DXF produit lors de cet exercice   * <Https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>

## En relation 

-   [L'atelier Draft](Draft_Workbench/fr.md)
-   [Draft Aimantation](Draft_Snap/fr.md)
-   [Draft Le plan de travail](Draft_SelectPlane/fr.md)




[Category   *Tutorials](Category_Tutorials.md) [Category   *Draft](Category_Draft.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/fr
