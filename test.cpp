#include <iostream>
#include <string>
#include <filesystem>

#include "Node.cpp"

using std::cout;
using std::endl;


void directory_iterator(std::string path){
  for (const auto &entry : std::filesystem::directory_iterator(path)){
    if (std::filesystem::is_directory(entry.path()))
      directory_iterator(entry.path().string());

    else if (entry.path().has_extension())
      cout << entry.path() << endl;
  }
}

int main() {
  std::string path = "C:\\Users\\user\\Desktop\\Song_Sorting_Program\\Song_Test_Data";
  directory_iterator(path);
  /*
  for (const auto &entry : std::filesystem::directory_iterator(path))
      std::cout << entry.path() << std::endl;
  */
}
