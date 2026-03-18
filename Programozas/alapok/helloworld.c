/* demo.c - Egyszerű demonstrációs program */
#include <stdio.h>

int global_var = 42;            // Globális változó
const char* message = "Hello World!";  // Globális konstans

int add_numbers(int a, int b) {
    return a + b;
}

int main() {
    int local_var = 100;        // Lokális változó
    int result;
    
    result = add_numbers(global_var, local_var);
    printf("%s\n", message);
    printf("Eredmény: %d\n", result);
    
    return 0;
}
