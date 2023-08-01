# Arch IFC/fr
## Description

Les ateliers <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/fr.md) et <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/fr.md) comportent un importateur et un exportateur [IFC (Industry Foundation Classes)](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes). Le format IFC est un format en constante évolution qui permet d\'échanger des données entre les applications [BIM](https://fr.wikipedia.org/wiki/Building_information_modeling) utilisées en architecture et en ingénierie.

L\'importateur et l\'exportateur dépendent tous deux de la bibliothèque [IfcOpenShell](IfcOpenShell/fr.md) qui est fournie dans certaines distributions de FreeCAD. Une façon simple de vérifier si IfcOpenShell est disponible est d\'entrer ce qui suit dans la [console Python](Python_console/fr.md):


```python
import ifcopenshell
```

Si aucun message d\'erreur n\'apparaît, IfcOpenShell est installé et vous pouvez procéder à l\'[importation](Std_Import/fr.md) des fichiers IFC. Sinon, vous devrez installer IfcOpenShell vous-même. Lisez la page [IfcOpenShell](IfcOpenShell/fr.md) pour en savoir plus sur ce processus.


**Remarque:**

: L\'outil **[<img src=images/BIM_Setup.svg style="width:16px"> [BIM Configuration](BIM_Setup/fr.md)** recherchera également IfcOpenShell et émettra une notification s\'il n\'est pas installé.


**Remarque:**

: Dans le passé (2013), l\'atelier Arch offrait un importateur IFC plus simple qui ne dépendait pas d\'IfcOpenShell. Cet ancien module est toujours inclus dans le code source mais à partir de la version 0.19, il n\'est plus du tout recommandé. Il ne pourra importer qu\'un très petit sous-ensemble d\'objets IFC et doit être considéré comme complètement obsolète.

## Importer

Toutes les entités [IfcProduct](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifckernel/lexical/ifcproduct.htm) à partir de fichiers IFC2x3 ou IFC4 seront importées dans le document FreeCAD. Les paramètres de préférences IFC vous permettent de définir le mode d\'importation des objets IFC:

-   **Objets Arch paramétriques complets**, la géométrie sera, autant que possible, modifiable dans FreeCAD.
-   **Objets Arch non paramétriques**, les objets porteront des informations et des propriétés IFC mais ne seront pas modifiables.
-   **Formes de Part non paramétriques**, la géométrie sera fidèlement restituée mais les informations IFC seront ignorées.
-   **Une forme de Part par étage**, un objet tout-en-un, juste pour référence.

Chacun de ces types perd des informations par rapport au précédent, mais est plus léger en ressources, ce qui permet d\'ouvrir des fichiers plus volumineux. Un dernier type permet de supprimer complètement l\'importation d\'objets Arch, ce qui est utile pour les modèles analytiques structurels.

Généralement, si vous essayez d\'ouvrir un fichier volumineux et que FreeCAD prend trop de temps pour l\'importer, essayez avec un mode d\'importation plus faible.

