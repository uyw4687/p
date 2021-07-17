#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int Answer;
int N,M,K;

bool chk(vector<unordered_set<int>> &ma, int start, vector<bool> &vst, vector<bool> &par) {
    vst[start] = true;
    par[start] = true;
    for (auto const &x : ma[start]) {
        if (par[x]) return false;
        if (vst[x]) continue;
        if (!chk(ma,x,vst,par)) return false;
    }
    par[start] = false;
    return true;
}

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	
    int T, test_case;

    cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{
        cout << "Case #" << test_case+1 << '\n';
        cin >> N >> M >> K;
        vector<unordered_set<int>> ma(N,unordered_set<int>());
        for (int j=0;j<M;j++) {
            int x,y;
            cin >> x >> y;
            ma[x-1].insert(y-1);
        }
        for (int j=0;j<K;j++) {
            int x,y;
            cin >> x >> y;
            
            if (ma[x-1].find(y-1)!=ma[x-1].end()) {
                    cout << '0';
            }
            else if (ma[y-1].find(x-1)!=ma[y-1].end()) {
                    cout << '1';
            }
            else {
                ma[x-1].insert(y-1);
                vector<bool> vst(N, false);
                vector<bool> par(N, false);
                if (chk(ma,x-1,vst,par)) {
                    cout << '0';
                }
                else {
                    cout << '1';
                    ma[x-1].erase(y-1);
                    ma[y-1].insert(x-1);
                }
            }
        }
        cout << '\n';
	}

	return 0;
}