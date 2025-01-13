# Macro FCInfo/ko
<div class="mw-translate-fuzzy">


{{Macro
|Name=FCInfo 매크로
|Icon=FCInfo.png
|Description=선택한 형상에 대한 정보를 제공하고 길이, 기울기(도, 라디안, 경사도, 백분율), 면적, 부피 및 무게를 다양한 단위(미터법 및 영국식 단위)로 변환하여 표시할 수 있습니다. 이제 이 매크로는 편집 상태에서 스케치의 요소에도 적용됩니다.
<br />프랑스 판[https://gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/57021aa2ac873bf5bdf0aad877cedaa59081dee1/FCInfo_fr_Ver_1-29b-rmu_Docked.FCMacro Version française]
|Author=Mario52
|Download=[https://wiki.freecad.org/images/5/53/FCInfo.png ToolBar Icon]
|Links=[매크로 레시피](Macros_recipes/ko.md)
[매크로 설치방법](How_to_install_macros/ko.md)

|Version=1.29b
|Date=2023/05/10
|FCVersion=모든 버전
|SeeAlso=[Arch Survey](Arch_Survey.md), [Macro SimpleProperties](Macro_SimpleProperties.md), [Macro FCInfoGlass](Macro_FCInfoGlass.md)
}}


</div>



## 설명

선택한 형상에 대한 정보를 제공하고 길이, 기울기(도, 라디안, 경사도, 백분율), 면적, 부피 및 무게를 다양한 단위(미터법 및 영국식 단위)로 변환하여 표시할 수 있습니다. 이제 이 매크로는 편집 상태에서 스케치의 요소에도 적용됩니다.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/c6dd9eabe1ae67d0baf235d672faa75dfd927ad6/FCInfo_en_Ver_1-30-rmu_Docked.FCMacro}}

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*



## 용법

객체를 선택하고 애플리케이션을 시작하거나, 애플리케이션을 먼저 시작한 다음 객체를 선택합니다. 객체가 분석되고 수집된 정보를 보여주는 대화 상자가 열립니다. 새로운 선택이 있을 때마다 길이 단위는 **mm**로 재설정되고 각도 단위는 **십진수**로 재설정됩니다. <img alt="window" src=images/Macro_FCInfo_06.png  style="width:900px;">






### 영역 1: 문서 

![FCInfo Document](images/Macro_FCInfo_Document_00.png )

-   문서 이름
-   객체의 표지와 내부 이름
-   하위 요소 이름 및 객체 유형
-   객체의 종류

*(상자를 숨기려면 변수 **switch_setVisible_GBox_001_Document**를 {{false}}로 체크할 수 있습니다)*



### 영역 2: 마우스 클릭 좌표 

![FCInfo Coordinate](images/Macro_FCInfo_Coordinate_click_mouse_00.png )

-   마우스로 클릭한 곳의 X, Y 및 Z 좌표

-    **button**은 **FreeCAD.Vector(-24.0, 240.0, 7.0)**에서 점, 축, 평면, 복사 벡터 축을 생성합니다.

*(상자를 숨기려면 변수 **switch_setVisible_GBox_002_Coordinate_Mouse**를 {{false}}로 체크할 수 있습니다)*



### 영역 3: 포인트에 색상 넣기 

![FCInfo Color_on_point](images/Macro_FCInfo_Color_on_point_00.png )

-   Color on point clicked.
    -   value 0.0 to 1.0

