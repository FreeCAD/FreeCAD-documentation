# Macro CenterOfMass/ko
<div class="mw-translate-fuzzy">


{{Macro
|Name=질량중심 매크로
|Description=여러 고체의 질량 중심을 계산하고 보여줍니다.
|Author=Schupins, SyProLei
|Version=0.7.6
|Date=2024-07-18
|FCVersion=0.19 이상
}}


</div>



## 설명

선택된 물체의 총 질량과 질량 중심의 위치를 ​​제공합니다. 각 물체에 대해 다른 밀도를 선택할 수 있습니다.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/CenterOfMass.FCMacro}}

<img alt="" src=images/CenterOfMass_exemple.png  style="width:600px;">



## 용법

1.  하나 이상의 고체를 선택합니다.
2.  매크로를 실행 합니다.
3.  고체를 나열하는 창이 생깁니다. 재료의 밀도를 다른 단위 체계로 지정하거나 미리 정의된 재료 중에서 선택할 수 있습니다.



### 가능한 선택사항 

-   밀도에 따라 고체의 색상 지정할 수 있습니다.

-   질량 중심의 위치를 ​​표시할 수 있습니다.

-   *질량*, *재료* 및 *밀도*를 내보내고 가져올 수 있습니다(매크로의 **.csv** 파일이 아니더라도 열의 이름은 이에 맞게 지정해야 함).

-   문서에서 밀도를 저장할 수 있습니다(재료를 {{ComboBox|기본값}}으로 설정할 때 다시 제거).

-    **도구 → 매개변수 편집 → 기본 설정 → 매크로**에서 일부 기본 설정을 변경할 수 있습니다.



## 스크립트

깃허브에서 매크로를 내려 받을 수 있습니다. [Macro CenterOfMass.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Information/CenterOfMass.FCMacro)

이 아이콘 파일을 도구 모음 아이콘으로 사용할 수 있습니다. ![](images/Macro_CenterOfMass.svg )



## 참고 문서 연결 

포럼 토론: [질량 중심을 계산하는 매크로](https://forum.freecad.org/viewtopic.php?f=24&t=31883)



## 버전

버전 / 병합 날짜

0.8.0 / 2025-01-06: Thanks to farahats9 for the contribution

-   New: Show Volume and Surface area
-   New: Calculate Moments of Inertia
-   Fix: Macro now works with the Assembly example in FreeCAD 1.0
-   Fix: Automatically select material for solids if it is already assigned by the new material system
-   Minor UI changes

0.7.6 / 2024-08-01: 주요 프리캐드 배포 준비

-   수정: 0.22.0dev 조립예제 작동하도록 만들기
-   수정: 사용자 정의 재료를 포함하는 BOM 가져오기
-   수정: 새로운 재료 카드 지원
-   수정: 아이콘 변경 또는 누락, 버전 확인

0.7.3 / 2023-09-11:

-   새 기능: 오림판에 복사 버튼 추가
-   새 기능: 확장 가능한 벡터 그래픽 아이콘
-   수정: 프리캐드 버전 및 웹 호환성

0.7.0 / 2023-02-13:

-   새 기능: 고체 검색창
-   새 기능: 더 나은 입력 허용 오차로 외부 BOM(자재 목록) 가져오기를 개선하기 위해 가져오기 기능을 재작업했습니다. 매크로의 이전 파일 내보내기에서 질량을 가져오려면 캡션 \"무게\"를 \"질량\"으로 변경해야 합니다.
-   새 기능: 계산 및 시각화에서 고체를 제외하기 위해 질량을 0으로 설정할 수 있습니다.
-   수정: 기본값 스핀 및 \"모두에 적용\" 동작
-   수정: \"새로 만들기\" 버튼을 눌렀을 때 원래 단색 색상을 유지합니다.

0.6.0 / 2022-08-27:

-   새 기능: 질량 편집 가능(요청이 많았던 기능)
-   새 기능: 작업 중인 고체를 강조 표시
-   새 기능: 그릇과 그릇에 담긴 내용물을 동시에 선택할 때 중복되지 않습니다.
-   새 기능: 파이 차트가 콤보 상자에 밀도 관계를 표시합니다.
-   새 기능: WCAG21 1.4.6 대비(향상) 적합성을 갖춘 색상이 있는 콤보 상자의 텍스트 가독성
-   수정: 메시(예: .stl)의 그릇으로 사용되는 부분이 올바르게 인식됩니다.
-   수정: 오류 및 언어 처리, 자료 편집, 콤보 상자 및 GUI 크기 조정에 대한 수정

0.5.8 / 2022-05-31:

-   다시 삽입: 바운딩 박스
-   새 기능: 구체 색상 설정
-   새 기능: 색상 맵 변경 설정
-   GUI 재배치: 업데이트 계산 추가, 총 밀도 추가
-   수정: 다중 모니터 설정에서 기본 화면에서 프리캐드를 실행하지 않을 때 메시지 상자를 사용할 수 없음
-   수정: 두 개 이상의 메시가 올바르게 계산되지 않음

0.5.0 / 2022-04-07: s-quirin(Saarland University의 SyProLei 프로젝트)에 의한 완전한 재작성

-   새 기능: 코드 기반, 요구 사항이 Qt5.12+ 및 Python3(프리캐드 0.19)으로 상향되었습니다.
-   새 기능: 각 고체의 질량을 표시합니다.
-   새 기능: 시작 창을 고정하거나 떠 있게 할 수 있습니다(매개변수 편집기에서 설정 가능).
-   새 기능: 선택 항목이 나무 보기에 맞춰 정렬되거나 이름별로 정렬됩니다(매개변수 편집기에서 설정 가능).
-   새 기능: 문서에서 밀도를 저장할 수 있습니다.
-   개선 사항: 프리캐드와 유사한 Gui 모양과 느낌.
-   개선 사항: 형상에 색을 입히기 위해 색상 팔레트를 조정했습니다(녹색에서 빨간색으로).

-   개선 사항: 단위의 내부 추적.
-   수정 사항: 모둠 및 모둠 객체 처리.
-   수정: App::Link 처리.
-   수정: 더 이상 사용되지 않는 Qt 클래스를 교체했습니다.

0.4.1 / 2019-05-25: 공식 저장소에서 이전 요구 사항 및 GUI를 사용할 수 있는 마지막 업데이트

0.1.2 / 2018-11-10: chupins의 초기 버전이 공식 저장소에 병합됨



---
⏵ [documentation index](../README.md) > Macro CenterOfMass/ko
