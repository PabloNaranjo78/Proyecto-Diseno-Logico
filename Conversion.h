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

    /**
     * Checks if the number that is
     * going to be be processed is valid
     * @param number number to be validated
     * @return if the number is valid
     */
    bool isValid(std::string num);

    /**
     * Checks if all the digits of
     * a number are on the octal range
     * @param num number to be checked
     * @return if the number is valid
     */
    bool composition(std::string num);

    /**
     * Counts the among of digits
     * of a number
     */
    void count ();

    /**
     * Converts an octal number to
     * a decimal number.
     * @param num octal number
     * @return octal to decimal conversion
     */
    int toDecimal(std::string num);

    /**
     * Converts a decimal number to
     * a binary number
     */
    void toBinary();

    void toHexadecimal();

private:
    int len;
    int decimal;
    int binary;
    int number;
    std::string hexadecimal;
    std::string validValues = "01234567";
};




#endif //PROYECTO_DISENO_LOGICO_CONVERSION_H