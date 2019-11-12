from random import choice
import datetime
import matplotlib.pyplot as plt
import numpy as np


starttime = datetime.datetime.now()


def ball():
    
   # global mclen
    global mclist
    global result
    global level
    global jishuqi
    global jianyancishu
    
    jiedian = {}
    boo = ["左", "右"]
    
    
    #result = {}
    #for r in mclist:
    #    result[r] = []
    
    jiedian[0] = choice(boo)
    jishuqi += 1
    i = 0    
    while i < (level - 1):
        for j in list(range(0,(mclist[-1]))):
            #print(f"正在检查节点{j}......")
            jianyancishu += 1
            if not j in jiedian.keys():
                #print("这个节点没状态")
                #print("-" * 20)
                continue
            elif jiedian[j] == "左":
                i += 1
                jiedian[j + i] = choice(boo)
                jishuqi += 1
                print(f"第{i}层的节点{j}的状态是：左")
                print("-" * 20)
            elif jiedian[j] == "右":
                i += 1
                jiedian[j + i +1] = choice(boo)
                jishuqi += 1
                print(f"第{i}层的节点{j}的状态是：右")
                print("-" * 20)
    
    for k in mclist:            
        try:
            print(f"结束时，第{i}层的节点{k}的状态是：{jiedian[k]}")
            
            result[k].append(jiedian[k])
            
            break
        except:
            continue
    
    
    for r in mclist:
        print(f"末层号码{r}装有：{result[r]}")
    

        
    print(mclist)
    
def zhexiantu(z):
    global mclist
    global mclen
    plt.figure(figsize=(7,7),dpi=100)
    plt.plot(mclist, mclen, linewidth = 1)
    plt.title(f"Normal Distribution", fontsize=24) 
    plt.xlabel(f"last floor", fontsize=14)
    plt.ylabel(f"{ballsamount} balls", fontsize=14) 
    #plt.ylim((min(dict1[l]), max(dict1[l])))
    
    my_x_ticks = np.arange(min(mclist), max(mclist)+1, 1)
    my_y_ticks = np.arange(min(mclen), max(mclen)+1, 10)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    
    
    plt.tick_params(axis='both', labelsize=10)
    plt.savefig(f"F:\\pythonxiong\\normal_b\\sdyxpng\\normalgdyx_{z}.png")


# buttons
ballsamount = 100000
floorsamount = 100
rounds = 1

level = floorsamount
mcn = 0
for m in list(range(1, level)):
    mcn += m
mclist = list(range(mcn, mcn + level))

result = {}    
for r in mclist:
   result[r] = []


# 计数器的设置
jishuqi = 0
jianyancishu = 0

for q in list(range(rounds)):
    
    balls = 0    
    while balls < ballsamount:
        balls += 1
        print("*" * 20)
        #print(f"现在第{balls}个球开始落下")
        ball()
        #print(f"现在第{balls}个球到达末层")
        print("*" * 20)
        
    
        
    mclen = []
    for r in mclist:
        mclen.append(len(result[r]))
    print(mclen)
    
    zhexiantu(q+1)
    

    
    #ballsamount = 20
    #floorsamount = 5

    result = {}
    for r in mclist:
        result[r] = []
       
print("%"*30)
print(mclist)
print(mclen)
print("%"*30)


endtime = datetime.datetime.now()
print(f"程序的运行时间为：{endtime-starttime}")
#print(f"总运算次数为：{jishuqi}")
print(f"总共需要检验节点信号{jianyancishu}次")

