# Manual:Creating renderings/fr
{{Manual:TOC/fr}}

Dans le langage des ordinateurs, un rendu ([rendering](https://en.wikipedia.org/wiki/Rendering_%28computer_graphics%29)) est un mot utilisé pour décrire une belle image produite à partir d\'un modèle 3D. Bien sûr, nous pourrions dire que ce que vous voyez dans la vue 3D FreeCAD est déjà sympa. Mais quiconque a vu un film récent de Hollywood sait qu\'il est possible de produire des images avec un ordinateur qui ne se distinguent guère d\'une photographie.

Bien sûr, produire de telles images photo-réalistes nécessite beaucoup de travail et une application 3D qui offre des outils spécifiques à cela, tels que des contrôles précis pour les matériaux et l\'éclairage. FreeCAD étant une application plus orientée vers la modélisation technique, elle ne présente pas d'outil de rendu avancé.

Heureusement, le monde open-source offre de nombreuses applications pour produire des images réalistes. Probablement le plus célèbre est [Blender](http://www.blender.org), qui est très populaire et largement utilisé dans les industries du cinéma et du jeu. Les modèles 3D peuvent très facilement et fidèlement être exportés de FreeCAD et importés dans Blender où vous pouvez ajouter des matériaux et des éclairages réalistes et produire des images ou même des animations.

Certains autres outils de rendu open source sont conçus pour être utilisés dans d\'autres applications et prendront soin d\'éxécuter des calculs complexes pour produire des images réalistes. À travers son [atelier Raytracing](Raytracing_Workbench/fr.md), FreeCAD peut utiliser deux de ces outils de rendu : [POV-Ray](https://fr.wikipedia.org/wiki/POV-Ray) et [LuxRender](https://fr.wikipedia.org/wiki/LuxRender). POV-Ray est un projet très ancien et est considéré comme un moteur classique de [Ray tracing](https://fr.wikipedia.org/wiki/Ray_tracing), tandis que LuxRender est beaucoup plus récent et est catégorisé comme un moteur de rendu impartial ([Unbiased rendering](https://en.wikipedia.org/wiki/Unbiased_rendering)). Les deux ont leurs points forts et leurs faiblesses selon le type d\'image que l\'on veut créer. La meilleure façon de le savoir est de regarder des exemples sur les deux sites Web des moteurs de rendu.

### Installation

Avant d\'être en mesure d\'utiliser l\'un de ces deux rendus dans l'atelier Raytracing dans FreeCAD, les applications doivent être installées sur votre système. C\'est généralement très simple. Les deux installateurs sont fournis pour de nombreuses plates-formes ou sont généralement inclus dans les dépôts de la plupart des distributions Linux.

Une fois que POV-Ray ou LuxRender est installé, nous devons définir le chemin d\'accès à son exécutable principal dans les préférences de FreeCAD. Cela n\'est généralement nécessaire que sur Windows et Mac. Sur Linux, FreeCAD va le choisir parmi les emplacements standard. L\'emplacement des exécutables de Povray ou LuxRender peut être trouvé en recherchant simplement dans votre système les fichiers appelés Povray (ou Povray.exe sur Windows) et LuxRender (ou Luxrender.exe sur Windows).

![](images/Exercise_raytracing_01.jpg )

Dans cet écran de préférences, nous pouvons également définir la taille de l\'image que nous voulons produire.

### Rendu avec PovRay 

Nous allons utiliser la table que nous avons modélisée dans le chapitre sur la [Modélisation traditionnelle](Manual:Traditional_modeling,_the_CSG_way/fr.md) pour produire des rendus avec PovRay et LuxRender.

-   Commencez par charger le fichier table.FCStd que nous avons modélisé plus tôt ou à partir du lien au bas de ce chapitre.
-   Appuyez sur la petite flèche vers le bas à côté du bouton <img alt="" src=images/Raytrace_New.svg  style="width:16px;"> [Nouveau projet Povray](Raytracing_New/fr.md), et choisissez le modèle **RadiosityNormal**.
-   Un message d\'avertissement peut apparaître indiquant que la vue en 3D actuelle n\'est pas dans le mode perspective et le rendu sera donc différent. Corrigez ceci en choisissant **Non**, en allant dans le menu **Affichage-\> Vue en perspective** et en choisissant à nouveau le modèle **RadiosityNormal**.
-   Vous pouvez également essayer d\'autres modèles après avoir créé un nouveau projet, simplement en éditant les **Propriétés** du modèle.
-   Un nouveau projet a été créé :

![](images/Exercise_raytracing_02.jpg )

-   Le nouveau projet a adopté le point de vue de la vue 3D comme il l\'était au moment où nous avons appuyé sur le bouton. Nous pouvons modifier la vue et mettre à jour la position de vue enregistrée dans le projet Povray à tout moment en appuyant sur le bouton <img alt="" src=images/Raytrace_ResetCamera.svg  style="width:16px;"> [Réinitialiser la caméra](Raytracing_ResetCamera/fr.md).
-   L'atelier Raytracing fonctionne de la même manière que l'[Atelier Drawing](Drawing_Workbench/fr.md) : une fois que le dossier de projet est créé, nous devons ajouter des **vues** de nos objets. Nous pouvons le faire en sélectionnant tous les objets qui composent la table en appuyant sur le bouton <img alt="" src=images/Raytrace_ResetCamera.svg  style="width:16px;"> [Insérer une pièce](Raytracing_InsertPart/fr.md):

![](images/Exercise_raytracing_03.jpg )

-   Les vues ont pris les valeurs de couleur et de transparence à partir de leurs pièces d\'origine mais vous pouvez modifier cela dans les propriétés de chaque vue individuellement si vous le souhaitez.
-   Nous sommes maintenant prêts à produire notre premier rendu avec Povray. Appuyez sur le bouton <img alt="" src=images/Raytrace_Render.svg  style="width:16px;"> [Rendu](Raytracing_Render/fr.md).
-   Remarque pour les utilisateurs de Windows: dans Povray, lors de l\'avertissement indiquant que \"les restrictions d\'E / S interdisent l\'accès en écriture \...\"
    -   Ouvrez Povray.
    -   Choisissez \"Options\> Restrictions E / S du script\" et assurez-vous qu\'il est défini sur \"Aucune restriction\"
    -   Relancez le rendu.
-   Vous devrez donner un nom de fichier et un chemin d\'accès pour l\'image .png qui sera enregistrée par Povray.
-   L\'application Povray se lancera et calculera alors l\'image.
-   Lorsque cela sera fait, cliquez simplement sur l\'image pour fermer la fenêtre de Povray. L\'image résulatnate sera chargée dans FreeCAD :

![](images/Exercise_raytracing_04.jpg )

### Rendu avec LuxRender 

-   Le rendu avec LuxRender fonctionne presque de la même manière. Nous pouvons laisser notre dossier ouvert et créer un nouveau projet Luxrender dans le même fichier ou le recharger pour démarrer à partir de zéro.
-   Appuyez sur la petite flèche vers le bas à côté du bouton <img alt="" src=images/Raytrace_Lux.svg  style="width:16px;"> [New Luxrender project](Raytracing_Lux/fr.md) et choisissez le modèle **LuxOutdoor**.
-   Sélectionnez tous les composants de la table. Si vous avez toujours le projet Povray dans votre document, assurez-vous également de sélectionner le projet LuxRender lui-même de sorte que les vues créées dans la prochaine étape n\'aillent pas dans le mauvais projet par erreur.
-   Appuyez sur le bouton <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width:16px;"> [Insérer une pièce](Raytracing_InsertPart/fr.md).
-   Sélectionnez le projet LuxRender et appuyez sur le bouton <img alt="" src=images/Raytrace_Render.svg  style="width:16px;"> [Rendu](Raytracing_Render/fr.md).
-   LuxRender fonctionne différemment de Povray. Lorsque vous démarrez le rendu, l\'application LuxRender s\'ouvre et commence immédiatement le calcul du rendu :

![](images/Exercise_raytracing_05.jpg )

-   Si vous quittez la fenêtre ouverte, LuxRender continuera à calculer et à donner le rendu définitif en affinant progressivement l\'image. C\'est à vous de décider quand l\'image aura atteint une qualité suffisante pour vos besoins et d'arrêter le calcul du rendu.
-   Il existe également de nombreux contrôles à tester/régler sur le panneau de gauche. Tous ces contrôles modifient l\'aspect de l\'image en temps réel, sans arrêter le calcul du rendu.
-   Lorsque vous estimez que la qualité est suffisante, appuyez sur **Calcul du Rendu-\> stop** puis sur **Fichier-\> Exporter vers une image-\> Gamme dynamique faible en mode ton mappé** (File-\>Export to image-\>Tonemapped low dynamic range ) pour enregistrer l\'image rendue dans un fichier .Png.

Vous pouvez étendre considérablement les possibilités de rendu de FreeCAD en créant de nouveaux modèles pour Povray ou Luxrender. Ceci est expliqué dans la documentation du [atelier Raytracing](Raytracing_Workbench/fr.md).

**Téléchargements**

-   Le modèle de table: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/table.FCStd>
-   Le fichier produit lors de cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/blob/master/files/render.FCStd>

**Lire plus d\'informations**

-   [L'atelier Raytracing](Raytracing_Workbench/fr.md)
-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)
-   [LuxRender](http://www.luxrender.net)




{{Raytracing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Manual:Creating renderings/fr
