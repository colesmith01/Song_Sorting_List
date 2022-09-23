#include <iostream>
#include "Node.hpp"

using namespace std;


/*Constructor(s)*/

Node::Node() {
	this->next = 0;
}


/*Setter Function(s)*/

void Node::setNext(Node *n) {
	next = n;
}

void Node::setFile(filesystem::directory_entry file) {
	this->file = file;
}


/*Getter Function(s)*/

Node* Node::getNext() const {
	return next;
}

filesystem::directory_entry Node::getFile() const {
	//last working line
	return file;
}

string Node::getPath() const {
	return file.path().string();
}


/*Destructor*/

//Define empty destructor
Node::~Node(){}