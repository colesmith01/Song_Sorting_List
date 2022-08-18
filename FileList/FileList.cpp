#include <FileList.hpp>
#include <iostream>

using std::cout;
using std::endl;

void FileList::directory_scraper(std::string path) {
    for (int i = 0; i < path.length(); i++) {
        if (path[i] < 0){
            brokenDirs.push_back(path);
            return;
        }
    }

    for (const auto &entry : std::filesystem::directory_iterator(path)){
        if (std::filesystem::is_directory(entry.path())){
            directory_scraper(entry.path().string());
        }
        else if (entry.path().has_extension()){
            Node* fileNode = new Node;
            fileNode->setFile(entry);
            
            addNode(fileNode);
        }
    }
}

FileList::FileList(){
    head = new Node;
    size = 0;
    listIteration = 0;
}

FileList::FileList(FileList *filelist, std::string extensionType){
    this->listIteration = filelist->listIteration + 1;

    for (int i = 0; i < filelist->getSize(); i++){
        Node *fileNode = filelist->getNode(i);
        
        if (fileNode->getFile().path().extension() == extensionType){
            addNode(fileNode);
        }
    }
}

void FileList::addNode(Node* n){
    
    if (this->head = 0)
        this->head = n;
    else{
        n->setNext(this->head);
        this->head = n;
    }

    size++;
}

Node* FileList::getHead() const{
    return this->head;
}


Node* FileList::getNode(int index) const{
    Node *n = head;
    
    for(int i = 1; i < index; i++){
        n = n->getNext();
    }
    cout << "testNode" << endl;

    return n;
}

int FileList::getSize() const{
    return size;
}

void FileList::exportList() const {}

/*
Declare destructor
*/
FileList::~FileList(){
    if (listIteration == 0) {
        Node *n;
    
        for(int i = 0; i < size; i++){
            n = head;
            head = n->getNext();
            delete n;
        }
    }
}

