#ifndef NODE_HPP_
#define NODE_HPP_

#include <string>
#include <filesystem>

/*
The Node class holds information about a specific cell in the connect four grid, and can be linked to another
instance of type Node
*/

class Node {
private:
	//Parameters
	std::filesystem::directory_entry file;
	Node* next;

public:
	Node();
	
	void setNext(Node* n);

	void setFile(std::filesystem::directory_entry filesystem);

	
	/*
	Get the next node
	*/
	Node* getNext() const;

	std::filesystem::directory_entry getFile() const;

	std::string getPath() const;

	std::string getExtension() const;

	/*
	Declare destructor
	*/
	virtual ~Node();
};


#endif