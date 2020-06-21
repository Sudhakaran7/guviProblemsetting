from main import Graph
def test_case1(return_val):
    flag=0

    if[{'a', 'e'}, {'b', 'f'}, {'c', 'g'}, {'d', 'h'}] == return_val:
        print(return_val)
        flag+=1
        exit(0)
    else:
        pass

    if([{'a', 'u'}, {'y', 'b'}, {'f', 't'}, {'g', 'r'}]==return_val):
        print(return_val)
        flag+=1
        exit(0)
    else:
        pass
    if ([{'z', 'a'}, {'b', 'y'}, {'c', 'x'}, {'d', 'w'}] == return_val):
        print(return_val)
        flag+=1
        exit(0)
    else:
        pass
    if ([{'q', 'p'}, {'w', 'o'}, {'e', 'i'}, {'r', 'u'}] == return_val):
        print(return_val)
        flag+=1
        exit(0)
    else:
        pass
    if ([{'a', 'l'}, {'s', 'k'}, {'j', 'd'}, {'f', 'h'}] == return_val):
        print(return_val)
        flag+=1
        exit(0)
    else:
        pass
    if(flag==0):
        print('0')
keys = list(map(str,input().split()))
values =list(map(str,input().split()))
g = {}
for key, value in zip(keys, values):
    g[key] = value
graph = Graph(g)
test_case1(graph.edges())
