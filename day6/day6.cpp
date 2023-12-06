#include <bits/stdc++.h>
#define ll long long int
using namespace std;

vector<ll> parseline(string s) {
    vector<ll> l = {};
    size_t pos = s.find(' ');
    while (pos < s.length()) {
        size_t npos = s.find(' ', pos+1);
        if (s[pos+1] != ' ')
            l.push_back(stoll(s.substr(pos+1,npos)));
        pos = npos;
    }
    return l;
}

ll parseline2(string s) {
  vector<char> digits; 
  size_t pos = s.find(' ');
  while (pos < s.length()) {
    if (s[pos] != ' ') digits.push_back(s[pos]);
    pos++;
  }
  string r(digits.begin(), digits.end());
  return stoll(r);
}

ll nwins(ll t, ll d) {
  double sD = sqrt(t * t - 4 * d);
  double x1r = (t - sD) / 2 + .001;
  double x2r = (t + sD) / 2 - .001;
  ll x1 = ceil(x1r);
  ll x2 = floor(x2r);
  return x2 - x1 + 1;
}

int main() {
//    freopen("test.txt", "r", stdin);
    string times, dists;
    getline(cin, times);
    getline(cin, dists);

    vector<ll> ts = parseline(times);
    vector<ll> ds = parseline(dists);
   
    ll total = 1; 
    for (size_t i = 0; i < ts.size(); i++) {
        total *= nwins(ts[i],ds[i]); 
    }

    cout << total << endl;

    ll t = parseline2(times);
    ll d = parseline2(dists);

    cout << nwins(t, d) << endl; 
}

