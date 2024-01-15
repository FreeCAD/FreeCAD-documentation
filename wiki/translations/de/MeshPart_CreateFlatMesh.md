---
 GuiCommand:
   Name: MeshPart CreateFlatMesh
   Name/de: MeshPart EbenesNetzErstellen
   MenuLocation: Netze , Netz abwickeln
   Workbenches: Mesh_Workbench/de
   Version: 0.19
   SeeAlso: MeshPart_CreateFlatFace/de
---

# MeshPart CreateFlatMesh/de



## Beschreibung

Der Befehl **MeshPart EbenesNetzErstellen** erstellt einen ebenen Repräsentanten eines Netzobjekts (mesh object), indem es eben ausgebreitet oder abgewickelt wird. Der erstellte Umriss ist ein [Part-Formelement](Part_Feature/de.md).

![](images/MeshPart_CreateFlatMesh_example.png ) 
*Ein Netzobjekt und in rot sein ebener Repräsentant*



## Anwendung

1.  Ein einzelnes Netzobjekt auswählen. Das Netz muss abwickelbar sein. Zum Beispiel muss ein zylindrisches Netz offene Enden und eine offene Naht besitzen, damit es abgewickelt werden kann. Gekrümmte Oberflächen müssen auch ein relativ fein unterteiltes Netz besitzen; bei Bedarf den Befehl [Mesh NeuVernetzenGmsh](Mesh_RemeshGmsh/de.md) verwenden.
2.  Den Menüeintrag **Netze → <img src="images/MeshPart_CreateFlatMesh.svg" width=16px> Netz abwickeln** auswählen.



## Eigenschaften

Siehe [Part Formelement](Part_Feature/de.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Category_Mesh.md) > [MeshPart](MeshPart_Workbench.md) > MeshPart CreateFlatMesh/de
