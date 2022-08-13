#include <FileList.hpp>

class SongList : public FileList {
public:
    SongList(std::string rootPath);
    
    void exportList() const;
};