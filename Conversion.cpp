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
    int num = std::stoi(aux);
    for (int i = 0; i < len; ++i) {
        decimal += (num%10)*pow(8,i);
        num = (int)num/10;
    }
    std::cout << decimal << std::endl;
    return 0;
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