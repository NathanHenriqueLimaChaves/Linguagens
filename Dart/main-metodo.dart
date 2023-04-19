import 'dart:io';

void main(){
  int a = int.parse(stdin.readLineSync());
  int b = int.parse(stdin.readLineSync());
  Calcula(a,b);
}

void Calcula(int a, int b){
  int result = a + b;
  print(result);
}

