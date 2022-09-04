#include <iostream>
#include "Conversion.h"

int main() {
    Conversion hp = Conversion();
    hp.isValid("354");
    hp.toDecimal("354");
    hp.toBinary();
    hp.toHexadecimal();
    return 0;

}
