### Troubleshooting

##### 2017-08-07

새로이 운영체제를 설치하고 나서 처음으로 로컬에서 오캐믈 코딩을 하려고 하는데, 내가 사용하는 [Merlin](https://github.com/ocaml/merlin) 설정에 문제가 생겨서 반나절동안 고생을 해서 해결하였다.  
  
문제는 내가 사용하는 Neovim 위에 타입 체킹 및 구문 교정을 해주는 Syntastic 플러그인을 올려서 사용하는데, 오캐믈 린터인 Merlin을 인식하지 못하는 것이었다.  
  
여러가지 시행착오를 거쳐 알게된 사실은 Merlin은 Ocamlmerlin이라는 바이너리를 사용하여 돌아가는데 리눅스 쉘에서 기본 PATH에 해당 바이너리 PATH가 추가되어야 하는 것이었다. 해당 문제에 대해서 [깃허브](https://github.com/Bloofer/nvim_config)에 정리하여 올려두었고 다음에 같은 문제가 발생하면 좀 더 쉽게 처리할 수 있길 바란다.

