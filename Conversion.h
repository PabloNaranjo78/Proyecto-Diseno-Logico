//
// Created by Fernando on 08/30/22.
//

#ifndef PROYECTO_DISENO_LOGICO_CONVERSION_H
#define PROYECTO_DISENO_LOGICO_CONVERSION_H

#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
#include <cmath>

class Conversion {
public:
    Conversion();

    int count (int num);
    int toDecimal(int num);
    bool isValid(float num);

private:
    int len;
    float decimal;
};




#endif //PROYECTO_DISENO_LOGICO_CONVERSION_H
