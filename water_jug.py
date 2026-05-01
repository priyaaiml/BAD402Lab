class waterjug:
    def __init__(self,j1,j2):
        self.j1=j1
        self.j2=j2
    def __eq__(self,other):
        return self.j1==other.j1 and self.j2==other.j2
    def __hash__(self):
        return hash((self.j1,self.j2))
    def dfs(current,visited,j1_cap,j2_cap,target):
        if current.j1==target or current.j2==target:
            if current.j1==target:
                print('Jug 1 now has ',target,'liters')
            else:
                print('Jug 2 now has ',target,'liters')
            return True
        visited.add(current)
        operations=[('Fill jug 1', j1_cap, current.j2),('Fill jug 2', current.j1, j2_cap),
                    ('Empty Jug 1',0,current.j2),('Empty Jug 2',current.j1,0),
                    ('Pour jug 1 to jug 2',max(0,current.j1+current.j2-j2_cap),min(j2_cap,current.j1+current.j2)),
                    ('Pour Jug 2 to Jug 1',min(j1_cap,current.j1+current.j2),max(0,current.j1+current.j2-j1_cap))]
        for operation in operations:
            action,new_j1,new_j2=operation
            new_state=waterjug(new_j1,new_j2)
            if new_state not in visited:
                print(f"Trying: {action} => ({new_j1,new_j2})")
            if dfs(new_state,visited,j1_cap,j2_cap,target):
                return True
                #print(new_j1,new_j2)
            return False
    def solve_problem(j1_cap,j2_cap,target):
        initial_state=waterjug(0,0)
        visited=set()
        if dfs(initial_state,visited,j1_cap,j2_cap,target):
            print('Solution Found!')
    #        print(j1_cap,j2_cap)
        else:
            print('Solution not possible')
    j1_cap=int(input('Enter jug 1 capacity:'))
    j2_cap=int(input('Enter jug 2 capacity:'))
    target=int(input('Enter target volume:'))
    print(f"Solving Water Jug Problem with capacities ({j1_cap},{j2_cap}) to remove {target} litres.")
    solve_problem(j1_cap,j2_cap,target)