IfcOpenShell prend en charge toutes les entités IFC2x3 et IFC4 (IFC4-add1 et IFC4-add2 sont implémentées dans la version 0.6 et peuvent être disponibles au moment où vous lisez ceci), mais elles ne peuvent pas toutes être converties en objets de l\'[Atelier Arch](Arch_Workbench/fr.md), celles qui ne peuvent pas être seront importées sous forme de formes simples de l\'[Atelier Part](Part_Workbench/fr.md). L'importateur IFC commence par importer toutes les entités IFC dérivées de [IfcProduct](http://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm), c'est-à-dire tous les objets qui composent un bâtiment, tel que des murs ou des fenêtres ou des tuyaux. Toutes les autres entités requises par l\'un de ces objets, telles que les profils d\'extrusion ou les composants d\'opérations booléennes, seront importées en fonction des besoins.

Si vous utilisez un mode d'importation qui utilise des objets Arch, paramétriques ou non, tous les objets porteront l'ensemble complet des [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) attaché à chaque objet, groupé par ensemble de propriétés.

Les structures de bâtiments telles que sites, bâtiments et étages sont également importées fidèlement et la structure est correctement recréée dans FreeCAD. Les structures de groupe (utilisant les IfcGroups) sont également importées et rendues dans FreeCAD et peuvent être combinées avec des structures de bâtiment par exemple, avoir des groupes dans des étages ou des étages dans des groupes.

Les objets [IfcAnnotation](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcproductextension/lexical/ifcannotation.htm) sont également importés ainsi que les objets linéaires ou basés sur des courbes [IfcStructuralItem](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralitem.htm).

Les quantités spécifiées dans le fichier IFC sont importées **NOT**. Cependant, puisque la géométrie est entièrement recréée dans FreeCAD, la plupart des quantités telles que la longueur, la surface, etc\... peuvent être facilement obtenues pour chaque objet.

Activer **afficher les messages de débogage** dans les paramètres de préférences IFC indiquera si un objet à partir du fichier IFC n\'aura pas été importé correctement.

**Remarque**: L\'atelier BIM comporte un outil [Explorateur IFC](BIM_IfcExplorer/fr.md) qui vous permet d\'ouvrir un fichier IFC en mode rapide uniquement en mode texte et d\'importer uniquement les pièces de votre choix.

## Exporter

L\'exportation vers des fichiers IFC exportera tous les objets sélectionnés et leurs descendants. Tous les objets Arch/BIM sont pris en charge ainsi que d\'autres objets créés dans d\'autres ateliers. Pour le moment, les seuls objets qui ne sont pas totalement pris en charge sont les **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**, **[<img src=images/Std_Part.svg style="width:16px"> [Std Parts](Std_Part/fr.md)** et les nouvelles structures telles que **[<img src=images/Link.svg style="width:16px"> [App Links](Std_LinkMake/fr.md)** et **[<img src=images/LinkGroup.svg style="width:16px"> LinkGroups**. Vous devrez donc les tester un peu avant de les utiliser. [Arch Référence](Arch_Reference/fr.md) exportera actuellement sous le nom `IfcBuildingElementProxies`.

Pour exporter un site ou un bâtiment entier, un étage entier ou un groupe contenant d\'autres objets, il suffit de sélectionner ce bâtiment, cet étage ou ce groupe. Les objets Arch seront exportés avec le type défini dans leur propriété \"Type IFC\". Leurs [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) sont également exportés, et si ces objets ont un UID IFC provenant d\'une importation précédente, le même UID sera conservé à l\'exportation. Les objets qui ne sont pas des objets Arch sont exportés sous le format [IfcBuildingElementProxy](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcsharedbldgelements/lexical/ifcbuildingelementproxy.htm).

Les fichiers IFC sont exportés au format IFC2x3 ou IFC4, selon votre version d\'IfcOpenShell, qui peut être compilé avec n\'importe lequel des schémas IFC. Si vous utilisez IfcOpenShell version 0.6 ou supérieure, la version IFC spécifiée dans les préférences Arch est utilisée.

Si la forme des objets exportés est basée sur une extrusion ou une opération booléenne, l\'opération et les composants seront correctement exportés au format IFC. Dans le cas contraire, la forme de l\'objet est exportée sous la forme [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4x1/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm). Si la forme contient des courbes, celles-ci seront triangulées. Toutefois, IfcOpenShell version 0.5 ou ultérieure comporte un sérialiseur qui doit être activé dans les préférences Import/Export → IFC. S\'il est activé, ce sérialiseur est capable d\'exporter des objets courbes très complexes tels que ceux basés sur NURBS et d\'éviter ainsi les faces triangulées. Au moment de la rédaction de ce document, cependant, rares sont les autres applications BIM qui prennent en charge les objets IFC NURBS. Il est donc conseillé d\'effectuer quelques tests.

## Plus d\'informations 

-   [IfcOpenShell](IfcOpenShell/fr.md), plus d\'informations sur l\'installation de cette bibliothèque.



---
⏵ [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Arch](Arch_Workbench.md) > Arch IFC/fr
