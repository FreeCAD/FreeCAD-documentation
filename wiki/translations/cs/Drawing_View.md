# Drawing View/cs
---
- GuiCommand   */cs   Name   *Drawing View   Name/cs   *Drawing View   Workbenches   *[MenuLocation   *Drawing → Insert view in drawing   Shortcut   *none   SeeAlso   *[[Drawing Landscape A3/cs|Výkres A3 na šířku](Drawing_Workbench/cs___Výkres]],_Complete.md)---


</div>

Tento nástroj výtváří nový pohled na vybraný objekt v aktivním výkresu.

<img alt="Výkres se třemi pohledy   * zepředu, shora a izometrický." src=images/Drawing_Views.png  style="width   *500px;">


<div class="mw-translate-fuzzy">

### Použití

Vyberete objekt buď ve 3D pohledu nebo ze stromu projektu, potom kliknete na nástroj Pohled. Pohled shora v měřítku 1   *1 (skutečná velikost) bude standardně umístěn do horní levé části stránky. Někdy tak může být objekt neviditelný je-li příliš malý nebo příliš velký na stránku.


</div>

Objekt **Pohled** je vložen do objektu **Stránka** ve stromu projektu. Pro číslování pohledů je za název přidáno tříciferné číslo. Kliknutím na šipku před složkou objektu Stránka se složka rozbalí a zobrazí se v ní obsažené pohledy.

If only the object is selected in the Project Tree, the view is added to the first page of the project. If you have multiple pages in your project please select the object and the page it should be added to. Then click on the icon to add the view to the selected page.

### Úpravy existujícího pohledu 

Ve stromu projektu rozbalíte složku objektu Stránka a vyberete pohled. Jeho parametry mohou být upravovány v záložce Data Pohledu.

<img alt="" src=images/Drawing_View_Properties.png‎ ) ![Izometrický pohled s vypnutou viditelností smooth lines](images/Drawing_View_Iso.png‎  style="width   *150px;"> <img alt="Izometrický pohled se zapnutou viditelností smooth lines" src=images/Drawing_View_Iso_SmoothLines.png‎‎  style="width   *150px;">

-   **Jmenovka**   * mění název pohledu ve stromu projektu. Také můžete kliknout na pohled ve stromu a pravým tlačítkem myši Přejmenovat nebo stisknout klávesu **F2**.
-   **Rotace**   * otáčí pohled. Například izometrický pohled bude potřebovat otočení o 60 stupňů (podívejte se také dále na parametry směru)
-   **Měřítko**   * nastaví měřítko pohledu.
-   **X**   * nastaví vodorovnou pozici pohledu na stránce v milimetrech.
-   **Y**   * nastaví svislou pozici pohledu na stránce v milimetrech. Všimněte si prosím, že souřadnice (0,0) je umístěna v levém horním rohu stránky, takže čím je vyšší číslo tím níže bude pohled na stránce.
-   **Směr**   * mění směr pohledu. Je dán hodnotami xyz, které definují vektor kolmý ke stránce. Pohled shora bude (0,0,1), a izometrický bude (1,1,1). Hodnoty mohou být záporné.
-   **Zobraz skryté čáry**   *  přepíná viditelnost skrytých čar výběrem hodnot *True* nebo *False*.
-   **Zobraz Smooth Lines**   * přepíná viditelnost smooth lines výběrem hodnot *True* nebo *False*. Smooth lines jsou také nazývány dotykové okraje. Tyto okraje indikují místa, kde jedne povrch přechází v druhý (dotýkají se).

### Průvodce Pohledem 

K automatickému generování výkresů se standardními pohledy používejte [Automatické výkresové makro](Macro_Automatic_drawing/cs.md). 

### Other

If you are looking for persective-orthographic toggling in 3D view check [Std PerspectiveCamera](Std_PerspectiveCamera.md) and [Std OrthographicCamera](Std_OrthographicCamera.md)


{{docnav
|[New A3 landscape drawing](Drawing_Landscape_A3.md)
|[Annotation](Drawing_Annotation.md)
|[Drawing Workbench](Drawing_Workbench.md)
|IconL=Drawing_Landscape_A3.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Annotation.png
}}


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Drawing_Workbench.md) > Drawing View/cs
