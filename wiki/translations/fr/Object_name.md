# Object name/fr


## Introduction


{{TOCright}}

Tous les objets du programme ont un [object name](Object_name/fr.md) qui les identifie de manière unique dans un [Document](App_Document/fr.md) donné.

Ces informations s\'appliquent à tous les objets dérivés de [App DocumentObject](App_DocumentObject/fr.md) (classe `App::DocumentObject`), qui comprend essentiellement tous les objets qu\'il est possible de créer dans un document.

## Les Names 

Il existe différentes propriétés pour les noms:

-   Le `Name` ne peut contenir que des caractères alphanumériques simples et le trait de soulignement, `[_0-9a-zA-Z]`.
-   Le `Name` ne peut pas commencer par un nombre. Il doit commencer par une lettre ou le trait de soulignement, `[_a-zA-Z]`.
-   Le `Name` est attribué au moment de la création de l\'objet ensuite, il n\'est plus modifiable. L\'objet ne peut jamais être renommé.
-   Le `Name` doit être unique dans tout le document. Peu importe si deux objets sont de types complètement différents, par exemple, l\'un est un [PartDesign Cavité](PartDesign_Pocket/fr.md) et l\'autre est un [Arch Mur](Arch_Wall/fr.md). Ils doivent avoir des noms différents.
-   Lors de la création d\'un objet du même type, normalement le nom est augmenté d\'un numéro séquentiel par exemple `Box`, `Box001`, `Box002` etc\.... Cela permet d\'éviter la collusion des noms..
-   Une fois l\'objet supprimé, son `Name` devient disponible pour être utilisé par un objet nouvellement créé. Cela signifie que si `Box`, `Box001` et `Box002` existent et que nous supprimons le premier élément, la boîte suivante créée avec [Part Cube](Part_Box/fr.md) ne sera pas `Box003`, ce sera à nouveau `Box`, cette chaîne étant disponible pour être réutilisée. Notez qu\'il n\'est pas possible de renommer `Box001` ou `Box002` en `Box` car leurs noms sont fixes.

En résumé, `Name` agit essentiellement comme un identifiant unique (UID) pour un objet. Puisqu\'un `Name` unique est très restrictif, tous les objets ont également une propriété `Label` qui permet de \"renommer\" l\'objet en quelque chose de plus descriptif. Le `Name` interne reste en fait fixe, mais le `Label` modifiable par l\'utilisateur peut être utilisé dans la plupart des situations où le `Name` serait utilisé. Dans l\'utilisation courante dans le programme et la documentation, \"renommer\" signifie changer le `Label` et non le `Name` réel de l\'objet.

## Les Labels 

Il existe différentes propriétés pour les étiquettes:

-   Le `Label` peut accepter n\'importe quelle chaîne UTF8, y compris les accents et les espaces.
-   La [vue en arborescence](tree_view/fr.md) affiche en fait le `Label` de l\'objet et pas le `Name`. Par conséquent, chaque fois qu\'un nouvel objet est créé, il est recommandé de remplacer `Label` par une chaîne plus descriptive. Pour renommer l\'objet, sélectionnez-le dans l\'arborescence et appuyez sur **F2**, ou ouvrez le menu contextuel (clic droit) et choisissez **Rename**.
-   Même après qu\'un objet a été renommé (ré-étiqueté), le `Name` interne sera toujours déclaré à de nombreux endroits, par exemple, dans la [Barre d\'état](status_bar/fr.md) ou dans la [Fenêtre de sélection](Selection_view/fr.md) lorsque l\'objet est sélectionné.
-   Étant donné que les fonctions internes du programme font référence aux objets par `Name`, de nombreuses boîtes de dialogue affichent le `Name` en premier suivi de l\'étiquette `Label` modifiable par l\'utilisateur entre parenthèses, par exemple, `Box (Extruded piece)`.
-   Par défaut, le `Label` est unique, tout comme le `Name`. Cependant, ce comportement peut être modifié dans [éditeur de préférences](Preferences_Editor.md), **Edition → Préférences → Général → Document → Autoriser la duplication des étiquettes dans un document**. Cela signifie qu\'en général, `Label` n\'est pas unique dans le document et peut en fait être répété. Cependant, la recommandation est de garder le `Label` unique, car c\'est probablement ce qui est le plus utile pour identifier différents objets. Lors de l\'écriture de fonctions personnalisées qui manipulent des objets, les méthodes doivent utiliser le `Name` de l\'objet plutôt que son `Label` pour garantir que l\'objet correct est utilisé.
-   Lors de l\'utilisation des [expressions](expressions/fr.md), par exemple, dans l\'[Éditeur de propriétés](Property_editor/fr.md) ou dans une [feuille de calcul](spreadsheet/fr.md), l\'étiquette peut être référencé à l\'aide de doubles crochets constitués de symboles \"moins que\" et \"plus que\".


