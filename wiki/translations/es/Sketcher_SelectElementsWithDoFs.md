---
- GuiCommand:/es
   Name:Sketcher SelectElementsWithDoFs
   Name/es:Croquizador SeleccionarElementosConGdL 
   MenuLocation:Croquis → Croquizador Herramientas → Seleccionar GdL del solucionador
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   Version:0.18
---

# Sketcher SelectElementsWithDoFs/es


</div>



## Descripción

Esta herramienta está pensada para ayudar a restringir completamente un croquis resaltando en verde los elementos del croquis con grados de libertad (GdL) (inglés: DoF Degrees of Freedom) restantes.



## Utilización

En el cuadro de mensajes del Solucionador, situado en la parte superior del [Pestaña Tareas](Task_panel/es.md), deberían aparecer los siguientes mensajes:

-   En caso de un croquis **restringido inferior**:

> Croquis bajo-restringido con X grados de libertad

donde \"X\" es el número de grados de libertad que quedan en el croquis; recibirá más información si hace clic en el enlace azul, o si utiliza el menú.

1.  Los elementos que tienen grados de libertad están ahora resaltados en verde.
2.  Haga clic en cualquier parte del croquis para borrar el color de resaltado.

-   En el caso de un croquis **totalmente-restringido**:

> Croquis totalmente restringido


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/es
