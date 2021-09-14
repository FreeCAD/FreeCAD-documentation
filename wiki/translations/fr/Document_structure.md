# Document structure/fr







{{TOCright}}

![](images/Screenshot_treeview.jpg ) Un document FreeCAD contient tous les objets compris dans votre scène. Il peut contenir des groupes ainsi que des objets créés avec n\'importe quel atelier. Vous pouvez donc basculer entre les ateliers et toujours travailler sur le même document. Ce document est ce qui est enregistré sur le disque quand vous sauvegardez votre travail. Vous pouvez aussi ouvrir plusieurs documents à la fois dans FreeCAD, et ouvrir plusieurs vues du même document.

À l\'intérieur du document, les objets peuvent être regroupés, et avoir un nom unique. La gestion des groupes, objets et noms d\'objets se fait à partir de la [vue arborescente](Tree_view/fr.md). **Remarque :** Elle peut bien évidemment se faire aussi, comme tout dans FreeCAD, depuis l\'interpréteur [Python](Python/fr.md). Dans la [vue arborescente](Tree_view/fr.md), avec un clic droit de la souris dans la [vue arborescente](Tree_view/fr.md) ou sur un objet, vous pouvez créer des [groupes](Std_Group/fr.md) <img alt="" src=images/Std_Group.svg  style="width:16px;">, déplacer des objets dans des groupes, supprimer des objets ou des groupes ; renommer des objets avec un double-clic sur leur nom ; ou possiblement d\'autres opération, selon l\'atelier actif.

Les objets dans un document FreeCAD peuvent être de différents types. Chaque atelier peut créer ses propres types d\'objets ; par exemple, l\'[atelier Maillages](Mesh_Workbench/fr.md) <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> crée des maillages, l\'[atelier Part](Part_Workbench/fr.md) <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> crée des objets pièces, l\'[atelier Draft](Draft_Workbench/fr.md) <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> crée aussi des objets pièces, etc.

S\'il y a au moins un document ouvert dans FreeCAD, il ne peut y avoir qu\'un seul document actif. Il s\'agit du document qui est affiché dans la vue 3D courante, le document sur lequel vous travaillez.

## Interface utilisateur et application 

Puisque l\'architecture de FreeCAD est totalement modulaire, l\'interface graphique ou environnement graphique est séparée de la partie application. Ceci est aussi valide pour les documents. Les documents sont aussi séparés en deux parties : le document Application, qui contient les objets, et le document Affichage, qui contient la représentation à l\'écran des objets.

Voyez cela comme deux espaces dans lesquels les objets sont définis. Leurs paramètres de construction (est-ce un cube ? un cône ? quelle taille ?) sont enregistrés dans le document Application, alors que leur représentation graphique (l\'objet est-il dessiné avec des lignes noires ? avec des faces de couleur bleue ?) est enregistrée dans le document Affichage. Pourquoi cela ? Parce que FreeCAD peut aussi être utilisé {{emphasis|sans}} l\'interface graphique, par exemple à l\'intérieur d\'autres programmes, et nous devons pouvoir manipuler les objets, même si rien n\'est affiché à l\'écran.

Le document Affichage contient aussi les vues 3D. Un document peut avoir plusieurs vues ouvertes, ce qui vous permet de l\'inspecter depuis plusieurs points de vue en même temps. Vous pourriez vouloir afficher à la fois une vue de dessus et une vue de face de votre projet. Deux vues du même document seront alors enregistrées dans le document Affichage. La création de nouvelles vues, ou la fermeture des vues peut être faite depuis le menu Vue, ou par un clic droit de la souris sur l\'onglet d\'une vue.

## Script

Les documents peuvent être créés, accédés et modifiés facilement depuis l\'interpréteur [Python](Python/fr.md). Par exemple : 
```python
FreeCAD.ActiveDocument
``` Retournera le document courant (actif) 
```python
FreeCAD.ActiveDocument.Blob
``` Accède à un objet nommé « Blob » à l\'intérieur de votre document 
```python
FreeCADGui.ActiveDocument
``` Retournera la vue document associée au document courant 
```python
FreeCADGui.ActiveDocument.Blob
``` Accède à la représentation graphique (vue) de l\'objet « Blob » 
```python
FreeCADGui.ActiveDocument.ActiveView
``` Retourne à la vue courante






