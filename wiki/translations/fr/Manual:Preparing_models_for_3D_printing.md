# Manual:Preparing models for 3D printing/fr







{{Manual:TOC/fr}}

L\'une des principales utilisations de FreeCAD est de produire des objets du monde réel. Ceux-ci peuvent être conçus dans FreeCAD puis fabriqués de différentes façons, par exemple transmis aux personnes qui les fabriqueront ou de plus en plus souvent envoyés directement à une imprimante 3D ([3D printer](https://en.wikipedia.org/wiki/3D_printing)) ou à une CNC ([CNC mill](https://en.wikipedia.org/wiki/Milling_%28machining%29)). Ce chapitre vous montrera comment préparer vos modèles à envoyer à ces machines.

Si vous avez été précautionneux lors de la modélisation, la plupart des difficultés que vous pourriez rencontrer lors de l\'impression de votre modèle en 3D a déjà été évitée. Cela implique essentiellement :

-   de vérifier que vos objets 3D sont des **solides**. Les objets du monde réel sont des solides, le modèle 3D doit aussi être un solide. Nous avons vu dans des chapitres précédents que FreeCAD vous aide beaucoup dans ce sens et que l'atelier Part Design ([PartDesign Workbench](PartDesign_Workbench.md)) vous informera si vous faites une opération qui empêche votre modèle de rester un solide. L'atelier Part ([Part Workbench](Part_Workbench/fr.md)) contient également un outil de vérification de la géométrie (<img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Check Geometry](Part_CheckGeometry/fr.md)) pour vérifier les défauts éventuels.
-   de vérifier les **dimensions** de vos objets. Un millimètre sur le modèle sera un millimètre dans la vie réelle. Toute dimension a son importance.
-   de contrôler la **dégradation**. Aucune imprimante 3D ou système de fraisage CNC ne peut utiliser directement les fichiers FreeCAD. La plupart d\'entre eux ne comprennent qu\'un langage machine appelé [G-Code](https://en.wikipedia.org/wiki/G-code). G-code a des dizaines de variantes différentes. Chaque machine ou fournisseur utilise généralement son propre G-code. La conversion de vos modèles en G-code peut être simple et automatique mais vous pouvez le faire également manuellement avec un contrôle total sur la sortie. En tout cas, une certaine perte de qualité de votre modèle se produira inévitablement pendant le processus. Lors de l\'impression en 3D, vous devez toujours vous assurer que cette perte de qualité reste inférieure à vos exigences minimales.

Ci-dessous, nous supposerons que les deux premiers critères sont respectés, et que maintenant, vous êtes en mesure de produire des objets solides avec des dimensions correctes. Nous allons maintenant voir comment traiter le troisième point.

### Exportation vers des trancheuses 

C\'est la technique la plus utilisée pour l\'impression en 3D. L\'objet 3D est exporté vers un autre programme (la trancheuse) qui générera le G-code à partir de l\'objet en le découpant en couches minces (d\'où le nom)et qui définira les mouvements que l\'imprimante 3D fera. Pas mal de ces imprimantes sont des faites maison et par conséquent il y a souvent de petites différences de l\'une à l\'autre. Les programmes offrent généralement des possibilités de configuration avancée qui permettent d'adapter exactement la sortie aux particularités de votre imprimante 3D.

L\'impression 3D réelle, cependant, est un sujet trop vaste pour ce manuel. Mais nous verrons comment exporter et utiliser ces trancheuses pour vérifier que la sortie est correcte.

### Conversion d\'objets en mailles 

Aucune des trancheuses, à cette date, ne prend directement la géométrie solide que nous produisons dans FreeCAD. Nous devons donc convertir l\'objet que nous souhaitons imprimer en 3D en un premier [maillage](https://en.wikipedia.org/wiki/Polygon_mesh) que le trancheur peut ouvrir. Heureusement, autant convertir un maillage en un solide est une opération compliquée, autant la conversion d\'un solide en maillage est très simple. Le point important, c\'est à ce moment que la dégradation mentionnée au-dessus se produira. Nous devons vérifier que la dégradation reste dans des limites acceptables.

Toute la gestion du maillage dans FreeCAD est effectuée par un atelier spécifique: l'([atelier Mesh](Mesh_Workbench/fr.md)). Cet atelier contient, outre les outils importants pour convertir les objets Part et Mesh, plusieurs utilitaires destinés à analyser et à réparer les maillages. Bien que travailler avec des maillages ne soit pas le point fort de FreeCAD, la modélisation 3D nécessite souvent de traiter des objets maillés car leur utilisation est très répandue parmi les autres applications. Cet atelier vous permet de les gérer entièrement dans FreeCAD.

