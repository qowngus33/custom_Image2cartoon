### Cutom Image2cartoon

* 이미지를 카툰 느낌으로 바꾸어주는 프로그램.
* Canny Edge Detector를 사용하여 edge detection을 수행한 후 morphological 연산으로 변형을 가한다. 이후, bitwise_and 함수로 원본 이미지와 이를 합하여 결과 이미지를 도출한다.

* 좋은 예시: 공포영화스러운 분위기를 만들 수 있다.
  <img width="1428" alt="Screenshot 2024-03-20 at 12 36 49 PM" src="https://github.com/qowngus33/custom_Image2cartoon/assets/83813866/2ad173e7-1550-434e-95a7-658f1df3932a">

* 나쁜 예시: 귀여운 고양이, 강아지나 풍경 사진과는 어울리지 않는다.
<img width="1385" alt="Screenshot 2024-03-20 at 12 37 49 PM" src="https://github.com/qowngus33/custom_Image2cartoon/assets/83813866/a43c0a51-58d8-4431-84b1-5d77d642200e">
<img width="1272" alt="Screenshot 2024-03-20 at 12 37 12 PM" src="https://github.com/qowngus33/custom_Image2cartoon/assets/83813866/4920986f-9386-40fb-a540-65e845da9e85">
