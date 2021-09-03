---
- GuiCommand:/ro
   Name:Part Chamfer
   Name/ro:Part Chamfer
   MenuLocation:Part → Chamfer
   Workbenches:[Part](Part_Workbench/ro.md), Complete
   SeeAlso:
---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Șanfrenarea marginii sau a marginilor selectate ale unui obiect. O casetă de dialog vă permite să alegeți marginea (marginile) la care să lucrați și să modificați diferitele setări ale șanfrenului.


</div>

![Chamfer example](images/Chamfer-example.png )

## Usage


<div class="mw-translate-fuzzy">

## Cum se utilizează {#cum_se_utilizează}

1.  Apăsați butonul **<img src="images/Part_Chamfer.svg" width=30px>** din aelierul [Part Workbench](Part_Workbench.md). Alternativ, puteți selecta {{MenuCommand|Part → Chamfer}}.
2.  Selectați forma care urmează să se șanfrenată din fereastra de dialog.
3.  Selectați margini care urmează să fie șanfrenate, bifând caseta corespunzătoare în fereastra de precizie sau selectându-le direct pe model.
4.  Editați parametrii chamfer.
5.  Apăsați OK pentru a închide caseta de dialog și a aplica șanfrenul.

## Utilisation

Démarrez l\'outil **![](images/)_[Chanfrein](Part_Chamfer/fr.md)** qui se trouve dans \" **Boîte déroulante des ateliers → **Part [24px|Part](File:Workbench_Part.png.md)** → **![](images/)_[Chanfrein](Part_Chamfer/fr.md)**** depuis la barre d\'outils, ou le menu. Vous pouvez sélectionner l\'objet au préalable.
Si la forme n\'a pas été sélectionnée au préalable, sélectionnez-la dans la **liste déroulante** du panneau des Tâches.
Sélectionnez le type de congé (Chanfrein), soit rayon constant (par défaut), ou rayon variable.
Sélectionnez les arêtes, soit dans la vue 3D, ou en les cochant, dans la liste du panneau des Tâches.
Réglez la valeur du rayon, puis cliquez **OK** pour valider.


</div>

## Options


<div class="mw-translate-fuzzy">

## Opțiuni

![Dialog-chamfer](images/Dialog-chamfer.png )

-   Când selectați marginile modelului, aveți opțiunea de a selecta marginea sau fațeta. Selectând fațeta veți selecta toate marginile fațetei respective.
-   Fascicul de lungime variabilă de lungime variabilă cu lungime constantă.
    -   O șanfrenă cu o lungime constantă va crea un șanfren cu muchii echidistant față de marginea originală la distanța specificată.

Un șanfren de lungime variabilă va avea marginile care pot fi setate la distanțe diferite de marginea originală, permițându-vă să creați un șanfren la un unghi variabil.

## Options {#options_1}

### Vue combinée → Tâche {#vue_combinée_tâche}

<img alt="Tâche options chanfrein" src=images/Part_Chamfer_fr_05.png  style="width:240px;"> {{TitreTache|<img src="images/Part_Fillet.png" width=16px> Chanfrein des arêtes}} {{TitreProprietes|Forme}}

-    {{OngletTache|Forme sélectionnée}}: Si une forme a été sélectionnée, elle est automatiquement affichée. Si aucune forme n\'est sélectionnée, vous pouvez sélectionner votre forme dans cette boîte déroulante. Cette boîte déroulante <img alt="" src=images/Tache_PartFillet_Fillet_fr_00.png  style="width:96px;">, liste toutes les formes qui peuvent être utilisées par l\'outil **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, vous pouvez sélectionner votre forme dans cette liste, (ou avant de sélectionner l\'outil **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, directement dans la fenêtre 3D, et, elle sera automatiquement affichée). (Défaut, **Aucune sélection**).


{{TitreProprietes|Paramètres de congé}}

-    ** Tous **: Sélectionne toutes les arêtes de la forme sélectionnée.

-    ** Aucun **: Décoche toutes les arêtes de la forme sélectionnée.
    Chaque arête peut être cochée séparément.

-    {{OngletTache|Type de congé}}: Cette option, vous permet de choisir le type de chanfrein a effectuer, <img alt="" src=images/Tache_PartFillet_Rayon_fr_00.png  style="width:96px;">, **Rayon constant**, ou **Rayon variable**. (Défaut, **Rayon constant**).

