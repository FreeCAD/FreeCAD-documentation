# Placement API/it
**(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

In FreeCAD, Placement (Posizionamento) definisce la posizione e la rotazione di un oggetto. Il concetto di posizionamento è spiegato in dettaglio in: [Placement](Placement/it.md).

Esempio di impostazione del Posizionamento di un oggetto del documento: 
```python
myObj = FreeCAD.ActiveDocument.ActiveObject
pl = FreeCAD.Placement()
pl.move(FreeCAD.Vector(2,0,0))
myObj.Placement = pl
```


{{APIClass|Placement| ) o (Placement) o (Matrix) o (Base, Rotation) o (Base,Rotation,Center) o (Base,Axis,Angle|costruisce un Placement, vuoto o con gli argomenti dati, o come una copia di un Placement dato.}}


{{APIProperty|Base|un vettore che rappresenta la posizione di Placement.}}


{{APIProperty|Rotation|un quaternione che rappresenta la rotazione di Placement.}}


{{APIFunction|inverse| |calcola la posizione inversa|un placement.}}


{{APIFunction|move|Vector|sposta il posizionamento lungo il vettore dato|nulla}}


{{APIFunction|multVec|Vector|applica il Placement al vettore data|il vettore risultante.}}


{{APIFunction|multiply|Placement|moltiplica questo Placement con un'altra|il placement risultante.}}


{{APIFunction|toMatrix| | |una matrice che rappresenta la trasformazione del Placement.}}


 

_ _

---
[documentation index](../README.md) > [API](Category_API.md) > Placement API/it
