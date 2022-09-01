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

bool Conversion::isValid(float num) {
    float fraction=0;
    int n =-1;
   while(num > 0){
       fraction += trunc(num*10) * pow(8, n);
       num = (num * 10) - trunc(num*10);
       n--;
   }
   decimal+=fraction;
   std::cout <<  decimal << std::endl;

}
