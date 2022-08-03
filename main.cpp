#include <iostream>
#include <string>
#include <cstring>
#include <filesystem>

#include <FileList.hpp>

using std::cout;
using std::endl;

int main() {
	
	std::string path = "D:\\Rekordbox USB Backup\\Contents";
  	
	FileList* songList = new FileList(path);
	
	//cout << songList->getSize() << endl;
	
	std::filesystem::create_directory("temp");

	for(int i = 0; i < songList->getSize(); i++){
		if(songList->getNode(i)->getFile().path().extension() != ".mp3")
			std::filesystem::copy(songList->getNode(i)->getFile().path(), "temp");
	}
	
	return 0;
}  