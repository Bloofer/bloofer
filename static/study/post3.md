### NP 문제에 대한 쉬운 설명  
  
</br>  
  
#### P 문제  
  
> Polynominal complexity의 알고리즘을 가지고 있는 쉬운 문제. 즉, 다항 시간내에 풀리는 문제.  
  
</br>  
  
#### NP 클래스  

> Non-deterministic Polynominal complexity를 가지는 문제들. 운에 기대면 현실적인 비용으로 해결할 수 있는 문제들. 예를 들자면 주어진 지도 위의 도시(그래프)를 한 번씩만 방문하는 경로 찾기 문제인 해밀턴 경로(Hamilton path) 문제가 대표적이다. 이를 다항시간 내에 푸는 알고리즘은 아직 없다.  
  
</br>  
  
#### 건너풀기(Problem Reduction)

> 문제 A를 푼 알고리즘으로 동일하게 B 문제를 해결할 수 있다면, 그 문제는 간접적으로 풀 수 있는 것이다. 단, A 문제로 푼 답을 B 문제의 답으로 옮기는 건 다항 시간내에 되야한다.  
  
</br>  
  
#### NP 완전(Complete)  

> 건너풀기로 NP 문제들을 모두 지배하는 하나의 문제가 있다. NP 클래스의 문제 중에 '종결자' 역할을 하는 대표적인 문제가 있는 것이다. 이 문제만 다항 시간내에 풀 수 있다면 나머지 NP 문제들은 모두 이 문제로 건너풀 수 있다. 이러한 NP에 있는 종결자 문제를 NP 완전 문제라고 한다. 참고로 해밀턴 경로 찾기 문제가 이 NP 완전에 속한다.  
  
</br>  
  
#### NP 하드(Hard)  

> NP 완전 문제들처럼 종결자 역할을 하지만 NP 문제인지 아닌지 확인되지 않은 문제들이 있다. 즉, NP 하드 문제를 풀면, 다른 모든 NP 문제들을 해결할 수 있지만, NP 하드 문제는 NP에 해당하는지 확인된 바가 없는 문제들이다.  
  
*출처 : [컴퓨터 과학이 여는 세계](http://book.naver.com/bookdb/book_detail.nhn?bid=9078133)*