Convertissons un des objets que nous avons modelés dans les chapitres précédents, comme la pièce de lego (qui peut être téléchargée à partir de la fin du chapitre précédent):

-   Ouvrez le fichier FreeCAD contenant la pièce Lego.
-   Passez à l'([atelier Mesh](Mesh_Workbench/fr.md)).
-   Sélectionnez la brique lego.
-   Sélectionnez le menu **Maillages → Créer un maillage à partir de la forme**.
-   Un panneau de tâches s\'ouvre avec plusieurs options. Quelques algorithmes de maillage supplémentaires (Mefisto ou Netgen) pourraient ne pas être disponibles, selon la manière dont votre version de FreeCAD a été compilée. L\'algorithme de maillage standard sera toujours présent. Il offre moins de possibilités que les deux autres, mais est totalement suffisant pour les objets plus petits que la taille d\'impression maximale d\'une imprimante 3D.

![](images/Exercise_meshing_01.jpg )

-   Sélectionnez le maillage **standard** et laissez la valeur d\'écart à la valeur par défaut de **0,10**. Appuyez sur **OK**.
-   Un objet maillage sera créé, exactement par dessus notre objet solide. Pour comparer les deux vous pouvez soit cacher le solide, soit déplacer l\'un des objets par rapport à l'autre.
-   Modifiez la propriété **Vue → Display option** du nouvel objet maillage en **Flat Lines** afin de voir comment s\'est déroulée la triangulation.
-   Si vous n\'êtes pas satisfait et pensez que le résultat est trop grossier, vous pouvez répéter l'opération, en abaissant la valeur d\'écart. Dans l\'exemple ci-dessous, le maillage gauche a utilisé la valeur par défaut de **0,10**, tandis que celui de droite utilise **0,01** :

![](images/Exercise_meshing_02.jpg )

Dans la plupart des cas, les valeurs par défaut donneront un résultat satisfaisant.

