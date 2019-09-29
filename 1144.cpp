class Solution {
public:
    int movesToMakeZigzag(vector<int>& num) {
        int odd = 0, even = 0;
        
        if( num.size() < 3 )
            return 0;
        
        for( int i = 1; i < num.size(); i += 2 )
        {
            int a = num[ i - 1 ], b = i == num.size() - 1? a : num[ i + 1 ];
            if( num[ i ] >= min( a, b ) )
                odd += num[ i ] - min( a, b ) + 1;
        }
        for( int i = 0; i < num.size(); i += 2 )
        {
            int a = num[ i? i - 1 : 1 ], b = i == num.size() - 1? a : num[ i + 1 ];
            if( num[ i ] >= min( a, b ) )
                even += num[ i ] - min( a, b ) + 1;
        }
        
        return min( odd, even );
    }
};
