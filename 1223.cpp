class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax) 
    {
        static int ans[ 5000 ][ 6 ][ 16 ] = { 0 }, MOD = 1000000007;
        int output = 0;
        
        memset( ans, 0, sizeof( ans ) );
        for( int i = 0; i < 6; ++i )
            for( int j = 1; j <= rollMax[ i ]; ++j )
                ans[ 0 ][ i ][ j ] = 1;
        for( int i = 1; i < n; ++i )
            for( int j = 0; j < 6; ++j )
                for( int k = 0; k <= rollMax[ j ]; ++k )
                    for( int l = 0; l < 6; ++l )
                        if( l == j )
                            ( ans[ i ][ j ][ k ] += k == rollMax[ j ]? 0 : ans[ i - 1 ][ j ][ k + 1 ] ) %= MOD;
                        else
                            ( ans[ i ][ j ][ k ] += ans[ i - 1 ][ l ][ 1 ] ) %= MOD;

        for( int i = 0; i < 6; ++i )
            ( output += ans[ n - 1 ][ i ][ 1 ] ) %= MOD;
        return output;
    }
};
