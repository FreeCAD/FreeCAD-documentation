# Part Loft Technical Details/fr
Cette page explique les détails de la création d\'une surface [lissée](Part_Loft/fr.md). Cela s\'applique également au [Part Balayage](Part_Sweep/fr.md) effectué le long d\'une trajectoire droite, bien qu\'il y ait des différences.

Les informations fournies sont spécifiques à la mise en œuvre et peuvent changer. L\'état actuel concerne FreeCAD 0.15.4119, version OCC: 6.7.0.



## Etapes de la création du lissage 

Pour expliquer le processus de lissage, il est pratique de le diviser en étapes :

1.  rendre égal le nombre de segments dans les profils (s\'ils ne le sont pas déjà)
2.  établir la correspondance entre les segments
3.  faire la surface du lissage



### Étape 1. Rendre le nombre de segments des profils identiques 

Le lissage a besoin d\'un nombre de segments ideniques afin de créer autant de surfaces entre les segments correspondants. Si le nombre de segments est correcte dans tous les profils, cette étape est ignorée.

Si au moins l\'un des profils a un nombre différent de segments, la procédure suivante est appliquée. Par simplicité, la procédure est expliquée ici dans le cas de deux profiles seulement .

1.  Les profils sont alignés temporairement de sorte qu\'ils sont coplanaires et leurs centres de gravité \* correspondent.
2.  (Voir l\'image) pour chaque sommet dans un même profil, le second profil est tranché dans le même angle polaire (le centre polaire est le centre de gravité). Si il y a plus d\'une tranche possible ou pas du tout de tranche possible (cela peut arriver sur des profils très convexes), le Lissage échoue généralement.
3.  On fait de même dans le direction opposée.

L\'opération est étendue à tous les profils, pour obtenir le même nombre de segments. Le nombre total de segments dans chaque profil sera égale à la somme de tous les nombres de segments de tous les profils (à condition qu\'aucun des sommets ne se trouvent être dans le même angle polaire).

+++
| <img alt="Le processus de découpage de profile2 (forme blanche en forme de croissant) pour créer des joints correspondant aux sommets de profile1 (pentagone violet). Les joints insérés sont marqués par des flèches jaunes." src=images/Loft-vertex-insertion.png  style="width:300px;"> | <img alt="Le résultat du lissage correspondant à l\'image à gauche." src=images/Loft_crescent_pentagon.png  style="width:300px;"> |
+++



### Étape 2. Établir la correspondance entre les segments 

<img alt="Démonstration de lissage en gardant le nombre de segments dans les profils quand ils correspondent. Notez comment les 3 arêtes du carré supérieur \"s\'effondrent\" en une petite pièce polygonale du profil inférieur." src=images/Loft_Number_of_verts_match.png  style="width:300px;"> Dans le cas où les nombres de segments dans tous les profils ne sont pas égaux, le découpage a été fait à l\'étape 1, et la correspondance est triviale. Dans le cas où les nombres de segments dans tous les profils sont égaux, les segments existants sont utilisés (voir l\'image), et c\'est à ce moment que la correspondance doit être établie.

L\'algorithme exact pour trouver les segments correspondants est complexe, mais il tend généralement à minimiser la torsion du lissage résultant. Cela signifie que si l\'on effectue un lissage entre deux carrés, la torsion maximale possible est \<45°. Une rotation supplémentaire de l\'un des carrés fera sauter le lissage à d\'autres sommets.

La correspondance entre les profils voisins est faite indépendamment. Cela signifie qu\'une torsion supplémentaire peut être obtenue en ajoutant plus de profils intermédiaires.

Une autre chose à noter est que lorsque le nombre de segments dans les profils est égal, le lissage résultant est considérablement plus robuste en ce qui concerne les profils complexes, en particulier pour les profils non convexes. 



### Étape 3. Faire la surface lissée 

<img alt="Une courbe d\'interpolation spline (rouge) qui suit la surface du lissage. Les points à interpoler sont représentés par des carrés rouges." src=images/Loft_B-spline.png  style="width:400px;"> S\'il n\'y a que deux profils, les surfaces créées sont des surfaces réglées entre les segments correspondants des profils. Les arêtes droites sont créées pour connecter les sommets correspondants des profils.

S\'il y a plus de deux profils, les surfaces sont faites de cannelures de la même manière que les lignes droites forment des surfaces réglées. Les splines imaginaires dont la surface est \"faite de\" sont dessinées à travers les points correspondants des segments correspondants des profils.

Les splines sont une interpolation B-spline.

-   Si le nombre de profils est inférieur à 10, l\'interpolation est effectuée par une B-spline avec un degré maximum possible (c\'est-à-dire degré = nombre_de_profils - 1).
-   Si le nombre de profils dépasse 10, l\'interpolation est commutée sur les B-splines du 3ème degré.

La méthode par les nœuds utilisée est celle de la \"longueur de corde approximative\". Approximative signifie que le vecteur des nœuds est exactement le même pour chaque spline d\'un lissage. Pour plus d\'informations sur ce qu\'est l\'interpolation d\'une B-spline, le vecteur de nœud, la méthode de la longueur de corde, voir, par exemple, [cs.mtu.edu Curve Global Interpolation](http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/INT-APP/CURVE-INT-global.html).

Notez que le lissage a une propriété \"Ruled\". Si elle est définie sur true, les surfaces réglées sont créées entre des profils voisins même s\'il existe plusieurs profils. C\'est-à-dire que l\'interpolation B-spline est remplacée par une interpolation linéaire par morceaux. 



## L\'essentiel

-   Le lissage effectue une interpolation de la B-spline entre les profils fournis. L\'interpolation est commutée en linéaire par morceaux lorsque la propriété \"Ruled\" est définie à true.
-   Lorsque le nombre de profils dépasse 9, le degré d\'interpolation est ramené à 3. Ce basculement peut réduire considérablement les oscillations.
-   La correspondance du nombre de segments (alias nombre de sommets) dans les profils permet de donner une légère torsion au lissage et permet généralement d\'utiliser des profils plus complexes.
-   Lorsque les nombres de segments ne correspondent pas, il est préférable de garder les profils représentables par une fonction r(phi) appropriée en coordonnées polaires.



## Remarques supplémentaires 

-   Il n\'est pas nécessaire que les profils soient parallèles (voir une image ci-dessous).
-   Pour le lissage, il n\'est pas nécessaire que les profils soient séparés (voir une image ci-dessous). Ils peuvent être coplanaires, mais ils ne devraient pas se croiser.
-   Lorsque la propriété \"closed\" du lissage est \"true\", il y a un cuspide dans toutes les splines formant le lissage (voir une image ci-dessous). Il n\'y a aucun moyen fiable maintenant de fermer le lissage en douceur.

++++
| <img alt="Il n\'est pas obligatoire que les profils soient parallèles." src=images/Loft_nonparallel.png  style="width:300px;"> | <img alt="Dans un lissage, les profils peuvent être coplanaires. Dans cet exemple, deux des trois profils sont coplanaires." src=images/Loft_Coplanar.png  style="width:300px;"> | <img alt="Exemple de lissage fermé entre trois profils pentagonaux (blanc). Notez le joint non lisse au profil le plus externe. C\'est le premier profil dans le lissage fermé." src=images/Loft-closed.png  style="width:300px;"> |
++++



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft Technical Details/fr
