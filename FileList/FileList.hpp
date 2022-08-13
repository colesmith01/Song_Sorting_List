#ifndef FILELIST_HPP_
#define FILELIST_HPP_


#include <vector>
#include <Node.hpp>

/*
The Node class holds information about a specific cell in the connect four grid, and can be linked to another
instance of type Node
*/

class FileList {
protected:
	//Parameters
	Node* head;
	int size;
	int listIteration;
	std::vector<std::string> brokenDirs;

	void directory_scraper(std::string rootPath);

public:
	FileList();
	FileList(FileList *filelist, std::string extensionType);

	Node* getHead() const;
	Node* getNode(int index) const;

	int getSize() const;

	void addNode(Node* n);

	virtual void exportList() const;

	/*
	Declare destructor
	*/
	~FileList();
};


#endif