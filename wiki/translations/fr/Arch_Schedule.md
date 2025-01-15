---
 GuiCommand:
   Name: Arch Schedule
   Name/fr: Arch Nomenclature
   MenuLocation: Gestion , Nomenclature
   Workbenches: BIM_Workbench/fr
   SeeAlso: 
---

# Arch Schedule/fr

## Description

L\'outil **Arch Nomenclature** vous permet de créer et d\'alimenter automatiquement une [feuille de calculs](Spreadsheet_Workbench/fr.md) avec les contenus recueillis dans le modèle.

Pour une solution plus générale, consultez l\'[atelier Reporting](https://github.com/furti/FreeCAD-Reporting/tree/master) dans la liste des [ateliers externes](External_workbenches/fr.md). Cet atelier utilise la syntaxe SQL pour extraire des informations du document.



## Utilisation

1.  Ouvrez ou créez un document FreeCAD contenant quelques objets.
2.  Appuyez sur le bouton **<img src="images/Arch_Schedule.svg" width=16px> [Nomenclature](Arch_Schedule/fr.md)**.
3.  Ajustez les options souhaitées. Activez l\'option **Lier à une feuille de calcul** si vous souhaitez que la nomenclature génère une [feuille de calcul](Spreadsheet_Workbench/fr.md) FreeCAD. Ou bien, cliquez avec le bouton droit de la souris sur la nomenclature dans la [vue en arborescence](Tree_view/fr.md) après sa création et sélectionnez **Joindre une feuille de calcul** dans le menu contextuel.
4.  Appuyez sur **OK**.



## Déroulement des tâches 

Tout d\'abord, vous devez disposer d\'un modèle. Par exemple, voici un document avec quelques objets. Ici ce sont des objets Arch, mais d\'autres objets sont également pris en charge.

![](images/Arch_schedule_example01.jpg )

Lorsque vous appuyez sur le bouton **<img src="images/Arch_Schedule.svg" width=16px> [Nomenclature](Arch_Schedule/fr.md)**, cette fenêtre de dialogue s\'ouvre :

![](images/ArchSchedule.png )

Vous pouvez maintenant remplir la nomenclature ligne par ligne. Chaque ligne est une \"requête\" et affichera une ligne dans la feuille de calcul. Appuyez sur le bouton **<img src="images/List-add.svg" width=16px> Ajouter une ligne** pour ajouter une nouvelle ligne, et double-cliquez sur chaque cellule de cette ligne pour remplir les valeurs. Le bouton **<img src="images/List-remove.svg" width=16px> Supprimer une ligne** supprimera la ligne qui contient une cellule sélectionnée et **<img src="images/Delete.svg" width=16px> Effacer** supprimera toutes les lignes. Les valeurs possibles pour les colonnes sont :

