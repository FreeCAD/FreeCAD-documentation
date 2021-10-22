# Installing additional components/pt-br
{{TOCright}}

# Introdução

Após instalar o FreeCAD para seu sistema operacional ([Windows](Installing_on_Windows.md), [Linux](Installing_on_Linux.md) ou [Mac](Installing_on_Mac.md)), você pode considerar a instalação de um ou mais dos seguintes componentes adicionais.

# Arquivos de ajuda 

A documentação offline não é enviada com todos os instaladores, mas está disponível como um pacote separado. Consulte a página [Instalando o arquivo de ajuda](Installing_Helpfile/pt-br.md) para mais informações.

# Bancadas de trabalho externas 

Além das [bancadas de trabalho](workbenches/pt-br.md) padronizadas, agrupadas com o FreeCAD, há uma grande coleção de [bancadas de trabalho externas](External_workbenches/pt-br.md) úteis feitas por membros da comunidade.

# Componente de software de terceiros 

O FreeCAD suporta vários pacotes de software de terceiros prontos para uso. Em muitos casos tudo o que você precisa fazer é instalar o software, e quando o FreeCAD for reiniciado, ele o encontrará automaticamente e poderá usá-lo. Esta seção visa fornecer uma lista de tais pacotes de software, juntamente com algumas informações sobre onde eles são usados no FreeCAD e onde podem ser baixados.

## Suporte

### GitPython

_ pode usar esta biblioteca. GitPython está incluída nos instaladores do FreeCAD para Windows e Mac.

### GraphViz

_.

### OpenCAMLib

_. Veja a página [OpenCamLib](OpenCamLib/pt-br.md) para instruções de instalação.

### OpenSCAD


<div class="mw-translate-fuzzy">

_ depende deste software e o [Bancada de Malhas](Mesh_Workbench/pt-br.md) o utiliza para suas ferramentas Booleanas. Ele também é necessário para a importação de arquivos SCAD com a ferramenta [Importar Std](Std_Import/pt-br.md).


</div>

## Formatos de arquivo 

Todos os softwares desta seção serão utilizados pelas ferramentas [Importar Std](Std_Import/pt-br.md) ou [Exportar Std](Std_Export/pt-br.md).

### CADExchanger

[CADExchanger](https://cadexchanger.com) é uma aplicação comercial para a conversão de vários formatos de arquivo CAD. Existe um [bancada de trabalho externo](https://github.com/yorikvanhavre/CADExchanger) para usar este aplicativo no FreeCAD.

### Importador DXF 

FreeCAD tem um importador e exportador nativo para arquivos DXF, programados em C++. Atualmente eles não implementam todas as características do formato DXF. Para essas características, o importador e exportador Python legado ainda estão disponíveis. Estes requerem a biblioteca _ para mais informações.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

### IfcOpenShell

_. ({{VersionMinus|0.18}}) e ferramentas [BIM IfcExplorer](BIM_IfcExplorer/pt-br.md). O IfcOpenShell está incluído nos instaladores do FreeCAD para Windows e Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) é uma biblioteca necessária para exportar para o formato de arquivo IFCJSON. O IFCJSON é um novo formato IFC que ainda não é suportado por muitas aplicações.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), também conhecida como python-collada, é uma biblioteca Python para ler e escrever arquivos Collada (DAE). O Pycollada está incluído nos instaladores do FreeCAD para Windows e Mac.

## Renderização


<div class="mw-translate-fuzzy">

### LuxCoreRender

_. Oficialmente, não é apoiado pelo _ para mais informações e instruções de instalação.


</div>


<div class="mw-translate-fuzzy">

### LuxRender

_. Em 2013 o projeto foi reiniciado tornando-se _ pode trabalhar com o Raytracing Workbench, talvez valha a pena tentar. Veja a página [LuxRender](LuxRender/pt-br.md) para mais informações e instruções de instalação, e o [LuxCoreRender](LuxCoreRender/pt-br.md) se você quiser experimentar um 'software' mais moderno.


</div>

### POV-Ray 


<div class="mw-translate-fuzzy">

_. Veja a página [POV-Ray](POV-Ray/pt-br.md) para mais informações e instruções de instalação.


</div>

## Elemento finito 

### CalculiX

_.

### Gmsh

_ e [Mesh FromPartShape](Mesh_FromPartShape/pt-br.md).

### Elmer

_.

### FEniCS


<div class="mw-translate-fuzzy">

_.


</div>

### Z88

_. O FreeCAD requer o pacote de código aberto Z88OS.

### OpenFOAM

_ e _.

# Páginas relacionadas 

-   [Importar Exportar](Import_Export/pt-br.md)
-   [Preferências de exportação de importação](Import_Export_Preferences/pt-br.md)
-   [Bibliotecas de terceiros](Third_Party_Libraries/pt-br.md)




_

---
[documentation index](../README.md) > Installing additional components/pt-br
