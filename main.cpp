#include <iostream>
#include <string>
#include <cstring>
#include <filesystem>

#include "Node.cpp"

using std::cout;
using std::endl;

void directory_iterator(std::string root_path){
	
	MP3 file;
	Node* currentSong = new Node();

	for (const auto &entry : std::filesystem::directory_iterator(root_path)){
		if (std::filesystem::is_directory(entry.path()))
			directory_iterator(entry.path().string());

		else if (entry.path().has_extension()){
			ID3::load();

			Node* currentSong = new Node();
			currentSong->setPath(entry.path().string());

			const int path_length = entry.path().string().length();

			char char_path[path_length];
			
			strcpy(char_path, entry.path().string().c_str());

			file.read(char_path);


			currentSong->setSong(file);

			ID3::ID3v1 id3v1 = file.getID3v1();
			
			cout << "Path: " << entry.path() << endl;

			if (entry.path().extension() != ".mp3")
				cout << "not an mp3: " << entry.path().extension() << endl << endl;
			else if(!file.hasID3v1)
				cout << "no id3 data detected" << endl << endl;
			else 
				cout << "Title: " << id3v1.title << endl << endl;
			
			delete currentSong;
			ID3::clear();
		}
	}

	
}

int main() {
	
	std::string path = "Song_Test_Data";
  	directory_iterator(path);
	
	
	/*
	ID3::load();
	
	MP3 file;
	Node* currentSong = new Node();

	file.read("Song_Test_Data\\Document One\\UnknownAlbum\\Document One - Bump the Sound.mp3");
	
	currentSong->setSong(file);
	
	ID3::ID3v1 id3v1 = file.getID3v1();
	
	cout << "Title: " << id3v1.title << endl << endl;

	ID3::clear();

	delete currentSong;
	*/

	return 0;
}