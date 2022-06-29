# Path ToolShape/fr
{{TOCright}}

## Description

Les Formes d\'outils sont un élément essentiel du système [Path Outils](Path_Tools/fr.md). Les Formes d\'outils sont les modèles à partir desquels les Outils coupants sont créés. Elles représentent la forme physique spécifique d\'un outil. Une forme d\'outil ne décrit pas complètement l\'outil - pour cela, des paramètres supplémentaires sont nécessaires, qui seront ajoutés lorsqu\'un outil réel sera paramétré à partir du modèle.

Initialement, les Formes d\'outils sont juste des documents FreeCAD avec un seul corps créé à partir de l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [atelier Part Design](PartDesign_Workbench/fr.md).

La création de nouvelles Formes d\'outils est un sujet avancé. Les Formes d\'outils les plus couramment utilisés existent déjà et sont fournis avec l\'installation de FreeCAD à l\'adresse suivante   *

-   Sous Linux, il s\'agit généralement de `/usr/lib64/FreeCAD/Mod/Path/Tools/Shape`.
-   Sous Windows, il s\'agit généralement de `C   *Program Files\FreeCAD\Mod\Path\Tools\Shape`.
-   Sous macOS, il s\'agit généralement de `/Applications/FreeCAD.app/Contents/Resources/Mod/Path/Tools/Shape`.

Ce sont    *

   *   
    **ballend.fcstd**
    

   *   
    **bullnose.fcstd**
    

   *   
    **chamfer.fcstd**
    

   *   
    **drill.fcstd**
    

   *   
    **endmill.fcstd**
    

   *   
    **probe.fcstd**
    

   *   
    **slittingsaw.fcstd**
    

   *   
    **thread-mill.fcstd**
    

   *   
    **v-bit.fcstd**
    

Elles se trouvent dans le sous-répertoire **/Mod/Path/Tools/Shape/** où FreeCAD a été installé.

## Utilisation

1.  Créez un nouveau document FreeCAD.
2.  Ouvrez l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width   *16px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).
3.  Créez un [Corps](PartDesign_Body/fr.md) et donnez au corps une étiquette que vous voulez voir apparaître dans la sélection des outils.
4.  Créez une <img alt="" src=images/PartDesign_NewSketch.svg  style="width   *16px;"> [Esquisse](PartDesign_NewSketch/fr.md) sur le plan XZ et dessinez la moitié du profil de la mèche.
5.  Contraignez le centre le plus bas de la mèche sur l\'origine `(0,0)`. Ce sera le centre de l\'axe sur lequel le code G fera tourner l\'outil.
    -   Remarque    * n\'ajoutez pas de contraintes dimensionnelles pour le moment.
6.  Fermez l\'esquisse.
7.  Faites une <img alt="" src=images/PartDesign_Revolution.svg  style="width   *16px;"> [Révolution](PartDesign_Revolution/fr.md) de l\'esquisse autour de l\'axe vertical de l\'esquisse.
8.  Ouvrez l\'<img alt="" src=images/Workbench_Path.svg  style="width   *16px;"> [atelier Path](Path_Workbench/fr.md).
9.  Sélectionnez l\'esquisse dans la [Vue en arborescence](Tree_view/fr.md). Cela garantit que le Conteneur d\'attibuts d\'outil coupant (PropertyBag) créé à l\'étape suivante sera imbriqué dans le corps.
10. Sélectionnez l\'option **Path → Utilitaires → Conteneur d'attibuts d'outil coupant** dans le menu.
11. Un PropertyBag nommé {{Value|Attributs}} est créé. Ce PropertyBag sera utilisé pour contrôler les dimensions dans l\'esquisse.
12. Double-cliquez sur PropertyBag dans la [Vue en arborescence](Tree_view/fr.md).
13. Le panneau de tâches **Property Bag** s\'ouvre.
14. Cliquez sur le bouton **Ajouter...**.
15. La boîte de dialogue **Créer une propriété** s\'ouvre.
16. Créez une propriété nommée {{Value|Diameter}}. Cette propriété est obligatoire pour les outils coupants. Les noms de propriété sont sensibles à la casse et ne peuvent pas contenir d\'espaces.
17. Sélectionnez {{Value|Shape}} dans la liste déroulante **Groupe**.
18. Sélectionnez le **Type** approprié.
19. Spécifiez éventuellement un **ToolTip**.
20. Cliquez sur le bouton **OK**.
21. Dans le panneau de tâches **Property Bag**, entrez une valeur pour la propriété *Diameter*.
22. De même, ajoutez toutes les autres propriétés requises.
23. Cliquez sur le bouton **OK** dans le panneau de tâches **Property Bag** lorsque vous avez terminé.
24. Double-cliquez sur l\'esquisse dans la [Vue en arborescence](Tree_view/fr.md).
25. Ajoutez des contraintes dimensionnelles et appliquez les propriétés du Conteneur d\'attibuts d\'outil coupant créé. Par exemple, pour appliquer la propriété **Diameter**    *
    1.  Double-cliquez sur une dimension.
    2.  Cliquez sur l\'icône <img alt="" src=images/Bound-expression.svg  style="width   *16px;">.
    3.  Saisissez {{Value|<<Attributs>>.Diameter}} dans l\'**Editeur de formule**.
    4.  Cliquez deux fois sur le bouton **OK**.
26. Répétez cette opération jusqu\'à ce que l\'esquisse soit entièrement contrainte.
27. Enregistrez le fichier **FCStd** là où FreeCAD s\'attend à trouver les fichiers des outils coupants. Voir [Description](#Description.md) ci-dessus.

-   Note 1. Si l\'accès au dossier vous est refusé sous Windows, démarrez FreeCAD en mode ADMINISTRATEUR.
-   Note 2. Le corps de l\'outil coupant doit être le premier objet de la [Vue en arborescence](Tree_view/fr.md). Ces instructions garantissent que c\'est le cas.

## Images miniatures des outils 

Les outils coupants auront une petite icône de l\'outil dans la [Vue en arborescence](Tree_view/fr.md) si le fichier est enregistré avec les vignettes actives.

Remarques importantes    *

-   Avant d\'enregistrer le document, assurez-vous que vous avez sélectionné Save Thumbnail et désélectionné Add program logo dans les préférences de FreeCAD.
-   Assurez-vous également de passer en vue de face et d\'adapter le contenu à l\'écran.
-   Ce que vous voyez lorsque vous enregistrez le document sera la représentation visuelle du modèle.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolShape/fr
