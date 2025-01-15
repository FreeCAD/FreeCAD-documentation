---
 GuiCommand:
   Name: Arch Pipe
   Name/fr: Arch Conduite
   MenuLocation: 3D/BIM , Conduite
   Workbenches: BIM_Workbench/fr
   Shortcut: **P** **I**
   Version: 0.17
   SeeAlso: 
---

# Arch Pipe/fr

## Description

L\'outil **Arch Conduite** vous permet de créer des conduites à partir de zéro ou à partir d\'objets basés sur (Draft, Sketch, etc..) sélectionnés et contenant une et une seule polyligne ouverte.



## Utilisation

1.  Vous pouvez sélectionner une forme linéaire de [Part](Part_Workbench/fr.md) telle qu\'une [Draft Ligne](Draft_Line/fr.md), une [Draft Polyligne](Draft_Wire.md) ou une [Esquisse](Sketcher_NewSketch/fr.md) ouverte.
2.  Lancez cette commande de plusieurs méthodes :
    -   En appuyant sur le bouton **<img src="images/Arch_Pipe.svg" width=16px> [Conduite](Arch_Pipe/fr.md)** de la barre d\'outils.
    -   En appuyant sur le raccourci clavier **P** puis **I**.
    -   Depuis **3D/BIM → Conduite** dans le menu supérieur.

## Options

-   Conduite partage les propriétés et comportements communs à tous les [Arch Composants](Arch_Component/fr.md)



## Propriétés



### Données


{{TitleProperty|Component}}

-    **Base|Link**: polyligne de base de la conduite, si il y en a une.

Pour les autres propriétés du groupe, voir [Arch Composant](Arch_Component/fr#Propriétés.md).


{{TitleProperty|Pipe}}

-    **Diameter|Length**: diamètre de la conduite tuyau si son **Profile Type** est {{Value|Circle}}.

-    **Height|Length**: hauteur de la conduite, si son **Profile Type** est {{Value|Rectangle}}.

-    **Length|Longueur**: longueur de la conduite s\'il n\'est pas basé une polyligne.

-    **Offset End|Length**: décalage par rapport à l\'extrémité de la conduite. Automatiquement défini si un [Arch Raccord](Arch_PipeConnector/fr.md) est ajouté à ce point pour que la conduite s\'adapte au connecteur. Voir [Processus de travail typique](#Processus_de_travail_typique.md) ci-dessous.

-    **Offset Start|Length**: décalage par rapport au point de départ de la conduite. Idem.

-    **Profile|Link**: profil de base de la conduite. S\'il n\'est pas défini, le profil de la conduite est déterminé par **Profile Type**.

-    **Profile Type|Enumeration**: profil de la conduite. Il n\'est utilisé que si **Profile** n\'est pas défini. Les options sont les suivantes : {{Value|Circle}}, {{Value|Square}} ou {{Value|Rectangle}}.

-    **Wall Thickness|Length**: épaisseur de la paroi de la conduite.

-    **Width|Length**: largeur de la conduite, si **Profile Type** est {{Value|Square}} ou {{Value|Rectangle}}.



## Flux de travail typique 

-   Commencez le placement des sanitaires (le fichier exemple ci dessous est un fichier step importé). Sélectionnez l\'objet et activez l\'Arch Equipements en cliquant sur le bouton [Arch Équipement](Arch_Equipment/fr.md).

![](images/Arch_pipe_example_01.jpg )

-   Dans Arch Équipement vous avez maintenant une nouvelle propriété **SnapPoints** qui est une liste de vecteurs 3D. Cela vous permet d\'ajouter des points d\'aimantation personnalisés, auxquels vous pouvez vous aimanter lorsque le bouton d\'aimantation [Draft Spécial](Draft_Snap_Special/fr.md) est activé. Actuellement, cette propriété n\'est cependant disponible que pour Python. Dans le cas ci-dessus, j\'ai ajouté un nouveau point d\'aimantation à la sortie du WC. Les vecteurs à l\'intérieur des SnapPoints apparaissent sur le modèle sous forme de points blancs:

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   Avec [Draft Aimantation Spécial](Draft_Snap_Special/fr.md), vous pouvez maintenant vous aimanter sur tous ces points:

![](images/Arch_pipe_example_03.jpg )

-   Maintenant vous pouvez créer vos conduites en utilisant les fonctions Draft Lignes, Draft Polylignes ou Esquisses. La meilleure solution est d\'utiliser uniquement des Draft Lignes :

![](images/Arch_pipe_example_04.jpg )

-   Il y a maintenant un nouvel outil [Draft Pente](Draft_Slope/fr.md) qui permet de donner une pente aux lignes, par exemple 5% (0.05). Nous pouvons donc donner facilement une pente aux conduites de décharge. Seule la coordonnée Z est changée avec cet outil, il faut donner le départ et la fin, la coordonnées de départ (haut) reste inchangé.

![](images/Arch_pipe_example_05.jpg )

-   Maintenant nous n\'avons qu\'a sélectionner les lignes et cliquer sur le bouton [Arch Conduite](Arch_Pipe/fr.md). Arch Conduite travaille avec n\'importe quel objet ligne et seulement avec des lignes ouvertes.

![](images/Arch_pipe_example_06.jpg )

-   Vous pouvez maintenant créer des connexions avec deux ou trois conduites coïncidents en cliquant sur le bouton [Arch Raccord](Arch_PipeConnector/fr.md). Si vous sélectionnez trois conduites, deux conduites doivent être alignées pour créer un élément de départ :

![](images/Arch_pipe_example_07.jpg )

-   Changer le rayon de courbure ne modifie pas la longueur résultante du tracé des conduites (pour changer la résultante, vous devez changer le départ et l\'arrivée des conduites). Vous pouvez donc tracer votre chemin de lignes sans vous soucier des courbes et rayon des coudes.

Il est aussi possible de créer une Arch conduite sans ligne de base, dans ce cas utilisez la propriété \"Length\" pour définir la longueur.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Conduite peut être utilisé dans une [macro](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Crée un objet `pipe` à partir de `baseobj` et `diameter`.
    -   
        `baseobj`
        
        est une [Draft Ligne](Draft_Line/fr.md) ou un [Draft Polyligne](Draft_Wire/fr.md).

    -   Si `baseobj` est omis, une conduite droite peut être créée avec seulement `diameter` et `length` dans la direction Z.
-   Si `placement` est donné, il est utilisé.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
line = Draft.make_wire([p1, p2, p3, p4])

pipe = Arch.makePipe(line, 200)
FreeCAD.ActiveDocument.recompute()

pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Pipe/fr
