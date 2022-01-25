# Base API/it
**(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

Il modulo Base è contenuto all\'interno del modulo FreeCAD e contiene i costruttori per i diversi tipi di oggetti intensamente utilizzati in FreeCAD.


{{APIClass|BoundBox|[Xmin,Ymin,Zmin,Xmax,Ymax,Zmax] ) o ( Tuple, Tuple ) o ( Vector, Vector|Crea una scatola di delimitazione. Una scatola di delimitazione è un cubo che serve a descrivere i limiti esterni. Si può ottenere una scatola di delimitazione da diversi tipi di 3D. Si utilizza spesso per verificare se una entità 3D interferisce con un altro oggetto. La verifica iniziale dei limiti di interferenza può evitare di perdere un sacco di tempo in calcoli!}}


{{APIClass|Matrix| |Crea una [Matrice](Matrix_API/it.md) 4x4, che può essere usata per applicare delle trasformazioni agli oggetti.}}


{{APIClass|Vector|) o ( x,y,z|Crea un [Vettore](Vector_API/it.md) 3D di FreeCAD, che rappresenta un punto 3D o una direzione.}}


{{APIClass|Placement| |Crea una [Posizione](Placement_API/it.md).}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Base API/it
