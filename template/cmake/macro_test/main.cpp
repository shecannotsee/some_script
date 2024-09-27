#include <iostream>


int main() {
#ifdef TEST
  std::cout << "define TEST" << std::endl;
#endif

#ifdef TEST_1
  std::cout << "define TEST_1" << std::endl;
#endif


#ifdef VALUE
  std::cout << "define VALUE" << std::endl;
#if VALUE == 10
  std::cout << "VALUE:10" << std::endl;
#elif VALUE == 20
  std::cout << "VALUE:20" << std::endl;
#else
  std::cout << "VALUE:"<< VALUE  << std::endl;
#endif
#endif

#ifndef VALUE
  std::cout << "not define VALUUE" << std::endl;
#endif

#if CMAKE_TEST == 100
  std::cout << "CMAKE_TEST 100" << std::endl;
#endif

  std::cout << "main done..." << std::endl;
  return 0;
}
