---
- GuiCommand:/fr
   Name:Part Helix
   Name/fr:Part Hélice
   MenuLocation:Pièce → [Créer des primitives...](Part_Primitives/fr.md) → Hélice
   Workbenches:[Part](Part_Workbench/fr.md), [OpenSCAD](OpenSCAD_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Helix/fr

## Description

La primitive géométrique **<img src=images/Part_Helix.svg style="width:16px"> [Part Hélice](Part_Helix/fr.md)** crée une forme d\'hélice définie par un rayon, un pas et une hauteur totale.

Un usage courant de la primitive hélice est pour la <img src=images/PartDesign_AdditivePipe.svg style="width:Création de vis](Thread_for_Screw_Tutorial/fr.md) en conjonction avec un profil fermé et le **<img src="images/Part_Sweep.svg" width=16px> [Part Balayage](Part_Sweep/fr.md)** opération. Ce processus fonctionne essentiellement de la même manière dans l\'[Atelier PartDesign](PartDesign_Workbench.md) en utilisant l\'outil **[16px"> [PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md)**.

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md).
2.  La boîte de dialogue Créer des primitives est accessible de plusieurs manières:
    -   En appuyant sur le bouton **<img src=images/Part_Primitives.svg style="width:16px"> [Création de primitives géométriques...](Part_Primitives/fr.md)** situé dans la barre d\'outils Pièce.
    -   Utilisation de l\'entrée **Pièce → <img src=images/Part_Primitives.svg style="width:16px"> [Créer des primitives...](Part_Primitives/fr.md) → Hélice** dans le menu Part.

![](images/PartHelixPrimitivesOptions_en.png )

#### Paramètres

-    {{Parameter|Pitch:}}Le pas correspond à l\'espace entre deux \"tours\" consécutifs de l\'hélice mesuré le long de l\'axe principal de l\'hélice.

-    {{Parameter|Height:}}La hauteur correspond à la hauteur globale de l\'hélice mesurée le long de l\'axe principal de l\'hélice.

-    {{Parameter|Radius:}}Le rayon correspond au rayon du cercle construit par l\'hélice en visualisant l\'hélice du haut ou du bas.

-    {{Parameter|Angle}}: Par défaut, l\'hélice est construite sur un cylindre imaginaire. Avec cette option, il est possible de construire l\'hélice sur un cône imaginay. Cet angle correspond à l\'angle du cône. La valeur doit être comprise entre 0 et +90 degrés.

-    {{Parameter|Right-handed or Left-handed:}}Ce paramètre spécifie la [handeness (chiralité)](https://en.wikipedia.org/wiki/Screw_thread) de l\'hélice.

#### Location

-    {{Parameter|X:}}L\'axe principal de l\'hélice sera traduit le long de l\'axe x de la valeur que vous indiquez dans ce champ.

-    {{Parameter|Y:}}L\'axe principal de l\'hélice sera traduit le long de l\'axe y de la valeur que vous indiquez dans ce champ.

-    {{Parameter|Z:}}L\'axe principal de l\'hélice sera traduit le long de l\'axe z de la valeur que vous indiquez dans ce champ.

-    {{Parameter|Direction:}}Par défaut, l\'axe principal de l\'hélice est l\'axe z. Ici, vous avez la possibilité de modifier l\'axe principal de l\'hélice. Si vous sélectionnez le paramètre \"défini par l\'utilisateur \...\", vous serez invité à indiquer l\'axe principal de l\'hélice en entrant les coordonnées de son vecteur.

-    {{Parameter|3D View:}}vous permet de sélectionner le centre dans la vue 3D

## Options

### Propriétés

Une fois l\'hélice créé vous avez la possibilité de modifier ses paramètres.

+----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ![](images/PartHelixProperty_en.png ) | Les paramètres de ce menu sont similaires que les réglages décrits plus haut.                            |
|                                                          | **Base**                                                                               |
|                                                          | \* {{Parameter|Placement:}} donne le déplacement ou (et) la rotation a donner à l\'hélice. |
|                                                          |                                                                                                          |
|                                                          | -                                                                                         |
|                                                          |     {{Parameter|Angle:}}                                                                                 |
|                                                          |                                                                                                       |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Helix/fr
