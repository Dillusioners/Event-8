#include <iostream>
#include <cmath>

int main(){
    int start, stop, range;
    std::cout << "Enter the starting value for the range of numbers: ";
    std::cin >> start;
    std::cout << "Enter the ending value for the range of numbers: ";
    std::cin >> stop;
    range = stop - start;
    std::cout << "These are the armstrong numbers between the range: " << std::endl;
    for(int i = start; i <= stop; i++){
        int arm = 0, digit, j= i;
        for(int j = i; j != 0; j /= 10){
            digit = j % 10;
            digit = pow(digit, 3);
            arm += digit;
        }
        if(j == arm){
            std::cout << arm << std::endl;
        }
    }
}