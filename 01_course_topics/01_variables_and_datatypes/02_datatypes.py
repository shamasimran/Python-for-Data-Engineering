
l = str("Hello World")  # l = "Hello World" str
m = int(20)  # m = 20 int
n = float(20.5)  # n = 20.5 float
o = complex(5, -2)  # o = 5 - 2j complex
p = list(("apple", "banana", "cherry"))  # p = ["apple", "banana", "cherry"] list
q = tuple(("apple", "banana", "cherry"))  # q = ("apple", "banana", "cherry") tuple
r = range(6)  # r = range(6) range
s = dict(name="John", age=36)  # s = {"name": "John", "age": 36} dict
t = set(("apple", "banana", "cherry"))  # t = {"apple", "banana", "cherry"} set
u = frozenset(("apple", "banana", "cherry"))  # u = frozenset({"apple", "banana", "cherry"}) frozenset
v = bool(5)  # v = True bool
w = bytes(5)  # w = bytes(5) bytes
x = bytearray(5)  # x = bytearray(5) bytearray
y = memoryview(bytes(5))  # y = memoryview(bytes(5)) memoryview
z = None

print(
    f"l={l}\n"
    f"m={m}\n"
    f"n={n}\n"
    f"o={o}\n"
    f"p={p}\n"
    f"q={q}\n"
    f"r={list(r)}\n"
    f"s={s}\n"
    f"t={t}\n"
    f"u={u}\n"
    f"v={v}\n"
    f"w={w}\n"
    f"x={x}\n"
    f"y={y}\n"
    f"z={z}"
)

# Type       | Ordered? | Mutable? | Duplicates? | Performance                                        | When to Use
# -----------|----------|----------|-------------|----------------------------------------------------|----------------------------------------------
# list       | Yes      | Yes      | Yes         | Fast index access (O(1)), slower search/insert O(n)| Ordered, editable, allows duplicates
# tuple      | Yes      | No       | Yes         | Same as list but faster & memory-efficient         | Ordered, read-only (constants, function returns)
# dict       | Yes*     | Yes      | Keys unique | Very fast key lookups/updates (average O(1))       | Key-value pairs for fast lookup (*since Py3.7)
# set        | No       | Yes      | No          | Very fast membership tests (average O(1))          | Unique items, unordered
# frozenset  | No       | No       | No          | Same as set, but immutable (hashable)              | Immutable set (can be dict/set keys)


