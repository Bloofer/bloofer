### 플라스크 Authentication 사용시 WSGI 설정 문제  
  
##### 2017-08-17  
  
오늘 블로그에 Basic Authentication을 다는 작업을 하고 있었는 데, 아파치 WSGI 디플로이 된 웹 앱 환경 때문에 Authentication 헤더가 먹혀버리는 현상이 있었다. (정확히 설명하자면, 인증 과정에 사용자 아이디와 비밀번호를 입력받는 데 헤더에 달려오는 이 값들이 None 타입으로 전달되는) 다행히 여러 시행 착오를 통해 문제를 해결했고, 그 과정을 잊지 않도록 기록해놓고자 한다.  
  
<code>/etc/apache2</code>에 있는 apache2.conf 파일을 열어준다.

<img class="img-responsive" src="https://jmyang.kr/static/img/auth_conf.jpg">
  
위 그림과 같이 설정파일에서 웹 앱이 디플로이 된 디렉토리 태그 내에 <code>WSGIPassAuthorization On</code> 한 줄을 추가해주면 된다. 스택 오버플로우나 여러 포럼에서 찾아본 결과 나와 같은 현상을 겪은 사용자들이 많았다. 대부분 이에 대한 해결책으로 <code>/etc/apache2/sites-enabled</code> 디렉토리 안의 설정파일에 WSGI 인증 설정을 추가하라는 이야기가 있었지만 나에게는 소용이 없었다. 아파치2 WSGI으로 디플로이 된 내 파이썬 플라스크 웹 앱은 이 방법이 해결책이 되었다.

