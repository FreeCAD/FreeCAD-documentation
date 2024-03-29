---
 GuiCommand:
   Name: Arch Roof
   Name/fr: Arch Toiture
   MenuLocation: Arch , Toiture
   Workbenches: Arch_Workbench/fr
   Shortcut: **R** **F**
   SeeAlso: Arch_Structure/fr, Arch_Wall/fr
---

# Arch Roof/fr

## Description

L\'outil **<img src="images/Arch_Roof.svg" width=16px> [Arch Toiture](Arch_Roof/fr.md)** permet de créer un toit en pente à partir d\'une polyligne sélectionnée. L\'objet Toiture créé est paramétrique et garde sa relation avec l\'objet de base. Le principe est que chaque arête se voit attribuer un profil de toiture (pente, largeur, surplomb, épaisseur).

**Remarque :** cet outil est encore en développement et peut échouer avec des formes très complexes.

<img alt="" src=images/RoofExample.png  style="width:600px;"> 
*Vue d'en haut d'un modèle de bâtiment montrant le toit avec une certaine transparence*



## Utilisation

1.  Créez une polyligne fermée dans le sens anti-horaire et sélectionnez la.

    :   <img alt="" src=images/CounterclockwiseWire.png  style="width:600px;">

2.  Cliquez sur le bouton **<img src="images/Arch_Roof.svg" width=16px> [Toiture](Arch_Roof/fr.md)** ou appuyez sur les touches **R** puis **F**.

3.  L\'objet Toiture par défaut a l\'air étrange car l\'outil manque de certaines informations nécessaires.

4.  Après la création de la par défaut, double cliquez sur l\'objet dans la [vue en arborescence](Tree_view/fr.md) pour accéder à son édition et ses propriétés. Les angles doivent être compris entre 0 et 90 degrés.

    :   ![](images/RoofTable.png )

5.  Chaque ligne correspond à un pan de la toiture. Vous pouvez ainsi définir les propriétés que vous dédirez pour chaque pan de la toiture.

6.  Pour vous aider, vous pouvez régler `Angle` ou `Run` sur `0` et définir un `Relative Id`, cela effectue un calcul automatique pour trouver les données relatives au `Relative Id`.

7.  Cela fonctionne ainsi :
    1.  Si `Angle &#61; 0` et `Run &#61; 0` alors le profil est identique au profil relatif.
    2.  Si `Angle &#61; 0` alors `Angle` est calculé de manière à ce que la hauteur soit identique au profil relatif.
    3.  Si `Run &#61; 0` alors `Run` est calculé de manière à ce que la hauteur soit identique à celle du profil relatif.
    4.  Enfin, fixez un angle à 90° pour faire un pignon.

    :   <img alt="" src=images/RoofProfil.png  style="width:600px;">

8.  
    **Remarque**: pour une meilleure compréhension, veuillez consulter cette [vidéo youtube](https://www.youtube.com/watch?v=4Urwru71dVk).

## Options

-   L\'objet Toiture partage les propriétés communes et le comportement de tous les [Arch Composants](Arch_Component/fr.md).



## Propriétés



### Données


{{TitleProperty|Roof}}

-    **Angles|FloatList**: liste des angles des segments de toit.

-    **Border Length|Length**: longueur totale des bordures de la toiture.

-    **Face|Integer**: numéro de la face de l\'objet de base utilisé pour construire le toit (non utilisé).

-    **Flip|Bool**: indique si la direction du toit doit être inversée.

-    **Heights|FloatList**: liste des hauteurs calculées des segments de toit.

-    **Id Rel|IntegerList**: liste des identifiants des profils correspondants aux segments de toit.

-    **Overhang|FloatList**: liste des porte-à-faux des segments de toit.

-    **Ridge Length|Length**: longueur totale des crêtes et des arêtiers de la toiture.

-    **Runs|FloatList**: liste des projections horizontales des segments de toit.

-    **Thickness|FloatList**: liste des épaisseurs des segments de toit.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Toiture peut être utilisé dans les [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```

-   Crée un objet `Roof` à partir de `baseobj` donné, qui peut être une polyligne fermée ou un objet solide.
    -   Si `baseobj` est une polyligne, vous pouvez fournir des listes de `angles`, `run`, `idrel`, `thickness` et `overhang` pour chaque arête de la polyligne afin de définir la forme du toit.
    -   Les listes sont automatiquement complétées pour correspondre au nombre d\'arêtes de la polyligne.

Exemple :


```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Roof/fr
