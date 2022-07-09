#include <iostream>
#include <string>
#include <filesystem>

#include "Node.cpp"

using std::cout;
using std::endl;


int main() {
	/*
	std::string path = "C:/";
    for (const auto &entry : std::filesystem::directory_iterator(path))
        std::cout << entry.path() << std::endl;
	*/
	
	ID3::load();
	
	MP3 file;
	Node* currentSong = new Node();

	file.read("653 - Alix Perez - Perfect Stranger.mp3");
	
	currentSong->setSong(file);
	
	ID3::ID3v1 id3v1 = file.getID3v1();

	ID3::clear();

	delete currentSong;
	
	return 0;
}