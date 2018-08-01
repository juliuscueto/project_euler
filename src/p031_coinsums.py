import numpy as np

class Node(object):
    def __init__(self,coins,target,depth=0):
        self.depth = depth
        self.coins = coins
        self.target = target

        self.leaf = (target == 0)
        self.root = (self.depth == 0)

        self.sub_nodes = []

    def split(self):
        if not self.leaf:
            n_coins = self.coins[:-1]
            coin = self.coins[-1]
            max_incl = self.target // coin
            for i in range(max_incl+1):
                n_target = self.target - i*coin
                sub_i = Node(n_coins,n_target,self.depth+1)
                sub_i.coin = coin
                sub_i.coin_num = i
                if len(self.coins) != 1:
                    sub_i.split()
                    sub_i.prune()
                self.sub_nodes.append(sub_i)

    def prune(self):
        copy_sub_nodes = self.sub_nodes.copy()
        remove_que = []
        for i in range(len(copy_sub_nodes)):
            if len(self.coins) == 1 and not copy_sub_nodes[i].leaf:
                remove_que.append(i)
            else:
                self.sub_nodes[i].prune()
                if self.sub_nodes[i].sub_nodes == [] and not self.sub_nodes[i].leaf:
                    remove_que.append(i)
        for i in remove_que:
            self.sub_nodes.remove(copy_sub_nodes[i])

    def __str__(self):
        if self.root:
            str_base = "Root"
        elif self.leaf or len(self.coins) >= 1:
            str_base = "\n" + "    "*self.depth + " -> " + "coin:" + str(self.coin) + " num:" + str(self.coin_num) + " "
        else:
            str_base = ""
        for i in self.sub_nodes:
            str_base += str(i)
        return str_base

    def __len__(self):
        if self.leaf:
            return 1
        else:
            return sum([len(sub_i) for sub_i in self.sub_nodes])

def ways_efficient(coins,amount):
    ways = np.zeros(amount+1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i],amount+1):
            ways[j] = ways[j] + ways[j-coins[i]]
    return ways[amount]

if __name__ == "__main__":
    import time
    coins = [1,2,5,10,20,50,100,200]
    target = 200
    Root = Node(coins,target)
    start_time = time.time()
    Root.split()
    # Root.prune()
    print(time.time()-start_time)
    print(len(Root))
    print(time.time()-start_time)
    start_time = time.time()
    print(ways_efficient(coins,target))
    print(time.time()-start_time)
