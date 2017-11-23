### Neovim 위에 Syntastic plugin에 Merlin 설정 올리기  
  
##### 2017-11-22  
  
오늘 쓰는 블로그는 제목이 길다. OS를 한번 밀고나서, 여러가지 세팅들을 해주는 데 그 중에서 가장 애먹었던 오캐믈 린터 Merlin 설정에 대한 시행착오 경험을 적고자 한다. 로컬에서든 서버에서든 Merlin 설정 자체가 너무 나를 괴롭혔기에 오늘의 시행착오를 기록하여, 다음 번의 일어날 고통을 조금이나마 피할 수 있으면 좋겠다.  
  
먼저, 내 상황은 Neovim 위에서 사용하는 플러그인 패키지 매니저 Vundle로 설치한 Syntastic 플러그 인 위에 Merlin을 올리고자 한 것이다. Merlin은 오캐믈 언어에 대해서 구문 확인 및 타입 확인, 외부 ml 바이너리 모듈 탐지 등등 오캐믈 개발에 있어서 필수적인 놈이다.  
  
내가 쓰는 Neovim 환경에서 Merlin을 올려서 사용해야 하는데, 알 수 없는 이유로 Merlin이 계속해서 인식 자체가 되지 않았다. 현재는 잘 인식되어 <code>:SyntasticInfo</code>로 현재 사용되는 체커를 확인하였을 때 다음과 같이 나온다.  
>Syntastic version: 3.8.0-97 (Vim 704, Neovim, Linux)</br>Info for filetype: ocaml</br>Global mode: active</br>Filetype ocaml is active</br>The current file will be checked automatically</br>Available checkers: camlp4o merlin</br>Currently enabled checker: merlin  
  
Syntastic Info 정보에 Merlin이 제대로 인식되어 나오고 있다. 처음에는 이게 정말 되지 않아 계속해서 여러 해결 방법을 찾게 되었다. 결론적으로는 Merlin 위키에 있는 Troubleshooting에 답이 있었다. [링크](https://github.com/ocaml/merlin/wiki/vim-from-scratch)  
  
저 중에서 확장 프로그램의 vim 파일들이 파이썬으로 컴파일되지 않는다는 게 내 문제였다. 나의 문제는 Neovim에서 플러그인 파이썬 컴파일 지원을 해줌으로써 해결할 수 있었다.([링크](https://github.com/neovim/python-client)) 처음에 OS를 밀고 Neovim을 새롭게 설치할 때 pip 설정 및 업데이트를 해주지 않았던 탓이다. 내 깃허브 [README](https://github.com/Bloofer/nvim_config)에 해당 사항에 대해 추가로 정리하였다.  
  
