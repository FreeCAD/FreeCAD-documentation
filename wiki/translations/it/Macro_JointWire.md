# Macro JointWire/it
**!!! This macro needs to be corrected. !!!**


{{Macro/it
|Name=JointWire
|Icon=Macro_JointWire.png
|Translate=Congiunzione di wire
|Description={{ColoredText|#ff0000|!!! This macro needs to be corrected. !!!}}<br/>Questa macro permette di trovare tutti gli elementi non collegati e di congiungerli con una linea a quello più vicino non collegato.
Usa come argomento una matrice di forme ([shape1,shape2,...])
|Author=Tremblou
|Version=1.0
|Date=2011-08-24
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/bb/Macro_JointWire.png ToolBar Icon]
}}

## Descrizione

Questa macro permette di trovare tutti gli elementi non collegati e di congiungerli con una linea a quello più vicino non collegato. Usa come argomento una matrice di forme (\[shape1,shape2,\...\])

## Script

Icona barra strumenti ![](images/Macro_JointWire.png )

**Macro_JointWire.FCMacro**


{{MacroCode|code=

 def findWires(edges):
    def verts(shape):
                return [shape.Vertexes[0].Point,shape.Vertexes[-1].Point]
        def group(shapes):
                shapesIn = shapes[:]
                pointTst = []
        pointOut =[]
        for s in shapesIn :
            pointTst=pointTst+[s.Vertexes[0].Point]
            pointTst=pointTst+[s.Vertexes[-1].Point]
        print pointTst               
        changed = False
                for s in shapesIn:
                        if len(s.Vertexes) < 2:
                print "one vertex, its a circle, just add"
                        else:                             
                                for v in verts(s):
                    twoDot=0
                                        for vv in pointTst:
                                                if v == vv:
                            twoDot=twoDot+1                           
                        if v==vv and twoDot==2 :                   
                            changed = True
                            print "found matching vert"
                            break
                                    if twoDot<2:
                        print "didn't find any matching vert..."
                        pointOut.append(v)
         print "Dots non connected", pointOut
                return(changed,pointOut)
    def joint(point):
        for p in range(len(point)/2) :
            print point
            deltI=Part.Vertex(100,100,100).Point
            pos=1
            for pp in range(len(point)-1) :
                print "position:",pp+1
                if len(point)-1>1:
                    deltN=(point[0]-point[pp+1])
                    if deltN.Length<deltI.Length:
                        deltI=deltN
                        pos=pp+1
                        print "changement",pos
                else:
                    pos=1   
            print "points a joindre",point[0],point[pos]
            if point[0]!=point[pos]:
                Part.show(Part.makePolygon([point[0],point[pos]]))
            else:
                print "WARNING les points ont la meme valeurs "
            point.pop(0)
            point.pop(pos-1)
        point=0 #to have a return normally void
        return(point)
    working = True
        edgeSet = edges
    result = group(edgeSet)
        working = result[0]
        edgeSet = result[1]
    joint(result[1])
        return result[1]

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro JointWire/it
