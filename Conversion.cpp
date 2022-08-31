//
// Created by Fernando on 08/30/22.
//

#include "Conversion.h"


Conversion::Conversion() {

}

int Conversion::toDecimal(int num){
    this->count(num);
    for (int i = 0; i < len; ++i) {
        decimal += (num%10)*pow(8,i);
        num = (int)num/10;
    }
    std::cout << decimal << std::endl;

    return 0;
}

int Conversion::count(int num) {
    int count = 0;
    while (num != 0){
        num = num/10;
        count++;
    }
    this->len = count;
}

bool Conversion::isValid(int num) {

}
