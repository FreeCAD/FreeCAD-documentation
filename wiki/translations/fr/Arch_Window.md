---
- GuiCommand:/fr
   Name:Arch Window
   Name/fr:Arch Fenêtre
   MenuLocation:Arch → Fenêtre
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**W** **I**
   SeeAlso:[Arch Mur](Arch_Wall/fr.md), [Arch Ajouter](Arch_Add/fr.md)
---

## Description

Un objet [Arch Fenêtre](Arch_Window/fr.md) est un objet de base pour toutes sortes d\'objets **intégrables**, comme les fenêtres et portes. Il est conçu pour être indépendant ou devenir **hôte** à l\'intérieur d\'un autre composant comme un [Arch Mur](Arch_Wall/fr.md), un élément d\'une [Arch Structure](Arch_Structure/fr.md) ou d\'un [Arch Toit](Arch_Roof/fr.md). Il a sa propre forme géométrique, qui peut être fait de plusieurs composants (généralement un cadre et des panneaux intérieurs) et définit également un volume à soustraire aux objets hôtes, afin de créer une ouverture.

Les fenêtres sont basées sur des objets 2D fermés comme des [Draft Rectangles](Draft_Rectangle/fr.md) ou des [esquisses](Sketcher_Workbench/fr.md) utilisés pour définir les composantes internes. L\'objet 2D de base peut donc contenir plusieurs fils fermés, qui peuvent être combinés pour constituer des panneaux pleins (un seul fil) ou cadres (plusieurs fils).

L\'outil Arch Fenêtre comporte également plusieurs **préréglages**. Cela permet à l\'utilisateur de créer des types communs de fenêtres et de portes avec certains paramètres modifiables, sans qu\'il soit nécessaire de créer manuellement les objets et composants 2D de base.

Toutes les informations applicables à une [fenêtre](Arch_Window.md) s\'appliquent également à une [porte](Arch_Door.md), car il s\'agit du même objet sous-jacent. La principale différence entre une fenêtre et une porte est que la porte a un panneau interne qui est représenté opaque (la porte elle-même), tandis que la fenêtre a un panneau qui est partiellement transparent (le verre).

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;"> 
*Fenêtre construite à partir d'un [Draft Rectangle](Draft_Rectangle/fr.md) puis insérée dans un [Arch Mur](Arch_Wall/fr.md). L’utilisation de [Arch Addition](Arch_Add/fr.md) découpe automatiquement une ouverture correcte dans le mur hôte.*

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Fenêtre complexe en cours de construction à partir d'une [esquisse](Sketcher_Workbench/fr.md). Lorsque vous entrez en mode édition de la fenêtre, vous pouvez créer différents composants, définir leur épaisseur puis sélectionner et affecter des fils de l'esquisse à ceux-ci.*

## Utilisation

### Utilisation des préréglages {#utilisation_des_préréglages}

1.  Appuyez sur le bouton **<img src="images/Arch_Window.svg" width=16px> [Crée une fenêtre...](Arch_Window/fr.md)** ou appuyez sur les touches **W** puis **I**.
2.  Sélectionnez un des préréglages dans la liste.
3.  Remplissez les paramètres souhaités.
4.  Dans la [Vue 3D](3D_view/fr.md), déplacez la fenêtre à l\'emplacement où vous souhaitez la placer. Si vous déplacez le pointeur sur un [Arch Mur](Arch_Wall/fr.md), le contour de la fenêtre doit s'aligner sur la face de cet objet.
5.  Cliquez sur la [Vue 3D](3D_view/fr.md) avec la souris ou appuyez trois fois sur la touche **Entrée** pour confirmer les coordonnées X, Y, Z du placement.


**Remarque:**

Si vous installez la \"Parts Library\" à partir de [Gestionnaire d\'Addon](AddonManager/fr.md), l\'outil recherchera des préréglages supplémentaires dans cette bibliothèque. Ces préréglages sont des fichiers FreeCAD contenant une seule fenêtre basée sur une esquisse paramétrique ayant des contraintes nommées. Vous pouvez placer des préréglages supplémentaires dans le répertoire `parts_library` de manière à ce qu\'ils soient trouvés par l\'outil Fenêtre.


```python
$ROOT_DIR/Mod/parts_library/Architectural\ Parts/Doors/Custom/
$ROOT_DIR/Mod/parts_library/Architectural\ Parts/Windows/Custom/
```

Le dossier `$ROOT_DIR` est le répertoire de l\'utilisateur où la configuration, les macros et les établis externes de FreeCAD sont stockés.

-   L\'emplacement habituel dans Linux est `/home/username/.FreeCAD/`
-   L\'emplacement habituel dans Windows est `C:\Users\username\AppData\Roaming\FreeCAD`
-   L\'emplacement habituel dans est `/Users/username/Library/Preferences/FreeCAD/`

