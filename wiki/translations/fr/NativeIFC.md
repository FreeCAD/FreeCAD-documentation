# NativeIFC/fr
**Attention** : la fonction NativeIFC est encore en cours d\'élaboration et n\'est pas terminée. Gardez cela à l\'esprit lorsque vous l\'utilisez et ne vous y fiez pas tant que vous n\'êtes pas sûr qu\'elle peut faire ce que vous voulez. Voir le [calendrier de développement](https://github.com/yorikvanhavre/FreeCAD-NativeIFC/blob/main/doc/roadmap2024.md) pour en savoir plus sur le développement, ce qui fonctionne et ce qui est prévu.

## Introduction

À partir de la version 1.0, FreeCAD utilise le [Concept natif d\'IFC](https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst). Il permet aux utilisateurs de FreeCAD d\'ouvrir, de manipuler et de créer des fichiers IFC nativement dans FreeCAD.

Bien que FreeCAD prenne en charge depuis longtemps l\'ouverture et l\'enregistrement de fichiers IFC via l\'atelier Arch, il le faisait, comme la plupart des autres applications BIM, en traduisant dans les deux sens entre le format IFC des fichiers et le modèle de données interne de FreeCAD. Cela signifie deux traductions, une à l\'ouverture et une autre à l\'enregistrement, ce qui entraîne une perte de données et une réécriture complète du fichier à chaque fois. Il n\'est donc pas adapté aux [systèmes de contrôle des versions](https://fr.wikipedia.org/wiki/Gestion_de_versions) tel que [Git](https://fr.wikipedia.org/wiki/Git), et il est très difficile de localiser les modifications.

IFC natif signifie que le fichier IFC est lui-même la structure de données dans FreeCAD. Lorsque vous ouvrez un fichier IFC dans FreeCAD, ce que vous voyez à l\'écran est un rendu direct du contenu du fichier IFC. Tout ce que vous modifiez modifiera directement le fichier IFC. Si vous ouvrez un fichier, que vous modifiez un élément et que vous enregistrez le fichier, la seule chose qui aura changé dans le fichier sera la ligne concernant cet élément. Le reste du fichier sera 100% identique à ce qu\'il était avant la sauvegarde. Pas de perte de données et des modifications très identifiables.

L\'idée de NativeIFC elle-même vient de [cet article de Bruno Postle](https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst). Elle est fortement inspirée par [BlenderBIM](https://blenderbim.org/) et essaie autant que possible d\'utiliser les mêmes concepts et de réutiliser le code. L\'objectif final est d\'offrir dans FreeCAD le même niveau de fonctionnalité et de performance que dans BlenderBIM, et d\'être le plus en amont possible d\'[IfcOpenShell](https://ifcopenshell.org/), le moteur IFC commun utilisé par les deux applications. Il a commencé comme un [projet séparé de Yorik](https://github.com/yorikvanhavre/FreeCAD-NativeIFC)

Travailler avec des fichiers IFC natifs dans FreeCAD est simple : ouvrez un fichier IFC existant ou créez un nouveau projet en utilisant l\'outil [Projet](BIM_Project/fr.md) de l\'[atelier BIM](BIM_Workbench/fr.md). Créez de nouveaux objets à l\'aide de n\'importe quel atelier ou outil de FreeCAD. Ajoutez ces objets à votre projet IFC en les faisant glisser dans la structure du projet. Enregistrez le fichier et vous avez terminé.

Lire ci-dessous pour plus de détails.



## Modes verrouillé et déverrouillé 

L\'[atelier BIM](BIM_Workbench/fr.md) offre deux modes de travail avec les fichiers IFC. Le passage d\'un mode à l\'autre se fait en cliquant sur le **bouton de verrouillage** de la barre d\'état de FreeCAD :

![](images/BIM-statusbar-lock.jpg )

-   **Mode déverrouillé** (par défaut) : vous pouvez avoir à la fois des projets IFC natifs et des éléments non-IFC dans un même document FreeCAD. Vous pouvez également travailler sur des modèles BIM sans créer de projet IFC natif, tout en exportant votre modèle au format IFC.
-   **Mode verrouillé** : votre document FreeCAD est un fichier IFC. Tout ce que vous faites entraîne des changements dans le fichier IFC. Tout nouvel objet que vous ajoutez est instantanément converti en IFC.

En mode verrouillé, tous les objets que vous créez sont immédiatement convertis en IFC et peuvent donc perdre certaines de leurs propriétés d\'origine et certains de leurs comportements paramétriques lorsque ceux-ci ne sont pas pris en charge par le format IFC. Ce mode est plus restrictif, ce qui est un inconvénient à certains moments du développement du projet, mais devient un avantage lorsque l\'intégrité et la fiabilité des données deviennent essentielles.

Il est également possible de créer des projets IFC natifs dans un document déverrouillé. Dans ce cas, les éléments IFC stricts coexistent avec les éléments non IFC dans votre document FreeCAD. Les objets d\'un projet IFC sont liés au fichier IFC qui leur est attaché. Travailler avec des projets IFC n\'est souvent pas nécessaire au début d\'un projet, mais si vous travaillez avec d\'autres personnes et que vous utilisez des fichiers IFC comme principal moyen de communication, l\'utilisation de projets IFC natifs peut devenir un avantage, car les modifications apportées à chaque version du fichier sont beaucoup moins importantes.

Vous pouvez toujours exporter votre modèle au format IFC lorsque vous en avez besoin, que vous utilisiez ou non des projets IFC. La différence est que lorsque vous utilisez un projet IFC, des modifications très minimes sont écrites dans le fichier IFC. Dans le cas contraire, l\'ensemble du fichier est réécrit à chaque exportation. Cela peut ou non être un problème pour vous.

L\'idée générale est de travailler en mode déverrouillé lorsque vous travaillez sur vos propres projets, de sorte que vous puissiez avoir des éléments IFC et non IFC dans vos documents, et d\'utiliser le mode verrouillé lorsque vous travaillez sur les fichiers IFC d\'autres personnes, de sorte que vous puissiez garder un contrôle strict sur ce que vous modifiez dans ces fichiers.



## Concepts de fichier 

Lorsque vous travaillez avec des fichiers IFC natifs dans FreeCAD, un projet IFC (qu\'il soit verrouillé ou déverrouillé) est toujours accompagné d\'un fichier IFC. Ce fichier IFC contient toutes les données de votre projet IFC dans FreeCAD et est également responsable de la fourniture de la géométrie de ses objets à FreeCAD.

Lors de la création d\'un nouveau projet IFC, il n\'y a pas encore de fichier IFC, la première fois que vous enregistrez le fichier, FreeCAD vous demandera où enregistrer le fichier IFC.

En mode verrouillé, vous travaillez directement dans un fichier IFC. Il n\'y a plus de fichier FreeCAD.

En mode déverrouillé, vous avez des objets de projet IFC attachés à des fichiers IFC, et le document FreeCAD dépend de ces fichiers IFC. Si vous souhaitez transmettre votre fichier FreeCAD à quelqu\'un d\'autre, vous devez également lui donner les fichiers IFC. Vous pouvez également définir le mode de forme de tous les objets sur \"Forme\" (voir ci-dessous). Ainsi, le fichier FreeCAD conservera la forme de tous les objets IFC et les rendra correctement, même sans le fichier IFC joint. Cependant, les objets IFC à l\'intérieur ne seront plus modifiables.



## Objets IFC versus objets BIM 

Lorsqu\'un objet BIM ou tout autre objet FreeCAD est lié à un [projet](BIM_Project/fr.md) IFC natif, il devient un objet IFC. Lier un objet à un projet IFC natif se fait simplement en faisant glisser, dans l\'arborescence, l\'objet sur le projet ou sur tout objet faisant déjà partie de ce projet, par exemple un bâtiment ou un étage.

Une fois qu\'un objet est devenu un objet IFC, il est entièrement contrôlé par les données IFC. Il perd son ancien objet paramétrique FreeCAD et peut perdre toutes les propriétés et caractéristiques paramétriques qui ne sont pas prises en charge par le format IFC. L\'objectif est de rendre tout cela transparent à l\'avenir et de conserver les mêmes possibilités d\'édition pour les objets IFC et non IFC.

## Ouvrir et importer des fichiers IFC 

Deux options s\'offrent à vous : ouvrir ou importer.

-   Si vous ouvrez, un nouveau document sera créé et vous serez automatiquement en **mode verrouillé**.
-   Si vous importez, un objet IFC natif [projet](BIM_Project/fr.md) sera ajouté au document en cours mais vous pourrez toujours créer des objets non-IFC en dehors de ce projet. Vous serez toujours en *mode déverrouillé*

Pour ouvrir un fichier IFC, utilisez le menu Fichier -\> Ouvrir et sélectionnez un fichier IFC. Pour importer un fichier IFC, utilisez le menu Fichier -\> Importer et sélectionnez un fichier IFC.

Pour maximiser la vitesse d\'importation initiale, l\'ouverture ou l\'importation de fichiers IFC ne rendra par défaut que l\'objet de niveau supérieur (généralement un site) dans FreeCAD. Pour développer le contenu de cet objet, vous devez double-cliquer dessus dans l\'arborescence (voir ci-dessous).

L\'importation ou l\'ouverture d\'un fichier IFC ne nécessite le réglage d\'aucune option. Cependant, certaines valeurs par défaut peuvent être modifiées dans le menu Édition -\> Préférences -\> BIM -\> NativeIFC.



## Créer un nouveau document IFC 

Vous pouvez choisir de travailler en mode verrouillé ou déverrouillé, selon que vous avez besoin d\'avoir des objets non-IFC dans votre document FreeCAD (déverrouillé) ou que vous souhaitez que tout ce que vous faites dans le document se passe dans le fichier IFC (verrouillé).

Lors de la création d\'un nouveau projet IFC, il n\'y a pas encore de fichier IFC attaché. Lors du premier enregistrement, FreeCAD vous demandera un emplacement pour enregistrer un fichier IFC.

**En mode verrouillé :**

1.  Créez un nouveau document FreeCAD avec le menu Fichier -\> Nouveau
2.  Appuyez sur le bouton <img alt="" src=images/IFC.svg  style="width:24px;"> [Verrouiller les IFC](BIM_ToggleNativeIFC/fr.md) dans la barre d\'état pour verrouiller le document.

**En mode déverrouillé :**

1.  Appuyez sur le bouton <img alt="" src=images/BIM_Project.svg  style="width:24px;"> [Projet](BIM_Project/fr.md) pour créer un projet IFC natif dans le document FreeCAD en cours. Vous pouvez en avoir plusieurs dans le même document FreeCAD.



## Enregistrer et exporter des fichiers IFC 

Vous pouvez toujours exporter n\'importe quel modèle FreeCAD en IFC, même s\'il n\'a pas été construit avec des outils BIM ou s\'il contient des éléments non BIM. Les objets non BIM seront simplement exportés en tant qu\'entités génériques IfcBuildingElementProxy, alors que les objets BIM peuvent avoir leur classe (IfcWall, IfcDoor,\...) définie.

Les projets NativeIFC, qu\'ils soient en mode verrouillé ou déverrouillé, ont toujours un fichier IFC attaché. Il n\'est plus nécessaire d\'exporter quoi que ce soit, il suffit d\'enregistrer ce fichier IFC. La manière d\'enregistrer le contenu IFC diffère selon le mode :

-   Lorsque vous travaillez en **mode verrouillé**, tout ce qui se passe dans votre document FreeCAD est sauvegardé dans le fichier IFC. Il n\'est plus nécessaire de sauvegarder le fichier FreeCAD, et les entrées de menu *\'Fichier -\> Enregistrer* et **Fichier -\> Enregistrer sous** sont remplacés par **Fichier -\> Enregistrer IFC\'\' et**Fichier -\> Enregistrer IFC sous\'\'\'. L\'enregistrement du fichier IFC est tout ce qui est nécessaire, il n\'y a plus de fichier .FCStd.

-   Lorsque vous travaillez en **mode déverrouillé**, chaque objet du [projet](BIM_Project/fr.md) IFC de votre document est attaché à un fichier IFC distinct. Un objet projet garde la trace des modifications et son icône affichera un point rouge lorsqu\'il contient des modifications non enregistrées. En sauvegardant votre document FreeCAD, vous sauvegarderez également tous les fichiers IFC attachés aux projets IFC trouvés dans le document.

En mode déverrouillé, vous pouvez également enregistrer manuellement les fichiers joints en cliquant avec le bouton droit de la souris sur le projet et en choisissant IFC -\> Enregistrer.



## Développer le contenu des fichiers 

Lors de l\'ouverture d\'un fichier IFC, seuls les objets de premier niveau (généralement le site et le bâtiment) sont restitués dans FreeCAD par défaut (ceci peut être modifié dans le menu Édition -\> Préférences -\> BIM -\> NativeIFC) et les données supplémentaires telles que les matériaux, les propriétés géométriques, la forme, les calques et les objets enfants ne sont pas rendues.

Pour charger toutes les données supplémentaires et afficher les enfants directs d\'un objet, double-cliquez sur celui-ci dans l\'arborescence.

Vous pouvez également réduire les objets développés en cliquant avec le bouton droit de la souris sur ces objets dans l\'arborescence et en sélectionnant IFC -\> réduire les enfants.



## Charger et décharger des formes 

Par défaut, pour gagner en rapidité, les objets IFC ne chargent pas leur forme complète. Seule une représentation 3D légère est affichée dans la vue 3D. Cela garantit des opérations d\'importation et d\'extension rapides. Cependant, les opérations géométriques complexes telles que les opérations booléennes ou les sections réalisées par des [plans de section](Arch_SectionPlane/fr.md) nécessitent la présence de la forme complète. Dans ce cas, vous devrez peut-être charger la forme des objets sur lesquels vous souhaitez effectuer ces opérations.

Pour charger la forme des objets sélectionnés, il suffit de définir leur propriété **Shape Mode** à **Shape**.

Pour décharger la forme et revenir au mode de représentation 3D léger, définissez la propriété **Shape Mode** à **Coin** (Coin est le nom de la bibliothèque de rendu 3D utilisée dans FreeCAD).

Il existe un troisième mode de forme, **None**, qui désactive complètement la représentation visuelle des objets IFC. Ceux-ci sont alors uniquement contrôlés via l\'arborescence.



## Classes, attributs et propriétés 

Tous les objets IFC ont toujours au moins deux propriétés : **Class** et **Step ID**. La classe est la classe IFC (IfcWall, IfcWindow, etc\...) et l\'ID du Step est l\'ID de l\'élément dans le fichier IFC. L\'ID du Step est en fait la seule donnée nécessaire pour localiser l\'objet dans le fichier IFC. Vous pouvez changer la classe d\'un objet à tout moment, cela n\'aura pas d\'impact sur la géométrie ou les ensembles de propriétés mais peut changer les attributs disponibles (voir ci-dessous). Vous ne pouvez changer de classe que vers une classe sœur, une classe parente ou une classe descendante. Si vous souhaitez passer à une classe très éloignée de la classe en cours, vous devrez connaître la structure des classes IFC et répéter l\'opération plusieurs fois.

Les **attributs** sont des propriétés supplémentaires codées en dur des objets IFC, telles que le nom, la description ou l\'ID. Les attributs dépendent de la classe. Par exemple, les IfcWindows ont également une longueur et une largeur, les IfcSites ont une longitude et une latitude, etc. Les attributs sont toujours regroupés dans le groupe **IFC** et sont toujours chargés avec un objet.

Lorsque l\'on modifie la classe d\'un objet, les attributs peuvent changer. Vous pouvez modifier la valeur des attributs, mais vous ne pouvez pas ajouter ou supprimer des attributs, car ceux-ci sont obligatoires et définis par la norme IFC.

Les **propriétés** IFC, qui sont regroupées sous les ensembles de propriétés, sont des propriétés personnalisées qui peuvent être attribuées à n\'importe quel objet IFC. Elles ne sont pas chargées par défaut, mais le sont lorsque vous double-cliquez sur un objet. Les ensembles de propriétés, qui sont des packs de propriétés attachés aux objets, sont rendus comme des groupes de propriétés dans l\'arborescence des propriétés de FreeCAD.



## Calques et matériaux 

Les **calques** sont chargés lorsqu\'on double-clique sur un objet. Les calques sont représentés comme des [calques normaux de FreeCAD](Draft_Layer/fr.md) mais ils sont hébergés dans le projet IFC. Lors de l\'utilisation de l\'outil [BIM Calque](BIM_Layers/fr.md), une icône supplémentaire indique si le calque fait partie d\'un projet IFC ou non.

Les **matériaux** suivent la même logique. Ils ne sont chargés qu\'en double-cliquant sur l\'objet, ils sont représentés comme des [matériaux](Arch_Material/fr.md) normaux mais sont hébergés dans le projet IFC.



## Structure des bâtiments 

Selon les standards IFC, tous les fichiers IFC doivent contenir un et un seul objet IfcProject (ou IfcProjectLibrary), qui constitue la racine de votre modèle IFC. Tous les autres objets IFC peuvent être librement agrégés sous cet objet racine (une idée que nous appelons \"fichier à plat\") mais les normes IFC exigent d\'avoir au moins un objet conteneur de bâtiment (IfcSite, IfcBuilding ou IfcBuildingStorey) sous l\'objet racine IfcProject. Dans FreeCAD, avec les options par défaut, les fichiers IFC exportés contiendront toujours le projet IfcProject et au moins un conteneur de bâtiment (des conteneurs par défaut seront créés si vous n\'en avez pas).

Bien que cela ne soit pas obligatoire, il est courant que les fichiers IFC aient toujours la même structure de base :

IfcProject
  -> IfcSite
     -> IfcBuilding
        -> IfcBuildingStorey

Vous pouvez également utiliser des [groupes](Std_Group/fr.md) dans vos projets IFC. Cependant, la norme IFC ne permet pas d\'imbriquer des groupes à l\'intérieur d\'une structure de bâtiment. Ces groupes seront donc convertis en assemblages IfcAssemblies. Cependant, comme la plupart des applications BIM travaillent volontiers avec des groupes imbriqués, vous pouvez désactiver cette conversion dans les préférences d\'exportation IFC.



## Vérifier les changements dans un projet IFC 

L\'un des principaux avantages du système IFC natif est que seules les modifications apportées dans FreeCAD sont répercutées dans le fichier IFC joint à un projet. Par conséquent, ce fichier IFC ne contient que très peu de modifications, contrairement aux applications BIM traditionnelles où le fichier IFC est entièrement réécrit à chaque exportation.

Cela permet de localiser précisément les changements à l\'intérieur du fichier. Le déplacement d\'un mur, par exemple, ne modifie qu\'une seule ligne : l\'emplacement de ce mur. Cela permet aux systèmes de contrôle de version tels que Git d\'identifier précisément ces changements et de ne sauvegarder que les incréments de chaque nouvelle version.

Vous pouvez obtenir une représentation visuelle (diff) des changements dans un projet IFC sélectionné en utilisant le menu Utilitaires -\> Différence entre deux documents IFC ou, en mode déverrouillé, en cliquant avec le bouton droit de la souris sur un projet IFC et en sélectionnant IFC -\> Différence.



## Ajouter, supprimer et modifier des objets 

En mode verrouillé, tout nouvel objet ajouté (BIM ou non) est immédiatement converti en IFC. Il n\'y a plus rien à faire.

En mode déverrouillé, tout nouvel objet (BIM ou non) ajouté au document doit être ajouté à un projet IFC. Pour ce faire, il suffit de faire glisser l\'objet dans l\'arborescence et de le déposer n\'importe où dans la structure d\'un projet IFC.

Supprimer des objets qui se trouvent dans un projet IFC les supprimera également du fichier IFC.

Une fois qu\'un objet devient un objet IFC, il perd ses anciennes capacités paramétriques FreeCAD et hérite de tout son comportement du fichier IFC. Depuis FreeCAD 1.0, les possibilités d\'édition des objets IFC sont encore limitées, et se font entièrement via les propriétés (aucune édition graphique n\'est encore disponible). Pour éditer un objet, vous devez avoir chargé ses propriétés géométriques. Cela se fait soit en double-cliquant sur l\'objet, soit en faisant un clic droit et en choisissant *IFC -\> ajouter des propriétés géométriques* dans l\'arborescence.

Des propriétés géométriques modifiables telles que la \"hauteur\" ou la \"largeur\" sont alors ajoutées à l\'objet. Il s\'agit d\'un travail en cours, toutes les propriétés ne sont pas encore prises en charge. La modification de la valeur de ces propriétés changera la forme de l\'objet.



---
⏵ [documentation index](../README.md) > NativeIFC/fr
