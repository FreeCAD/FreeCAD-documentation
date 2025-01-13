# DAG view/ko
## 소개




**DAG**는 방향성 비순환 그래프( [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph))의 약어로 DAG 보기(DAG view)는 여러 개체들 간의 관계를 보여 주는 문서입니다. <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">[부품설계 작업대등에서](PartDesign_Workbench/ko.md) 많은 도형특징과 참조를 통해 만들어지는 복잡한 모형에서 특정 객체가 다른 객체에 어떻게 종속되는지 보여주기 위한 것입니다.

DAG 보기는 Git 저장소 및 해당 분기에서 생성할 수 있는 그래프와 유사합니다. 표준 [나무 보기(tree view)](tree_view/ko.md) 및 [종속성 그래프와](Std_DependencyGraph/ko.md) 함께, DAG 보기는 문서에 있는 개체의 매개변수 기록을 검사하는 도구입니다.



## 예제

아래의 간단한 모형은 다양한 보기(view)로 볼 수 있습니다.

![](images/FreeCAD_DAG_view_3D.png ) 
*2D 및 3D 형상을 사용한 모형
.*

<img alt="" src=images/FreeCAD_DAG_view_Tree_view.png ) ![](images/FreeCAD_DAG_view.png  style="width:" height="500px;">



*왼쪽: 표준 [나무 보기](tree_view/ko.md)에 표시된 개체. 오른쪽: DAG 보기에 ​​표시된 개체.*

![](images/FreeCAD_DAG_view_Std_DependencyGraph.png )



*[종속성 그래프](Std_DependencyGraph/ko.md)에 표시된 개체 간의 관계.
*



## DAG 보기 활성화 

DAG 보기는 고급 사용자와 개발자를 위한 실험적 기능으로 0.17에 도입되었습니다.복잡한 모델의 문제를 해결할 수 있도록 말이죠; 따라서 DAG 보기는 프리캐드에서 기본적으로 곧바로 사용할 수 없습니다.

이 보기를 사용하려면 [매개변수 편집기를](Std_DlgParameter/ko.md) 사용하십시오. 존재하지 않는 경우 다음 하위 모둠(group)을 만듭니다.

-    `BaseApp/Preferences/DockWindows/DAGView`
    

그런 다음 `Boolean` 유형의 매개변수 `Enabled`를 추가하고 이를 `True`로 설정합니다.

프리캐드를 다시 시작하고 DAG 보기를 활성화합니다: **{{StdMenu|[View](Std_View_Menu.md)** → 패널 → DAG 보기}}.

[매개변수 편집기에서](Std_DlgParameter/ko.md) 다음 하위 모둠의 일부 속성을 변경할 수도 있습니다.

-    `BaseApp/Preferences/DAGView`
    

-   FontPointSize - 텍스트 글꼴 크기를 설정하고 높은 DPI 디스플레이에서 가독성을 높일 수 있습니다. 기본 글꼴 크기를 0으로 설정합니다.

-   SelectionMode
    -   0 - 한 번 클릭하면 항목이 선택됩니다. 선택 항목에 항목을 추가하려면 Ctrl 키를 누른 채 클릭하세요.
    -   1 - 클릭할 때마다 선택 항목에 항목이 추가/제거됩니다.

-   Direction - 항목이 표시되는 순서입니다.
    -   1 - 위쪽에 자식, 그 밑에 부모를 표시
    -   -1 - 위쪽에 부모, 그 아래에 자식을 표시



## 참고

-   [DAGView](https://forum.freecadweb.org/viewtopic.php?f=20&t=11276), 새로운 도구를 소개하는 토론 기록입니다.
-   [easter egg of PartDesign Next: DAG View](https://forum.freecadweb.org/viewtopic.php?t=15375), 부품설계 작업대 업데이트와 함께 보기(view)를 포함합니다.


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > DAG view/ko
