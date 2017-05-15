from collections import deque

def build(start, end):
    if start is None or end is None:
        return False
    if start is end:
        return True
    queue = deque()
    queue.append(start)
    start.visit_state = State.visited
    while queue:
        node = queue.popleft()
        if node is end:
            return True
        for adj_node in node.adj_nodes.values():
            if adj_node.visit_state == State.unvisited:
                queue.append(adj_node)
                adj_node.visit_state = State.visited
    return False

val = build(1, 2)
print(val)
