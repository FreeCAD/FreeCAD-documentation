# Surface Workbench/pt-br
<div class="mw-translate-fuzzy">





</div>

<img alt="Surface workbench icon" src=images/Workbench_Surface.svg  style="width:128px;">


{{TOCright}}

## Introdução

A bancada de trabalho Superfície foi introduzida no FreeCAD 0.17 e fornece ferramentas para criar e modificar [NURBS surfaces](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) simples. Essas ferramentas tem uma funcionalidade similar à ferramenta [Part Builder](Part_Builder/pt-br.md) quando as opções \"Faces das bordas\" são utilizadas. Entretanto, ao contrário dessa ferramenta, as ferramentas da bancada Superfície são paramétricas e fornecem opções adicionais. Quanto a isso, as ferramentas nesta bancada são similares a recursos como [PartDesign AdditiveLoft](PartDesign_AdditiveLoft/pt-br.md) e [PartDesign AdditivePipe](PartDesign_AdditivePipe/pt-br.md).

Alguns dos recursos disponíveis são:

-   Criação de superfícies a partir de bordas de limite.
-   Alinhamento da curvatura a partir das faces vizinhas.
-   Restrição de superfícies para curvas e vértices adicionais.
-   Extensão de faces.
-   Uma malha pode ser usada como modelo para criar curvas spline em sua superfície.

<img alt="" src=images/Surface_example.png  style="width:350px;">

## Uso

A bancada de trabalho Superfície tem por objetivo criar faces com formas, o que não é possível fazer com as ferramentas padrões em outras bancadas. O OCCT kernel dá como exemplo uma caixa retangular com cantos arredondados de diferentes raios.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">



*Superfície criada com esboços colocados em um plano de referência com as ferramentas de [PartDesign Workbench](PartDesign_Workbench/pt-br.md).*

A bancada Superfície se integra com outras bancadas do FreeCAD. O exemplo acima foi criado a partir de [esboços](Sketcher_Workbench/pt-br.md) colocado sobre [planos de referência](PartDesign_Plane/pt-br.md) na [Bancada PartDesign](PartDesign_Workbench/pt-br.md). O projeto pode ser totalmente paramétrico, quando todos os planos de referência e esboços são definidos de acordo. Na maioria dos casos é suficiente desejar um esboço fechado para definir a borda para uma face; então, opções estão disponíveis para modificar ainda mais sua forma.

The generated surface cannot be placed inside a **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**. However, the generated surface can be contained inside a **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** together with the associated **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)** that holds the datum planes and sketches. The non-parametric **[<img src=images/Part_Builder.svg style="width:16px"> [Part Builder](Part_Builder.md)** tool can then be used in order to create a [shell](Glossary#Shell.md) and finally a [solid](Glossary#Solid.md).

## Ferramentas da bancada Superfície 

-   <img alt="" src=images/Filling.svg  style="width:32px;"> [Enchimento](Surface_Filling/pt-br.md): enche uma série de curvas limite com uma superfície. A superfície pode ser modificada pela adição de curvas de restrição e vértices. A superfície muda de forma para que a superfície passe pelos elementos de restrição adicionados.
-   <img alt="" src=images/BSplineSurf.svg  style="width:32px;"> [Encher curvas limite](Surface_GeomFillSurface/pt-br.md): cria uma superfície a partir de duas, três ou quatro bordas limite. Três diferentes modos de enchimento estão disponíveis:alongar, Coons, Curvar.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Fill boundary curves](Surface_GeomFillSurface.md): creates a surface from two, three or four boundary edges.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Sections](Surface_Sections.md): creates a surface from edges that represent transversal sections of surface. <small>(v0.19)</small> 

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extend face](Surface_ExtendFace.md): extrapolates the surface at the boundaries with its local U parameter and V parameter.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> [Curve on mesh](Surface_CurveOnMesh.md): create approximated spline segments on top of a selected [mesh](Mesh_Workbench.md).


<div class="mw-translate-fuzzy">





</div>


{{Surface Tools navi

}} 

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Surface Workbench/pt-br