-   Nous pouvons maintenant exporter notre maillage à un format de maillage, par exemple [STL](https://fr.wikipedia.org/wiki/Fichier_de_st%C3%A9r%C3%A9olithographie), actuellement le format le plus utilisé dans l\'impression 3D, en utilisant le menu **Fichier → Exporter** et choisir le format de fichier STL.

Si vous ne possédez pas d\'imprimante 3D, il est généralement très facile de trouver des services commerciaux qui vont imprimer et vous envoyer les objets imprimés par courrier. Parmi les plus célèbres, on trouve [Shapeways](http://www.shapeways.com/) et [Sculpteo](http://www.sculpteo.com/), mais vous en trouverez généralement beaucoup d\'autres dans votre propre ville. Dans toutes les grandes villes, vous trouverez également aujourd\'hui des [Fab labs](https://en.wikipedia.org/wiki/Fab_lab), qui sont des laboratoires ou ateliers équipés d\'une gamme de machines de fabrication 3D, incluant presque toujours au moins une imprimante 3D. Les FabLabs sont habituellement des espaces communautaires, qui vous permettront d\'utiliser leurs machines, moyennant des frais ou gratuitement selon le FabLab, mais aussi vous apprendre à les utiliser et à promouvoir d\'autres activités autour de la fabrication 3D.

### Utilisation de Slic3r 

[Slic3r](http://slic3r.org/) est une application qui convertit des objets STL en G-code pouvant être envoyé directement vers les imprimantes 3D. Comme FreeCAD, il est gratuit, open-source et s\'exécute sous Windows, Mac OS et Linux. La configuration correcte des paramètres pour l\'impression 3D est un processus compliqué, où vous devez avoir une bonne connaissance de votre imprimante 3D ; il n\'est donc pas très utile de générer du G-code avant de pouvoir effectivement imprimer (votre fichier de G-code peut ne pas fonctionner correctement sur une autre imprimante), mais c\'est utile pour nous de toute façon, pour vérifier que notre fichier STL sera imprimable sans problème.

Ceci est notre fichier STL exporté ouvert dans Slic3r. En utilisant l\'onglet **Aperçu**, et en déplaçant le curseur droit, nous pouvons visualiser le chemin que la tête d\'imprimante 3D suivra pour construire notre objet.

![](images/Exercise_meshing_03.jpg )

### Utilisation du greffon (addon) Cura 

[Cura](https://ultimaker.com/en/products/cura-software) est une autre application Slicer gratuite et open-source pour Windows, Mac et Linux, maintenue par le fabricant d\'imprimantes 3D [Ultimaker](https://ultimaker.com). Certains utilisateurs de FreeCAD ont créé un atelier Cura ([Cura Workbench](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)) qui utilise Cura en interne. L'atelier Cura est disponible dans le dépôt [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons). Pour l\'utiliser, vous devez également installer le logiciel Cura qui n'est pas inclus dans l\'atelier.

Une fois que vous avez installé Cura et l\'atelier Cura, vous pourrez l\'utiliser pour produire le fichier G-code directement à partir des objets Part, sans avoir besoin de les convertir en maillages et sans avoir besoin d\'ouvrir une application externe. Produire un autre G-code à partir du fichier de notre brique Lego, en utilisant l'atelier Cura cette fois, se déroule comme suit :

-   Chargez le fichier contenant notre brique Lego (il peut être téléchargé à la fin du chapitre précédent)
-   Allez dans l'[atelier Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin).
-   Configurez l\'espace de l\'imprimante en choisissant le menu **Impression 3D → Définir une imprimante 3D**. Comme nous n\'allons pas imprimer de façon réelle, nous pouvons laisser les paramètres tels qu\'ils sont. La géométrie du lit d\'impression et l\'espace disponible seront affichés dans la vue 3D.
-   Déplacez la brique Lego à un endroit approprié, comme le centre du lit d\'impression. N\'oubliez pas que les objets PartDesign ne peuvent pas être déplacés directement, donc vous devez soit déplacer sa toute première esquisse (le premier rectangle), ou déplacer (et créer) une copie, qui peut être faite avec l\'outil [Part -\> Créer copie simple](Part_SimpleCopy.md). La copie peut être déplacée, par exemple avec l'outil <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Déplacer](Draft_Move/fr.md).
-   Sélectionnez l\'objet à imprimer et sélectionnez dans le menu **Impression 3D → Trancher avec le moteur Cura**.
-   Dans le panneau de tâches qui s\'ouvre, assurez-vous que le chemin d\'accès à l\'exécutable Cura est correctement défini. Comme nous n\'allons pas vraiment imprimer, nous pouvons laisser toutes les autres options telles qu\'elles sont. Appuyez sur **OK**. Deux fichiers seront générés dans le même répertoire que votre fichier FreeCAD, un fichier STL et un fichier G-code.

![](images/Exercise_meshing_05.jpg )

-   Le G-code généré peut également être réimporté dans FreeCAD (en utilisant le préprocesseur slic3r) pour vérification.

### Génération du G-code 


{{VeryImportantMessage|'''Attention:''' cette section est destinée à FreeCAD 0.16. Des modifications importantes ont été apportées au chemin de création. Reportez-vous à la documentation du [ Path workbench](Path_Workbench_.md) en général ou au tutoriel [L'atelier Path pas à pas pour l'impatient](Path_Walkthrough_for_the_Impatient/fr.md)!}}

FreeCAD offre également des moyens plus avancés pour générer directement le G-code. C\'est souvent beaucoup plus compliqué que l\'utilisation d\'outils automatiques comme nous l\'avons vu ci-dessus, mais a l\'avantage de vous laisser contrôler pleinement la sortie. Ceci n\'est généralement pas nécessaire lors de l\'utilisation d\'imprimantes 3D, mais devient très important lors de la gestion du fraisage CNC, car les machines sont beaucoup plus complexes.

La génération des parcours d'outils en G-code dans FreeCAD se fait avec l'atelier Path ([Path Workbench](Path_Workbench.md)). Il comporte des outils qui génèrent des chemins d\'outils complets et d\'autres qui ne génèrent que des parties d\'un projet G-code qui peuvent ensuite être assemblés pour former une opération de fraisage complète.

La génération de parcours de fraisage CNC est un autre sujet qui est trop vaste pour être adapté à ce manuel, nous allons donc montrer comment construire un projet de cheminement simple, sans se soucier de la plupart des détails de l\'usinage CNC réel.

-   Chargez le fichier contenant notre pièce de lego, et passez à l'([atelier Path](Path_Workbench/fr.md)).
-   Puisque la pièce finale ne contient plus une face supérieure rectangulaire, cachez la dernière étape de la pièce de lego, et montrez le premier bloc parallélipipédique que nous avons fait, qui a une face supérieure rectangulaire.
-   Sélectionnez la face supérieure et appuyez sur le bouton <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Profilage](Path_Profile/fr.md).
-   Définissez sa propriété **Offset** (décalage) à 1mm, ce qui correspond au rayon de la fraise.

![](images/Exercise_path_01.jpg )

-   Ensuite, dupliquons cette première boucle à plusieurs reprises, de sorte que l\'outil découpera le bloc tout entier. Sélectionnez le contour Profilage et appuyez sur le bouton <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Réseau](Path_Array/fr.md).
-   Réglez la propriété **Copies** du réseau linéaire sur 8, et son **Décalage** (Offset) à -2 mm dans la direction Z (profondeur de passe), et déplacez la position du réseau linéaire de 2 mm dans la direction Z, de sorte que la coupe commencera un peu au dessus du bloc, et inclura aussi la hauteur des bossages.

![](images/Exercise_path_02.jpg )

-   Maintenant, nous avons défini un parcours d'usinage qui, après exécution par la fraiseuse, va contourner un volume rectangulaire sur un bloc de matériau. Nous devons maintenant réaliser l\'espace entre les bossages, afin de les révéler. Cachez le bloc, et montrez à nouveau la pièce finale, afin que nous puissions choisir la face qui se trouve entre les bossages.
-   Sélectionnez la face supérieure et appuyez sur le bouton <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Poche](Path_Pocket_Shape/fr.md). Définissez la propriété **Décalage** (Offset) à 1mm (toujours le rayon de la fraise), et la **hauteur de dégagement d'outil** (retraction height) à 20mm. C\'est la hauteur de l\'endroit où l'outil se déplace lorsque vous passez d\'une boucle du parcours à l\'autre. Sinon, la fraise pourrait couper tout droit à travers un de nos bossages :

