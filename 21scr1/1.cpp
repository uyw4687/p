#define _CRT_SECURE_NO_WARNINGS
#define SIZE 100000
#include <iostream>

using namespace std;

int ns[SIZE];
int ps[SIZE];
int rs[SIZE];
bool in[SIZE];

int pa(int a, int ps[]) {
	if (ps[a] == a) {
		return a;
	}
	ps[a] = pa(ps[a], ps);
	return ps[a];
}

void tog(int a, int b, int ps[], int rs[]) {
	int p1 = pa(a, ps);
	int p2 = pa(b, ps);

	if (p1 == p2) return;
	if (rs[p1] < rs[p2]) {
		int temp = p1;
		p1 = p2;
		p2 = temp;
	}

	rs[p1] += rs[p2];
	ps[p2] = p1;
}

int main(int argc, char** argv)
{
	int T, test_case;

	cin >> T;
	int num;
	int cnt = 0;
	for (test_case = 0; test_case < T; test_case++)
	{
		cin >> num;
		for (int j = 0; j < num; j++) {
			cin >> ns[j];
			ps[j] = j;
			rs[j] = 1;
			in[j] = false;
		}

		for (int j = 0; j < num; j++) {
			if (ns[j] + j >= num) continue;
			tog(j, ns[j] + j, ps, rs);
		}

		for (int j = 0; j < num; j++) {
			ps[j] = pa(j, ps);
		}

		cnt = 0;
		for (int j = 0; j < num; j++) {
			if (!in[ps[j]]) {
				in[ps[j]] = true;
				cnt++;
			}
		}

		cout << "Case #" << test_case + 1 << endl;
		cout << cnt << endl;
	}

	return 0;
}