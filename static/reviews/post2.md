<img class="img-responsive" src="https://mae.chab.in/wp-content/uploads/2015/05/Atom.png">
## IDE같은 에디터 아톰(Atom)
#### 깃허브(Github)에서 만들어 믿고 쓰는 
  
내가 처음 아톰을 접하게 된 계기는 웹 어플리케이션의 Front-end를 개발하던 중이었다. 무거운 IDE로 스크립트를 개발하는 데 불편함을 많이 느껴 어느 정도 가벼운 새로운 에디터를 찾고 있었다. 그러다가 발견하게 된 아톰은 윈도우 환경에서 작업하기 아주 적합한 환경이었고 플러그인들이 다양하게 제공되어 있어 편리하게 개발할 수 있었다.
  
</br>
  
<img class="img-responsive" src="https://jmyang.kr/static/img/octocat.jpg">  
*"대기업에서 만든 제품이니 안심하고 쓰라구!"*
  
</br>
  
아톰은 깃허브에서 만든 에디터라 그런지 다른 에디터들보다 더욱 신경을 많이 쓴 느낌이 난다. 특히나 개발된 언어가 Coffee-script로 짜여져 있어서 운영체제에 상관없이 동일하게 UI를 제공하고(마치 접속하는 클라이언트의 운영체제에 영향을 받지 않는 웹 어플리케이션처럼), 동일한 인터페이스를 제공한다.  
플러그인들은 세계 최대의 플랫폼인 깃허브를 기반으로 하기 때문에, 개발자의 관리차원에 있어서도 훨씬 선호되는 편이다. 아톰은 플레인한 그 자체는 에디터지만 플러그인과 곁들여 사용할 때 더욱 빛이 나는 것 같다. 여기 내가 사용하고 경험하며 만족했던 몇몇 플러그인을 추천한다.  
  
</br>
  
**추천하는 플러그인**  
  
1. <a href="https://atom.io/packages/git-plus" target="_blank">git-plus</a><img class="img-responsive" src="https://i.github-camo.com/78e2bafa5f9b3afdf47d7e02e3f949fea4801fc0/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f616b6f6e77692f6769742d706c75732f6d61737465722f636f6d6d69742e676966">git은 개발에 있어서 거의 필수이다. 하지만 에디터 위에서 git을 설치해 사용하고자 할 때 여간 불편한 것이 아닌데, git-plus는 아톰 위에서 명령어 팔레트의 간단한 명령을 통해 모든 기본 git 명령어들을 편리하게 사용할 수 있도록 해준다.
2. <a href="https://atom.io/packages/script" target="_blank">script</a><img class="img-responsive" src="https://i.github-camo.com/405fb492595dd819647af375b68c716fd862ee80/68747470733a2f2f636c6f75642e67697468756275736572636f6e74656e742e636f6d2f6173736574732f313639343035352f333232363230312f63343538616362632d663036372d313165332d383461302d6461323766653333346635652e676966">script는 아톰 위에서 바로 코드를 실행시킬 수 있도록 해주는 플러그인이다. 짧게 짜여진 파이썬 스크립트나 웹 스크립트 언어로 짜여진 파일을 바로 실행하여 확인해보고 싶을 경우에 유용하다.</br>  
3. <a href="https://atom.io/packages/linter" target="_blank">linter</a></br><img class="img-responsive" src="https://i.github-camo.com/a7fa1da3b5b4bdea00b5d25591f47e0751f64d4e/68747470733a2f2f636c6f75642e67697468756275736572636f6e74656e742e636f6d2f6173736574732f343237383131332f32333837393933332f31616231376532612d303837322d313165372d383033642d3366653063636663363739302e676966">linter는 특정 언어의 프로그램을 파싱하여 Convention/Warning/Error/Refactor/Fatal 같은 메세지를 띄워주는 소프트웨어이다. 기본 언어 패키지를 지원하는 IDE들은 컴파일러를 내장하고 있어 linter가 필요없다. 하지만 아톰은 말그대로 기본적인 에디터이기 때문에 해당 언어에 대한 문법 및 규칙을 확인해줄 수 있는 linter를 설치해주어야 한다.
4. <a href="https://atom.io/packages/autocomplete-plus" target="_blank">autocomplete-plus</a><img class="img-responsive" src="https://i.github-camo.com/c90b92e60288c36d664f03908ba025d6480b0c38/68747470733a2f2f636c6f75642e67697468756275736572636f6e74656e742e636f6d2f6173736574732f3734343734302f373635363836312f39666238626363342d666165612d313165342d393831342d3964636132313864656439332e706e67">autocomplete-plus는 기존에 IDE에서 제공되는 것처럼 해당 키 스트로크에 대해서 가능한 여러가지 힌트(변수명, 함수명, 패키지명 등)를 주어 생산성을 높여주는 도구이다.
5. <a href="https://atom.io/packages/minimap" target="_blank">minimap</a><img class="img-responsive" src="https://i.github-camo.com/bb671dcf7706c32eb432472c2cd69d354f824661/68747470733a2f2f6769746875622e636f6d2f61746f6d2d6d696e696d61702f6d696e696d61702f626c6f622f6d61737465722f7265736f75726365732f73637265656e73686f742e706e673f7261773d74727565">minimap은 코드의 전체와 현재의 위치를 미니맵으로 보여주는 플러그인이다. 원래는 sublime에서 지원되던 기능인데 현재는 여러 에디터들이 이 기능을 탑재하고 있다. 개인적으로 상당히 만족하여 사용한 기능 중 하나.  
  
</br>  
  
**사용후기** 

* 스크립트 언어(Coffee-script)로 작성되어 운영체제에 독립적이라는 장점이 있다.

* 개발자 플러그인이 비교적 다양한 편임.

* 수려한 UI/UX. 개인적인 생각이지만 시중에 나와있는 에디터 중에 제일 낫다고 생각한다.

