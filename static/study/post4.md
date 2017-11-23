### OCaml 컴파일과 빌드  
  
<br>  
  
#### OCaml 컴파일러 
  
* ocamlc - OCaml 바이트코드 컴파일러. .byte를 만들어낸다.  
* ocamlopt - OCaml 네이티브코드 컴파일러. .native를 만들어낸다.  
  
<br>  
  
#### 파일 확장자명 종류  
  
> <code>.o</code> - c object를 나타냄<br><code>.a</code> - c archive를 나타냄(archive란 오브젝트 파일들을 모아 하나의 파일로 만든 것)<br><br><code>.cmi</code> - mli object를 나타냄 (mli는 ml 인터페이스 파일)<br><code>.cmo</code> - ocaml object를 나타냄 (byte code)<br><code>.cmx</code> - ocaml object를 나타냄 (native code)<br><code>.cmxs</code> - native plugin을 나타냄. OPAM으로 사용하는 ocamlgraph, cil같은 외부 패키지들을 이런 식으로 가져와서 링킹함. (dynamic linking)<br><br><code>.cma</code> - ocaml archive를 나타냄 (byte code)<br><code>.cmxa</code> - ocaml archive를 나타냄 (native code)<br>  
  
<br><br>  
  
#### OCaml 프로젝트 빌드와 컴파일하기  
  
<br>  
 
ocamlopt를 이용하여 컴파일 할 때 main.ml이 ocamlgraph와 cil 모듈을 사용한다면 다음과 같이 명령어를 길게 써주어야 한다.   
<code>ocamlopt -c main.mli main.ml -I ~/.opam/4.04.2/lib/ocamlgraph -I ~/.opam/4.04.2/lib/cil</code>
> **ocamlopt 컴파일러 옵션**<br>-I [directory] : Add directory to the list of include directories<br>-c : Compile only (do not link)
-I 옵션을 이용하여 의존하는 모듈의 디렉토리 주소를 직접 컴파일러에게 알려주는 것이다. 만약 -I 옵션을 사용하지 않는다면 컴파일에 실패할 것이다.  
  
<br>  
  
하지만 위 명령은 사실 cil이 Big int라는 오캐믈 내부 라이브러리를 사용하기 때문에 제대로 컴파일되지 않는다. 따라서 아래와 같이 nums.cmxa라는 내부 라이브러리 파일을 직접 링킹해줘야 한다. 내부 라이브러리의 경우 컴파일러에게 주소를 알려줄 필요가 없다.  
<code>ocamlopt nums.cmxa ~/.opam/4.04.2/lib/cil/cil.cmxa main.cmx -o main.native</code>  
  
<br><br>  
  
#### ocamlbuild로 오캐믈 프로젝트 빌드하기  
  
<br>  
  
이런 식으로 컴파일러에게 옵션을 줘가면서 링킹을 하고 컴파일을 할 수 있지만, 좀 더 편하게 할 수 있다. **ocamlbuild**를 사용하는 것이다. ocamlbuild를 사용할 때는 tags라는 파일을 만들어서 그 안에 패키지를 찾도록 알려줄 수 있는 데 tags의 내용은 아래와 같다.     
  
> true: package(ocamlgraph), package(cil)  
  
true는 컴파일하는 파일 전체에 대해서 해당 패키지를 링킹해주는 것이다. 그리고 컴파일하는 대신 ocamlbuild를 이용해 전체를 빌드해주면 되는 데, 여기서 **ocamlfind**를 이용하면 OPAM으로 설치한 사용하는 패키지에 대해서 자동으로 디렉토리를 찾아주기 때문에 컴파일러에 옵션으로 길게 디렉토리를 적어주었던 것처럼 할 필요가 없다. ocamlfind는 OPAM에서 새로운 패키지를 설치할 때마다 패키지의 디렉토리 주소를 자동으로 업데이트하여 똑똑하게 패키지 주소를 알려준다.  
  
<code>ocamlbuild -use-ocamlfind main.native</code>  
  
위 명령은 ocamlbuild를 이용하여 main.ml을 컴파일하고, 타겟으로 main.native를 만들어내는 데 필요한 외부 패키지는 ocamlfind를 이용하여 찾겠다는 의미이다. 그리고 빌드 된 결과는 build 디렉토리에 생성되는 데 ocamlbuild -clean으로 빌드 된 결과를 전부 지울 수 있다.  
  
<br><br>  
  
#### make로 빌드 명령 간소화하기  
  
<br>  
  
ocamlbuild로 의존하는 외부 패키지를 찾아 링킹해주고 컴파일도 할 수 있게 되었지만, make로 이를 좀 더 간소화시키고 싶다. Makefile을 만들어 해당 명령을 그대로 쳐주기만 하면 된다.  
  
<br>  
  
> .PHONY: all clean<br>all:<br>&nbsp;&nbsp;&nbsp;&nbsp;ocamlbuild -use-ocamlfind main.native<br>clean:<br>&nbsp;&nbsp;&nbsp;&nbsp;ocamlbuild -clean  
  
* Makefile의 타겟 명령선언줄에는 항상 tab으로 띄어주어야 한다.  
* 맨 윗줄에 쓰인 [PHONY 타겟의 의미](http://pinocc.tistory.com/131)  
  
<br>  
  
이제, make all 혹은 make로 프로젝트 전체가 컴파일된다. 물론 추가적인 변경사항이 있을 때마다 tags 파일과 Makefile을 수정해주면 된다. 큰 프로젝트 빌드시에 서브 디렉토리 구조가 나누어진 경우, 최상위 디렉토리에서 빌드하면 ocamlbuild는 알아서 링킹을 해줄 수 있다. 즉, src/core와 src/domain과 같은 디렉토리에 서로 모듈들이 의존한다면, src에서 빌드를 하면 각 의존하는 모듈의 위치를 찾아서 빌드할 수 있다.  
  
