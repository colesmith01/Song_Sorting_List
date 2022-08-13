#include <SongList.hpp>
#include <iostream>
#include <fstream>

SongList::SongList(std::string rootPath){
    head = new Node;
    size = 0;
    listIteration = 0;

    FileList::directory_scraper(rootPath);
}

void SongList::exportList() const{
    std::cout << "test" << std::endl;
    
    if (!std::filesystem::exists("temp"))
        std::filesystem::create_directory("temp");
    
    FileList newSongs;

	for(int i = 0; i < size; i++){
        Node* n;
        n = getNode(i);

		if(n->getFile().path().extension() != ".mp3" && !std::filesystem::exists("temp\\" + this->getNode(i)->getFile().path().filename().generic_string())){
            std::cout << this->getNode(i)->getFile().path() << std::endl; 
			std::filesystem::copy(n->getFile().path(), "temp");
            newSongs.addNode(n);
        }
    }

    for(int i = 0; i < newSongs.getSize(); i++){
        if (!std::filesystem::exists("temp\\" + this->getNode(i)->getFile().path().filename().generic_string())){
            char* brokenDir;
            strcpy(brokenDir, newSongs.getNode(i)->getFile().path().string().c_str());

            std::string brokenDir_str = brokenDir;
            this->brokenDirs.push_back(brokenDir_str);
        }
    }

    std::cout << std::endl;


     std::ofstream brokenDirsFile_of;

    if (!std::filesystem::exists("Broken-Directories.txt")){
        std::ofstream brokenDirsFile_of("Broken-Directories.txt");
        brokenDirsFile_of.close();
    }
    brokenDirsFile_of.open("Broken-Directories.txt");

    
    brokenDirsFile_of << "Ur gay lol. \n second text \n";

    brokenDirsFile_of.close();

    std::ifstream brokenDirsFile_if;
    
    brokenDirsFile_if.open("Broken-Directories.txt");

    char c;
    while (brokenDirsFile_if.get(c))
        std::cout << c;

    if (brokenDirsFile_if.eof())                      
        std::cout << "[EoF reached]\n";
    else
        std::cout << "[error reading]\n";
    

    

    brokenDirsFile_if.close(); 
        
    
}