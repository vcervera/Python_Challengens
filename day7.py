
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 2, 3, 2, 5]))

def find_uniq(ls):
    return[x for x in ls if ls.count(x) == 1]
