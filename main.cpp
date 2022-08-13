#include <iostream>
#include <string>
#include <cstring>
#include <filesystem>
#include <SongList.hpp>

using std::cout;
using std::endl;

int main() {
	
	std::string path = "D:\\Rekordbox USB Backup\\Contents";
  	
	SongList* songList = new SongList(path);
	
	songList->exportList();
	
	
	return 0;
}  