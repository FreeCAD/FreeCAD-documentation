---
- GuiCommand:/it
   Name:Mesh BuildRegularSolid
   Name/it:Solido regolare
   MenuLocation:Mesh → Solido regolare...
   Workbenches:[Mesh](Mesh_Workbench/it.md)
---

## Descrizione

Il comando **Solido regolare** crea un oggetto mesh solido parametrico regolare.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare l\'opzione **Mesh → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Solido regolare...** dale menu.
2.  Si apre la finestra di dialogo **Solido regolare**.
3.  Prima selezionare un tipo di oggetto mesh dall\'elenco a discesa:
    -   
        **<img src="images/Mesh_Cube.svg" width=16px> Cubo
**
        

    -   
        **<img src="images/Mesh_Cylinder.svg" width=16px> Cilindro
**
        

    -   
        **<img src="images/Mesh_Cone.svg" width=16px> Cono
**
        

    -   
        **<img src="images/Mesh_Sphere.svg" width=16px> Sfera
**
        

    -   
        **<img src="images/Mesh_Ellipsoid.svg" width=16px> Ellissoide
**
        

    -   
        **<img src="images/Mesh_Torus.svg" width=16px> Toro
**
        
4.  Specificare le impostazioni richieste. Le impostazioni disponibili dipendono dal tipo di oggetto mesh. Vedere [Proprietà](#Proprietà.md).
5.  Per le mesh con superfici curve: un valore **Campionatura** più alto produce una mesh più fine.
6.  Premere il pulsante **Crea** per creare l\'oggetto mesh.
7.  Se necessario, creare più oggetti mesh.
8.  Premere il pulsante **Chiudi** per chiudere la finestra di dialogo e terminare il comando.


</div>

## Note

-   Gli oggetti mesh creati con questo comando sono parametrici. Ogni volta che vengono ricalcolati, ad esempio dopo aver modificato uno dei loro parametri, viene ricostruita la loro mesh. Ciò significa che manipolarli con comandi come [ Affinamento](Mesh_RemeshGmsh/it.md), [Scala](Mesh_Scale/it.md) ecc. Di solito non ha senso.

## Proprietà

Mesh objects created with this command inherit all [Mesh Feature](Mesh_Feature.md) properties. In addition each mesh object type has a number of properties to control its parametric behavior:

### <img alt="" src=images/Mesh_Cube.svg  style="width:32px;"> Cube 

#### Data


{{TitleProperty|Cube}}

-    **Height|FloatConstraint**: the height of the cube.

-    **Length|FloatConstraint**: the length of the cube.

-    **Width|FloatConstraint**: the width of the cube.

### <img alt="" src=images/Mesh_Cylinder.svg  style="width:32px;"> Cylinder 

#### Data 


{{TitleProperty|Base}}

-    **Closed|Bool**: if set to `False`, the planar ends of the cylinder are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cylinder.

-    **Radius|FloatConstraint**: the radius of the cylinder.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Cone.svg  style="width:32px;"> Cone 

#### Data 


{{TitleProperty|Base}}

-    **Closed|Bool**: if set to `False`, the planar end(s) of the cone are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cone.

-    **Radius 1|FloatConstraint**: the first radius of the cone. Can be {{value|0}}.

-    **Radius 2|FloatConstraint**: the second radius of the cone. Can be {{value|0}}.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Sphere.svg  style="width:32px;"> Sphere 

#### Data 


{{TitleProperty|Base}}

-    **Radius|FloatConstraint**: the radius of the sphere.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Ellipsoid.svg  style="width:32px;"> Ellipsoid 

#### Data 


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: the first radius of the ellipsoid.

-    **Radius 2|FloatConstraint**: the second radius of the ellipsoid.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Torus.svg  style="width:32px;"> Torus 

#### Data 


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: the first (main) radius the torus.

-    **Radius 2|FloatConstraint**: the second radius of the torus.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}  