```python
<<Custom Label With Spaces>>.Height
<<Label may use UTF8 characters>>.Width
```

### Label2 {{Version/fr|0.19}}

Cette propriété a été introduite dans la version 0.19. Il s\'agit d\'une chaîne simple qui peut contenir du texte arbitraire et peut donc être utilisée pour documenter (décrire plus en détail) l\'objet créé.

-   Dans la [vue en arborescence](tree_view/fr.md), modifiez le champ à côté de l\'icône, sous \"Description\", en cliquant dessus et en appuyant sur **F2**.
-   Vous pouvez également modifier cette propriété en modifiant l\'attribut `Label2` à partir de la [console Python](Python_console/fr.md).
-   L\'attribut **Label2** est normalement masqué dans [Éditeur de propriétés](Property_editor/fr.md) mais peut être rendu visible en ouvrant le menu contextuel (clic droit) et en sélectionnant **Show all**.

## Script


**Voir aussi:**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](scripted_objects/fr.md).

Tout objet du logiciel est créé en interne avec la méthode `addObject()` du document. La majorité des objets 2D et 3D que l\'utilisateur verra dans la [vue 3D](3D_view/fr.md) sont dérivés d\'un [Part Feature](Part_Feature/fr.md). Dans l\'exemple suivant, l\'objet créé est une [Part Box](Part_Box/fr.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Box", "Name")
obj.Label = "Custom label"
```

### Name (Nom) 

La fonction `addObject` a deux arguments de chaîne de base.

-   Le premier argument indique le type d\'objet, dans ce cas, `"Part::Box"`.
-   Le deuxième argument est une chaîne qui définit l\'attribut `Name`. S\'il n\'est pas fourni, il utilise par défaut le même nom que la classe de l\'objet, c\'est-à-dire `"Part__Box"` où les deux symboles invalides, les deux-points `::`, sont remplacé par deux traits de soulignement `__`.
    -   Le `Nom` ne peut contenir que des caractères alphanumériques simples et le trait de soulignement, `[_0-9a-zA-Z]`. Si d\'autres symboles sont donnés, ils seront convertis en traits de soulignement; par exemple, `"A+B:C*"` est converti en `"A_B_C_"`.
    -   Le `Name` ne peut pas commencer par un nombre; il doit commencer par une lettre ou le trait de soulignement, `[_a-zA-Z]`. Par exemple, `"123ABC"` est converti en `"_23ABC"`.
    -   Le `Name` est fixe au moment de la création; il ne peut pas être modifié par la suite.
    -   Le `Name` doit être unique dans tout le document. Si le même `"Nom"` est utilisé, un numéro séquentiel sera ajouté automatiquement afin que les noms résultants soient uniques; par exemple, si `"Name"` existe déjà, les nouveaux objets seront appelés `"Name001"`, `"Name002"`, `"Name003"} } etc...

        ===Label (Etiquette) ===

        {{Incode|Label` est une propriété de l'objet créé et peut être changé en un texte plus significatif.
        * Lors de la création de l'objet, le `Label` est le même que le `Name`.
        * Cependant, contrairement au `Name`, `Label` peut accepter n'importe quelle chaîne UTF8 y compris les accents et les espaces.
        * Le `Label` peut être modifié à tout moment en affectant simplement la chaîne souhaitée, <code>obj.Label = "New label"</code>

        === Accéder à un objet par Name ou Label  ===

        Tous les objets d'un document sont des attributs de données de l'objet [Document](App_Document/fr.md) correspondant. Le nom de l'attribut correspond à `Name` interne de l'objet.

        
```python
        import FreeCAD as App

        obj1 = App.ActiveDocument.Box
        obj2 = App.ActiveDocument.Box001
        obj3 = App.ActiveDocument.Box002
        
```

        Cela équivaut à utiliser la méthode `getObject` de document.
        
```python
        import FreeCAD as App

        obj1 = App.ActiveDocument.getObject('Box')
        obj2 = App.ActiveDocument.getObject('Box001')
        obj3 = App.ActiveDocument.getObject('Box002')
        
```

        Cependant, il est également possible d'obtenir l'objet par `Label` davantage descriptif.
        
```python
        import FreeCAD as App

        obj1 = App.ActiveDocument.getObjectsByLabel("Concrete wall")[0]
        obj2 = App.ActiveDocument.getObjectsByLabel("Custom parallelepiped")[0]
        obj3 = App.ActiveDocument.getObjectsByLabel("Some special name for this cube__002")[0]
        
```

        Étant donné que `Label` n'est en général pas unique, la méthode `getObjectsByLabel` renvoie une liste avec tous les objets trouvés avec cette `Label`. Cependant, si `Label` est unique dans le document, le premier élément de cette liste doit être l'objet souhaité.

        {{Userdocnavi}}
