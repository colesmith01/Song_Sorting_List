#include <iostream>
#include "Node.hpp"

using namespace std;


/*Constructor(s)*/

Node::Node(){
	this->next = 0;
}


/*Setter Function(s)*/

void Node::setNext(Node *n) {
	next = n;
}

void Node::setSong(MP3 mp3){
	this->song = mp3;
}


/*Getter Function(s)*/

Node* Node::getNext() const{
	return next;
}

MP3 Node::getSong() const{
	return song;
}


/*Destructor*/

//Define empty destructor
Node::~Node(){}