-   Line Edit display the color value in different formats: {{LineEdit|"3435973887" , "#cccccc" , "0xcccccc" , "204,204,204" , "(0.8,0.8,0.8)"}}
    -   **3435973887** : Mode RVBA Int unsigned (format in FreeCAD preferences) Alpha = 255
    -   **#cccccc** : Mode RVB Hexadecimal (Qt: `setStyleSheet("color : #cccccc")`)
    -   **0xcccccc** : Mode RVB Hexadecimal (Python: `hex(0xcccccc`)
    -   \"**204,204,204** \" : RVB decim: Mode RVB (Qt: `setStyleSheet(u"QLineEdit {"background-color: rgb(204, 204, 204)};")`)
    -   **(0.8,0.8,0.8)** : RVB float: Mode RVB format float de 0.0 à 1.0
    -   (The number of decimals depend of the option *\"x (Decimals)\"*)

-    {{CheckBox|Sub.Objet}}: Change the color of the selected object or subobject. If this box is activated {{CheckBox|TRUE|Sub.Objet}} the face or sub Object selected is modified or duplicated. If it is not activated (default) the object is modified (color) or duplicated

-    **Coul. Obj**: Change the color of the shape or the face depend of the choice. In case object Mesh or Points the complete object is colored.

-    **Dupl. Obj**: Duplicates the face or the object depend to the chosen option. In the case of a Mesh object or Points the complete object is colored. Duplicate a Mesh object keeps the original and creates a solid shape. Duplicate a Points object keeps the original and creates a copy.

-    {{SpinBox|0}}: Degree of transparency of the selected face or object depend on the option chosen **0 = opaque** , **100 = transparent**

*(you can checked to {{false}} the variable **switch_setVisible_GBox_003_Color** for hidden the Box)*



### 영역 4: 메시 구성 요소 

![FCInfo Component Mesh](images/Componant_Mesh_v_1-28.png )

선택 항목이 메시 객체인 경우에만 \'**\'\"구성 요소(Componants)\"**\'영역이 표시되고 다음을 보여줍니다.

-   모서리 : 모서리의 개수 {{LineEdit|9561}}.
-   면 : 면의 개수 {{LineEdit|6374}}.
-   점 : 점의 개수 {{LineEdit|3189}}.

*(상자를 숨기려면 변수 **switch_setVisible_GBox_004_Object_Mesh**를 {{false}}로 체크할 수 있습니다)*


### 영역 5: 단위 

![FCInfo Units](images/Macro_FCInfo_Units_00.png )

-    {{ComboBox|mm}}: 객체가 면의 둘레인 경우 객체의 길이가 표시됩니다. 단위 크기를 선택할 수 있습니다:
    km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

-   물체의 길이 : 물체의 길이 또는 면의 둘레 {{LineEdit|10.0 mm}}.

-   객체가 원이면 두 번째 줄 **반경 :**이 열리고 원의 반지름과 지름 {{LineEdit|2.0 mm (직경 4.0 mm)}}이 표시됩니다.

-   형상의 둘레(12). 객체의 둘레와 객체에 포함된 하위 객체(Edges)의 수 {{LineEdit|120.0mm}}.

*(상자를 숨기려면 변수 **switch_setVisible_GBox_005_Value_Unit**을 {{false}}로 체크할 수 있습니다)*



### 영역 6: 기울기 

![FCInfo Inclination](images/Macro_FCInfo_Inclination_00.png )

-   **객체의 기울기**는 다음과 같이 표시될 수 있습니다:
    -   10진수 도수, 예: {{LineEdit|174.831872611°}}
    -   도 분 초, 예: {{LineEdit|174° 49' 54.741401''}}
    -   라디안, 예: {{LineEdit|3.05139181449 rad}}
    -   등급, 예: {{LineEdit|194.257636235 gon}}
    -   백분율, 예: 30° = {{LineEdit|57.74%}}
-   **XY, YZ, ZX 평면의 경사각** 및 해당 좌표
-   **방향 객체**, {{LineEdit|벡터(0.0, 0.0, -10.0)}}는 객체의 방향을 제공합니다. 계산은 다음과 같습니다: coord_1 - coord_2 = 방향(또는 역방향)
    -   
        **Direction**
        
        이 버튼은 객체 방향으로 선을 만듭니다.
-   **ValueAt(0)**, {{LineEdit|Vector (0.0, 0.0, 10.0)}}는 매개변수 값에 해당하는 3D 벡터를 반환합니다.
    -   
        **ValueAt(0)**
        
        이 버튼은 객체의 ValueAt 방향으로 선을 생성합니다.
-   **NormalAt(0,0)**, {{LineEdit|Vector (0.0, 0.0, 1.0)}}는 매개변수 값에 해당하는 3D 벡터를 반환합니다.
    -   
        **NormalAt(0,0)**
        
        이 버튼은 객체의 NormalAt 방향으로 선을 만듭니다. *(상자를 숨기려면 변수 **switch_setVisible_GBox_006_Inclination**을 {{false}}로 체크할 수 있습니다)*



### 영역 7: 표면과 부피 

![FCInfo Surface and Volume](images/Macro_FCInfo_Surface_and_Volume_00.png )

-   표시되는 형태의 표면, 단위 크기 선택 가능. {{LineEdit|600.0 mm2}}

-   표시되는 면의 표면, 단위 크기 선택 가능. {{LineEdit|0.0 mm2}}

-   표시되는 형태의 부피, 단위 크기 선택 가능. {{LineEdit|1000.0 mm3}}

-   단위, 원하는 단위를 선택하세요.

-    {{ComboBox|gram}}단위 질량을 선택할 수 있습니다.
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct.

-   표시되는 형의 무게, 단위 질량을 선택할 수 있습니다. {{LineEdit|2.7 g}}

-   dm3에 의한 재료의 밀도(kg) {{LineEdit|2.7000 kg (by dm3)}}

-   재료 {{ComboBox|금속 알루미늄 (Al),2.7,10.0,adapt Price}}
    -   매크로 검색을 시작할 때 **FCInfo_material.txt** 파일이 없으면 하나의 FCInfo_material.txt 파일이 생성됩니다.
    -   이 형식으로 저장된 10가지 유형의 자료를 사용하여 파일이 생성됩니다.
        -   **재료 제목, dm3의 밀도, dm3의 가격, 선택에 대한 텍스트 정보**
        -   *(쉼표로 구분된 4개 필드)*
        -   액체 물 (H2o),1,10.0,적응 가격
        -   재료 베톤 (Beton),2.4,10.0,적응 가격
        -   금속 알루미늄 (Al),2.7,10.0,적응 가격
        -   금속 구리 (Cu),8.96,10.0,적응 가격
        -   금속 금 (Au),19.3,10.0,Gratis
        -   금속 철 (Fe),7.87,10.0,적응 가격
        -   금속 납 (Pb),11.35,10.0,적응 가격
        -   금속 마그네슘 (Mg),1.43,10.0,적응 가격
        -   금속 니켈 (Ni),8.27,10.0,적응 가격
        -   금속 땜납 (Sn),7.29,10.0,적응 가격
        -   금속 백금 (Pt),21.45,10.0,적응 가격
        -   금속 은 (Ag),10.5,10.0,적응 가격
        -   금속 나트륨 (Na),0.97,10.0,적응 가격
        -   금속 티타늄 (Ti),4.4,10.0,적응 가격
        -   금속 아연 (Zn),7.1,10.0,적응 가격
        -   나무 너도밤나무,0.8,10.0,적응 가격
        -   나무 MDF,0.75,10.0,적응 가격
        -   나무 마호가니,0.6,10.0,적응 가격
        -   나무 참나무,0.7,10.0,적응 가격
        -   나무 잣나무,0.4,10.0,적응 가격

-   새로운 재료 또는 편집 {{LineEdit|Metal Nickel (Ni),8.27,10.0,적응 가}}
    -   이 형식으로 새로운 료 하나를 수정하거나 편집할 수 있습니다:

    -   **제목, dm3의 밀도, dm3의 가격, 선택에 대한 텍스트 정보**

    -   *(쉼표로 구분된 4개 필드)*

    -   *또한 특정 형식을 준수하여 좋아하는 편집기에서 파일을 편집할 수도 있습니다.*

    -   원하는 경로에 다음 변수를 사용하여 파일을 저장할 수 있습니다: **seTMaterialSavePathName**

    -   *기본적으로 파일은 매크로 경로에 생성됩니다.*

    -   
        **Delete 1/17**
        
        : 표시된 필드를 삭제합니다

    -   
        **Save**
        
        : 수정 사항이나 새로운 자료를 저장합니다

*(상자를 숨기려면 변수 **switch_setVisible_GBox_007_Surface_and_Volume**을 {{false}}로 선택할 수 있습니다)*



### 영역 8: 가격 

![FCInfo Cost](images/Macro_FCInfo_Cost_00.png )

-   비용 총계: 선택한 객체의 비용 총계 {{LineEdit|0.027 Eu}}
-   가격(kg/dm3): 선택한 재료의 가격(*금속 알루미늄(Al),2.7,***10.0***,적응 가격*) {{SpinBox|10,0000 Eu(kg 기준)}}

\'(상자를 숨기려면 변수 **switch_setVisible_GBox_008_Cost_And_Price**를 {{false}}로 선택할 수 있습니다)\'\'



### 영역 9: 경계상자 

![FCInfo BoundBox](images/Macro_FCInfo_BoundBox_00.png )

-   경계상자는 형상의 극한 치수를 보여 줍니다.
    -   최대 X 길이: {{LineEdit|10.0mm}}

    -   최대 Y 길이: {{LineEdit|10.0mm}}

    -   최대 Z 길이: {{LineEdit|10.0mm}}

    -   대각선 길이: {{LineEdit|17.3205mm}}

    -   
        **Tracing**
        
        : 경계상자 크기에 맞춰 6개의 사각형을 만듭니다.

    -   
        **Volume**
        
        : 경계상자의 치수에 맞춰 볼륨을 생성합니다

    -   If the {{CheckBox|TRUE|Text Dim.}} is checked, the spinbox dimension of text {{SpinBox|3,000}} is operational for give your value *(3.0 by default)*

*(you can checked to {{false}} the variable **switch_setVisible_GBox_009_BoundBox** for hidden the Box)*



### 영역 10: 중심 

![FCInfo Center of\...](images/Macro_FCInfo_Center_of_00.png )

-   형상의 중심과 그 XYZ 좌표

-   질량 중심과 그 XYZ 좌표

-    **버튼**은 점, 축, 평면, 복사 벡터축 형태인 **FreeCAD.Vector(-24.0, 240.0, 7.0)**을 생성합니다.(영역13 참고)

*(상자를 숨기려면 변수 **switch_setVisible_GBox_010_Center_Mass**를 {{false}}로 체크할 수 있습니다)*



### 영역 11: 관성 

![FCInfo Inertia](images/Macro_FCInfo_Inertia_00.png )

-   관성모멘트와 이 좌표들의 길이와 무게
-   The button creates on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)** *(see Sector 13)*
    -   action line 1 : {{LineEdit|x1}}, {{LineEdit|y1}}, {{LineEdit|z1}}, {{LineEdit|0.0}}
    -   action line 2 : {{LineEdit|x2}}, {{LineEdit|y2}}, {{LineEdit|z2}}, {{LineEdit|0.0}}
    -   action line 3 : {{LineEdit|x3}}, {{LineEdit|y3}}, {{LineEdit|z3}}, {{LineEdit|0.0}}
    -   action 4 diagonal : {{LineEdit|x1}}, {{LineEdit|y2}}, {{LineEdit|z3}}

same for length and weigth

-   Determinant 1 : {{LineEdit|4629629629629.633}} computes the determinant of the matrix, in [scientific value](https://en.wikipedia.org/wiki/Scientific_notation)
-   Determinant 2 : {{LineEdit|4629629629629.6328125}} computes the determinant of the matrix, in decimal value

*(you can checked to {{false}} the variable **switch_setVisible_GBox_011_Inertia** for hidden the Box)*



### 영역 12: 스프레드시트 

![FCInfo Disabled](images/Macro_FCInfo_Disabled_module_00.png )

-    {{CheckBox|Disabled module}}CheckBox for search or not all details of the object. If it is not checked, only the principal value is displayed.

-   Vertexes and details of the shape (compt_Edge), (compt_Faces), (compt_Vector of the Face)

-   Max 200 lines in the table, if there are more than 200 lines it appears **(!+ 200)** and the number of lines

-   If the object is complicated with many objects, the time is long and the search is repeated with every mouse click. The write function in the spreadSheet included, decreases the display time for this it is disabled by default

-   Full details can save be the **Save** button in a file in CSV format and can be viewed the file in spreadsheet with the **Read** or by an external spreadsheet as [LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) or other

*(you can checked to {{false}} the variable **switch_setVisible_GBox_012_SpreadSheet** for hidden the Box)*



### 영역 13: 스프레드시트 생성 

![FCInfo SpreedSheet](images/Macro_FCInfo_SpreedSheet_00.png )

-    **SpreadSheet**: create a new spreadsheet in a document

-    {{LineEdit|SpreadSheet}}: the current spreadsheet. if the spreadsheet does not exist one spreadsheet is created

-    **Refresh**: refresh the list of spreadsheet in document

-    {{ComboBox|-}}: the spreadsheet(s) present in document

-    **Read**: read the data in a spreadsheet saved **.FCInfo** or txt, asc, csv

-    **Save**: save the data in disk in the form selected below **.FCInfo** or txt, asc, csv

-    {{RadioButton|TRUE|Tabulation}}: the separator is Tabulation (by default)

-    {{RadioButton|Comma}}: the separator is Comma

-    {{RadioButton|Semicolon}}: the separator is Semicolon

-    {{RadioButton|Space}}: the separator is Space

Option for **save** or **read** the spreadsheet with different separator, Tabulation, Comma, Semicolon, Space
The Tabulation are the separator for the FreeCAD \[Spreadsheet_Workbench\|Spreadsheet workbench\]
The number of this four separator are calculate for help if unknown
The COMMA are the old (01.16 and before) separator of the FCInfo macro
Now for compatibility with the FreeCAD spreadsheet and since 01.17 version the TABULATION is the separator by default
If you want to convert your old FCInfo spreadsheet : Open it in FCInfo and save it with the Tabulation option checked
*(you can checked to {{false}} the variable **switch_setVisible_GBox_013_SpreadSheet_Creation** for hidden the Box)*



### 영역 14: 주요 도구 

![FCInfo Main](images/Macro_FCInfo_Main_00.png )

-    {{CheckBox|Info}}: if this CheckBox is checked, the informations are displayed in the report view window

-    {{CheckBox|Point}}: if checked, one point is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{CheckBox|Axis}}: if checked, one axis is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{CheckBox|Plane}}: if checked, one axis plane is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{RadioButton|Clip-B0}}: None clipBoard

-    {{RadioButton|Clip-B1}}: If checked the coordinate are copy in the clipBoard Form : **FreeCAD.Vector(X.0, Y.0, Z.0)** FreeCAD model

-    {{RadioButton|Clip-B2}}: If checked the coordinate are copy in the clipBoard Form : **X, Y, Z** with Comma separator

-    {{RadioButton|Clip-B3}}: If checked the coordinate are copy in the clipBoard Form : **X Y Z** as is with Space separator

-    {{CheckBox|Left/Right}}: if this CheckBox is not checked, the window macro are displayed to right (default). If it is checked the window macro are displayed to left.
    If the option is 1 mode fly *(User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo/**seTPositionFlyRightLeft**)* this button is not visible .

-    {{SpinBox|4 (Decimales)}}: give the number of decimal displayed

-    {{SpinBox|12 (Dim. texte)}}: give the dimensionof text in the macro

-    **Forum**: direction FCInfo forum tread *(you must to be connected to internet)*

-    **Wiki**: direction Wiki FCInfo *(you must to be connected to internet)*

-    **Ref**: refresh the display of data in report view

-    **Exit**: exit properly the macro *(not use the red cross of the window)*

*(you can checked to {{false}} the variable **switch_setVisible_GBox_014_Main_Tools** for hidden the Box)*

매크로를 실행하면 매크로가 활성 상태를 유지하고 창은 계속 표시됩니다. **Exit**를 눌러 매크로를 종료합니다. x로 종료하면 매크로는 메모리에 남아 있으며, 데이터는 FreeCAD의 \"보고서 보기\"에 나타납니다. 이를 종료하려면 FreeCAD를 다시 시작해야 합니다.


<center>

Image:Macro_FCInfo_04.png\|오른쪽에 고정, Image:Macro FCInfo 05.png\|또는 콤보 보기로 두고 탭으로 접근 가능하게 하거나, 고정하지 않고 선택할 수 있습니다.


</center>






## 선택 사항 



### 사용된 단위 



#### 길이 단위: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.



#### 각도 :

1.  **decimal degree**, ex: 174.831872611°
2.  degree minute seconde, ex: 174° 49\' 54.741401\'\'
3.  radian, ex: 3.05139181449 rad
4.  grade, ex: 194.257636235 gon
5.  percent ex: 30° = 57.74%

FCInfo 표시에서 각도에 대한 이해.


<center>

Image:Macro FCInfo 02.png\|FCInfo 표시의 각도 이해 Image:Macro FCInfo 03.gif\|FCInfo 표시에서 각도를 백분로 이해하기
동영상을 보려면 두 번 클릭하세요(이미지는 전체 화면이어야 함)


</center>






#### 무게 단위 : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct



#### FCInfo 구성 

-   Location : **Tools \> Edit parameter \> \*User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo/**
-   **switchNotInfoOnBeginning** **\#** SetBool {{true}} or \[{{false}}\]
    -   Display or not this text information on run macro
        -   \[{{false}}\] = display this information

        -   
            {{true}}
            
            = this Information is Not displayed On Beginning
-   **switchVersionSearch** **\#** SetBool {{true}} or \[{{false}}\]
    -   Search if one new version exist on run macro
-   **switchWarning** **\#** SetBool {{true}} or \[{{false}}\]
    -   Display or not display the window warning in case not good selection
-   **switchCreatePoint** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create point checkBox
-   **switchCreateAxis** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create axis checkBox
-   **switchCreatePlane** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create plane checkBox
-   **switchDisplayInfoObject** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the info checkBox
-   **switchClearDisplayReportView** **\#** SetBool {{true}} or \[{{false}}\]
    -   if switchClearDisplayReportView is {{true}} the ReportView is cleared
-   **seTWidgetPosition** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Widget Position Left/Right checkBox
    -   if seTWidgetPosition \[{{false}}\] : if seTPositionFlyRightLeft = 2 = docked to Right
    -   if seTWidgetPosition {{true}} : if seTPositionFlyRightLeft = 3 = docked to Left
    -   if it is 1 the window macro is not docked
-   **switchBoundBoxCreateText** **\#** SetBool {{true}} or \[{{false}}\]
    -   Create the text dimension of the BoundBox
-   **seTBoundBoxTextHeigth** **\#** seTBoundBoxTextHeigth = 3.0
    -   Give the Heigth of the text dimension (independent of the seTTextHeigthValue)
-   **seTBoundBoxTextArround** **\#** seTBoundBoxTextArround = 3
    -   Give the arround of the text dimensions (independent of the seTDecimalValue)
-   **seTMemoClipBoard** **\#** SetInt \[0\], 1, 2, 3
    -   Give one value \[0\], 1, 2, 3 clipBoard
        -   \[0\] = desactivate the clipBoard
        -   1 = the data string is memorised to : FreeCAD.Vector( X, Y, Z )
        -   2 = the data string is memorised to : X, Y, Z
        -   3 = the data string is memorised to : X Y Z
-   **seTTextHeigthValue** **\#** SetInt 11
    -   Give one text heigth value of the macro
-   **seTDecimalValue** **\#** SetInt 4
    -   Give the number of decimal displayed
    -   If the number is -1 the total decimal value is displayed)
-   **seTMaterialCurrentIndex** **\#** SetInt 0
    -   Set the index of the ComboBox
-   **seTMaterialFileName** **\#** SetString FCInfo_material.txt
    -   Name of the material file
-   **seTMaterialSavePathName** **\#** SetString C:\\\...\\Macro\\FCInfo_material.txt
    -   Path name of the material file
-   **seTMaterialPrice** **\#** SetFloat
    -   Material price by Kg
-   **seTMaterialSuffixDevise** **\#** SetString
    -   Devise money
-   **seTMaterialSuffixCost** **\#** seTMaterialSuffixCost
    -   Suffix Devise cost
-   **seTMaterialCost** **\#** SetFloat
    -   Material cost
-   **seTDensiteValue** **\#** SetFloat 1.0
    -   Give the densite value
-   **seTDensiteDecimalNumber** **\#** SetInt 4
    -   Give the number of decimal for the densite value
-   **seTDensiteSingleStep** **\#** SetFloat 1.0
    -   Give the step for one click, by default 1.0 (possible 0.01 or \...)
-   **seTDensiteSuffixChain** **\#** SetString kg (by dm3)
    -   Choice your suffix string
-   **seTPositionFlyRightLeft** **\#** SetInt 2
    -   Choice your position, Fly, \[Right\], Left
        -   1 = the macro window is fly (not docked)
        -   \[2\] = the macro window is positioned to Right
        -   3 or other = the macro window is positioned to Left
-   **seTIndexUnitWeight** **\#** SetInt
    -   Set unit Weight index
-   **seTUnitSymbolMicro** **\#** U
    -   Set Symbol Micro
-   **seTUnitSymbolCube** **\#** 3
    -   Set Symbol Cube
-   **seTUnitSymbolCarre** **\#** 2
    -   Set Symbol Square
-   **seTIndexUnitLength** **\#** SetInt
    -   Set unit Length index
-   **setBSplineToByArcValue** **\#** SetFloat 0.00001
    -   Set unit for cut the BSpline for seack the radius on point given
-   **setMeshTopologyValue** **\#** SetFloat 0.1
    -   Set unit for create the Mesh to Shape
-   **switchBSplineCreateCircleConstructorAxis** **\#**SetBool {{true}} or \[{{false}}\]
    -   Display the axis of the circles (arcs) for create the BSpline
-   **switchBSplineCreateCircleConstructor** **\#**SetBool {{true}} or \[{{false}}\]
    -   Display the circles cretors for create the BSpline
-   **switchCreateLineDiVatNatOnClick** **\#**SetBool {{true}} or \[{{false}}\]
    -   Create the Line info on point (0,0,0) or on point mouse clicked (x,y,z) if it is {{true}}
    -   If it is {{true}} one \'\*\' is displayed in front of text. EX: \'\*Direction\'

This switch *(section GroupBox)* allows you to view only the desired section(s) (just visual) {{False}} or {{True}}.

All calculations are done without taking account of this option

-   section GroupBox begin
    -   **switch_setVisible_GBox_001_Document** = True (1)
    -   **switch_setVisible_GBox_002_Coordinate_Mouse** = True (1)
    -   **switch_setVisible_GBox_003_Color** = True (1)
    -   **switch_setVisible_GBox_004_Object_Mesh** = True (1)
    -   **switch_setVisible_GBox_005_Value_Unit** = True (1)
    -   **switch_setVisible_GBox_006_Inclination** = True (1)
    -   **switch_setVisible_GBox_007_Surface_and_Volume** = True (1)
    -   **switch_setVisible_GBox_008_Cost_And_Price** = True (1)
    -   **switch_setVisible_GBox_009_BoundBox** = True (1)
    -   **switch_setVisible_GBox_010_Center_Mass** = True (1)
    -   **switch_setVisible_GBox_011_Inertia** = True (1)
    -   **switch_setVisible_GBox_012_SpreadSheet** = True (1)
    -   **switch_setVisible_GBox_013_SpreadSheet_Creation** = True (1)
    -   **switch_setVisible_GBox_014_Main_Tools** = True (1)
-   section GroupBox end



## 스크립트

\"FCInfo.FCMacro\"라는 파일에 매크로 내용을 복사합니다.

-   Windows: 형식은 일반적으로 **\" 드라이브:\\사용자\\사용자_이름\\AppData\\Roaming\\FreeCAD\\ \"**입니다.
-   Ubuntu: 형식은 일반적으로 **\" /home/your_user_name/.FreeCAD \"**입니다.
    또는 FreeCAD 인터페이스에서 직접
    아이콘은 매크로와 같은 디렉토리에 있어야 합니다.

<img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> 아이콘에 이미지 위치를 다운로드한 다음 마우스 오른쪽 버튼을 클릭하여 \"다른 이름으로 저장\"을 클릭합니다(이름을 변경하지 마세요)
**추신: 코드가 너무 길어서 위키 페이지에 담을 수 없습니다(현재 위키 페이지는 64KB만 허용합니다). 매크로 코드는 포럼에 게시했습니다**
gist에 있는 매크로 파일을 다운로드하세요 **오른쪽에 고정됨**


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|last version Macro_FCInfo}}

(또는 **[포럼에서.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**추신:** 이 매크로는 **getSelection()**을 사용하고 객체 목록은 1부터 시작합니다. 예: 상자의 경우 **Edge1\~Edge12**이고 콘솔의 코드는 0부터 시작합니다. 예: 상자의 경우 **Edge\[0\]\~Edge\[11\]**
이는 정상입니다. OpenCascade 내부에서 배열/목록의 계산은 항상 **1\'에서 시작하고 0**에서 시작하지 않습니다.



### 제한사항

항상 **Exit** 버튼을 눌러종료 하세요. **Exit** 버튼을 누르지 않고 프로그램을 종료하면, 프로그램은 메모리에 남아 계속 실행되고, 디스플레이는 \"보고서 보기\"에 머물러 있습니다.
표에는 객체의 처음 200개 요소만 표시됩니다. 객체에 200개가 넘는 항목이 있는 경우 **(! +200)** 신호가 표시됩니다. 전체 데이터 목록은 **Save** 버튼을 눌러 저장된 파일에서 볼 수 있습니다.

실행 후 창 매크로가 보이지 않으면 아래 창을 확인하세요.

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 

프로젝트:
~~테이블에서 파일을 직접 읽기.~~ 완료
~~\"모서리\"와 해당 좌표를 일치시키기.~~ 완료
~~물질과 밀도의 연관성~~
~~전역 객체보다는 요소에 대한 기울기~~ 완료
~~FreeCAD 인터페이스에 바로 박어 넣기~~ 완료


## 버전

ver \"1.30\" 2025/01/02 : delette all reference to PySide PySide2 and QtWidgets modify the (Qt) Save file


```python
#
import PySide2
from PySide2 import QtGui , QtCore, QtWidgets
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QTableWidget, QApplication
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

            OpenName, Filter = PySide2.QtWidgets.QFileDialog.getOpenFileName(None, u"Read a txt file", setPathLatestDirectory, "*.FCInfo *.csv *.asc *.txt;;FCInfo (*.FCInfo);;Cvs (*.csv);;Ascii (*.asc);;TXT (*.txt);;(*.*);;(*)")#PySide2
