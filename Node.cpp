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

void Node::setSong(MP3 mp3) {
	this->song = mp3;
}

void Node::setPath(std::string path) {
	this->path = path;
}


/*Getter Function(s)*/

Node* Node::getNext() const {
	return next;
}

MP3 Node::getSong() const {
	return song;
}

string Node::getPath() const {
	return path;
}


/*Destructor*/

//Define empty destructor
Node::~Node(){}