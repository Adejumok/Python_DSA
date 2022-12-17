from collections import deque

graph = {}


def search(name):
    searched = []
    search_queue = deque()
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if neg(person):
                print(f"{person} is a neg")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def neg(name):
    return name[-1] == 'n'


graph["me"] = ["Ololade", "Omo", "Dami"]
graph["Ololade"] = ["Eden", "John"]
graph["Omo"] = ["Bright", "GodKnows"]
graph["Dami"] = ["Tutu", "Hannah"]
print(search(graph["me"]))
