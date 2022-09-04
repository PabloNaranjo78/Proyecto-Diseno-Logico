//
// Created by Fernando on 08/30/22.
//

#include "Conversion.h"


Conversion::Conversion() {

}

bool Conversion::isValid(std::string num){
    this->number = std::stoi(num);
    if (composition(num) and this->number > 0 and this->number <= 777){
        std::cout <<  "Radio Check" << std::endl;
        this->count();
        return true;
    } else{
        return false;
    }
}

bool Conversion::composition(std::string num) {
    for (char i : num) {
        if (validValues.find(i) == std::string::npos) {
            return false;
        }
    }
    return true;
}

void Conversion::count() {
    int aux = this->number;
    int count = 0;
    while (aux != 0){
        aux = aux/10;
        count++;
    }
    this->len = count;
}

int Conversion::toDecimal(std::string aux){

    int num = std::stoi(aux), count = 0;
    for (int i = 0; i < len; ++i) {
//        std::cout << (num%10)*pow(8,i) << std::endl;
        count += (num%10)*pow(8,i);
        num = (int)num/10;
    }
    decimal = count;
    std::cout << decimal << std::endl;
    return 0;
}

void Conversion::toBinary() {
    int aux = decimal;
    int aux2, exp = 1, format = 0;
    while (aux != 0){
        aux2 = aux % 2;
        format = format + (aux2 * exp);
        aux = aux/2;
        exp *= 10;
    }
    this->binary = format;
    std::cout << binary << std::endl;
}


void Conversion::toHexadecimal() {
    int aux = decimal, i = 0;
    char hexa[100];
    while (aux != 0){
        int aux2 = 0;
        aux2 = aux % 16;
        if (aux2 < 10){
            hexa[i] = aux2 + 48;
            i++;
        }else{
            hexa[i] = aux2 + 55;
            i++;
        }
        aux = aux / 16;
    }
    for (int j = i - 1; j >= 0; j--){
        hexadecimal+=hexa[j];
//        std::cout << hexa[j] << std::endl;
    }
    std::cout << hexadecimal << std::endl;


}













//bool Conversion::isValid(float num) {
//    float fraction=0;
//    int n =-1;
//   while(num > 0){
//       fraction += trunc(num*10) * pow(8, n);
//       num = (num * 10) - trunc(num*10);
//       n--;
//   }
//   decimal+=fraction;
//   std::cout <<  decimal << std::endl;
//
//}