# Assembly Preferences/fr
Les préférences pour l\'<img alt="" src=images/Workbench_Assembly.svg  style="width:24px;"> [atelier Assembly](Assembly_Workbench/fr.md) peuvent être trouvées dans [réglages des préférences](Preferences_Editor/fr.md). Dans le menu, sélectionnez **Édition → Préférences...** puis **<img src="images/Workbench_Assembly.svg" width=16px> Assembly**. Ce groupe n\'est disponible que si l\'atelier Assembly a été chargé dans la session FreeCAD en cours.

Il n\'y a qu\'une seule page : Général.

![](images/Preferences_Assembly_Page_General.png )

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                | Description                                                                                                                                                                                                                                                                                                                                                          |
+====================================================+======================================================================================================================================================================================================================================================================================================================================================================+
|                                     | Si cette case est cochée, presser sur la touche **Échap** permet de quitter le mode d\'édition Assembly.                                                                                                                                                                                                                                           |
| **Échap pour quitter le mode édition** |                                                                                                                                                                                                                                                                                                                                                                      |
|                                                 |                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                     | Si cette case est cochée, les étapes successives du solveur sont enregistrées. Utile si vous souhaitez signaler un bogue. Les fichiers se nomment **runPreDrag.asmt** et **dragging.log** et se trouvent dans le répertoire par défaut de {{Incode|std::ofstream}} (sous Windows, il s\'agit du bureau). |
| **Journal des étapes successives**     |                                                                                                                                                                                                                                                                                                                                                                      |
|                                                 |                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                     | Lorsque vous [insérez](Assembly_InsertLink/fr.md) la première pièce de l\'assemblage, vous pouvez choisir de bloquer la pièce automatiquement. Les options sont les suivantes :                                                                                                                                                                              |
| **Bloquer la première pièce**          |                                                                                                                                                                                                                                                                                                                                                                      |
|                                                 | -   *Demander*                                                                                                                                                                                                                                                                                                                                                       |
|                                                    | -   *Toujours*                                                                                                                                                                                                                                                                                                                                                       |
|                                                    | -   *Jamais*                                                                                                                                                                                                                                                                                                                                                         |
+++





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [Assembly](Assembly_Workbench.md) > Assembly Preferences/fr
