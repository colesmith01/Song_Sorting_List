#include <iostream>
#include <string>
#include <cstring>
#include <filesystem>

using std::cout;
using std::endl;

int i = 0;
int test;

void directory_iterator(std::string root_path){
	for (const auto &entry : std::filesystem::directory_iterator(root_path)){
		if (std::filesystem::is_directory(entry.path())){
			cout << entry.path() << endl;
			directory_iterator(entry.path().string());
			cout << entry.path() << endl;
		}
		else if (entry.path().has_extension()){
			const int path_length = entry.path().string().length();

			char char_path[path_length];
			
			strcpy(char_path, entry.path().string().c_str());
			
			i++;

			if (entry.path().extension() != ".mp3"){
				cout << "Path: " << entry.path() << endl;
				cout << "not an mp3: " << entry.path().extension() << endl << endl;
				test = 0;
			}
			else{
				//search for high bitrate
			}

			cout << "test " << test++ << ": " << entry.path() << endl;
		}
	}

	

	
}

int main() {
	
	std::string path = "D:\\Rekordbox USB Backup\\Contents";
  	//directory_iterator(path);
	cout << "ō" << endl;

	return 0;
}