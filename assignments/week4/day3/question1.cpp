#include <vector>
using namespace std;

int collision(vector<int> speed, int pos) {
	int s = speed[pos];
	int count = 0; 

	for(int i = 0; i < pos; i++) {
		if(speed[i] > s) {
			count++;
		}
	}

	for(int i = pos+1; i < speed.size(); i++) {
		if(speed[i] < s) {
			count++;
		}
	}

	return count;
}

int main() {
	return 0;
}