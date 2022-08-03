#ifndef FILELIST_HPP_
#define FILELIST_HPP_


#include <vector>
#include <Node.hpp>

/*
The Node class holds information about a specific cell in the connect four grid, and can be linked to another
instance of type Node
*/

class FileList {
private:
	//Parameters
	Node* head;
	int size;
	int listIteration;
	std::vector<std::string> brokenDirs;

	void directory_iterator(std::string rootPath);
	void addNode(Node* n);

public:
	FileList();
	FileList(FileList *filelist, std::string extensionType);
	FileList(std::string rootPath);

	Node* getHead() const;
	Node* getNode(int index) const;

	int getSize() const;

	/*
	Declare destructor
	*/
	virtual ~FileList();
};


#endif