```

replaced and change command by


```python
#
import PySide
try:
    from PySide import QtWidgets
    from PySide.QtWidgets import *
except Exception:
    None
from PySide import QtGui , QtCore
from PySide.QtGui import *
from PySide.QtCore import *

            OpenName, Filter = QFileDialog.getOpenFileName(None, u"Read a txt file", setPathLatestDirectory, "*.FCInfo *.csv *.asc *.txt;;FCInfo (*.FCInfo);;Cvs (*.csv);;Ascii (*.asc);;TXT (*.txt);;(*.*);;(*)")#PySide

```

ver \"1.29b\" 2024/05/10 **PySide2** 관성 \"MatrixX1\*uniteM을 (MatrixX1\*uniteM)\"으로 수정하고 spinBox 관성을 추가했습니다.

-   [Moment of inertias calculation](https://forum.freecad.org/viewtopic.php?p=713935#p713935)
-   [Momentof Interia - FCInfo macro](https://forum.freecad.org/viewtopic.php?t=64653)

ver 1.29 2024/05/06 **프랑스어** 버전 **fr PySide6** sylvainbx 작성 <https://gist.github.com/sylvainbx/af09a30be3e1427de56305825331fb29> sylvainbx님께 감사

ver 1.28b 1.28c 2023/10/30 철자

ver 1.28 01/09/2023 변수 이름 수정, 각 영역 숨김 가능, 문서에 데이터 스프레드시트 저장, 표면 반경, webWiki 및 webForum 버튼 추가

ver 1.27 2023/06/30 스타일시트 최적화, 좌우 위치 수정, 스케쳐 편집 후 뷰 복원 
```python
            self.PB_00_Decrement.setStyleSheet("background-color: white; border:2px solid rgb(215, 10, 22);")      # bord white and red
