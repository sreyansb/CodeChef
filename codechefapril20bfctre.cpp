#include <bits/stdc++.h>

using namespace std;

#define N   1000001

#define um unordered_map

typedef long long int ll;

ll mod=1000000007;

vector<ll> costarray;

um<ll,um<ll,ll>> prodpath;

void addEdge(vector<ll> v[],

             ll x,

             ll y)

{

    v[x].push_back(y);

    v[y].push_back(x);

}



ll sievemasterd[N];



void sievemaster()

{

    sievemasterd[1] = 1;

    for (ll i=2; i<N; i++)



        sievemasterd[i] = i;



    for (ll i=4; i<N; i+=2)

        sievemasterd[i] = 2;



    for (ll i=3; i*i<N; i++)

    {

        if (sievemasterd[i] == i)

        {

            for (ll j=i*i; j<N; j+=i)



                if (sievemasterd[j]==j)

                    sievemasterd[j] = i;

        }

    }

}



ll findallfact(vector<ll> stck)

{

    ll i;

    unordered_map<ll,ll> primct;

    for (i = 0; i < (ll)stck.size();i++) {

        //cout<<stck[i]<<" ";

        if(prodpath.count(stck[i]))

        {

            for(auto it : prodpath[stck[i]])

            {

                if(primct.count(it.first))

                    primct[it.first]=(primct[it.first]+it.second);

                else

                    primct.insert({it.first,it.second});

            }

        }

        else

        {

            ll x=costarray[stck[i]];

            while (x != 1)

            {

                if(primct.count(sievemasterd[x]))

                {

                    primct[sievemasterd[x]]=(primct[sievemasterd[x]]+1);

                }

                else

                {

                    primct.insert({sievemasterd[x],1});

                }

                if(prodpath[stck[i]].count(sievemasterd[x]))

                {

                    prodpath[stck[i]][sievemasterd[x]]=(prodpath[stck[i]][sievemasterd[x]]+1);

                }

                else

                {

                    prodpath[stck[i]].insert({sievemasterd[x],1});

                }



                x = x / sievemasterd[x];

            }

        }

    }

    ll divisors=1;

    for(auto it : primct)

    {

        //cout<<it.first<<"->"<<it.second<<"\n";

        divisors=(divisors%mod * (it.second+1)%mod)%mod;

    }

    return divisors;

}



void DFS(vector<ll> v[],bool vis[],ll x,ll y,vector<ll> stck)

{

    ll ans;

    stck.push_back(x);

    if (x == y) {



        ans=findallfact(stck);

        cout<<ans<<"\n";

    }

    vis[x] = true;



    int flag = 0;

    if (!v[x].empty()) {

        for (ll j = 0; j < v[x].size(); j++) {

            if (vis[v[x][j]] == false) {

                DFS(v, vis, v[x][j], y, stck);

                flag = 1;

            }

        }

    }

    if (flag == 0) {

        stck.pop_back();

    }

}



void bfs(ll x,

             ll y,

             vector<ll> v[],

             ll n,

             vector<ll> stck)

{

    bool vis[n + 1];

    memset(vis, false, sizeof(vis));

    DFS(v, vis, x, y, stck);

}



int main()

{

    ios_base::sync_with_stdio(false);

    cin.tie(NULL);



    int t;

    cin>>t;

    sievemaster();

    while(t--)

    {

        ll n,q;

        int a,b;

        prodpath.clear();

        

        cin>>n;

        vector<ll> stck;

         vector<ll> v[n+1];

        costarray.resize(n+1);

        for(ll i=0;i<n-1;i++)

        {

            cin>>a>>b;

            addEdge(v,a,b);

        }

        for(ll i=1;i<n+1;i++)

        {

            cin>>costarray[i];

        }

        cin>>q;

        for(ll i=0;i<q;i++)

        {

            cin >> a>>b;

            bfs(a,b,v,n,stck);



        }



    }

    return 0;

}