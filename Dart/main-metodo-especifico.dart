import 'dart:io';

void main(){
  print(ParouImpar(6));
  print(ParouImpar(7));
  print(ParouImpar(15));
}

String ParouImpar(int nume){
  if(nume % 2 == 0){
    return 'O número é par!';
  }else{
    return 'O número é ímpar!';
  }
}


