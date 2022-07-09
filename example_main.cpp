#include <iostream>

#include "mp3_code\mp3.hpp"

int main() {
	std::cout << "Hello, world!" << std::endl;

	ID3::load();

	MP3 file;
	file.read("653 - Alix Perez - Perfect Stranger.mp3");
	file.setChar("TRCK", 9, '2');
	file.write("C418 - Key.mp3");

	file.read("C418 - Door.mp3");
	file.setChar("TRCK", 9, '1');
	file.write("C418 - Door.mp3");

	ID3::clear();

	return 0;
}