# FEM Python Scripting/it
# Creare mesh FEM 

## Creare una mesh con 10 nodi 

    import FreeCAD, Fem
    # create a empty mesh
    m = Fem.FemMesh()
    #create the nodes
    m.addNode(0,1,0)
    m.addNode(0,0,1)
    m.addNode(1,0,0)
    m.addNode(0,0,0)
    m.addNode(0,0.5,0.5)
    m.addNode(0.5,0.03,.5)
    m.addNode(0.5,0.5,0.03)
    m.addNode(0,0.5,0)
    m.addNode(0.03,0,0.5)
    m.addNode(0.5,0,0)
    # add the volume with the created nodes
    m.addVolume([1,2,3,4,5,6,7,8,9,10])

    Fem.show(m)

Se si desidera avere elementi predefiniti e la numerazione dei nodi:


    m.addNode(0.0,1.0,0.0,1)

    m.addVolume([1,2,3,4,5,6,7,8,9,10],1)

# Manipolazione visiva 

Evidenziare alcuni nodi nella vista:

    import FreeCAD, Fem

    m = Fem.FemMesh()

    m.addNode(0,1,0)
    m.addNode(0,0,1)
    m.addNode(1,0,0)
    m.addNode(0,0,0)
    m.addNode(0,0.5,0.5)
    m.addNode(0.5,0.03,.5)
    m.addNode(0.5,0.5,0.03)
    m.addNode(0,0.5,0)
    m.addNode(0.03,0,0.5)
    m.addNode(0.5,0,0)
    m.addVolume([1,2,3,4,5,6,7,8,9,10])

    Fem.show(m)
    Gui.ActiveDocument.ActiveObject.HighlightedNodes = [1,2,3]

Colori post elaborazione e posizione:

Evidenziare alcuni nodi nella vista:

    # set the volume 1 to red
    Gui.ActiveDocument.ActiveObject.ElementColor= {1:(1,0,0)}
    # set the node 1 and 2 to a certain Color and interpolate the survace
    Gui.ActiveDocument.ActiveObject.NodeColor= {1:(1,0,0),2:(1,0,0)}
    # set the node 1 and 2 to a certain displacement
    Gui.ActiveDocument.ActiveObject.NodeDisplacement= {1:FreeCAD.Vector(1,0,0),2:FreeCAD.Vector(1,0,0)}
    # double the factor of the displacement shown
    Gui.ActiveDocument.ActiveObject.animate(2.0)






[<img src="images/Property.png" style="width:16px"> Poweruser\_Documentation/it](<img src="images/Property.png" style="width:16px"> Poweruser_Documentation/it.md) [<img src="images/Property.png" style="width:16px"> Developer/it](<img src="images/Property.png" style="width:16px"> Developer/it.md) [<img src="images/Property.png" style="width:16px"> Python\_Code/it](<img src="images/Property.png" style="width:16px"> Python_Code/it.md)

---
[documentation index](../README.md) > FEM Python Scripting/it
