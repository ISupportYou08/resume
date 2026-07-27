# # # # # # # # # #Single Fact - Representation of on label, one value
# # # # # # # # # bot_location = "Room 3"
# # # # # # # # # print(bot_location)

# # # # # # # # # #len()
# # # # # # # # # rooms =["Room1","Room2","Room3","Room4"]
# # # # # # # # # print(rooms)
# # # # # # # # # print(len(rooms))

# # # # # # # # #Dictionary - hold several realted Facts about single identity
# # # # # # # # robot_status ={
# # # # # # # #     "location" : "Room3",
# # # # # # # #     "battery" : 80
# # # # # # # #     "carrying_item : False
# # # # # # # # }

# # # # # # # # print(robot_status["location"])
# # # # # # #===========================================================

# # # # # # # state = "off"

# # # # # # # def toggle(state):
# # # # # # #     return "on" if state == "off" else "off"
# # # # # # # state = toggle (state)
# # # # # # # print(state)
# # # # # # #===========================================================
# # # # # # #Dictionary  
# # # # # # #connection= rules
# # # # # # conn = {
# # # # # #     "Room1" : ["Room2"],
# # # # # #     "Room2" : ["Room1","Room2"],
# # # # # #     "Room3" : ["Room2","Room4"],
# # # # # #     "Room4" : ["Room3"]
# # # # # # }

# # # # # # #current states = actions
# # # # # # curr_state = "Room2"
# # # # # # print("Possible actions", conn[curr_state])


# # # # # def can_disp(balance, price):
# # # # #     return balance >= price
# # # # # balance, price = 20,15
# # # # # #rules
# # # # # if can_disp(balance,price):
# # # # #     balance-=price
# # # # # #action
# # # # #     print("Dispensed. Remaining: ", balance)
# # # # # else:
# # # # #     print("Blocked: insufficient balance: ")

# # # #  #===========================================================
# # # # path_so_far =["Room 1", "Room 2"]
# # # # print("Visited so far", path_so_far)

# # # # path_so_far.append("Room 3")
# # # # print("Updated path: ", path_so_far)

# #  #===========================================================
# maze = {"A": ["B"],"B":["A","C"],"C": ["B","D"],"D":["C"]}
# # print("MAZE STRUCTURE ", maze)
# # print("Neigbors of B" , maze ["B"])

# # stud = [{"name": "marco", "score": 88},{"name": "diane", "score":92}]

# # for s in stud:
# #     print(s["name"], "score", s["score"])
# #========================================
# # maze = {"A": ["B"],"B":["A",""],"C": ["B","D"],"D":["C"]}

# # start,goal= ("A","C"), "D"
# # frontier = maze[start]
# # search_space = list(maze.keys())

# # print("\nFrontier (immediate options): ",frontier)
# # print("Full Search space(all states): ", search_space)
# # print("Is goal frontier right now", goal in frontier)


# current = start 
# path = [current]

# while current != goal:
#     frontier = maze[current]
#     for neighbor in frontier:
#         if neighbor not in path:
#             current = neighbor
#             path.append(current)
#             break

# print("Final path taken", path)
# print("Reached goal?", current == goal)

maze = {"A": ["B","C"],
        "B":["A","D","E"],
        "C": ["A","F"],
        "D":["B"],
        "E":["B"],
        "F":["C","G"],
        "G":["F"],
        }

def dfs_find_path(maze,start,goal,path=None):
    if path is None:
        path = [start]
    else:
        path= path+ [start]

    print("Visiting ",start, " | Path so far:", path)

    if start == goal:
        return path
    for neighbor in maze[start]:
        if neighbor not in path:
            result = dfs_find_path(maze, neighbor,goal,path)
            if result:
                return result

    return None
print(dfs_find_path(maze,"A","G"))
#================================================
# from collections import deque
maze = {"A": ["B","C"],
        "B":["A","D","E"],
        "C": ["A","F"],
        "D":["B"],
        "E":["B"],
        "F":["C","G"],
        "G":["F"],
        }

def bfs(maze,start,goal):
    queue =deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        print("Exploring", path)

        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in maze[node]:
                queue.append(path+[neighbor])
    return None
print(bfs(maze, "A", "G"))