### Création à partir de zéro {#création_à_partir_de_zéro}

1.  Optionnellement, sélectionnez une face ou un objet Arch où vous devez insérer votre fenêtre.
2.  Basculez vers l\'[atelier Sketcher](Sketcher_Workbench/fr.md).
3.  Créez une nouvelle esquisse.
4.  Dessinez une ou plusieurs formes fermées (boucles).
5.  Fermez l\'esquisse.
6.  Activez l\'[atelier Arch](Arch_Workbench/fr.md)
7.  Appuyez sur le bouton **<img src="images/Arch_Window.svg" width=16px> [Arch Fenêtre](Arch_Window/fr.md)** ou appuyez sur les touches **W** puis **I** .
8.  Pour ajuster les composants de la fenêtre et diverses propriétés, entrez dans le [Panneau des tâches](Task_panel/fr.md) de la fenêtre en double-cliquant sur l\'objet créé dans la [Vue en arborescence](Tree_view/fr.md).


**Remarque:**

lors de la création de l\'esquisse, faites très attention à l\'ordre de création des boucles. La numérotation des \"fils\" dans le [Panneau des tâches](Task_panel/fr.md) (\"Window elements\") en dépend.

## Préréglages

Les préréglages suivants sont disponibles :

Image:ParametersDoorGlass.svg\|Porte de verre Image:ParametersDoorSimple.svg\|Simple porte Image:ParametersWindowDouble.svg\|Fenêtre à double ouvrant Image:ParametersWindowFixed.svg\|Fenêtre fixe Image:ParametersWindowSimple.svg\|Fenêtre simple ouverture Image:ParametersWindowStash.svg\|Fenêtre à ouverture verticale

## Création de composants {#création_de_composants}

Arch Windows peut inclure trois types de composants : panneaux, cadres et grilles. Les panneaux et grilles sont constitués d\'un fil fermé, obtenu par extrusion, tandis que les armatures sont faites de 2 fils fermés ou plus, où chacune est extrudée, puis les plus petites sont soustraites des plus grandes. Vous pouvez accéder, créer, modifier et supprimer des composants d\'une fenêtre en mode d\'édition (double-cliquez sur la fenêtre dans la vue 3D). Les composants ont les propriétés suivantes :

-   **Name**: Le nom du composant
-   **Type**: Le type de composant The type of component. Peut être, \"un panneau de verre\", \"panneau solide\" ou \"une persienne\"
-   **Wires**: Liste de fils séparés par une virgule
-   **Thickness** : l\'épaisseur de l\'extrusion du composant.
-   **Z Offset** : la distance entre le composant, et, sa ligne de base 2D.

-   **Hinge**: Ceci vous permet de sélectionner un bord de l\'objet 2D de base, puis de définir ce bord comme une charnière pour ce composant et ceux qui sont dans la liste
-   **Opening mode**: Si vous avez défini une charnière dans ce composant ou un autre dans la liste, le réglage du mode d\'ouverture permettra à la fenêtre d\'apparaître ouverte ou d\'afficher les symboles 2D d\'ouverture en plan ou en élévation.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">

## Options

-   L\'objet Windows partage les propriétés communes et le comportement de tous les objet [Arch Composants](Arch_Component/fr.md)
-   Si la case \'\' Auto-include \'\' est cochée , la fenêtre ne sera pas insérée dans l\'objet hôte.
-   Ajoutez une fenêtre sélectionnée sur un [mur](Arch_Wall/fr.md), pressez sur le bouton **<img src="images/Arch_Add.svg" width=16px> [ajouter](Arch_Add/fr.md)**.
-   Supprimez la fenêtre sélectionnée du [mur](Arch_Wall/fr.md), pressez sur le bouton **<img src="images/Arch_Remove.svg" width=16px> [effacer](Arch_Remove/fr.md)**.
-   Lors de l\'utilisation des préréglages, il est souvent commode de transformer le \"Near\" [Draft Accrochage](Draft_Snap/fr.md), donc vous pouvez coller votre fenêtre sur une face existante.
-   L\'emplacement créé par une fenêtre sur objet hôte est déterminé par deux propriétés: {{PropertyData/fr|Hole Depth}} (Profondeur de l\'emplacement) et {{PropertyData/fr|Hole Wire}} (Lignes de l\'emplacement) ({{Version/fr|0.17}}). Le numéro d\'emplacement de la ligne peut être sélectionné dans la vue 3D ou dans le panneau de tâches de la fenêtre en double-cliquant sur la fenêtre dans l\'arborescence de la Vue combinée
-   L\'outil Windows peut utiliser la fonction [Arch Matériaux multiples](Arch_MultiMaterial/fr.md). La fenêtre cherchera dans Multi-Material les couches de matériaux avec le même nom pour chacun des composants de la fenêtre et l\'utiliser si le composant est trouvé. Par exemple, un composant appelé \"OuterFrame\" cherchera dans le Multi-Material attaché, une couche de matériau appelée \"OuterFrame\". Si une telle couche de matériau est trouvée, son matériau sera attribué au composant OuterFrame. La valeur de l\'épaisseur de la couche de matériau n\'est pas prise en compte.

