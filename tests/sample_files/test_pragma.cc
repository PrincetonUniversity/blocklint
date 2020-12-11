int test(std::vector<int> blacklist, int master){ // blocklint: pragma
    // looking for master/slave blocklint: pragma
    int slave = 0; // blocklint: some other tags pragma
    for(int i : blacklist) // blocklint: pragma
        if(i == master) // blocklint: pragma
            return slave;
}
