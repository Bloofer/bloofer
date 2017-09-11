### GNU make  
  
##### 2017-08-22  
  
GNU make는 기본적으로 프로그램 그룹 중에서 어느 부분이 새롭게 컴파일되어야 하는지를 자동적으로 판단해서 필요한 커맨드를 실행한다. GNU make에 그 프로그램의 타겟과 의존성들을 알려주는 것이 Makefile이다. Makefile의 기본적인 구조는 아래와 같다.  
  
</br>  
  
---
**< Makefile의 기본 구조 >**  
  
target ... : dependency ...  
&nbsp; &nbsp; &nbsp; &nbsp; command  
&nbsp; &nbsp; &nbsp; &nbsp; ...  
&nbsp; &nbsp; &nbsp; &nbsp; ...
---

타겟은 말 그대로 명령이 수행되어 얻을 결과 파일이고 의존성은 타겟이 의존하고 있는, 즉 타겟이 컴파일되기 위해 필요한 파일들을 의미한다.  
  
* 참고로 타겟에는 결과 파일만 올 수 있는 것뿐 아니라 clean과 같은 레이블도 올 수 있다.  
* 명령 부분은 앞에 반드시 TAB으로 구분한다. make는 명령어를 앞단에서 TAB으로 구분하기 때문이다.  
*  * 나의 경우처럼 TAB 기본 설정이 nvim.init 에디터 설정에서 다르게 적용된 경우, 이를 끄고 Makefile을 작성해야 make가 제대로 된다.  
  
</br>  
  
---
**< 오캐믈 프로그램 Makefile 예제 >**  
  
all: run  
  
run: m.cmo error.cmo lexer.cmo parser.cmo main.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -o run m.cmo error.cmo lexer.cmo parser.cmo pp.cmo main.cmo  
  
error.cmo : error.ml m.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -c error.ml  
  
m.cmo : m.ml  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -c m.ml  
  
pp.cmo : pp.ml m.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -c pp.ml  
  
parser.ml: parser.mly m.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlyacc parser.mly  
  
parser.mli: parser.mly m.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlyacc parser.mly  
  
parser.cmi: parser.mli  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -c parser.mli  
  
parser.cmo: parser.ml parser.cmi  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -c parser.ml  
  
main.cmo : main.ml m.cmo pp.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -c main.ml  
  
lexer.cmo: lexer.ml error.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamlc -c lexer.ml  
  
lexer.ml: lexer.mll parser.cmo m.cmo  
&nbsp; &nbsp; &nbsp; &nbsp; ocamllex lexer.mll  
  
clean:  
&nbsp; &nbsp; &nbsp; &nbsp; rm -f ✳️.cmx ✳️.cmi parser.mli parser.ml lexer.ml run ✳️.o ✳️.cmo  
---
  
기본적으로 타겟은 만들어 낼 결과 프로그램을 의미하지만 all, clean과 같은 레이블은 지정되어 있는 의미가 있다.  
  
* all : 전체 프로그램을 컴파일한다. 기본 타겟이 되어야하는 레이블이다.  
* install : 프로그램을 컴파일하고 실행가능한 파일들, 라이브러리들, 그리고 실제로 사용되는 파일들 등을 복사한다.  
* clean : 현재 디렉토리 내에 프로그램이 빌드되었을 때 생성된 모든 파일을 삭제한다.  
  
*출처 : [GNU make 매뉴얼](https://www.gnu.org/software/make/manual/html_node/Standard-Targets.html#Standard-Targets)*
