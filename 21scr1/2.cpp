#include <iostream>

using namespace std;

int Answer;
int t, len;
char x;
int bits[50000];
int ans[50000];

bool chk_ps(int k) {
    if (k+t<len) {
        if (ans[k+t]==1)
            return true;
    }
    if (k-t>=0) {
        if (ans[k-t]==1)
            return true;
    }
    return false;
}

bool pos_p(int k) {
    if (k+t >= len) return false;
    if (k+2*t >= len) return true;
    if (bits[k+2*t]==1)
        return true;
    else
        return false;
}

int main(int argc, char** argv)
{
	int T, test_case;

	cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{
        cin >> len >> t;
        for(int k=0;k<len;k++) {
            cin >> x;
            bits[k] = (x=='0') ? 0 : 1;
            ans[k] = 0;
        }
        getchar();
        
        for(int k=0;k<len;k++) {
            if (bits[k]==0) continue;
            if (chk_ps(k)) continue;
            if (pos_p(k)) {
                ans[k+t] = 1;
            }
            else {
                ans[k-t] = 1;
            }
        }

		cout << "Case #" << test_case+1 << endl;
        for(int k=0;k<len;k++) {
		    cout << ans[k];
        }
        cout << endl;
	}

	return 0;
}