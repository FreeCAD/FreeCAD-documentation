---
- GuiCommand:/fr
   Name:Sketcher_MapSketch
   Name/fr:Sketcher Appliquer une esquisse sur une face
   MenuLocation:Part Design/Sketch → Appliquer une esquisse sur une face...
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md), [PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[Sketcher Créer une esquisse](Sketcher_NewSketch/fr.md)
---

## Description

Cet outil applique une esquisse existante sur la face d\'une forme. Les fonctions PartDesign créées à partir de l\'esquisse seront fusionnées au solide sous-jacent dans le case de fonctions d\'ajout de matière (Protrusion, Révolution) ou seront soustraites du solide sous-jacent dans le cas de fonctions d\'enlèvement de matière (Cavité, Enlèvement de matière par révolution).

Veuillez noter que cet outil n\'est pas utilisé pour créer de nouvelles esquisses. Il ne fait qu\'appliquer, ou ré-appliquer une esquisse existante sur la face d\'un solide ou d\'une fonction PartDesign. Les usages typiques sont :

-   L\'esquisse a été créée sur un plan standard (XY, XZ, YZ) et vous voulez l\'appliquer sur la face d\'une solide afin d\'ajouter une fonction au solide.
-   L\'esquisse avait été appliquée à une face du solide, mais vous désirez l\'appliquer sur une face différente.
-   La réparation d\'un modèle brisé (avec des fonctions échouées).

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">

## Utilisation

-   Sélectionnez la face d\'une fonction PartDesign ou d\'un solide.
-   Cliquez sur l\'icône **<img src="images/Sketcher_MapSketch.svg" width=16px> [Appliquer une esquisse sur une face](Sketcher_MapSketch/fr.md)** de la barre d\'outils (ou encore depuis le menu PartDesign ou Sketch, selon l\'atelier actif)
-   Dans la fenêtre de dialogue **Sélection de l\'esquisse** s\'ouvre, sélectionnez l\'esquisse à appliquer depuis la liste puis cliquez sur OK.
-   Vous êtes amené sur le mode d\'édition de l\'esquisse.

## Utiliser pour réparer un modèle cassé {#utiliser_pour_réparer_un_modèle_cassé}

L\'outil Appliquer une esquisse sur une face est souvent utilisé pour réparer un modèle cassé.

Un cas typique est quand le graphique de dépendences est cassé. (Vous pouvez visionner le graphique de dépendances via le menu **Outils** → **[Graphique de dépendances](Std_DependencyGraph/fr.md)**.) Ceci peut survenir quand vous supprimez une fonction au milieu de votre arborescence de modèle. Dans l\'exemple suivant, nous casserons puis réparerons un modèle.

Voici le modèle de base. Il est formé d\'une protrusion (Pad), une cavité (Pocket) et une protrusion (Pad001) à l\'intérieur de la cavité. Notez que le graphique de dépendances est linéaire.

![](images/JschremppFCADEdit1.png )

Ici, nous avons supprimé la cavité et l\'esquisse qui a créé la cavité (Pocket et Sketch001). Notez que le graphe de dépendance est cassé. Pour réparer ce modèle, nous voulons rattacher l\'esquisse Sketch002 à la face supérieure de la protrusion (Pad). Dans la vue du modèle, on peut voir qu\'il serait facile de sélectionner la mauvaise face.

![](images/JschremppFCADEdit2.png )

Pour réparer le modèle, nous devons d\'abord basculer la visibilité des solides. Nous cachons Pad001 et rendons Pad visible.

![](images/JschremppFCADEdit3.png )

Maintenant, nous sélectionnons la face de dessus de la protrusion (Pad) puis cliquons sur l\'outil Appliquer une esquisse sur une face. Dans la fenêtre de dialogue qui apparaît, nous sélectionnons Sketch002. Notre modèle est maintenant réparé. Dans l\'arborescence du modèle, nous rendons Pad001 visible et cachons Pad, et le modèle correct est alors affiché.

![](images/JschremppFCADEdit4.png )





{{Sketcher Tools navi

}}  
