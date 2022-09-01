#include <iostream>
#include "Conversion.h"

int main() {
    Conversion hp = Conversion();
    hp.toDecimal(326);
    hp.isValid(0.63);
    return 0;
}