``` 로 대체됨 
```python
            self.PB_00_Decrement.setStyleSheet("QPushButton {background-color: white; border:2px solid rgb(215, 10, 22)};")      # bord white and red
```

-   ver 1.26c 2022/04/19 B조절곡선 오류를 기어 B조절곡선=Line으로 업그레이드

-   ver 1.26b 2022년 2월 20일 하위객체에서 B조절곡선 감지를 위한 업그레이드

-   ver 1.26 06/02/2022 메시 및 포인트 객체에 대한 정보 추가, 색상 디코딩, 객체 또는 하위 객체 복제, 최신 경로 및 기타 기본 설정 기억

-   ver 1.25e 2021년 12월 18일 B조절곡선(ToByArcs)에 대한 자세한 정보와 정보 \"sel\[0\].TypeId\" 추가
-   ver 1.25d 2021년 12월 12일 \-\--
-   ver 1.25c 2021년 12월 12일 \"strAround((\"를 \"str(Around(\" 및 기타 작은 \...로 수정
-   ver 1.25b 2021년 12월 11일 변경/신규 자료 수정 및 재구성 시 수정 오류
-   ver 1.25 2021년 12월 10일 PySide2와 comboBox 소재 추가
-   ver 1.24 2021년 12월 2일 edwilliams16님이 몸통, 경계상자 추적을 위한 배치를 위해 수정한 [adjustedGlobalPlacement](https://forum.freecadweb.org/viewtopic.php?f=22&t=59852)를 추가
-   ver 1.23cb 2021년 11월 25일 **\"import Sketcher \* \"** 삭제 \"**open(OpenName, \"r\")**\"와 충돌 발생 ?? 추가


```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```

-   ver 1.25d, 2021년 12월 13일 재료 필드에서 약간의 수정 \"\'try\...Except\"의 주석 처리를 해제하세요!!!
-   ver 1.25c, 2021년 12월 12일 약간의 수정, 새 재료
-   ver 1.23b, 2021년 11월 20일 약간의 수정, 시작 실행 매크로에 텍스트 정보 추가 및 텍스트 코드 순서 지정
-   ver 1.23, 2021년 11월 19일 매크로의 아이콘, 표시되는 소수점 숫자, 텍스트 높이, 기본 설정 FC의 옵션 구성, 편집 모드에서 스케치 요소에 대한 올바른 정보가 포함됩니다.
-   ver 1.22, 2020년 12월 11일: 이제 매크로가 완전히 제거되어 다음을 사용합니다:


```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` 그리고 \"오류 메시지\" 창을 기본적으로 \"거짓\"으로 표시할지 여부를 선택할 수 있는 가능성을 추가했습니다. 경고 창을 활성화하려면 다음으로 이동하세요. 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```

