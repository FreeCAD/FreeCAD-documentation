---
- GuiCommand:
   Name:Path Deburr
   Name/fr:Path Ébavurage
   MenuLocation:Path - Ébavurer
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.18
---

# Path Deburr/fr

## Description

L\'outil <img alt="" src=images/Path_Deburr.svg  style="width:24px;"> [Ébavurage](Path_Deburr/fr.md) sert principalement à ébavurer un bord.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Deburr.svg" width=16px> [Ébavurer](Path_Deburr/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Deburr.svg" width=16px> Ébavurer** dans le menu.
2.  Le panneau de tâches **Ébavurer** s\'ouvre. Voir [Options](#Options.md).
3.  Sélectionnez **Géométrie de base**.
4.  Spécifiez les paramètres requis.
5.  Appuyez sur le bouton **OK**.

## Options

Après avoir sélectionné la géométrie dans la section **Géométrie de base** du panneau de tâches, vous pouvez appuyer sur **Appliquer** pour voir le parcours de l\'outil tel que défini par les options par défaut.

Ensuite, vous pouvez vérifier vos profondeurs et hauteurs, comme avec les autres commandes de parcours.

La dernière étape consiste à activer la section **Opération** où vous pouvez spécifier ce qui suit :

-    **Commande d'outil**: sélectionnez l\'outil à utiliser.

-    **Mode de refroidissement**: sélectionnez {{Value|Aucun}}, {{Value|Liquide}} ou {{Value|Brumisateur}}.

-    **Directions**: sélectionnez {{Value|Sens horaire}} (CW) ou {{Value|Sens anti-horaire}} (CCW).

-    **W**: dimension de votre arête.

-    **h**: décalage par rapport au bas de l\'outil. Il s\'agit d\'un dispositif de sécurité car si la pointe dépasse le bord, l\'outil ne coupera plus.

:   <img alt="Deburring interface with the options" src=images/Path_Deburr_Operations-tab.png  style="width:300px;">



## Propriétés



### Données


{{TitleProperty|Base}}

-    **Placement**:

-    **Label**: nom d\'utilisateur de l\'objet (UTF-8)


{{TitleProperty|Deburr}}

-    **Direction**: {{Value|CCW}} ou {{Value|CW}}.

-    **Entry Point**: point d\'entrée de l\'opération, s\'il est défini à 2, il ira dans 2 coins par rapport à la valeur par défaut.

-    **Extra depth**: profondeur supplémentaire (**h** dans le panneau de tâches).

-    **Join||Hidden**: comment joindre les segments de chanfrein, {{Value|Round}} ou {{Value|Miter}}.

-    **Side||Hidden**: le côté de l\'opération, {{Value|Outside}} ou {{Value|Inside}}.

-    **Width**: largeur du chanfrein (**W** dans le panneau des tâches).


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour dégager les brides et les obstructions (définie par défaut à `OpStockZMax + SetupSheet.ClearanceHeightOffset`).

-    **Safe Height**: hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (définie à `OpStockZMax + SetupSheet.SafeHeightOffset`).

-    **Start Depth**: profondeur de départ de l\'outil, première profondeur de coupe en Z.

-    **Step Down**: pas de descente incrémentale de l\'outil


{{TitleProperty|Op Values}}

-    **Op Stock ZMax**: valeur Z maximale du brut.

-    **Op Stock ZMin**: valeur Z minimale du brut.

-    **Op Tool Diameter**: diamètre de l\'outil.


{{TitleProperty|Path}}

-    **Active**: mis à `False`, pour empêcher l\'opération de générer du code.

-    **Base**: géométrie de base pour cette opération, des arêtes ou une face.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Coolant Mode**: mode de refroidissement pour cette opération.

-    **Cycle Time**: durée estimée du cycle pour cette opération.

-    **Tool Controller**: contrôleur d\'outil qui sera utilisé pour calculer le parcours.

-    **User Label**: étiquette attribuée par l\'utilisateur.





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Deburr/fr
