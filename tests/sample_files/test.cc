int test(std::vector<int> blacklist, int master){
    // looking for master/slave
    int slave = 0;
    for(int i : blacklist)
        if(i == master)
            return slave;
}
