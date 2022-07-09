#include <iostream>
using namespace std;
#include <fstream>
using std::ifstream;
#include <cstdlib>
#include <vector>
using std::vector;

class gay{
public:
    string getName()
    {
        return name;
    }
private:
    string name = "Dom";
};

int main() {
    ifstream indata; // indata is like cin
    char letter; // variable for input value

    indata.open("653 - Alix Perez - Perfect Stranger.mp3"); // opens the file
    if(!indata) { // file couldn't be opened
      cerr << "Error: file could not be opened" << endl;
      exit(1);
    }
    indata >> letter;
    while ( !indata.eof() ) { // keep reading until end-of-file
      cout << "The next letter is " << letter << endl;
      indata >> letter; // sets EOF flag if no value found
    }
    indata.close();
    cout << "End-of-file reached.." << endl;
    return 0;
}
