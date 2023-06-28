#include <cmath>
using namespace std;

int minCost(vector<vector<int>> cost) {
    int len = cost.size();

    for(int i = 1; i < len; i++) {
        cost[i][0] += min(cost[i-1][1], cost[i-1][2]);
        cost[i][1] += min(cost[i-1][0], cost[i-1][2]);
        cost[i][2] += min(cost[i-1][0], cost[i-1][1]);
    }

    //answers stored in last row, top-down approach
    int endIdx = len-1;
    return min(cost[endIdx][0], min(cost[endIdx][1], cost[endIdx][2]));
}