![](images/Exercise_path_03.jpg )

-   Encore une fois, créez un tableau de copie. Sélectionnez l\'objet Poche et appuyez sur le bouton Copie réseau (<img alt="" src=images/Path_Array.svg  style="width:16px;"> [Réseau](Path_Array/fr.md)). Réglez le **nombre de copies** sur 1 et le **décalage** à -2 mm dans la direction Z. Déplacez la position du réseau (pas de la copie) à 2 mm dans la direction Z. Nos deux opérations sont maintenant terminées :

![](images/Exercise_path_04.jpg )

-   Il ne reste plus qu\'à réunir ces deux opérations en une seule. Cela peut être fait avec une [Path Tâche](Path_Job/fr.md). Appuyez sur le bouton <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Tâche](Path_Job/fr.md).
-   Définir la propriété **Use Placements** du projet à True car nous avons changé le placement des réseaux et nous voulons que cela soit pris en compte dans le projet.
-   Dans l\'arborescence, faites glisser et déposez les deux réseaux dans le projet. Vous pouvez réorganiser des réseaux à l\'intérieur du projet si nécessaire, en double-cliquant dessus.
-   Le projet peut maintenant être exporté en G-code, en le sélectionnant, en choisissant le menu **Fichier → Exporter**, en sélectionnant le format G-code et dans la boîte de dialogue contextuelle qui s\'ouvrira en sélectionnant un post processeur adapté à votre machine.

Il existe de nombreuses applications disponibles pour simuler l'usinage réel, l\'une d\'entre elles étant également multi-plate-forme et open-source, comme FreeCAD, est [Camotics](http://camotics.org/).

**Téléchargements**

-   Le fichier STL généré dans cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/lego.stl>
-   Le fichier généré lors de cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/path.FCStd>
-   Le fichier G-code généré dans cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/lego.gcode>

**Lire plus d\'informations**

-   [L'atelier Mesh](Mesh_Workbench/fr.md)
-   [Le format de fichier STL](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [L'atelier Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [L'atelier Path](Path_Workbench/fr.md)
-   [Camotics](http://camotics.org/)

### Vidéos

-   [Comment utiliser FreeCAD pour l\'impression 3D \| Utilisation de la branche Realthunder](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) Une playlist de vidéos par Maker Tales sur la façon d\'utiliser FreeCAD pour l\'impression 3D.




[Category:Path](Category:Path.md) [Category:Mesh](Category:Mesh.md) [Category:Tutorials](Category:Tutorials.md)
