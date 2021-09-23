# TopoShape API/fr
 {{VeryImportantMessage | (novembre 2018) Ces informations peuvent être incomplètes et obsolètes. Pour la dernière API, consultez la [https://www.freecadweb.org/api documentation de l'API générée automatiquement].}}

L\'objet TopoShape est l\'objet principal du Module Part. Tous les types de formes (fil, face, solide, etc\...) du module part sont des TopoShapes, et, partagent les attributs, et, méthodes suivantes. 
```python
import Part
sh = Part.makeBox(10,10,10)
print sh.Faces
for f in sh.Faces:
   print f.Edges
```


{{APIProperty/fr|Area|La superficie totale des faces de la forme.}}


{{APIProperty/fr|CompSolids|Répertorie les formes ultérieures dans cette forme.}}


{{APIProperty/fr|CenterOfMass|Donne le centre de la masse de la forme actuelle. Si le champ de gravitation est uniforme, c'est le centre de gravité. Les coordonnées retournées pour le centre de masse sont exprimées dans le système de coordonnées cartésiennes absolu.}}


{{APIProperty/fr|Compounds|Répertorie les composantes de cette forme.}}


{{APIProperty/fr|Edges|Répertorie les contours de cette forme.}}


{{APIProperty/fr|Faces|Répertorie les visages de cette forme.}}


{{APIProperty/fr|Length|Longueur totale des bords de la forme.}}


{{APIProperty/fr|Orientation|l'orientation de la forme.}}


{{APIProperty/fr|ShapeType|Le type de la forme.}}


{{APIProperty/fr|Shells|Répertorie les formes ultérieures dans cette forme.}}


{{APIProperty/fr|Solids|Liste des formes ultérieures dans cette forme.}}


{{APIProperty/fr|Vertexes|Liste des sommets de cette forme.}}


{{APIProperty/fr|Volume|Volume total des solides de la forme.}}


{{APIProperty/fr|Wires|Liste des fils de cette forme.}}


{{APIProperty/fr|BoundBox|Les dimensions hors tout de l'objet}}


{{APIProperty/fr|Matrix|Donne une matrice de la transformation actuelle de l'objet}}


{{APIProperty/fr|Placement|Donne la transformation actuelle de l'objet comme placement}}


{{APIFunction/fr|approximate| |Se rapproche d'une courbe B-Spline|a BSplineCurve object}}


{{APIFunction/fr|check| |Vérifie les erreurs de forme et les rapporte dans la structure de la forme. Il s'agit d'une vérification plus détaillée comme cela se fait dans isValid().| }}


{{APIFunction/fr|common|TopoShape|Intersection de la forme et une forme donnée.|un TopoShape}}


{{APIFunction/fr|complement| |Calcule le complément de l'orientation de cette forme, c'est-à-dire inverse l'état intérieur/extérieur des limites de cette forme.|un TopoShape}}


{{APIFunction/fr|copy| |Crée une copie de cette forme|un TopoShape}}


{{APIFunction/fr|cut|TopoShape|Différence entre la forme et une forme donnée.|un TopoShape}}


{{APIFunction/fr|distToShape| TopoShape |Calcule la distance minimale entre ceci et une donnée TopoShape. |float <distance minimum>, list < le point le plus proche >, list < la forme secondaire la plus proche & ces paramètres > }}


{{APIFunction/fr|exportBrep| string |Exporte le contenu de cette la forme dans un fichier BREP. BREP est le format natif de CasCade.| }}


{{APIFunction/fr|exportIges| string |Exporte le contenu de la forme dans un fichier IGES.| }}


{{APIFunction/fr|exportStep| string |Exporte le contenu de la forme dans un fichier STEP.| }}


{{APIFunction/fr|exportStl| string |Exporte le contenu de la forme dans un fichier de maillage STL.| }}


{{APIFunction/fr|extrude|Vector|Extrude la forme le long d'une direction.|un TopoShape}}


{{APIFunction/fr|fuse|TopoShape|Union de la forme et une forme donnée.|un TopoShape}}


{{APIFunction/fr|getAllDerivedFrom| |Retourne toute la descendance de ce type d'objet|une liste}}


{{APIFunction/fr|hashCode| |Cette valeur est calculée à partir de la valeur de la référence sous-jacente de la forme et l'emplacement. L'orientation n'est pas prise en compte.|a string}}


{{APIFunction/fr|isClosed| |Vérifie si la forme est fermée.|un booléen}}


{{APIFunction/fr|isDerivedFrom|string|Retourne la valeur true si le type donné est le père (maître)|boolean}}


{{APIFunction/fr|isEqual|TopoShape|Retourne true si les deux formes partagent le même TShape, ont le même emplacement et ont la même orientation.|un booléen}}


{{APIFunction/fr|isInside|Vector,float,Boolean|Vérifie si un point est à l'intérieur d'un solide, avec une certaine tolérance. Si le troisième paramètre est '''true''' un point sur une face est considéré comme inside|un booléen}}


{{APIFunction/fr|isNull| |Vérifie si la forme est nulle.|un booléen}}


{{APIFunction/fr|isPartner|TopoShape|Renvoie true si les deux formes partagent le même TShape, mais peut avoir un emplacement différent et avoir une orientation différente.|un booléen}}


{{APIFunction/fr|isSame|TopoShape|Vérifie si les deux formes partagent la même géométrie, donne true si les deux formes partagent le même TShape, elles ont le même emplacement mais peuvent avoir une orientation différente.|un booléen}}


{{APIFunction/fr|isValid| |Vérifie si la forme est valide, c'est à dire ni nulle, ni vide ni endommagée.|un booléen}}


{{APIFunction/fr|makeFillet|float,TopoShape|Retourne un nouvel objet basé sur un TopoShape, mais avec un rayon de courbure "float" appliqué à chaque arête.|un TopoShape}}


{{APIFunction/fr|makeHomogenousWires|wire|Construit un fil homogène avec le même nombre d'arêtes| a wire}}


{{APIFunction/fr|makeOffset|float|Décale la forme selon une distance donnée|un TopoShape}}


{{APIFunction/fr|makePipe|wire|Fait un tube en suivant une ligne.|un TopoShape}}


{{APIFunction/fr|makePipeShell|wire|Rend un loft défini par son profil le long d'une ligne.|un TopoShape}}


{{APIFunction/fr|makeShapeFromMesh|mesh|Fait une forme composée de données de maillage. Remarque : Cela devrait être utilisé plutôt pour de petites mailles.|un TopoShape}}


{{APIFunction/fr|makeThickness|list,float,float|Un solide évidé est construit à partir d'un solide initial, et, un ensemble de faces sur ce solide, qui doivent être éliminés. Les faces restantes du solide deviennent les murs du solide évidé, leur épaisseur est définie au moment de la construction. Les arguments à transmettre sont une liste des faces à ignorer, l'épaisseur des murs, et, une valeur de tolérance.|un TopoShape}}


{{APIFunction/fr|nullify| |Détruit la référence à la forme sous-jacente stockée sous cette forme. En conséquence, cette forme devient nulle.| }}


{{APIFunction/fr|project|TopoShape|Projete une forme sur votre forme|un TopoShape}}


{{APIFunction/fr|read|string|Lit un fichier IGES, STEP ou BREP.|un TopoShape}}


{{APIFunction/fr|reverse| |Inverse l'orientation de cette forme.| }}


{{APIFunction/fr|revolve|Vector, Vector, float|S'articule autour d'un axe à un degré donné. ex : Part.revolve(Vector(0,0,0),Vector(0,0,1),360) tourne la forme autour d'un axe Z de 360 degrés.|un TopoShape}}


{{APIFunction/fr|rotate|Vector, Vector, float|Applique la rotation (en degré) à l'emplacement actuel de cette forme. ex : Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) fait pivoter la forme autour de l'axe Z de 180 degrés.|un TopoShape}}


{{APIFunction/fr|scale| |S'applique à l'échelle avec le point et le facteur de cette forme.|un TopoShape}}


{{APIFunction/fr|section|TopoShape|Section de la forme avec une forme toposhape.|un TopoShape}}


{{APIFunction/fr|sewShape| |La machine raccorde la forme s'il y a un écart.| }}


{{APIFunction/fr|tessellate|float|Tessellate (Paver) la forme et retourne une liste des sommets et indices de la faces. Le float donnée est la tolérance.|a list}}


{{APIFunction/fr|toNurbs| |Transformation de la géométrie complète d'une forme en géométrie NURBS. Par exemple, toutes les courbes soutenant les bords de la forme de base, sont convertis en courbes de BSP, et toutes les surfaces soutenant ses faces sont converties en surfaces de BSP.|a NURBS curve}}


{{APIFunction/fr|transformGeometry|matrix|Applique la transformation géométrique sur une copie de la forme. La transformation à appliquer, est définie comme une matrice 4x4. La géométrie sous-jacente des formes suivantes peuvent être changées en courbes qui prennent en charge les extrémités de la forme, ou une surface qui prend en charge une face de la forme. Par exemple, un cercle peut être transformé en une ellipse lorsque vous appliquez une transformation d'affinité. Il peut également arriver que le cercle est alors représenté comme une courbe b-spline. La transformation s'applique à toutes les courbes qui supportent les bords de la forme et toutes les surfaces qui prennent en charge les faces de la forme. Remarque : Si vous voulez transformer une forme sans changer la géométrie sous-jacente, puis utilisez les méthodes traduites ou les faire pivoter.|un TopoShape}}


{{APIFunction/fr|transformShape|matrix|Applique la transformation d'une forme sans changer la géométrie sous-jacente.| }}


{{APIFunction/fr|translate|Vector|Applique la conversion à l'emplacement actuel de cette forme.| }}


{{APIFunction/fr|writeInventor| |Écrit le maillage au format OpenInventor dans une chaîne.|a string}}

Certains attributs et méthodes s\'appliquent uniquement à certains TopoShapes.

Ces points s\'appliquent aux bords (TopoShapeEdge).


{{APIProperty/fr|FirstParameter|La valeur du paramètre du bord à une extrémité. Pas nécessairement le Vertex[0]. [http://fr.wikipedia.org/wiki/%C3%89quation_param%C3%A9trique Voir équations paramétriques]}}


{{APIProperty/fr|LastParameter|La valeur du paramètre du bord à l'autre extrémité. Pas nécessairement le Vertex[1].}}


{{APIFunction/fr|centerOfCurvatureAt|Float|Retourne le centre (points 3D) ou la valeur des paramètres du cercle.|Vector}}


{{APIFunction/fr|curvatureAt|Float|Retourne  la valeur des paramètres de la courbe du bord.|Float}}


{{APIFunction/fr|getParameterByLength|Float|Retourne l’intervalle [0,Length] jusqu'au prochain intervalle [Premier Paramètre,dernier Paramètre]|Float }}


{{APIFunction/fr|normalAt|Float|Retourne la valeur des paramètres de la normale du bord (uniquement s'il existe).|Vector}}


{{APIFunction/fr|parameterAt|Vertex,[Face]|Retourne la valeur correspondante au Vertex (points 3D).|Float}}


{{APIFunction/fr|tangentAt|Float|Retourne la valeur des paramètres de la direction du vecteur de la tangente du bord (s'il existe).|Vector}}


{{APIFunction/fr|valueAt|Float|Retourne la valeur du vecteur correspondant au paramètre 3D.|Vector}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
