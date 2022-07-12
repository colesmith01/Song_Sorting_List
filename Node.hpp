#ifndef NODE_HPP_
#define NODE_HPP_

#include <vector>
#include <string>

#include "mp3_code\mp3.hpp"

/*
The Node class holds information about a specific cell in the connect four grid, and can be linked to another
instance of type Node
*/

class Node {
private:
	//Parameters
	MP3 song;
	std::string path;
	Node* next;

public:

	/*
	Create a new node that stores nothing and is connected to nothing
	*/
	Node();
	

	/*
	Link the inputted Node to this Node
	*/
	void setNext(Node* n);

	/*
	Set an integer representing the cell type of this Node
	*/
	void setSong(MP3 mp3);

	
	/*
	Get the next node
	*/
	Node* getNext() const;

	/*
	Get an integer representing the cell type of this Node
	*/
	MP3 getSong() const;


	/*
	Declare destructor
	*/
	virtual ~Node();
};


#endif