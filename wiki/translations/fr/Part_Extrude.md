---
- GuiCommand:
   Name: Part Extrude
   Name/fr: Part Extrusion
   MenuLocation: Part - Extrusion...
   Workbenches: [Part](Part_Workbench/fr.md)
   SeeAlso: [Draft Ajuster ou prolonger](Draft_Trimex/fr.md), [PartDesign Protrusion](PartDesign_Pad/fr.md)
---

# Part Extrude/fr

## Description

**Part Extrusion** prolonge une forme dans une distance et une direction spécifiées. Le type de la forme résultante pourra varier selon le type de la forme initiale et des options sélectionnées.

Dans les scénarios les plus courants, la liste suivante détaille les formes résultantes attendues depuis une forme initiale donnée :

-   Extrusion d\'un vertex (point) produit une arête linéaire (ligne)
-   Extrusion d\'une arête ouverte (ligne, arc) produit une face ouverte (par ex. plan)
-   Extrusion d\'une arête fermée (cercle) produit une face fermée (par ex. un cylindre aux extrémités ouvertes) ou si le paramètre \"solid\" est réglé à \"true\" produit un solide (par ex. un cylindre solide)
-   Extrusion d\'une polyligne ouverte (par exemple une Draft polyligne), produira une coque ouverte (plusieurs faces jointes)
-   Extrusion d\'une polyligne fermée (par exemple une Draft polyligne), produira éventuellement une coque (plusieurs faces jointes) ou si le paramètre \"solid\" est réglé à \"true\", cela produira un solide
-   Extrusion d\'une face (ex. plane) produit un solide (par ex. un cube)
-   Extrusion d\'un objet **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Formes à partir texte](Draft_ShapeString/fr.md)** produit un composé de solides (la chaîne de texte est un composé de lettres et chacune d\'elle forme un solide)
-   Extrusion d\'une coque de faces produira un Compsolid.

![600px](images/Part_Extrude_demo.png)



*Exemples d'extrusion*



## Utilisation

1.  Sélectionner une ou des formes dans la [vue 3D](3D_view/fr.md) ou dans le modèle de la [vue en arborescence](Tree_view/fr.md).
2.  Cliquer sur le bouton **<img src="images/Part_Extrude.svg" width=16px> [Extrusion](Part_Extrude/fr.md)
** dans la barre d\'outils ou aller dans le menu **Part → Extrusion**
3.  Définir la direction et la longueur et éventuellement d\'autres paramètres (voir la section suivante [Paramètres](#Param.C3.A8tres.md) pour plus de détails).
4.  Cliquer sur **OK**.

La sélection peut également être faite après le lancement de l\'outil en sélectionnant une ou plusieurs formes dans le [Panneau des tâches](Task_panel/fr.md).

L\'arborescence du modèle contient autant d\'objets Extrude que de formes sélectionnées. Chaque forme initiale est placée sous son objet Extrude.



## Paramètres

La forme extrudée est définie par les paramètres suivants qui peuvent être édités après sa création dans l\'[Éditeur de propriétés](Property_editor/fr.md).