Sur cette exemple l\'option est réglée sur **[Rayon constant](#Chanfrein_symétrique.md)**, et, un seul réglage de rayon est possible.

-    {{OngletTache|Rayon}}: Réglage du paramètre rayon, ici un seul rayon, pour un **Rayon constant**, pour un **![](images/)_[chanfrein](Part_Chamfer/fr.md)** **symétrique**.




<img alt="Tâche options Chanfrein" src=images/Part_Chamfer_fr_06.png  style="width:240px;">
Sur cette exemple l\'option est réglée sur **[Rayon variable](#Chanfrein_asymétrique.md)**, et, deux réglages de rayons sont demandés.

-    {{OngletTache|Rayon}}: Réglage des paramètres rayon, ici deux rayons sont a entrer, **Rayon initial**, et, **Rayon final**, pour avoir un **Rayon variable**, pour un **![](images/)_[chanfrein](Part_Chamfer/fr.md)** **asymétrique**. (Défaut, **Rayon constant**).





</div>

## Properties


<div class="mw-translate-fuzzy">

## Proprietăți

![Part\_Chamfer Properties](images/Part_Chamfer-Properties.png )

## Propriétés

### Vue combinée → Propriétés Vue {#vue_combinée_propriétés_vue}

<img alt="Propriétés Vue Chanfrein" src=images/Part_Chamfer_fr_03.png  style="width:240px;"> {{PartOngletVue_2/fr}} 

### Vue combinée → Propriétés Données {#vue_combinée_propriétés_données}

<img alt="Propriétés Données" src=images/Part_Chamfer_fr_04.png  style="width:240px;">


{{TitreProprietes|Base}}

-    {{ProprieteDonnees|Label}}: Label donné à la forme, modifiable à volonté.

