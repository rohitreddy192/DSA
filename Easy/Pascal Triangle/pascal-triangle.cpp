//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// #define ll long long
#include <iostream>
#include <vector>

class Solution{
public:
    vector<long long> nthRowOfPascalTriangle(int n) {
        vector<vector<long long>> res {{1}};
        int mod = 1000000007; // Modulus value
        for (int i = 1; i < n; ++i) {
            vector<long long> l;
            for (int j = 0; j <= i; ++j) {
                if (j == 0 || j == i) {
                    l.push_back(1);
                } else {
                    l.push_back((res[i - 1][j - 1] + res[i - 1][j]) % mod);
                }
            }
            res.push_back(l);
        }
        return res.back();
    }
};


//{ Driver Code Starts.


void printAns(vector<long long> &ans) {
    for (auto &x : ans) {
        cout << x << " ";
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        auto ans = ob.nthRowOfPascalTriangle(n);
        printAns(ans);
    }
    return 0;
}

// } Driver Code Ends