import numpy as np

def move(cordinate):
    all_cut=[]
    x=cordinate[0]
    t=cordinate[1]
    cordinate=np.array(cordinate)
    cut_restriction=[1,t]
    for i in range(cut_restriction[0],min(x,cut_restriction[1])+1):
        all_cut.append(tuple(cordinate+[-i,1]))
    return all_cut

def get_number(all):
    if all==[]:
        val=0
    else:
        max_val=max(all)
        per_seq=set(range(max_val+2))
        non_exs=list(per_seq-set(all))
        val=min(non_exs)
    return int(val)

def get_grundynumber(cordinate,grundy_dict):
    all_moves=move(cordinate)
    all_number=[]
    for m in all_moves:
        try:
            number=grundy_dict[m]
        except KeyError:
            number=get_grundynumber(m, grundy_dict)
        all_number.append(number)
    grundy_number=get_number(all_number)
    grundy_dict[cordinate]=grundy_number
    return grundy_number

grundy_dict={}
for i in range(20):
    for j in range(20):
        cordinate=(i,j)
        get_grundynumber(cordinate, grundy_dict)

p_position=[]
for i in grundy_dict:
    if i[0]!=0 and grundy_dict[i]==0:
        p_position.append(i)

print(p_position)
