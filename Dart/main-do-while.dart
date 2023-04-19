import 'dart:io';

void main() {
  int numero = int.parse(stdin.readLineSync());
  do{
    print(numero);
    numero = int.parse(stdin.readLineSync());
  }while(numero != 10);
}

