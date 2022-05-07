#include<set>
#include<algorithm>

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int min[ 200000 ] = { nums[ 0 ] };
        set<int> shown;
        
        for( int i = 1; i < nums.size(); ++i )
            min[ i ] = std::min( min[ i - 1 ], nums[ i ] );
        shown.insert( nums.back() );
        for( int i = nums.size() - 2; i > 0; --i )
        {
            set<int>::iterator it = shown.insert( nums[ i ] ).first;
            if( nums[ i ] > min[ i - 1 ] && shown.begin() != it && *--it > min[ i - 1 ] )
                return true;
        }
        return false;
    }
};
