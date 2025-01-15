# Draft API/fr
**(Novembre 2018) Ces informations peuvent être incomplètes et obsolètes. Pour la dernière API, voir l'[https://www.freecadweb.org/api auto-génération de la documentation de l'API].**

Ces fonctions font partie de l\'établi [Draft](Draft_Workbench/fr.md), et, une fois que le module a été importé, elles peuvent être utilisées, dans les scripts, les [macros](macros/fr.md), ou dans l\'interpréteur [Python](Python/fr.md).

Exemple: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction|cut|FreeCAD.Object, FreeCAD.Object|Renvoie un objet construit, à partir de la différence de la coupe des 2 objets sélectionnés. Les objets originaux obtenu sont cachés.|Un nouvel objet est créé}}


{{APIFunction|extrude|FreeCAD.Object, Vector|Extrude l'objet sélectionné dans la direction donnée par le vecteur. L'objet d'origine est caché.|Un nouvel objet est créé}}


{{APIFunction|formatObject|FreeCAD.Object, [FreeCAD.Object]|Cette fonction s'applique à l'objet cible, compte tenu des propriétés actuelles, fixées sur la barre d'outils Draft (couleur et largeur de la ligne), ou, le cas échéant copie les propriétés d'un deuxième objet. Il met également l'objet dans le groupe de construction si le bouton de construction est pressé.|Aucun}}


{{APIFunction|fuse|FreeCAD.Object, FreeCAD.Object|Retourne un objet fabriqué à partir de la fusion des 2 objets sélectionnés. Si les objets sont coplanaires, un '''Draft Wire''' spécial est utilisé, sinon l'objet final est une fusion standard (standard Part fuse).|Un nouvel objet est créé}}


{{APIFunction|getDraftPath|[string]|Retourne le chemin d'accès utilisateur, ou système,  à partir duquel, le Draft module est exécuté. Si un sous-dossier ou un nom de fichier est fourni, le chemin complet vers le sous-dossier de l'intérieur du Draft module est renvoyé.|Le chemin du fichier}}


{{APIFunction|getGroupContents|list|Scanne récursivement la liste de données pour les groupes. Si les groupes sont trouvés, leur contenu est ajouté à la liste.|Une liste d'Objets FreeCAD}}


{{APIFunction|getRealName|string|Sépare le numéro du nom de l'objet.|Le nom dépouillé de l'objet}}


{{APIFunction|getSelection| |Retourne la sélection actuelle FreeCAD.|Retourne la sélection actuelle FreeCAD.}}


{{APIFunction|makeCircle|radius, [placement], [facemode], [startangle], [endangle]|Crée un objet cercle de rayon donné. Si une coordonnée est fournie, elle est utilisée. Si '''facemode est False''', le cercle est représenté comme un fil de fer (filaire), sinon, comme une face. Si '''startAngle''' et '''endAngle''' (en degrés) sont donnés, ils sont utilisés et l'objet apparaîtra comme un arc.|Un nouvel objet est créé.}}


{{APIFunction|makeDimension|Vector, Vector, [Vector] or FreeCAD.Object, int, int, [Vector]|Crée un objet '''Cotation''', mesure la distance entre le premier et le deuxième vecteur, avec la dimension de la ligne passant par le troisième vecteur, s'il est fourni. La largeur de ligne et la couleur affichée sur de la barre d'outils du projet seront utilisés. Au lieu de 2 vecteurs, vous pouvez également créer un objet FreeCAD de deux entiers (et éventuellement un vecteur) où la ligne de cotation doit passer. Dans ce cas, la dimension sera '''associée''' à l'objet, et la mesure des deux sommets, indiquée par les deux chiffres à l'indice donné.|Un nouvel objet est créé.}}


{{APIFunction|makeLine|Vector, Vector|Crée une ligne entre les deux vecteurs donnés. La largeur de ligne, et, la couleur courante sélectionnés dans la barre d'outils Draft seront utilisés.|Un nouvel objet est créé.}}


{{APIFunction|makeRectangle|length, width, [placement], [facemode]|Crée un objet Rectangle avec une longueur dans la direction X et la hauteur dans la direction Y. Si une position est donnée, elle est utilisée. Si '''facemode est False''', le rectangle est représenté comme un fil de fer (filaire), sinon, comme une face. La largeur de ligne et la couleur courante sélectionnés dans la barre d'outils Draft seront utilisés.|Un nouvel objet est créé.}}


{{APIFunction|makeText|string or list, [Vector], [screenmode]|Crée un '''objet Texte''', au point donné, contenant la chaîne ou les chaînes figurant dans la liste, une chaîne par ligne. La couleur actuelle de la barre d'outils Projet la hauteur du texte et la police spécifiée dans les préférences sont utilisés. Si '''screenmode est sur True''', le texte fait toujours face à la direction de la vue, sinon il se trouve sur le plan '''X, Y'''.|Un nouvel objet est créé.}}


{{APIFunction|makeWire|list or Part.Wire, [closed], [placement], [facemode]|Crée un objet (wire) dans la liste de données des vecteurs ou du fil donné. Si c'est un objet fermé (True), ou, si le premier et le dernier point sont identique, le fil est fermé. Si '''facemode est (True)''' (le fil est fermé), le fil, apparaîtra rempli. La largeur de ligne et la couleur courante sélectionnés dans la barre d'outils seront utilisés.|Un nouvel objet est créé.}}


{{APIFunction|move|FreeCAD.Object or list, Vector, [copymode]|Déplace l'objet ou les objets sélectionnés contenus dans la liste donnée ,dans la direction et la distance indiquée par le vecteur. Si '''CopyMode''' est sur True les objets réels ne sont pas déplacés, mais copiés à sa (leur) place.|L'objet ou les objets (ou leurs copies, si '''CopyMode''' était sur True).}}


{{APIFunction|precision| |Retourne la valeur de précision définie dans les paramètres utilisateur.|Un integer.}}


{{APIFunction|rotate|FreeCAD.Object or list, angle, [center], [axis] ,[copymode]|Tourne l'objet donné ou les objets sélectionnés à l'angle donné et autour du centre donnée s'ils sont fourni, en utilisant l'axe comme un axe de rotation. Si l'axe est omis, la rotation se fera autour de l'axe vertical '''Z'''. Si '''CopyMode''' est sur True, les objets réels ne sont pas déplacés, mais les copies sont créées à leur place.|Les objets (ou leurs copies).}}


{{APIFunction|scale|FreeCAD.Object or list, vector, [center], [copymode]|Redimensionne l'objet donné ou les objets sélectionnés au facteur d'échelle définis par le vecteur de donnés '''(X, Y et Z)''' autour du centre donné s'il est fourni. Si '''CopyMode''' est sur True les objets réels ne sont pas déplacés, mais les copies sont créées à la place.|Les objets (ou leurs copies).}}


{{APIFunction|select|FreeCAD.Object| Désélectionne tout, et, sélectionne uniquement l'objet survolé|Aucune.}}


{{APIFunction|shapify|FreeCAD.Object|Transforme un objet de forme '''paramétrique''' en objet '''non-paramétrique'''.|Un nouvel objet est créé.}}


{{APIFunction|draftify|FreeCAD.Object or list|Met l'objet, ou, chaque objet sélectionné(s) en fils paramétriques Projet.|Aucune.}}


{{APIFunction|getSVG|FreeCAD.Object, [linemodifier], [textmodifier], [(u,v)]|Crée une représentation SVG de l'objet donné. L'attribut '''linemodifier''' est le facteur d'échelle (en pourcent) pour la largeur de la ligne, et '''textmodifier''' pour la taille du texte. Vous pouvez également éventuellement fournir un tuple de vecteurs pour définir un plan de projection, sinon la forme géométrique sera projetée sur le plan '''X, Y'''.|Une chaîne contenant la représentation SVG de l'objet sélectionné.}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Draft](Draft_Workbench.md) > Draft API/fr
