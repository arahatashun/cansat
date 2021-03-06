#include <iostream>
#include <ctime>
#include "camera.hpp"

int main(){
  Camera camera;
  int i=0;
  clock_t start = clock();
  while(1)
  {
  camera.takePhoto();
  camera.binarize();
  camera.countArea();
  camera.getCenter();
  clock_t end = clock();     // 終了時間
  std::cout << "duration = " << (double)(end - start) / CLOCKS_PER_SEC << "sec.\n"<<std::endl;
  }
}