## Ouvertures


**Voir aussi:**

[Tutoriel pour les fenêtres ouvertes](Tutorial_for_open_windows/fr.md)

Les portes et fenêtres peuvent apparaître partiellement ou entièrement ouvertes dans le modèle 3D ou peuvent afficher des symboles d\'ouverture en plan et/ou en élévation. Par conséquent, elles apparaîtront également dans les vues 2D extraites générées par une [Draft Projection 2D d\'une forme](Draft_Shape2DView/fr.md) ou l\'[atelier TechDraw](TechDraw_Workbench/fr.md) ou l\'[atelier Drawing](Drawing_Workbench/fr.md). Pour obtenir ceci, au moins un des composants de la fenêtre doit avoir une charnière et un mode d\'ouverture défini (voir la section [Composants de construction](#Cr.C3.A9ation_de_composants.md) ci-dessus). Ensuite, en utilisant les propriétés {{PropertyData/fr|Opening}}, {{PropertyData/fr|Symbol Plan}} ou {{PropertyData/fr|Symbol Elevation}}, vous pouvez configurer l\'apparence de la fenêtre:

<img alt="" src=images/Arch_window_openings.png  style="width:600px;"> 
*Porte indiquant le plan des symboles, leur élévation et les propriétés d'ouverture au travail*

## Définition des types de fenêtres {#définition_des_types_de_fenêtres}

Les fenêtres peuvent également tirer parti d\'autres outils, notamment des processus de travail de [PartDesign](PartDesign_Workbench/fr.md), pour définir un type. Un type est un objet qui définit la forme de la fenêtre. Il est particulièrement bien adapté pour travailler avec [App Parts](App_Part/fr.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Téléchargez le fichier d\'exemple ci-dessus](https://github.com/FreeCAD/Examples/blob/master/Arch_Example_Files/Window_Type.FCStd)

### Exemple de processus de travail {#exemple_de_processus_de_travail}

