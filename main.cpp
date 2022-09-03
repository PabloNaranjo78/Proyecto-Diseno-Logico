#include <iostream>
#include "Conversion.h"

int main() {
    Conversion hp = Conversion();
    hp.isValid("0000000");
    hp.toDecimal("00000026");
    return 0;
}
