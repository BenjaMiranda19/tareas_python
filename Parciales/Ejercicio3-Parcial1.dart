import 'dart:io';
import 'dart:math';

void main() {
  List lista1 = [];
  List lista2 = [];
  List lista3 = [];

  for (int i = 0; i < 10; i++) {
    lista1.add(Random().nextInt(11) + 10);
  }

  for (int i = 0; i < 10; i++) {
    lista2.add(Random().nextInt(11) + 10);
  }

  print("Ingrese 5 números enteros: ");
  for (int i = 0; i < 5; i++) {
    int num = int.parse(stdin.readLineSync()!);
    lista3.add(num);
  }

  List listaTotal = [...lista1, ...lista2, ...lista3];

  double promedio = listaTotal.reduce((a, b) => a + b) / listaTotal.length;

  listaTotal.sort();

  print("Lista 1: $lista1");
  print("Lista 2: $lista2");
  print("Lista 3: $lista3");
  print("Lista concatenada: $listaTotal");
  print("Promedio de la lista: $promedio");
}