-   ver 1.21-3.01, 2019년 7월 11일 \# 2019년 7월 11일 ver \"01.21-3-rmu\" 문자 micro = \"U\", square = \"2\", cube = \"3\", degrees = \"deg\"를 대체합니다. \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819%22를> 참조하세요.
-   ver 1.21-2.01 (1.21-rmu) 2019년 11월 6일 rmu는 ex에서 127을 넘는 모든 문자를 \"°\"로 바꿉니다. chr(176)) #degree
-   ver 1.21.01 (1.21-rmu) 2019년 5월 30일 rmu는 rmu75가 qt 레이아웃 grid.addWidget()에 고정된 위치를 변경합니다. rmu75 포크 \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8%22를> 참조하세요.
-   ver 1.21, 2019년 4월 16일 Py 3\... Qt 5\... FreeCAD 0.15\~0.19 릴리스에 대한 최적화

ver 1.20, 2018년 1월 29일 최적화 ver 1.19, 2018년 1월 20일 원하는 경우 객체의 모든 요소를 ​​감지하는 데 사용할 체크박스를 만듭니다. 매크로가 더 빠릅니다. 최적화

-   ver 1.18 , 2017년 12월 19일 \...
-   ver 1.17c , 2017년 12월 14일 한 프로젝트에서 주어진 좌표로 다른 프로젝트에서 평면을 생성하고 \"FCInfo\"를 \"\_\_title\_\_\"로 바꿉니다.
-   ver 1.17b , 2017년 12월 13일 FCTreeView를 FCInfo로 약간 수정
-   ver 1.17 , 2017년 12월 12일 pinq의 관성 모멘트(mm 및 kg) 업그레이드 추가 [FCMacro 및 조립 관성 모멘트](https://forum.freecadweb.org/viewtopic.php?t=23888), 평면, 축, 점 생성 및 스프레드시트에 대한 옵션 구분 기호 추가
-   ver 1.16 , 2017년 6월 21일 제어 높이 정책(여기서는 PointSize 8)과 창을 오른쪽 또는 왼쪽으로 위치시키는 체크박스를 추가했습니다.
-   ver 1.15 , 2015년 12월 19일 PyQt4 옵션 억제 [참조](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541), 보고서 보기에서 정보 편집을 위한 체크박스 추가
-   ver 1.14 , 2014년 8월 4 PyQt4와 PySide를 교체하고 PySide에 표시되지 않는 도구 설명을 수정하고 fg를 추가했습니다.
-   ver 1.13 , 2014년 7월 27일 FCInfo_en_Ver_1-12_Docked.FCMacro를 FCInfo_en_Ver_1-13_Docked.FCMacro로 교체하여 PyQt4 및 PySide를 허용합니다.
-   ver 1.12 , 2014년 10월 3일 도구설 추가
-   ver 1.11 , 2014년 3월 4일 µm, nm, pm, fm, µg, ng, pg, percent 추가 , 보석의 질량단위를 ~~\"cd\"~~에서 **\"ct\"**로 수정, 표지 내부 이름을 표시, 복합 형상에서 XY YZ ZX각도의 계산오류 수정, FreeCAD에서 도킹 가능한 창
-   ver 1.10b , 12013년 11월 19일 스크롤바 외부 버튼과 창 크기 차단
-   ver 1.10 , 2013년 11월 18일 스크롤바 생성
-   ver 1.08b , 2013년 10월 11일 영어 번역 단위, 표에 나열된 면의 면적을 표시하기 위한 오류 수정 및 \"**print**\"를 \"**App.Console.PrintMessage**\"로 교체
-   ~~ver 1.09, 2013년 4월 11일 Windows 및 Linux에서 완벽하게 작동합니다(Linux에서는 오류로 인해 문자: ² ³ ° \"순서가 범위(128)에 없습니\")~~
-   ver 1.08 , 2013년 10월 24 (저장된 파일에서) 100개의 개체를 표시하는 상단 \'면\'과 \'모서\'의 수정
-   ver 1.07 , 2013년 11월 10일은 \"면\"과 그 좌표의 일치.

\*ver 1.06 , 2013년 9월 22일 \"모서리\"와 해당 좌표의 일치, 전역 객체보다는 요소에 대한 기울
\*ver 1.05 , 2013년 9월 17일 스프레드시트 아이콘, 프랑스어 변환 배럴, 좌표 대신 전체 치수 표시가 추가.
\*ver 1.04 , 2013년 11월 9일: 테이블에서 파일을 직접 읽.
\*ver 1.03 , 2013년 9월 9일: 보기 보고서에서 더 명확하게 표시되고 \"typeObject = sel\[0\].Shape.ShapeType\"으로 대체됨
\*ver 1.02 , 2013년 9월 7일 : 작은 업데이트
\*ver 1.00 , 2013년 9월 6일


## 참고 문서 연결 

<img alt="아치 조사" src=images/Arch_Survey.svg  style="width:36px;"> [건축 작업대의 측량도](Arch_Survey/ko.md) 참고하세요.

포럼에서 [Info Workbench - 아이콘에 대한 도움말을 부탁드립니다.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)주제로 의견을 나눌 수 있습니다
[FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)의 또 다른 게시물이 있습니다.



---
⏵ [documentation index](../README.md) > Macro FCInfo/ko
