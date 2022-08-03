#include <iostream>
#include <string>
#include <cstring>
#include <filesystem>
#include <sstream>

using std::cout;
using std::endl;

int i = 0;
int test;

std::string to_hex(char ch) {
    std::ostringstream b;
    b << "\\x" << std::setfill('0') << std::setw(2) << std::setprecision(2)
        << std::hex << static_cast<unsigned int>(ch & 0xff);
    return b.str();
}

void directory_iterator(std::string root_path){

	//refine code
	for (int i = 0; i < stringTest.length(); i++) {
		if (stringTest[i] < 0)
			cout << "Skipped" << endl;
			return;
	}

	
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
	/*
	std::string path = "D:\\Rekordbox USB Backup\\Contents";
  	directory_iterator(path);
	 */
	std::string stringTest = "D:\\Rekordbox USB Backup\\Contents\\Ajja; Simiantics\\Kenshō";


	

	//cout << (int)stringTest[stringTest.length()-1] << endl;  
	
	return 0;
}  