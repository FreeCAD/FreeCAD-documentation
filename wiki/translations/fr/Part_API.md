 {{VeryImportantMessage|(Novembre 2018) Ces informations peuvent être incomplètes et obsolètes. Pour la dernière API, voir l'[https://www.freecadweb.org/api auto-génération de la documentation de l'API].}}

Le module **Part** <img alt="" src=images/Workbench_Part.png  style="width:16px;"> est une connexion directe entre **FreeCAD** et le noyau **OpenCasCade**. Il fournit principalement des [TopoShapes](TopoShape_API/fr.md) qui sont les types d\'objets principaux utilisés par OpenCascade. Le module **Part** contient également une variété de fonctions utiles pour créer et manipuler des **topoShapes**. Exemple : 
```python
import Part
mycube = Part.makeBox(2,2,2)
Part.show(mycube)
```


{{APIFunction/fr|__fromPythonOCC__|OCC.Object|Méthode d'assistance pour convertir un shape pythonocc en un shape interne|Un Part.Shape}}


{{APIFunction/fr|__sortEdges__|list of edges|Méthode d'assistance pour trier une liste d'arêtes (edges) non triée de manière à ce que les sommets de début et de fin de deux arêtes consécutives coïncident géométriquement. Il renvoie une liste unique d'arêtes et l'algorithme s'arrête après le premier ensemble d'arêtes connectées, ce qui signifie que la liste de sortie peut être plus petite que la liste d'entrée. La liste triée peut être utilisée pour créer un fil.|Une liste d'arêtes (edges)}}


{{APIFunction/fr|__toPythonOCC__|Part.Shape|Méthode d'assistance pour convertir une forme interne en une forme pythonocc|Un OCC.Shape}}


{{APIFunction/fr|cast_to_shape|Part.Shape|Cast du type de forme réelle| }}


{{APIFunction/fr|export|list,string|Exporte une liste d'objets dans un seul fichier.| }}


{{APIFunction/fr|getSortedClusters|list of edges|Méthode d'assistance pour trier et grouper une variété des bords| }}


{{APIFunction/fr|insert|string,string|Insère le fichier (chemin d'accès donné comme premier argument) dans le document donné (second argument).| }}


{{APIFunction/fr|makeBox|length,width,height,[pnt,dir]|Crée une zone située à ce point avec les dimensions (longueur, largeur, hauteur). Par défaut le point est au Vecteur(0,0,0) et la direction au Vecteur(0,0,1)|Crée une forme}}


{{APIFunction/fr|makeCircle|radius,[pnt,dir,angle1,angle2]|Fait un cercle d'un rayon donné. Par défaut le point est au Vecteur(0,0,0), et la direction est, Vecteur(0,0,1), angle1 est 0° et angle2 est 360°|Crée une forme}}


{{APIFunction/fr|makeCompound|list|Crée un compound parmi une liste de formes.|Crée une forme}}


{{APIFunction/fr|makeCone|radius1,radius2,height,[pnt,dir,angle]|Fait un cône avec les rayons et la hauteur. Par défaut le point est au Vecteur(0,0,0), et la direction est, Vecteur(0,0,1) et l'angle est de 360°|Crée une forme}}


{{APIFunction/fr|makeCylinder|radius,height,[pnt,dir,angle]|Crée un cylindre avec une taille et un rayon donné. Par défaut le point est au Vecteurr (0,0,0), et la direction est, Vecteur(0,0,1), et, l'angle est de 360°|Crée une forme}}


{{APIFunction/fr|makeHelix|pitch,height,radius,[angle]|Rend une hélice avec un pas donné, la hauteur et le rayon. Par défaut, une surface cylindrique est utilisée pour créer l'hélice. S'il y a un quatrième paramètre, une surface conique est utilisée à la place|Crée une forme}}


{{APIFunction/fr|makeLine|(x1,y1,z1),(x2,y2,z2)|Crée une ligne en deux points|Crée une forme}}


{{APIFunction/fr|makeLoft|shapelist<profiles>,[boolean<solid>,boolean<ruled>]|Crée une forme de loft en utilisant la liste des profils. Crée éventuellement un résultat solide (vs surface/coque) ou une surface lignée.|Crée une forme de loft.|Crée une forme}}


{{APIFunction/fr|makePlane|length,width,[pnt,dir]|Crée un plan. Par défaut le point est au Vecteur(0,0,0) et la direction au Vector(0,0,1)|Crée une forme}}


{{APIFunction/fr|makePolygon|list|Crée un polygone avec une liste de vecteurs|Crée une forme}}


{{APIFunction/fr|makeRevolution|Curve,[vmin,vmax,angle,pnt,dir]|Crée une forme de révolution en faisant tourner la courbe, ou une partie de celle-ci autour d'un axe donné par (point, direction). Par défaut, vmin et vmax sont définis aux limites de la courbe, l'angle est de 360°, le point est au Vecteur(0,0,0) et la direction est au Vecteur(0,0,1)|Crée une forme}}


{{APIFunction/fr|makeRuledSurface|Edge or Wire,Edge or Wire|Crée une surface réglée hors de deux arêtes ou fils. Si les fils sont utilisés ils doivent avoir le même nombre d'arêtes.|Crée une forme}}


{{APIFunction/fr|makeShell|list|Crée une coquille à partir d'une liste de faces.|Crée une forme}}


{{APIFunction/fr|makeSolid|Part.Shape|Crée un solide hors du shell, à l'intérieur d'une forme.|Crée une forme}}


{{APIFunction/fr|makeSphere|radius,[pnt, dir, angle1_Debut,angle2_Fin,angle3]|Crée une sphère de rayon donné. Par défaut le point est au Vecteur(0,0,0), et la direction est au Vecteur(0,0,1), angle1 est -90°, angle2 est 90° et angle3 est 360°|Crée une forme}}


{{APIFunction/fr|makeTorus|radius1,radius2,[pnt,dir,angle1,angle2,angle]|Crée un tore avec une donnée de rayon d'angles. Par défaut le point est au Vecteur (0,0,0), et la direction est au vecteur (0,0,1), angle1 est 0°, angle2 est 360° et l'angle est de 360°|Crée une forme}}


{{APIFunction/fr|makeTube|edge,float|Crée un tube.|Crée une forme}}


{{APIFunction/fr|open|string|Crée un nouveau document et charge le fichier dans le document.| }}


{{APIFunction/fr|read|string|Charge le fichier et retourne un shape.|Une forme}}


{{APIFunction/fr|show|shape|Ajouter la forme du document actif ou en crée un si aucun document n'existe.| }}


 

[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)
