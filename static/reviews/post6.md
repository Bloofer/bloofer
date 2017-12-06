<img width=400 class="img-thumbnail" src="https://raw.githubusercontent.com/neovim/neovim.github.io/master/logos/neovim-logo.png">
## Neovim, 리눅스 에디터의 미래  
#### Vim 호환성을 갖춘 hackable Vim
  
리눅스에서 단연 많이 사용되는 에디터로 Vim을 빼놓고 말할 수가 없을 것이다. Vim의 장점은 가벼우면서도 강력한 여러가지 기능들, 텍스트 편집 기능과 여러 정규 표현식 문법, 그리고 다양한 편집 환경 변경 자유도를 제공한다는 것이다. 이러한 Vim을 개선시킨 것이 Neovim인데, Neovim을 사용해야 하는 이유 중 가장 큰 것은 이전 Vim에서 개선되지 않았던 Vim에서의 작업 중 비동기적으로 실행 중인 작업에 대한 엑세스일 것이다.   
  
오늘 리뷰에서는 내가 Neovim을 사용하면서 겪었던 경험과 후기를 공유해보고자 한다. 기본적으로는 나는 Neovim을 사용하는데 만족하고 있는데, Neovim은 여러가지 장점을 가지고 있기 때문이다. Neovim위에서의 여러 플러그인의 지원 및 관리를 제공하는 Vundle을 이용해 간편하게 패키지 관리를 할 수 있고, 높은 자유도로 IDE 비슷한 환경을 만들어 사용할 수도 있다.  
  
Neovim을 사용하면서 좋았던 플러그인 및 확장프로그램, 그리고 기능들에 대해서 소개하고 자한다. 내가 현재 사용하는 Neovim 설정은 내 [Github 저장소](https://github.com/Bloofer/nvim_config)에 있다.
  
</br>  
  
#####내가 사용하는 Neovim plugin들

1. **Vundle**</br>Neovim위에서 돌아가는 Neovim 확장 프로그램들의 패키지 매니저이다. <code>/.config/nvim/init.vim</code> 에 작성되어 있는 Vim 스크립트에 Vundle 기본 문법에 따라 패키지 설정들을 작성해 주면 Vundle이 알아서 자동으로 플러그인 패키지들을 설치하고 관리해준다.<img class="img-thumbnail" src="https://jmyang.kr/static/img/vundle.jpg">   
  
2. **NERD-Tree**</br>Neovim에서 디렉토리 traversal을 지원하는 플러그인이다. 설치는 Vundle로 이루어지며, Neovim에서 연 파일 디렉토리를 기준으로 Neovim 위에서 디렉토리 traversal이 가능하다. 주로 화면분할해서 다른 파일을 찾거나 다른 디렉토리의 파일 목록을 찾아보는데 유용하다.<img class="img-thumbnail" src="https://jmyang.kr/static/img/nerdtree.jpg">  
  
3. **syntastic**</br>syntastic은 Neovim 위에서 필수적으로 사용해야 할 확장 프로그램이다. syntastic은 각 프로그래밍 언어 별로 각각 syntax checker를 바인딩해주어 Neovim을 IDE처럼 사용할 수 있게 해준다. 아래 두 린터들은 내가 실제로 Neovim을 사용하면서 제일 많이 이용한 것들이다.
  
* * **merlin**</br>merlin은 OCaml 개발을 쉽게 도와주는 린터이다. 내가 가장 많이 사용하는 merlin의 기능은 auto-completion(자동완성), locate(정의부 따라가기), type-of(타입 확인)이다. locate는 내가 사용하는 외부 모듈이 컴파일만 되어 있다면 merlin이 따라가서 그 정의부를 보여주기 때문에 외부 모듈의 실제 구현을 확인하는데 아주 유용하다. type-of는 함수 타입, 변수 타입을 확인하는 데 사용할 수 있다. </br>merlin의 적용은 OPAM에서 따로 설치하고, syntastic으로 바인딩 시켜주면 된다. 추가적으로, conf-vim이라는 dependency를 OPAM으로 설치해주어야 Neovim 위에서 merlin의 기능을 제대로 사용할 수 있다.<img class="img-thumbnail" src="https://jmyang.kr/static/img/merlin.jpg"> 
  
* * **pylint & jedi-vim**</br>pylint와 jedi-vim은 Neovim 위에서 파이썬 개발을 도와주는 린터와 자동완성기이다. pylint는 해당 파이썬 파일에 대해서 5가지 요소를 검사해주는데, C:conventions, R:refactors, W:warnings, E:errors, F:fatals가 있다. 이 중에서, CRW는 프로그램의 리팩토링 요소이기 때문에 나의 경우, 설정에서 제외해 놓았다. 필수적인(통과를 못하면 컴파일 자체가 안되는) EF만 enable해놓은 상태이다. 이러한 pylint로 파이썬 프로그램을 전처리하여 자동완성 기능까지 하려면 jedi-vim이라는 프로그램이 필요한데, IDE처럼 해당 타이핑 된 문자까지 보고 자동완성을 지원한다. </br>pylint의 적용은 pip 파이썬 패키지 매니저로 따로 설치해주고, syntastic에 바인딩해주면 된다. jedi-vim의 설치는 Vundle 패키지 매니저로 이루어질 수 있다.<img class="img-thumbnail" src="https://jmyang.kr/static/img/py-autocomplete.jpg">  
  
</br>  
  
**설치 및 적용**  
  
Neovim의 설치 과정은 여러가지 방법으로 설치하여 보았으나, [홈페이지](https://github.com/neovim/neovim/wiki/Installing-Neovim)에 있는 설치 방법을 참조하여 apt-get 패키지 매니저로 설치하는 방법이 제일 안전하고, Neovim 위에서의 vim 스크립트(Neovim 설정파일들)를 파이썬으로 실행시키기 때문에, 파이썬 설정도 필요하다.
 
그 외에 Neovim 위에서의 플러그인 설치 과정은 Vundle 패키지 매니저 이용하여 간단하게 이루어진다. Neovim이 제대로 설치되고, 파이썬 설정이 제대로 이루어져있다면, Neovim을 처음 킬 때 init.vim 파일에 따라서 Vundle 패키지 매니저가 자동으로 설치되고 Neovim 안에 들어가서 <code>:VundleInstall</code>후 <code>:VundleUpdate</code>를 해주면 된다.
  
</br>  

**결론 : 만족. 높은 자유도로 IDE 환경 비슷하게 만들어 사용할 수 있다.**  
  
</br>  
  
**사용 후기**  
  
* 리눅스 로컬/서버에서 가장 편하고 가볍게 쓰기 좋은 에디터
  
* Vim 호환성을 완전히 갖춘 새로운 Vim  
  
* 플러그인 올려서 사용해도 부담이 없고, 사용자의 세팅에 따라서 IDE급의 환경으로 만들어 작업할 수도 있음 

* 굳이 단점을 이야기 하자면, ocamlformat이 지원 안된다는 점
