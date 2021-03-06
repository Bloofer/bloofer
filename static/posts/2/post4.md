### 오캐믈 코딩과 삽질  
  
##### 2017-09-11  
  
오늘 오캐믈 코딩을 오랜만에 하던 중에 예상치 못한 타입 에러가 계속해서 발생하여 문제를 해결하는 데 머리를 싸매고 시간을 보내게 되었다. 발생한 문제에 대해서 이야기하자면, 함수를 정의하고 그 안에서 재귀적으로 호출하는 부분이 있었는데, 호출부분 안에 인자로 함수를 <code>fun x -> f' (g x)</code> 다음과 같이 넣어주게 되었다. 이 부분에서 정의부분과 호출부분 모두 확인하였으나 문제가 없지만 이상하게 타입에러가 계속해서 발생하게 되었다. 그래서 내가 코딩을 잘못한 건가 함수의 정의를 조금 바꿔보기도 하고, 아예 새롭게 짜보기도 했지만 해결이 되질 않았다.  
  
그러다가 어렵게 문제해결을 하게되었는데, 문제는 내가 인자에 대해 괄호로 블럭화 해놓지 않아 인자가 함수타입이 아닌 앞부분 토큰들의 다른 타입으로 파싱된 것이었다. 그걸 발견한 순간 정말 손쉽게 문제해결을 할 수 있었다. 단순히 함수에 대해 괄호로 분리하면 되는 것이었으니깐. <code>(fun x -> f' (g x))</code> 정말 단순한 거지만 이러한 과오를 반복하지 않기 위해, 함수 타입이나 정의가 길어지는 부분에 대해서는 괄호로 분리를 열심히 하도록 해야지. 