-   Créez un objet de cadre de fenêtre, un panneau de verre et tout autre composant de fenêtre dont vous avez besoin, à l\'aide des outils [atelier Part](Part/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md).
-   Par exemple, créez une esquisse rectangulaire de base pour votre fenêtre, puis une esquisse de profil pour le cadre et créez un [Part Balayage](Part_Sweep/fr.md) pour balayer le profil autour de l\'esquisse de base. Créez un [Part Décalage 2D](Part_Offset2D/fr.md) à partir de l\'esquisse de base, puis un [Part Extrusion](Part_Extrude/fr.md) pour créer le panneau de verre
-   Assurez-vous que toutes ces pièces ont un nom unique et significatif (par exemple, \"Cadre\" ou \"Panneau en verre\")
-   Créez un [App Part](App_Part/fr.md) et placez tous vos sous-composants dedans
-   Créez un volume à soustraire du mur, par exemple en extrudant l\'esquisse de base. Ajoutez ce volume à App Part. Assurez-vous que le volume est désactivé.
-   Si vous utilisez FreeCAD version 0.19 ou ultérieure, vous pouvez ajouter 3 propriétés à votre partie d\'application, en cliquant avec le bouton droit sur sa vue des propriétés et en cochant \"Afficher tout\". Ajoutez les propriétés suivantes (toutes sont facultatives, le groupe n\'a pas d\'importance):
    -   **Height** en tant que PropertyLength et le lier, par exemple, à une contrainte verticale de votre esquisse de base
    -   **Width** en tant que PropertyLength et le lier, par exemple, à une contrainte horizontale de votre esquisse de base
    -   **Subvolume** en tant que PropertyLink et le lier au volume à soustraire que nous avons créé ci-dessus
    -   **Tag** en tant que PropertyString

### Materiaux

Notre type de fenêtre est maintenant prêt. Nous pouvons créer des objets de fenêtre à partir de celui-ci, simplement en sélectionnant la partie d\'application et en appuyant sur le bouton de la fenêtre. Les propriétés \"Height\", \"Width\", \"Subvolume\" et \"Tag\" de la fenêtre seront liées à la propriété correspondante de la partie d\'application, si elle existe.

Pour créer un matériau pour des fenêtres basées sur un type:

-   Créer un [Arch Matériaux multiples](Arch_MultiMaterial/fr.md)
-   Créez une entrée dans le multi-matériau pour chaque composant de votre partie d\'application. Par exemple, un «cadre», un «panneau de verre» comme nous l\'avons utilisé ci-dessus. Assurez-vous d\'utiliser exactement le même nom.
-   Attribuer ce multi-matériau à chacune des fenêtres dérivées du même type

Vous pouvez utiliser tout autre type de workflow que celui décrit ci-dessus, les points importants à retenir sont:

-   L\'objet type doit être un seul objet, quel que soit le type (App Part, PartDesign Body, Part Compound, ou même Arch Window)
-   L\'objet type doit avoir une propriété \"Subvolume\" (liée à la propriété Subvolume de la fenêtre) pour que les ouvertures des objets hôtes fonctionnent
-   L\'objet type doit avoir une propriété \"Group\" avec différents enfants portant le même nom que les éléments multi-matériaux pour que les multi-matériaux fonctionnent.

## Propriétés

-    {{PropertyData/fr|Window Parts}}: une liste chaîne (5 chaînes par composant, réglez les options des composants ci-dessus)

-    {{PropertyData/fr|Louvre Width}}: Si un des composants est réglé sur \"Louvres\", cette propriété définit la taille des éléments de la persienne

-    {{PropertyData/fr|Louvre Spacing}}: Si un des composants est réglé sur \"Louvres\", cette propriété défini l\'espacement entre les éléments de la persienne

-    {{PropertyData/fr|Hole Wire}}: Le nombre de lignes pour l\'objet de base est utilisé pour créer l\'emplacement dans l\'objet hôte de cette fenêtre. Cette valeur peut être graphiquement en double cliquant sur la fenêtre dans la vue 3D. Si vous donner la valeur 0 la fenêtre sera automatiquement construite sur la plus grande valeur de la ligne de l\'emplacement.

-    {{PropertyData/fr|Window Parts}}: Une liste d\'éléments (5 éléments par composant, définissant les options de composant ci-dessus)

-    {{PropertyData/fr|Louvre Width}}: Si un des composants est réglé sur \"Louvres\", cette propriété définit la taille des éléments du louvre

-    {{PropertyData/fr|Louvre Spacing}}: Si un des composants est réglé sur \"Louvres\", cette propriété définit l\'espace entre les éléments du louvre

-    {{PropertyData/fr|Opening}}: Tous les composants dont le mode d\'ouverture est défini, et à condition qu\'une charnière soit définie dans ceux-ci ou dans un composant antérieur de la liste, apparaissent ouverts par un pourcentage défini par cette valeur

-    {{PropertyData/fr|Symbol Plan}}: Affiche le symbole d\'ouverture dans le plan 2D

-    {{PropertyData/fr|Symbol Elevation}}: Affiche le symbole d\'ouverture en élévation dans le plan 2D

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Fenêtre peut être utilisé à l\'intérieur d\'une [macro](macros/fr.md), et, à partir de la console [Python](Python/fr.md), en utilisant la fonction suivante : 
```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```

-   Créer un objet `Window` basé sur `baseobj`, qui devrait être un [fil](Draft_Wire/fr.md) fermé ou une [esquisse](Sketcher_Sketch/fr.md)
-   Si disponible, définir la largeur `width`, hauteur `height` et le nom `name` (label) de la fenêtre.
-   Si `baseobj` n\'est pas une forme fermée, l\'outil ne pourra pas créer une figure solide correcte.

Exemple: 
```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

Vous pouvez également créer une fenêtre à partir d\'un préréglage. 
```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```

-   Crée un objet `Window` basé sur `windowtype` qui devrait être l\'un des noms définis dans `Arch.WindowPresets`
    -   Certains de ces préréglages sont: `"Fixed"` (fixe), `"Open 1-pane"` (un battant ouvert), {{incode | ""Open 2-pane"}} (2 battants ouverts), `"Sash 2-pane"` (2 vantaux), {{incode |"Sliding 2-pane"}} (2 volets coulissants), `"Simple door"` (Porte simple), `"Glass door"` (Porte vitrée), `"Sliding 4-pane"` (4 volets coulissants).

-    `width`et `height` définissent la taille totale de l\'objet en millimètres.

-   Les paramètres `h1`, `h2`, `h3` (décalages verticaux), `w1`, `w2` (largeurs), `o1` et `o2` (décalages horizontaux) spécifient des distances différentes en millimètres et dépendent du type de préréglage en cours de création.

-   Si un `placement` est donné, il est utilisé.

Exemple: 
```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```









