# O-X-Y Type Attachment Modes/pl
Niniejszy opis podaje bardziej szczegółowe informacje na temat korzystania z trybów typu **Wyrównanie O-X-Y** w edytorze [dołączenia](Part_EditAttachment/pl.md) środowiska pracy Część.

Są to następujące tryby:

-   Wyrównanie O-Z-X
-   Wyrównanie O-Z-Y
-   Wyrównanie O-X-Y
-   Wyrównanie O-X-Z
-   Wyrównanie O-Y-Z
-   Wyrównanie O-Y-X

Tryby te są używane do dołączania do określonego wierzchołka, z orientacją określoną przez odniesienie do innych wierzchołków lub krawędzi.


**Odniesienie1**

musi być wierzchołkiem. Punkt odniesienia połóżenia jest mapowany do tego wybranego punktu.

Uwaga: Jeśli dla parametru **Odniesienie1** wybrano krawędź, tryby typu O-X-Y nie są dostępne.


**Odniesienie 2**

i **Odniesienie 3** muszą być wierzchołkami lub krawędziami. Dostarczają one informacji o kierunku. W przypadku wierzchołka jest to kierunek od początku do wybranego wierzchołka. W przypadku krawędzi jest to kierunek krawędzi. **Odniesienie 3** jest opcjonalne.

Weźmy tryb O-X-Z jako przykład:

-   **O** reprezentuje punkt odniesienia, odpowiadający parametrowi **Odniesienie 1**.
-   **X** wskazuje, że oś X dołączonego obiektu ma być wyrównana z kierunkiem **Odniesienie 2**.
-   **Z** wskazuje, że oś Z dołączonego obiektu ma być wyrównana ze składową kierunku **Odniesienie 3** pod kątem prostym do osi X.
-   Oś **Y** uzupełnia triadę ortogonalnej prawej osi.

W przypadku innych trybów osie są mapowane w odpowiedni sposób.

Jeśli parametr **Odniesienie 3** nie zostanie podany, FreeCAD dokona wyboru domyślnego.


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > O-X-Y Type Attachment Modes/pl
