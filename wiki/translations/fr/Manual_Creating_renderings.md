# Manual:Creating renderings/fr
{{Manual:TOC}}

Le [rendu photoréaliste](https://fr.wikipedia.org/wiki/Rendu_photor%C3%A9aliste) est le processus de création d\'images très réalistes à partir de modèles 3D en simulant l\'éclairage, les matériaux et les textures. Il est couramment utilisé dans des secteurs tels que le cinéma, les jeux vidéo et la conception de produits, où des visualisations photoréalistes sont nécessaires pour présenter des conceptions ou des concepts. Si le rendu permet de créer des images très proches de photographies réelles, il nécessite des outils spécialisés pour contrôler des éléments tels que l\'éclairage, les reflets et les ombres.

FreeCAD, cependant, se concentre principalement sur la modélisation technique plutôt que sur les effets artistiques ou visuels. Son objectif premier est de créer des modèles 3D précis pour l\'ingénierie, la conception et la fabrication. Par conséquent, FreeCAD ne dispose pas d\'outils de rendu intégrés avancés pour le photoréalisme.

Cependant, FreeCAD propose l\'atelier [Render](https://github.com/FreeCAD/FreeCAD-render?tab=readme-ov-file), qui peut être installé en tant que module complémentaire (ce n\'est pas l\'un des ateliers par défaut). Cet atelier permet aux utilisateurs de connecter les modèles FreeCAD à des moteurs de rendu externes tels que Blender Cycles, LuxCoreRender ou POV-Ray. Grâce à l\'atelier Render, les utilisateurs peuvent utiliser leurs modèles et tirer parti de ces puissants outils externes pour rendre leurs conceptions avec un éclairage et des textures réalistes. Cette approche permet à FreeCAD de rester léger et concentré, tout en offrant la flexibilité nécessaire à un rendu photoréaliste lorsque cela est nécessaire.

L\'atelier Render de FreeCAD s\'intègre à plusieurs moteurs de rendu externes, notamment [LuxCorerender](https://fr.wikipedia.org/wiki/LuxRender), [POV-Ray](https://fr.wikipedia.org/wiki/POV-Ray) et [Blender Cycles](https://www.cycles-renderer.org/). LuxCoreRender est un moteur de rendu moderne, basé sur la physique, qui produit des images photoréalistes, mais qui nécessite une puissance de calcul importante, en particulier pour les scènes de grande taille. POV-Ray, bien que plus ancien, reste un moteur [raytracing](https://fr.wikipedia.org/wiki/Ray_tracing) fiable et moins gourmand en ressources, bien qu\'il n\'ait pas le réalisme des technologies plus récentes. Blender Cycles, accessible via FreeCAD lorsque Blender est installé, offre une solution de rendu puissante avec prise en charge du GPU et du CPU, produisant efficacement des images de haute qualité. Cependant, il faut installer Blender séparément et exporter les modèles vers Blender pour le rendu. Chaque moteur de rendu offre des avantages qui dépendent de l\'équilibre entre le réalisme, les performances et les capacités du système de l\'utilisateur. Chaque option a ses forces et ses faiblesses, en fonction du type d\'image que l\'on veut rendre. La meilleure façon de s\'en rendre compte est de regarder des exemples sur le site web de chaque moteur.

### Installation

Avant d\'utiliser l\'atelier Render dans FreeCAD, vous devrez installer à la fois l\'atelier lui-même (comme indiqué dans [cette section](https://wiki.freecad.org/Manual:Installing/fr#Installation_de_contenu_suppl%C3%A9mentaire)) et l\'une des applications de rendu externes telles que LuxCoreRender, POV-Ray, ou Blender Cycles (avec Blender installé). L\'installation de ces applications est généralement simple, car elles fournissent des installateurs pour différentes plateformes et sont souvent incluses dans les dépôts de logiciels des distributions Linux. Une fois ces outils installés, vous pourrez connecter FreeCAD à ces moteurs de rendu pour produire des images de haute qualité.

Une fois que POV-Ray ou LuxCorerender est installé, nous devons définir le chemin d\'accès à son exécutable principal dans les préférences de FreeCAD. Cela n\'est généralement nécessaire que sur Windows et Mac. Sur Linux, FreeCAD va le choisir parmi les emplacements standard. L\'emplacement des exécutables de Povray ou LuxRender peut être trouvé en recherchant simplement dans votre système les fichiers appelés Povray (ou Povray.exe sur Windows) et LuxRender (ou Luxrender.exe sur Windows). Dans l\'onglet **Préférences**, vous pouvez désigner le chemin et définir certains paramètres.

![](images/FreeCAD_Render_Preferences.png )



### Rendu avec PovRay 

Nous allons utiliser la table que nous avons modélisée dans le chapitre sur la [Modélisation traditionnelle](Manual:Traditional_modeling,_the_CSG_way/fr.md) pour produire des rendus avec PovRay.

-   Commencez par charger le fichier table.FCStd que nous avons modélisé plus tôt ou à partir du lien au bas de ce chapitre et entrez dans l\'<img alt="" src=images/Render_workbench_icon.svg  style="width:16px;"> [Render](https://github.com/FreeCAD/FreeCAD-render/fr%7Catelier).
-   Créez un projet de rendu en appuyant sur le bouton de la barre d\'outils correspondant à votre moteur de rendu. Pour notre exemple, nous choisirons le moteur de rendu povray <img alt="" src=images/Render_Povray.svg  style="width:16px;">.
-   Sélectionnez un modèle adapté à votre projet. Nous choisirons le modèle **povray_sunlight.pov**.
-   Vous pouvez également essayer d\'autres modèles après avoir créé un nouveau projet, simplement en modifiant sa propriété **Template**.
-   Un nouveau projet a maintenant été créé :

![](images/FreeCAD_Render_Project.png )

-   Vous pouvez ajouter les objets souhaités au projet en les sélectionnant et en appuyant sur l\'option <img alt="" src=images/Render_RenderingView.svg  style="width:16px;"> [vue de rendu](Render_RenderingView/fr.md).

![](images/FreeCAD_Render_Bodies.png )

-   Si nous le souhaitons, nous pouvons appliquer un matériau à nos corps en appuyant sur l\'option <img alt="" src=images/Arch_SetMaterial.svg  style="width:16px;"> [Matériau](Arch_SetMaterial/fr.md). Dans notre cas, nous choisirons l\'option matte.
-   Nous pouvons maintenant appuyer sur le bouton <img alt="" src=images/Render_workbench_icon.svg  style="width:16px;"> et notre résultat apparaîtra dans une fenêtre séparée.

![](images/FreeCAD_Render_Result.png )

À vrai dire, le résultat final n\'est pas très impressionnant. Le processus de rendu est itératif et il faut du temps et de la patience pour obtenir des résultats de haute qualité. En outre, comme indiqué plus haut, POV-Ray est quelque peu limité en termes de réalisme. N\'hésitez pas à expérimenter d\'autres outils de rendu. La procédure reste en grande partie la même, la seule différence étant la sélection d\'un autre moteur de rendu au début du processus.

**Téléchargements**

-   Le modèle de table: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/table.FCStd>
-   Le fichier produit lors de cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/blob/master/files/render.FCStd>

**Lire plus d\'informations**

-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)




{{Raytracing Tools navi}}



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Manual:Creating renderings/fr
