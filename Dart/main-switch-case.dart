import 'dart:io';

void main() {
  int dia = int.parse(stdin.readLineSync());

  switch(dia){
    case 1:
      print("Domingo");
    break;
    case 2:
      print("Segunda");
    break;
    case 3:
      print("Terça");
    break;
    case 4:
      print("Quarta");
    break;
    case 5:
      print("Quinta");
    break;
    case 6:
      print("Sexta");
    break;
    case 7:
      print("Sábado");
    break;
    default:
      print("Valor inválido!");
    break;
  }
}

