import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def cartons(n, b):
    k = -(-n//b)
    return f"The {pl(n,' can',' cans')} at {pl(b,' can',' cans')} a carton {v(n,'takes','take')} {pl(k,' carton',' cartons')}, the last carton holding {pl(n-(k-1)*b,' can',' cans')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' can',' cans')} at {pl(w,' can',' cans')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' can',' cans')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' carton',' cartons')} at ${m(pc)} a carton {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} a can."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' can',' cans')} at {pl(pm,' can',' cans')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(785)
R = random.randint
cases = [
 dict(fn="cartons", args=["468","24"], expect=cartons(468,24)),
 dict(fn="weeks", args=["468","65"], expect=weeks(468,65)),
 dict(fn="cost", args=["20","9.60","468"], expect=cost(20,960,468)),
 dict(fn="time", args=["468","15"], expect=time_(468,15)),
 dict(fn="cartons", args=["1","1"], expect=cartons(1,1)),
 dict(fn="cartons", args=["456","24"], expect=cartons(456,24)),
 dict(fn="cartons", args=["1000000","1000"], expect=cartons(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["455","65"], expect=weeks(455,65)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="cartons", args=[str(n),str(b)], expect=cartons(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["cartons",["0","24"]],["cartons",["1000001","12"]],["cartons",["2.5","12"]],["cartons",["468","0"]],["cartons",["468","1001"]],
 ["weeks",["0","30"]],["weeks",["468","0"]],["weeks",["468","100001"]],["weeks",["468","1.5"]],["weeks",["1000001","30"]],
 ["cost",["0","9.60","468"]],["cost",["100001","9.60","468"]],["cost",["20","0","468"]],["cost",["20","9.605","468"]],["cost",["20","9.60","0"]],
 ["time",["0","15"]],["time",["468","0"]],["time",["468","101"]],["time",["468","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