-   **Description** : une description de cette requête. La colonne Description sera la première colonne de la feuille de calcul résultante. La description est obligatoire pour qu\'une requête soit exécutée. Si vous laissez la cellule de description vide, la ligne entière sera ignorée et laissée vide dans la feuille de calcul. Cela vous permet d\'ajouter des lignes \"séparatrices\".
-   **Propriété** : c\'est la requête réelle que vous souhaitez effectuer sur tous les objets sélectionnés par la requête. Il peut s\'agir de deux choses : soit le mot `count`, soit une propriété de l\'objet :
    -   Si vous entrez `count` (ou `Count` ou `COUNT`, la casse n\'est pas prise en compte), les objets sélectionnés seront simplement comptés.
    -   Si vous saisissez une propriété d\'objet, la valeur de cette propriété sera récupérée pour chacun des objets sélectionnés et additionnée. Les objets qui n\'ont pas la propriété donnée seront ignorés. En général, le nom d\'une propriété est celui qui apparaît dans l\'[éditeur de propriétés](Property_editor/fr.md), sans espace (par exemple, tapez `PerimeterLength` dans la colonne Propriété si l\'objet a un `Perimeter Length` dans l\'éditeur de propriétés). Utilisez la notation par points pour récupérer les propriétés des propriétés : `PropertyOfObject.PropertyOfProperty1.PropertyOfProperty2`. Si la propriété précédant le premier point commence par une lettre minuscule, elle sera considérée comme une référence à l\'objet lui-même et sera ignorée. Saisir par exemple `object.Shape.Volume` revient à saisir `Shape.Volume`.
-   **Unité** : une unité facultative pour exprimer les résultats. Par exemple, si vous recherchez des volumes, vous devez utiliser une unité de volume, telle que `m^3` ou `m³`. Si vous utilisez une mauvaise unité pour la propriété, par exemple `cm` pour le volume, vous obtiendrez de faux résultats.
-   **Objets** : si vous pouvez laisser ce champ vide alors tous les objets du document seront pris en compte par cette requête, ou rentrez une liste de noms d\'objets séparés par des points-virgules `;`. Si l\'un des objets de cette liste est un groupe, ses enfants seront également sélectionnés. La manière la plus simple d\'utiliser cette fonction est donc de regrouper vos objets de manière significative dans le document, et de donner un nom de groupe ici. Vous pouvez également utiliser le **<img src="images/Edit-select-all.svg" width=16px> Ajouter une sélection** pour ajouter les objets sélectionnés dans le document. Vous devez utiliser des noms internes ici. Pour sélectionner les objets par leur étiquette, laissez cette colonne vide et utilisez la colonne Filtre à la place.
-   **Filtre** : ici vous pouvez ajouter une liste de filtres séparés par un point-virgule `;`. Chaque filtre est écrit sous la forme : `property:value`. Vous ne pouvez utiliser que des propriétés contenant une chaîne de caractères. La propriété et la valeur sont insensibles à la casse. `value` peut être omis mais pas `:`. Pour gérer correctement les nomenclatures créées avec des versions antérieures d\'Arch Nomenclature, la propriété `type` sera traduite en propriété `ifctype`. Il est conseillé de ne pas utiliser `type` dans les nouveaux programmes.

+++
| Requête                                | Description                                                                                                                                                                                                                                                                                                                         |
+========================================+=====================================================================================================================================================================================================================================================================================================================================+
|                         | Cette requête ne retient que les objets dont le **Label** contient \"floor1\" et dont **IFC Type** contient \"window\". Une fenêtre avec **Label** \"Floor1-AA\" et **IFC Type** \"Window Standard Case\" sera incluse. |
| `label:floor1;ifctype:window` |                                                                                                                                                                                                                                                                                                                                     |
|                                     |                                                                                                                                                                                                                                                                                                                                     |
+++
|                         | Ne retiendra que les objets ayant \"door\" dans leur **Label**                                                                                                                                                                                                                                           |
| `label:door`                  |                                                                                                                                                                                                                                                                                                                                     |
|                                     |                                                                                                                                                                                                                                                                                                                                     |
+++
|                         | Ne retiendra que les objets qui n\'ont pas \"door\" dans leur **Label**                                                                                                                                                                                                                                  |
| `!label:door`                 |                                                                                                                                                                                                                                                                                                                                     |
|                                     |                                                                                                                                                                                                                                                                                                                                     |
+++
|                         | Ne retiendra que les objets qui ont \"structural\" dans leurs **IFC Type**                                                                                                                                                                                                                               |
| `ifctype:structural`          |                                                                                                                                                                                                                                                                                                                                     |
|                                     |                                                                                                                                                                                                                                                                                                                                     |
+++
|                         | Ne retiendra que les objets qui n\'ont pas \"structural\" dans **IFC Type** ou qui n\'ont pas la propriété **IFC Type**.                                                                                                                                                      |
| `!ifctype:something`          |                                                                                                                                                                                                                                                                                                                                     |
|                                     |                                                                                                                                                                                                                                                                                                                                     |
+++
|                         | Ne conservera que les objets qui n\'ont pas la propriété **IFC Type**.                                                                                                                                                                                                                                   |
| `!ifctype:`                   |                                                                                                                                                                                                                                                                                                                                     |
|                                     |                                                                                                                                                                                                                                                                                                                                     |
+++

: Exemples de requêtes de filtrage

Le bouton **<img src="images/Document-open.svg" width=16px> Importer** vous permet de créer cette liste dans un autre tableur et de l\'importer ici sous forme de fichier CSV.

La nomenclature terminée peut ressembler à ceci :

![](images/ArchScheduleExample.png )

Enfin, appuyez sur **OK** et une nouvelle nomenclature est ajoutée au document. Si l\'option connexe a été sélectionnée, la nomenclature contiendra une feuille de calcul associée :

![](images/Arch_schedule_example04.jpg )

Pour modifier une nomenclature existante, double-cliquez dessus dans l\'arborescence. En double-cliquant sur la feuille de calcul, vous obtenez les résultats dans 3 colonnes : Description, Valeur, Unité (le cas échéant) :

![](images/Arch_schedule_example05.jpg )

La feuille de calcul peut ensuite être exportée au format CSV normalement à partir de l\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md).



## Propriétés dynamiques 

Il est possible d\'ajouter vos propres propriétés aux objets. Celles-ci sont appelées [propriétés dynamiques](Property_editor/fr#Actions.md). Si elles ont été ajoutées avec l\'option **Prefix group name** sélectionnée, leurs noms commenceront effectivement par le nom du groupe, mais ce préfixe ne sera pas affiché dans l\'[éditeur de propriétés](Property_editor/fr.md). Leurs noms ont la forme suivante : `NameOfGroup_NameOfProperty`. Pour les référencer dans une nomenclature, ce nom complet doit être utilisé.



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Schedule/fr