-    {{ProprieteDonnees|Placement}}: \[(**0,00 0,00 1,00**);**0,00**;(**0,00 0,00 0,00**)\], donne l\'ensemble des données **Angle, Axis**, et, **Position** ci dessous.
    Si vous sélectionnez, le titre **Placement** <img alt="Options Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">, un bouton avec **trois petits points** s\'affiche, en cliquant sur ce bouton **''' ... '''**, vous avez accès à la fenêtre d\'options **[Tâche Placement](Tasks_Placement/fr.md)**.

-    {{ProprieteDonnees|Angle}}: Angle de rotation par rapport aux coordonnées **X, Y, Z**. (Défaut, **0,00°**).

-    {{ProprieteDonnees|Axis}}: Cette option spécifie l\'axe des axes autour desquels la pièce de révolution créée doit être pivotée **PAS RÉVOLUTIONNÉE** (la valeur exacte du pivotement est défini par l\'option **Angle** ci-dessus).

Cette option demande trois arguments, qui sont passés sous forme de nombres dans les cases de la boîte à outils, définissants les coordonnées **x, y ou z**, .
La modification d\'une valeur de plus d\'un axes provoque la rotation avec l\'angle de chaque axe.
**Par exemple :** nous déterminons un angle de **15°**, nous spécifions une valeur de **1,0 pour x** et **2,0 pour y**, cette configuration, aura pour effet, une rotation finale de la pièce qui sera de, **\" 15° dans l\'axe x \"** et **\" 30° dans l\'axe y \"**.

:\* {{ProprieteDonnees| X }} : Angle à donner dans la direction **X** . (Défaut, **0,00**).

:\* {{ProprieteDonnees| Y }} : Angle à donner dans la direction **Y** . (Défaut, **0,00**).

:\* {{ProprieteDonnees| Z }} : Angle à donner dans la direction **Z** . (Défaut, **1,00**).

-    {{ProprieteDonnees|Position}}: **\[0,00 0,00 0,00\]** récapitulation des coordonnées de position, par rapport coordonnée d\'origine **0,00 0,00 0,00**.

:\* {{ProprieteDonnees| X }} : Déplacement à donner dans la direction **X** .(Défaut, **0,00**).

:\* {{ProprieteDonnees| Y }} : Déplacement à donner dans la direction **Y** .(Défaut, **0,00**).

:\* {{ProprieteDonnees| Z }} : Déplacement à donner dans la direction **Z** .(Défaut, **0,00**). 


</div>


{{Properties_Title|Base}}


<div class="mw-translate-fuzzy">


{{Properties_Title|Base}}

-    **Base**: The shape onto which the chamfer is to be applied.

-    **Placement**: Specifies the orientation and position of the shape in the 3D space.

-    **Label**: Label given to the object. Change to suit your needs.




## Propriétés {#propriétés_1}

### Vue combinée → Propriétés Vue {#vue_combinée_propriétés_vue_1}

<img alt="Propriétés Vue Chanfrein" src=images/Part_Chamfer_fr_03.png  style="width:240px;"> {{PartOngletVue_2/fr}} 

### Vue combinée → Propriétés Données {#vue_combinée_propriétés_données_1}

<img alt="Propriétés Données" src=images/Part_Chamfer_fr_04.png  style="width:240px;">


{{TitreProprietes|Base}}

-    {{ProprieteDonnees|Label}}: Label donné à la forme, modifiable à volonté.

-    {{ProprieteDonnees|Placement}}: \[(**0,00 0,00 1,00**);**0,00**;(**0,00 0,00 0,00**)\], donne l\'ensemble des données **Angle, Axis**, et, **Position** ci dessous.
    Si vous sélectionnez, le titre **Placement** <img alt="Options Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">, un bouton avec **trois petits points** s\'affiche, en cliquant sur ce bouton **''' ... '''**, vous avez accès à la fenêtre d\'options **[Tâche Placement](Tasks_Placement/fr.md)**.

-    {{ProprieteDonnees|Angle}}: Angle de rotation par rapport aux coordonnées **X, Y, Z**. (Défaut, **0,00°**).

-    {{ProprieteDonnees|Axis}}: Cette option spécifie l\'axe des axes autour desquels la pièce de révolution créée doit être pivotée **PAS RÉVOLUTIONNÉE** (la valeur exacte du pivotement est défini par l\'option **Angle** ci-dessus).

Cette option demande trois arguments, qui sont passés sous forme de nombres dans les cases de la boîte à outils, définissants les coordonnées **x, y ou z**, .
La modification d\'une valeur de plus d\'un axes provoque la rotation avec l\'angle de chaque axe.
**Par exemple :** nous déterminons un angle de **15°**, nous spécifions une valeur de **1,0 pour x** et **2,0 pour y**, cette configuration, aura pour effet, une rotation finale de la pièce qui sera de, **\" 15° dans l\'axe x \"** et **\" 30° dans l\'axe y \"**.

:\* {{ProprieteDonnees| X }} : Angle à donner dans la direction **X** . (Défaut, **0,00**).

:\* {{ProprieteDonnees| Y }} : Angle à donner dans la direction **Y** . (Défaut, **0,00**).

:\* {{ProprieteDonnees| Z }} : Angle à donner dans la direction **Z** . (Défaut, **1,00**).

-    {{ProprieteDonnees|Position}}: **\[0,00 0,00 0,00\]** récapitulation des coordonnées de position, par rapport coordonnée d\'origine **0,00 0,00 0,00**.

:\* {{ProprieteDonnees| X }} : Déplacement à donner dans la direction **X** .(Défaut, **0,00**).

:\* {{ProprieteDonnees| Y }} : Déplacement à donner dans la direction **Y** .(Défaut, **0,00**).

:\* {{ProprieteDonnees| Z }} : Déplacement à donner dans la direction **Z** .(Défaut, **0,00**). 


</div>

## Limitations

Chamfer might do nothing if the result would touch or cross the next adjacent edge. So if you do not get the expected result, try with a smaller value. This is the same for <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Fillet](Part_Fillet.md).

Also note that the Chamfer feature is affected by the [Topological naming problem](Topological_naming_problem.md) when the any change is done to a modeling step earlier in the chain that affects the number of facets or vertices. This could cause unpredictable result. Until that is resolved (possibly with V0.20) it is advised to apply Chamfer and <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Fillet](Part_Fillet.md) operations at the last steps in the chain.

## Scripting


<div class="mw-translate-fuzzy">

## Script

Instrumentul Chamfer poate fi utilizat în [macros](macros.md) și din consolă python prin adăugarea unui obiect Chamfer în document. Cet outil applique des **![](images/)_[chanfreins](Part_Chamfer/fr.md)**, sur les arêtes sélectionnées d\'un objet. Une boite de dialogue vous permet de choisir sur quels objets, et, sur quelles arêtes travailler.
<img alt="Chanfreins" src=images/Part_Chamfer_fr_01.png  style="width:480px;">


## Utilisation {#utilisation_1}

Démarrez l\'outil **![](images/)_[Chanfrein](Part_Chamfer/fr.md)** qui se trouve dans \" **Boîte déroulante des ateliers → **Part [24px|Part](File:Workbench_Part.png.md)** → **![](images/)_[Chanfrein](Part_Chamfer/fr.md)**** depuis la barre d\'outils, ou le menu. Vous pouvez sélectionner l\'objet au préalable.
Si la forme n\'a pas été sélectionnée au préalable, sélectionnez-la dans la **liste déroulante** du panneau des Tâches.
Sélectionnez le type de congé (Chanfrein), soit rayon constant (par défaut), ou rayon variable.
Sélectionnez les arêtes, soit dans la vue 3D, ou en les cochant, dans la liste du panneau des Tâches.
Réglez la valeur du rayon, puis cliquez **OK** pour valider.

## Options {#options_2}

### Vue combinée → Tâche {#vue_combinée_tâche_1}

<img alt="Tâche options chanfrein" src=images/Part_Chamfer_fr_05.png  style="width:240px;"> {{TitreTache|<img src="images/Part_Fillet.png" width=16px> Chanfrein des arêtes}} {{TitreProprietes|Forme}}

-    {{OngletTache|Forme sélectionnée}}: Si une forme a été sélectionnée, elle est automatiquement affichée. Si aucune forme n\'est sélectionnée, vous pouvez sélectionner votre forme dans cette boîte déroulante. Cette boîte déroulante <img alt="" src=images/Tache_PartFillet_Fillet_fr_00.png  style="width:96px;">, liste toutes les formes qui peuvent être utilisées par l\'outil **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, vous pouvez sélectionner votre forme dans cette liste, (ou avant de sélectionner l\'outil **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, directement dans la fenêtre 3D, et, elle sera automatiquement affichée). (Défaut, **Aucune sélection**).


{{TitreProprietes|Paramètres de congé}}

-    ** Tous **: Sélectionne toutes les arêtes de la forme sélectionnée.

-    ** Aucun **: Décoche toutes les arêtes de la forme sélectionnée.
    Chaque arête peut être cochée séparément.

-    {{OngletTache|Type de congé}}: Cette option, vous permet de choisir le type de chanfrein a effectuer, <img alt="" src=images/Tache_PartFillet_Rayon_fr_00.png  style="width:96px;">, **Rayon constant**, ou **Rayon variable**. (Défaut, **Rayon constant**).

Sur cette exemple l\'option est réglée sur **[Rayon constant](#Chanfrein_symétrique.md)**, et, un seul réglage de rayon est possible.

-    {{OngletTache|Rayon}}: Réglage du paramètre rayon, ici un seul rayon, pour un **Rayon constant**, pour un **![](images/)_[chanfrein](Part_Chamfer/fr.md)** **symétrique**.




<img alt="Tâche options Chanfrein" src=images/Part_Chamfer_fr_06.png  style="width:240px;">
Sur cette exemple l\'option est réglée sur **[Rayon variable](#Chanfrein_asymétrique.md)**, et, deux réglages de rayons sont demandés.

-    {{OngletTache|Rayon}}: Réglage des paramètres rayon, ici deux rayons sont a entrer, **Rayon initial**, et, **Rayon final**, pour avoir un **Rayon variable**, pour un **![](images/)_[chanfrein](Part_Chamfer/fr.md)** **asymétrique**. (Défaut, **Rayon constant**).




## Propriétés {#propriétés_2}

### Vue combinée → Propriétés Vue {#vue_combinée_propriétés_vue_2}

<img alt="Propriétés Vue Chanfrein" src=images/Part_Chamfer_fr_03.png  style="width:240px;"> {{PartOngletVue_2/fr}} 

### Vue combinée → Propriétés Données {#vue_combinée_propriétés_données_2}

<img alt="Propriétés Données" src=images/Part_Chamfer_fr_04.png  style="width:240px;">


{{TitreProprietes|Base}}

-    {{ProprieteDonnees|Label}}: Label donné à la forme, modifiable à volonté.

-    {{ProprieteDonnees|Placement}}: \[(**0,00 0,00 1,00**);**0,00**;(**0,00 0,00 0,00**)\], donne l\'ensemble des données **Angle, Axis**, et, **Position** ci dessous.
    Si vous sélectionnez, le titre **Placement** <img alt="Options Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">, un bouton avec **trois petits points** s\'affiche, en cliquant sur ce bouton **''' ... '''**, vous avez accès à la fenêtre d\'options **[Tâche Placement](Tasks_Placement/fr.md)**.

-    {{ProprieteDonnees|Angle}}: Angle de rotation par rapport aux coordonnées **X, Y, Z**. (Défaut, **0,00°**).

-    {{ProprieteDonnees|Axis}}: Cette option spécifie l\'axe des axes autour desquels la pièce de révolution créée doit être pivotée **PAS RÉVOLUTIONNÉE** (la valeur exacte du pivotement est défini par l\'option **Angle** ci-dessus).

Cette option demande trois arguments, qui sont passés sous forme de nombres dans les cases de la boîte à outils, définissants les coordonnées **x, y ou z**, .
La modification d\'une valeur de plus d\'un axes provoque la rotation avec l\'angle de chaque axe.
**Par exemple :** nous déterminons un angle de **15°**, nous spécifions une valeur de **1,0 pour x** et **2,0 pour y**, cette configuration, aura pour effet, une rotation finale de la pièce qui sera de, **\" 15° dans l\'axe x \"** et **\" 30° dans l\'axe y \"**.

:\* {{ProprieteDonnees| X }} : Angle à donner dans la direction **X** . (Défaut, **0,00**).

:\* {{ProprieteDonnees| Y }} : Angle à donner dans la direction **Y** . (Défaut, **0,00**).

:\* {{ProprieteDonnees| Z }} : Angle à donner dans la direction **Z** . (Défaut, **1,00**).

-    {{ProprieteDonnees|Position}}: **\[0,00 0,00 0,00\]** récapitulation des coordonnées de position, par rapport coordonnée d\'origine **0,00 0,00 0,00**.

:\* {{ProprieteDonnees| X }} : Déplacement à donner dans la direction **X** .(Défaut, **0,00**).

:\* {{ProprieteDonnees| Y }} : Déplacement à donner dans la direction **Y** .(Défaut, **0,00**).

:\* {{ProprieteDonnees| Z }} : Déplacement à donner dans la direction **Z** .(Défaut, **0,00**). 

## Exemple

### Chanfrein symétrique {#chanfrein_symétrique}


<center>

Image:Part\_Fillet\_fr\_07.png\|Sélectionnons une arête, sur la forme à modifier, Image:Part\_Fillet\_fr\_08.png\|une fois sélectionnée, la fenêtre de propriétés de la forme s\'affiche.


</center>



<center>

Image:Part\_Chamfer\_fr\_09.png\|Sélectionnez l\'outil **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, Image:Part\_Chamfer\_fr\_10.png\|une nouvelle fenêtre s\'affiche, la fenêtre des options du **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, notre forme **Box001** est affichée dans {{OngletTache|Forme sélectionnée}}, faisons glisser l'ascenseur,


</center>



<center>

Image:Part\_Chamfer\_fr\_11.png\|pour voir notre arête cochée. Image:Part\_Chamfer\_fr\_12.png\|Modifions notre rayon à **5 mm**,


</center>



<center>

Image:Part\_Chamfer\_fr\_13.png\|et réglons notre paramètre {{OngletTache|Type de congé}} sur **Rayon constant**. (Valeur, par défaut, **Rayon constant**). Image:Part\_Chamfer\_fr\_14.png\|Validons avec ** OK **, pour voir notre **![](images/)_[Chanfrein](Part_Chamfer/fr.md)** s\'effectuer.


</center>

===Chanfrein asymétrique===


<center>

Image:Part\_Chamfer\_fr\_15.png\|Sélectionnons notre deuxième arête à modifier. Image:Part\_Chamfer\_fr\_16.png\|De nouveau notre {{OngletTache|Forme sélectionnée}} **Box** s\'affiche, et, notre arête est cochée.


</center>



<center>

Image:Part\_Chamfer\_fr\_17.png\|Réglons notre paramètre {{OngletTache|Type de congé}} sur **Rayon variable**. Image:Part\_Chamfer\_fr\_18.png\|Une nouvelle fenêtre s\'affiche, et, ici, il y a deux paramètres de rayons à entrer.


</center>



<center>

Image:Part\_Chamfer\_fr\_19.png\|Entrons **5 mm**, pour le rayon de départ, Image:Part\_Chamfer\_fr\_20.png\|et, **20 mm** pour le rayon d\'arrivée.


</center>



<center>

Image:Part\_Chamfer\_fr\_21.png\|Validons avec ** OK **, pour voir s'effectuer notre **chanfrein variable**. Image:Part\_Chamfer\_fr\_22.png\|Une nouvelle icône par opération s\'affiche dans la **Vue combinée**, renseignant l(es)\'opération(s).
Si vous cliquez sur la flèche, vous pouvez voir les formes d\'origine, qui ont servi dans l\'opération de **![](images/)_[Chanfrein](Part_Chamfer/fr.md)**.
Les formes originales peuvent être effacées, pour ne conserver que le produit final.


</center>


## Comparaison Chanfrein PartDesign [16px\|text-top=Chanfrein\|link=PartDesign\_Chamfer/fr](File:PartDesign_Chamfer.png.md), et, Chanfrein Part [16px\|text-top=Chanfrein\|link=Part\_Chamfer/fr](Image:Part_Chamfer.png.md) {#comparaison_chanfrein_partdesign_16pxtext_topchanfreinlinkpartdesign_chamferfr_et_chanfrein_part_16pxtext_topchanfreinlinkpart_chamferfr}

**Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ne doit pas être confondu avec son équivalent de l\'atelier Part **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)****.
Bien qu\'ils partagent la même icône, ces outils sont différents, et s\'utilisent différemment.

### Voici quelques différences : {#voici_quelques_différences}

-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** est *paramétrique*. Après l\'application d\'un **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)**, sa dimension peut être modifié ; ce n\'est pas le cas du **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)**.
-   Les arêtes doivent être sélectionnées avant de démarrer le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)**. Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)**, quant à lui, peut être lancé, puis, suivi de la sélection du solide, et, enfin des arêtes.
-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ajoute une entrée distincte dans l\'arborescence Projet. Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)** devient le parent de l\'objet auquel il a été appliqué.
-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** affiche un aperçu en temps réel de l\'application du chanfrein avant la validation de la fonction.
-   Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)** supporte les dimensions variables (avec une dimension de départ, et, une dimension d\'arrivée). Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ne le permet pas.





</div>

**Exemplu de Script:**

## Exemple {#exemple_1}

### Chanfrein symétrique {#chanfrein_symétrique_1}


<center>

Image:Part\_Fillet\_fr\_07.png\|Sélectionnons une arête, sur la forme à modifier, Image:Part\_Fillet\_fr\_08.png\|une fois sélectionnée, la fenêtre de propriétés de la forme s\'affiche.


</center>



<center>

Image:Part\_Chamfer\_fr\_09.png\|Sélectionnez l\'outil **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, Image:Part\_Chamfer\_fr\_10.png\|une nouvelle fenêtre s\'affiche, la fenêtre des options du **![](images/)_[chanfrein](Part_Chamfer/fr.md)**, notre forme **Box001** est affichée dans {{OngletTache|Forme sélectionnée}}, faisons glisser l'ascenseur,


</center>



<center>

Image:Part\_Chamfer\_fr\_11.png\|pour voir notre arête cochée. Image:Part\_Chamfer\_fr\_12.png\|Modifions notre rayon à **5 mm**,


</center>



<center>

Image:Part\_Chamfer\_fr\_13.png\|et réglons notre paramètre {{OngletTache|Type de congé}} sur **Rayon constant**. (Valeur, par défaut, **Rayon constant**). Image:Part\_Chamfer\_fr\_14.png\|Validons avec ** OK **, pour voir notre **![](images/)_[Chanfrein](Part_Chamfer/fr.md)** s\'effectuer.


</center>

===Chanfrein asymétrique===


<center>

Image:Part\_Chamfer\_fr\_15.png\|Sélectionnons notre deuxième arête à modifier. Image:Part\_Chamfer\_fr\_16.png\|De nouveau notre {{OngletTache|Forme sélectionnée}} **Box** s\'affiche, et, notre arête est cochée.


</center>



<center>

Image:Part\_Chamfer\_fr\_17.png\|Réglons notre paramètre {{OngletTache|Type de congé}} sur **Rayon variable**. Image:Part\_Chamfer\_fr\_18.png\|Une nouvelle fenêtre s\'affiche, et, ici, il y a deux paramètres de rayons à entrer.


</center>



<center>

Image:Part\_Chamfer\_fr\_19.png\|Entrons **5 mm**, pour le rayon de départ, Image:Part\_Chamfer\_fr\_20.png\|et, **20 mm** pour le rayon d\'arrivée.


</center>



<center>

Image:Part\_Chamfer\_fr\_21.png\|Validons avec ** OK **, pour voir s'effectuer notre **chanfrein variable**. Image:Part\_Chamfer\_fr\_22.png\|Une nouvelle icône par opération s\'affiche dans la **Vue combinée**, renseignant l(es)\'opération(s).
Si vous cliquez sur la flèche, vous pouvez voir les formes d\'origine, qui ont servi dans l\'opération de **![](images/)_[Chanfrein](Part_Chamfer/fr.md)**.
Les formes originales peuvent être effacées, pour ne conserver que le produit final.


</center>


## Comparaison Chanfrein PartDesign [16px\|text-top=Chanfrein\|link=PartDesign\_Chamfer/fr](File:PartDesign_Chamfer.png.md), et, Chanfrein Part [16px\|text-top=Chanfrein\|link=Part\_Chamfer/fr](Image:Part_Chamfer.png.md) {#comparaison_chanfrein_partdesign_16pxtext_topchanfreinlinkpartdesign_chamferfr_et_chanfrein_part_16pxtext_topchanfreinlinkpart_chamferfr_1}

**Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ne doit pas être confondu avec son équivalent de l\'atelier Part **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)****.
Bien qu\'ils partagent la même icône, ces outils sont différents, et s\'utilisent différemment.

### Voici quelques différences : {#voici_quelques_différences_1}

-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** est *paramétrique*. Après l\'application d\'un **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)**, sa dimension peut être modifié ; ce n\'est pas le cas du **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)**.
-   Les arêtes doivent être sélectionnées avant de démarrer le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)**. Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)**, quant à lui, peut être lancé, puis, suivi de la sélection du solide, et, enfin des arêtes.
-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ajoute une entrée distincte dans l\'arborescence Projet. Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)** devient le parent de l\'objet auquel il a été appliqué.
-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** affiche un aperçu en temps réel de l\'application du chanfrein avant la validation de la fonction.
-   Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)** supporte les dimensions variables (avec une dimension de départ, et, une dimension d\'arrivée). Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ne le permet pas.





```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
chmfr.Base = FreeCAD.ActiveDocument.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
FreeCADGui.ActiveDocument.myCube.Visibility = False
FreeCAD.ActiveDocument.recompute()
```

**Example Script Explanation:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
```


<div class="mw-translate-fuzzy">

-   Creează un cub de 5 mm pentru noi cu marginile cotate la. Vedeți [Part\_API](Part_API.md) pentru o explicație a metodei makeBox.


</div>


```python
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
```

-   Adaugă un obiect nou în documentul Chamfer (din modulul Part) cu etichetă\"myChamfer\".


```python
chmfr.Base = FreeCAD.ActiveDocument.myCube
```

-   Specifică faptul că forma de bază a obiectului chamfer ar trebui să fie \"myCube\".


```python
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
```

-   Creează o matrice goală \"myEdges\" și apoi adaugă matricele cu parametrii de șanfrare ale fiecărei margini.
-   Sintaxa pentru fiecare element ar trebui să fie (marginea \#, lungimea de start a șanfrenului, lungimea de final a șanfrenului)


```python
chmfr.Edges = myEdges
```

-   Setează atributul Edges al obiectului Chamfer egal cu matricea pe care tocmai am creat-o.


```python
FreeCADGui.ActiveDocument.myCube.Visibility = False
```

-   Această linie ascunde pur și simplu \"myCube\", astfel încât obiectul nou creat \"myChamfer\" este singurul vizibil.


```python
FreeCAD.ActiveDocument.recompute()
```

-   Recalculează toate componentele modificate de pe ecran și reîmprospătează afișajul.





 
