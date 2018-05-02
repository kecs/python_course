# Python tanfolyam

Házi feladat:
A homework.py programot befejezni. Ez egy crawler, ami magyar username szótárat állít elő egy magyar híroldal felhasználóiból.
Követelmények:
- A kész programot 1 héten belül feltölteni a saját githubodra új nyilvános projektként, nekem a linket elküldeni mailben
- A program fusson le hiba nélkül
- A program állítson elő egy legalább 2000 soros file-t (users.txt) amiben 1 sor egy felhasználónév
- Minden felhasználónév legyen mutálva
- Törekedj tiszta formátumra, kövesd az alap program konvencióit
- 1 és 10 másodperc közötti véletlenszerű értéket alszik két request között, hogy ne tűnjön bot-nak. Kezdd ezzel!
- Tanácskozni, kérdezni ér, de egymásét ne adjátok be

--------------------------------------------------------
## Vázlat
- Interpretált, vm-en fut
- DE gyors, mert C
- Általanos célú
- Raspberry pi, web, desktop
- Linux/osx eleve fent van
- Bytecodre-ra fordul, létezik c/java compiler

Előnyök:
- Modulok, cummunity
- Easy to read
- Punk

Hátrányok:
- Eltérő syntax
- Nem enterprise?
- Deploy
- Többszálúság

IDE?

repl
-----------------------------------
-változók
a = 69
b = 420
c, d = 13, 42
s = "hello world"
print(s)
print(a, b, c, d)
print(a * 666, b + c, str(a) + '!!!')

-tömb
a1 = (1, 2, 3)
a2 = ("a", "b", "c")

-for, while?
for v in a1: print(v)
for i in range(5): print(i * 2)

-function
def f(v1, v2=666):
print(v1)
print(v2)

g = f

-class?
class C:
p1 = 69
p2 = (3.14, 2.71)

-import

-save/run eg.: python -m http.server 7777

-file ops

