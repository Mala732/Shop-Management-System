def choice_list(choice,list):
    choiceList=[]
    len_ch=len(choice)
    for k in range(0,1):
        for i in list:
            num=list.index(i)
            if choice in i and choice!='' and choice==i[0:len_ch] :
                print(num,'.',i)
                choiceList.append(i) 
    return choiceList

def item_select(choice_list,choice,item_list):
    if len(choice_list)>0:
        item_choice=int(input("Item no:"))
        itm=item_list[item_choice]
    else:
        itm=choice
    return itm


