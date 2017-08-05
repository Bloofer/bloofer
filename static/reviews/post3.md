<img class="img-responsive" src="https://letsencrypt.org/images/le-logo-twitter.png">  
## Let's Encrypt SSL/TLS 인증  
#### 개인 홈페이지를 https://로 보안 연결해보자!  
  
Let's Encrypt는 SSL/TLS 보안 인증을 지원해주는 **무료** 인증 기관이다. 개인 홈페이지를 운영하는 데 있어서 보안에 대해 신경을 쓰지 않을 수 없다. 기존의 여러 인증 기관들은 소정의 비용을 받아 SSL/TLS 인증 지원을 해주었는데, 이 혁신적인 기업은 전세계 모든 사이트들의 암호화 통신을 기원하며 무료로 모든 보안 인증을 지원하고 있다. 오늘은 이 Let's Encrypt를 리눅스 서버에 설치하여 개인 홈페이지를 http에서 https로 통신할 수 있도록 만드는 방법을 소개하고자 한다.  
  
</br>  
  
<img class="img-responsive" src="">  
  
</br>  
  
Let's Encrypt 인증 설치 과정은 매우 간단하다. 본 리뷰는 본인의 서버(Ubuntu 16.04 64bit) 환경을 기준으로 한다. 가동중인 웹 어플리케이션은 파이썬 플라스크 프레임워크를 이용하였고, 아파치 WSGI 위에 디플로이 되었다.  
  
먼저, apt-get 패키지 매니저를 통해서 letsencrypt를 설치해준다.  
  
<code># apt-get install letsencrypt</code>  
*sudo 권한이 필요할 수도 있다.(아마도)*  
  
그 다음, 인증 프로그램을 실행하여 내 홈페이지의 도메인을 인증 기관에 등록하고, 확인 과정을 거쳐 인증을 받도록 한다.  
  
<code># sudo letsencrypt --apache</code>

letsencrypt가 실행되면 예전 윈도우95 시절 도스창 처럼 파란 창이 하나 뜨는데, 거기에 나오는 순서대로 도메인명, 이메일 주소를 등록해주도록 한다.  
  
**여기서 등록 중에 'Name Duplicate' 에러가 발생하는 경우**  
  
* 아파치 WSGI 설정에 이름과 letsencrypt 인증 간의 이름 충돌이 발생하는 것이므로 잠시 WSGI 설정에 이름 충돌 나는 부분을 지웠다가(주석화) 인증 완료 후 다시 되돌리면 된다.  
  
**설정 완료 후**  
  
<img class="img-thumbnail" src="https://jmyang.kr/static/img/cert.png">  
  
보안 연결이 설정되고 인증기관은 Let's Encrypt로 제대로 설정된 것을 볼 수 있다.  
  
**추가 : 홈페이지 http 연결 자동 https 리디렉션**  
  
<img class="img-thumbnail" src="https://jmyang.kr/static/img/conf.png">  

아파치 설정 파일에 redirect 태그를 통해 강제 리디렉션을 해주도록 한다. 이제 홈페이지에 http로 접속한 사용자도 강제로 https로 리디렉션이 된다.  
  
**사용 후기**  
  
* 개인 홈페이지에 보안 인증을 달 수 있는 가장 쉽고 빠른 방법  
  
* 안 할 이유가 없다.  
  
* 무료로(자선으로) 인증을 지원하기 때문에 상시로 후원을 받는데, 나중에 여유가 생겼을 때 후원을 하는 것도 고려해 봄직하다.


