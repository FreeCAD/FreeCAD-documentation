---
- GuiCommand   */fr
   Name   *Part EditAttachment
   Name/fr   *Part Ancrage
   MenuLocation   *Part → Ancrage...
   Workbenches   *[Part](Part_Workbench/fr.md), [PartDesign](PartDesign_Workbench/fr.md)
   Version   *0.17
   SeeAlso   *[Placement](Placement/fr.md), [Tutoriel Les bases pour l'ancrage](Basic_Attachment_Tutorial/fr.md), [Part Part2DObject](Part_Part2DObject/fr.md)
---

# Part EditAttachment/fr

## Description

**Part Ancrage** est un utilitaire permettant d\'ancrer un objet à un autre. L\'objet ancré est lié à l\'autre objet, ce qui signifie que si le placement de ce dernier est modifié par la suite, l\'objet ancré sera mis à jour à sa nouvelle position.

## Utilisation

1.  Sélectionnez l\'objet à ancrer.
2.  Allez dans le menu **Part → Ancrage\...**.

       *   **Remarque**   * lorsque vous travaillez dans [PartDesign](PartDesign_Workbench/fr.md) et que vous créez des esquisses, des géométries de référence ou des primitives, les étapes 1 et 2 sont inutiles   * la boite de dialogue Ancrage est automatiquement activée.
3.  Sous les paramètres **Ancrage**, *Non ancré* peut être lu. Le premier bouton est **Sélection...** pour indiquer qu\'il attend une sélection dans la vue 3D.
4.  Sélectionnez un élément de topologie sur l\'objet auquel ancrer   * sommet, arête ou face/plan. La géométrie de référence à partir de [Part Conteneurs](Std_Part/fr.md) est également sélectionnable.
5.  L\'étiquette du premier bouton adopte maintenant le type de topologie sélectionné. Dans le champ blanc à sa droite, l\'objet référencé et son élément sont ajoutés. Par exemple, si une face sur un cube primitif est sélectionnée, le champ affiche Box   *Face6.
6.  Sélectionnez un [Mode d\'ancrage](#Mode_d.27ancrage.md) dans la liste. Les modes disponibles sont filtrés par les références sélectionnées. *Ancré avec le mode * sera affiché sous l\'en-tête **Mode d\'ancrage**.

       *   Pour des informations en direct sur les modes d\'ancrage, passez la souris sur l\'un des modes de la liste pour qu\'une info-bulle apparaisse.
7.  Éventuellement, ajoutez jusqu\'à 3 autres références en appuyant sur les boutons **Référence2**, **Référence3** et **Référence4** et en répétant l\'étape 4.
8.  Définir facultativement un [Décalage de la pièce ancrée](#D.C3.A9calage_de_l.27ancrage.md).
9.  Appuyez sur **OK**.

## Options

![](images/Part_Offset_Tasks_fr.png )

### Mode d\'ancrage 

#### Désactivé

Par défaut, aucune référence sélectionnée.

#### Normal à une arête 

L\'objet est rendu perpendiculaire au bord. La référence au sommet, facultative, définit l\'emplacement.

   *; Combinaisons de référence   *

   *   arête
   *   arête, sommet
   *   sommet, arête


{{Part Tools navi/fr}}

#### Alignement O-Z-X 

Fait correspondre l\'origine de l\'objet avec le premier sommet référencé, puis aligne sa normale avec l\'axe horizontal du plan vers le sommet/le long de la ligne.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   sommet, sommet, arête
   *   sommet, arête, sommet
   *   sommet, arête, arête
   *   sommet, sommet
   *   sommet, arête

#### Alignement O-Z-Y 

Fait correspondre l\'origine de l\'objet avec le premier sommet référencé et aligne sa normale avec l\'axe vertical du plan vers le sommet/le long de la ligne.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   sommet, sommet, arête
   *   sommet, arête, sommet
   *   sommet, arête, arête
   *   sommet, sommet
   *   sommet, arête

#### Alignement O-X-Y 

Fait correspondre l\'origine de l\'objet avec le premier sommet référencé et aligne ses axes horizontal et vertical vers le sommet/le long de la ligne.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   sommet, sommet, arête
   *   sommet, arête, sommet
   *   sommet, arête, arête
   *   sommet, sommet
   *   sommet, arête

#### Alignement O-X-Z 

Fait correspondre l\'origine de l\'objet avec le premier sommet référencé et aligne son axe horizontal et sa normale sur le sommet/le long de la ligne.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   sommet, sommet, arête
   *   sommet, arête, sommet
   *   sommet, arête, arête
   *   sommet, sommet
   *   sommet, arête

#### Alignement O-Y-Z 

Fait correspondre l\'origine de l\'objet avec le premier sommet référencé et aligne son axe vertical et sa normale vers le sommet/le long de la ligne.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   sommet, sommet, arête
   *   sommet, arête, sommet
   *   sommet, arête, arête
   *   sommet, sommet
   *   sommet, arête

#### Alignement O-Y-X 

Fait correspondre l\'origine de l\'objet avec le premier sommet référencé et aligne ses axes vertical et horizontal vers le sommet/le long de la ligne.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   sommet, sommet, arête
   *   sommet, arête, sommet
   *   sommet, arête, arête
   *   sommet, sommet
   *   sommet, arête

#### Translation de l\'origine 

L\'origine de l\'objet est alignée sur le sommet correspondant. L\'orientation est contrôlée par la propriété [Placement](Placement/fr.md).

   *; Combinaisons de référence   *

   *   sommet.

#### XY de l\'objet 

Le plan est aligné sur le plan local XY de l\'objet lié.

   *; Combinaisons de référence   *

   *   Tout, Conique.

#### XZ de l\'objet 

Le plan est aligné sur le plan local XZ de l\'objet lié.

   *; Combinaisons de référence   *

   *   Tout, Conique.

#### YZ de l\'objet 

Le plan est aligné sur le plan local YZ de l\'objet lié.

   *; Combinaisons de référence   *

   *   Tout, Conique.

#### Face plane 

Le plan est positionné pour coïncider avec la face plane.

   *; Combinaisons de référence   *

   *   plan.

#### Tangent à une surface 

Le plan est rendu tangent à la surface en un sommet.

   *; Combinaisons de référence   *

   *   face, sommet
   *   sommet, face

#### Frenet NB 

Le plan est défini sur des axes normaux-binormaux (NB) du [Système de Coordonnées Frenet-Serret](https   *//fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet) au point de la courbure de l\'arête le plus proche du sommet (ou défini par la propriété MapPathParameter, si le sommet n\'est pas lié). L\'origine de l\'objet est déplacée au sommet si le sommet est en premier, ou conservée à la courbe si l\'arête est en premier. Ce mode est similaire à *Normal à une arête*, sauf que l\'axe X est bien défini.

   *;Combinaisons de référence   *

   *   courbe
   *   courbe, sommet
   *   sommet, courbe
   *   <img alt="" src=images/Attacher_mode_FrenetNB.png  style="width   *250px;">

#### Frenet TN 

Le plan est défini sur les axes tangente-normale (TN) du [Système de Coordonnées Frenet-Serret](https   *//fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet) au point de la courbure de l\'arête le plus proche du sommet (ou défini par la propriété MapPathParameter, si le sommet n\'est pas lié). L\'origine de l\'esquisse est déplacée au sommet si le sommet est en premier, ou conservée à la courbe si l\'arête est en premier. Effectivement, si la courbe est plane, le plan d\'esquisse est le plan de la courbe.

   *;Combinaisons de référence   *

   *   courbe
   *   courbe, sommet
   *   sommet, courbe
   *   <img alt="" src=images/Attacher_mode_FrenetTN.png  style="width   *250px;">

#### Frenet TB 

Le plan est défini sur les axes tangente-binormale (TB) du [Système de Coordonnées Frenet-Serret](https   *//fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet) au point de la courbure de l\'arête le plus proche du sommet (ou défini par la propriété MapPathParameter, si le sommet n\'est pas lié). L\'origine de l\'esquisse est déplacée au sommet si le sommet est en premier, ou conservée à la courbe si l\'arête est en premier. Effectivement, si la courbe est plane, le plan d\'esquisse est le plan de la courbe.

   *;Combinaisons de référence   *

   *   courbe
   *   courbe, sommet
   *   sommet, courbe
   *   <img alt="" src=images/Attacher_mode_FrenetTB.png  style="width   *250px;">

#### Concentrique

S\'aligne sur le plan au cercle osculateur d\'une arête. Un lien sommet optionnel définit l\'endroit.

   *; Combinaisons de référence   *

   *   courbe
   *   cercle
   *   courbe, sommet
   *   cercle, sommet
   *   sommet, courbe
   *   sommet, cercle

#### Section de révolution 

Le plan est perpendiculaire à l\'arête et l\'axe Y correspond à l\'axe du cercle osculateur. Un lien sommet optionnel définit l\'endroit.

   *; Combinaisons de référence   *

   *   courbe
   *   cercle
   *   courbe, sommet
   *   cercle, sommet
   *   sommet, courbe
   *   sommet, cercle

#### Plan par 3 points 

Fait passer le plan XY par trois sommets.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   droite, sommet
   *   sommet, droite
   *   droite, droite

#### Normal à 3 points 

Fait passer le plan par les deux premiers sommets, perpendiculairement au plan défini par les 3 sommets.

   *; Combinaisons de référence   *

   *   sommet, sommet, sommet
   *   droite, sommet
   *   sommet, droite
   *   droite, droite

#### Pliage

Mode spécifique pour le pliage des polyèdres. Sélectionnez 4 arêtes dans l\'ordre    * arête collable, ligne de pliage, autre ligne de pliage, autre arête collable. Le plan sera aligné sur le pliage de la première arête. Dans l\'image ci-dessous, il n\'est pas nécessaire que les deux feuilles à plier ensemble soient les mêmes.

   *; Combinaisons de référence   *

   *   droite, droite, droite, droite
   *   ![ 250px](images/Attacher_mode_Folding.png )

#### Inertie 2-3 

L\'objet sera ancré à un plan passant par les deuxième et troisième axes principaux d\'inertie (passe par le centre de masse).

   *; Combinaisons de référence   *

   *   Tout
   *   Tout, Tout
   *   Tout, Tout, Tout
   *   Tout, Tout, Tout, Tout

### Décalage de l\'ancrage 

Le décalage de l\'ancrage est utilisé pour appliquer un décalage linéaire ou rotatif par rapport à l\'objet référencé. Cela signifie que les décalages sont relatifs au système de coordonnées \"local\" et non au système de coordonnées global.Il devient actif quand un mode d\'ancrage autre que \"Désactivé\" a été sélectionné.

-   **X**    * définit une distance de décalage dans l\'axe X de l\'objet de référence.

-   **Y**    * définit une distance de décalage dans l\'axe Y de l\'objet de référence.

-   **Z**    * définit une distance de décalage dans l\'axe Z de l\'objet de référence. Cette coordonnée doit être utilisée pour le cas d\'utilisation fréquente pour lequel vous souhaitez décaler une esquisse perpendiculairement au plan.

-   **Yaw**    * (tangage) fait pivoter l\'objet ancré le long de l\'axe Z de l\'objet de référence.

-   **Pitch**    * (lacet) fait pivoter l\'objet ancré le long de l\'axe Y de l\'objet de référence.

-   **Roll**    * (roulis) fait pivoter l\'objet ancré le long de l\'axe X de l\'objet de référence.

-   **Flip sides**    * (Retourner les côtés) si coché, le plan XY de l\'objet ancré est inversé.

## Limitations

-   Les conteneurs [Part](Std_Part/fr.md) et [Corps](PartDesign_Body/fr.md) ne sont pas supportés. Bien qu\'il soit possible d\'utiliser Ancrage pour les aligner, la pièce ancrée ne sera pas paramétriquement liée.
-   Si la sélection de deux lignes entraîne un suivi avec \"les points sont colinéaires. Impossible de créer un plan\", essayez de sélectionner trois points à la place [\# p473594](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614).





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/fr
