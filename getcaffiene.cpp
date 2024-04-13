#include<stdio.h>
#include<String>
using namespace std;

getCaffeine(type){
String Caffeine;

const map = {
  'Coffee' = '95 mg',
  'RedBull' = '125 mg',
  'Tea' = '11 mg',
  'Soda' = '21 mg'
  };

caffeine = map[type] ?? 'Not Found' ;
return caffeine;
}

int main(){
  
getCaffeine();
  
return 0;
}