-   **Base** : la forme initiale (la forme à partir de laquelle l\'extrusion est appliquée).

-   **Dir** : la direction pour étendre la forme. Si **Dir Mode** est sur \'Custom\', vous pouvez éditer **Dir**. Sinon, **Dir** est en lecture seule et est calculé à partir de la forme liée.

-   **Dir Link** : lien paramétré sur une arête (ligne) qui définit la direction de l\'extrusion.

-   **Dir Mode** : définit le mode de contrôle de **Dir**. \"Custom\" signifie que **Dir** est éditable. \"Edge\" signifie que Dir est obtenu à partir d\'une arête (ligne) lié par un **Dir Link**. \"Normal\" signifie que Dir est perpendiculaire au plan de la forme de départ.

-   **Length Fwd** : longueur d\'extrusion. Si **Length Fwd** et **Length Rev** sont tous deux égaux à zéro, la longueur du vecteur **Dir** est utilisée.

-   **Length Rev** : longueur supplémentaire à extruder dans le sens inverse de **Dir**.

-   **Solid** : si True, l\'extrusion d\'une arête fermée ou d\'une polyligne fermée donnera un solide. Si False, une coque en résultera.

-   **Reversed** : inverse l\'extrusion par rapport à **Dir**.

-   **Symmetric** : si True, l\'extrusion est centrée par rapport à la forme d\'entrée et la longueur totale est **Length Fwd**. **Length Rev** est ignoré.

-   **Taper Angle** et **Taper Angle Rev** : applique un angle de dépouille à l\'extrusion, de sorte que les côtés de l\'extrusion soient dessinés selon l\'angle spécifié. Un angle positif signifie que la section transversale se dilate. **Taper Angle Rev** définit l\'angle de dépouille de la partie inversée de l\'extrusion (la partie de **Length Rev**).
    -   
        {{Version/fr|0.20}}
        
        Les structures internes reçoivent l\'angle de conicité opposé. Ceci est fait pour faciliter la conception des moules et des pièces moulées.

    -   
        {{VersionMinus/fr|0.19}}
        
        L\'extrusion conique n\'est prise en charge que pour les formes sans structure interne. L\'extrusion conique ne fonctionne pas bien si la forme contient des B-splines.

-   **Face Maker Class** : définit le nom de classe en C++ du code de création d\'une face, utilisé lors de la création de solides à partir de filaires. Cette propriété est là pour prendre en charge la compatibilité ascendante. Ne pas y touchez sauf si vous savez ce que vous faites.

-   **Placement** : les paramètres standard de [positionnement](Placement/fr.md).

-   **Label** : étiquette à afficher dans la [vue en arborescence](Tree_view/fr.md) du modèle (non disponible lors de la création d\'extrusion).



## Boîte de dialogue 

![](images/Part_Extrude_dialog.png )

-   Le bouton **OK** crée l\'extrusion et ferme la boîte de dialogue.

-   Le bouton **Fermer** ferme le dialogue sans rien faire.

-   Le bouton **Appliquer** crée l\'extrusion, mais ne ferme pas la boîte de dialogue. Vous pouvez ensuite sélectionner une autre forme dans la liste du bas et créer davantage d\'extrusions. Un clic sur **Appliquer** plusieurs fois crée de nombreuses extrusions.

-   Boutons radio \"Direction\" : définissent la manière dont la direction d\'extrusion est calculée.

-   Le bouton **Sélectionner** : cliquez dessus, puis choisissez une arête dans la [vue 3D](3D_view/fr.md). Cette arête apparaîtra dans le champ de texte à côté du bouton, au format \"ObjectName:EdgeN\". Vous pouvez également taper le lien manuellement. Les valeurs X, Y, Z seront remplies en fonction de la direction de l\'arête.

-   Les boutons **X**, **Y**, **Z** : cliquez sur le bouton *x* pour définir la direction d\'extrusion sur l\'axe +*x*. Cliquez à nouveau pour définir l\'axe -*x*.

-   Champs de saisie **X**, **Y**, **Z** : définissez ou affichez le vecteur de direction de l\'extrusion. Si les deux longueurs sont égales à zéro, la longueur de ce vecteur définit la longueur de l\'extrusion et les valeurs sont toujours exprimées en mm, quelles que soient les préférences de l\'unité.

-   Champs de la longueur : définissez la longueur d\'extrusion. Ces champs d\'entrée ont un support d\'unité.

-   Symétrique : étend l\'extrusion dans les deux sens, de sorte que le profil reste au centre.

-   Angle de dépouille extérieur : angle positif signifie que le profil est élargi à l\'autre extrémité de l\'extrusion.

-   Créer le solide : si coché, l\'extrusion d\'une polyligne ou d\'une arête fermée donnera un solide. Il est coché par défaut si une polyligne fermée a été présélectionné avant de lancer Part Extrusion.

-   Forme : ici, vous sélectionnez les formes à extruder. Si plusieurs objets sont sélectionnés, plusieurs objets d\'extrusion seront créés.



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) avec les objets visibles appropriés à l\'intérieur peuvent également être utilisés comme profils et pour spécifier la direction. {{Version/fr|0.20}}

-   La boîte de dialogue des tâches n\'offre pas d\'aperçu. **Appliquer** crée un objet d\'extrusion chaque fois que vous cliquez dessus, ce qui peut être utile comme aperçu. Cependant, ils resteront et un autre sera créé lorsque vous cliquerez sur **OK**. [Annuler](Std_Undo/fr.md) peut être utile pour les nettoyer avant de cliquer sur **OK**.



## Comparaison avec PartDesign Protrusion 

[PartDesign Protrusion](PartDesign_Pad/fr.md) est également une fonctionnalité d\'extrusion mais il existe des différences importantes :

-   Part Extrusion crée toujours une forme autonome. PartDesign Protrusion fusionne le résultat de l\'extrusion avec le reste du corps.
-   Part Extrusion ne se soucie pas de sa position dans l\'arborescence du modèle. PartDesign Protrusion ne peut se trouver qu\'à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md).
-   Part Extrusion peut extruder tout objet ayant une géométrie Part (forme [OpenCASCADE](OpenCASCADE/fr.md)), à l\'exception des solides et des CompSolids.
-   Part Extrusion peut extruder des faces individuelles d\'autres objets. PartDesign Protrusion n\'acceptera comme profil que des esquisses ou des faces d\'objets PartDesign.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Extrude/fr
