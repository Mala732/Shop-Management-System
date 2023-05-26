import pandas as pd
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("item_directory.csv")
item_list=list(df.iloc[:,0])
df.set_index('Item',inplace=True)
earnings=pd.read_csv('data.csv')

from unti import append_list_as_row
import mod1


while True:
    print()
    print("--------------------------------------------------------------------------------")
    print("1.Stock details\t\t2.Update stock\n3.Create bill\t\t4.Sales summary\n0.Exit")
    user_ch=int(input("Proceed with:"))
    print()
    if user_ch==0:
        break

    elif user_ch==1:
        print("1.Stock of particular item\n2.Stock list")
        print()
        stock_ch=int(input("Choice: "))
        if stock_ch==2:        
            print(df.iloc[0:30,5])
            print(df.iloc[30:60,5])
            print(df.iloc[60:90,5])
            print(df.iloc[90:101,5])
            print()
        elif stock_ch==1:
            ch=input("Enter item: ")
            ch=ch.upper()
            ch_list=mod1.choice_list(ch,item_list)
            itm=mod1.item_select(ch_list,ch,item_list)
            if itm in item_list:
                print("Current Stock:",df.loc[itm,'Qty'])
            else:
                pass
                        
    elif user_ch==2:
        while True:
            ch=input("Enter item: ")
            ch=ch.upper()
            ch_list=mod1.choice_list(ch,item_list)
            itm=mod1.item_select(ch_list,ch,item_list)       
            if itm in ch_list:
                print("Current stock:",df.loc[itm,'Qty'])
                updated_stock=int(input("Update stock: "))
                df.loc[itm,'Qty']=df.loc[itm,'Qty']+updated_stock
                print("UPDATED STOCK:",df.loc[itm,'Qty'])
                print()
            if ch=='':
                break
            df.to_csv("item_directory.csv")

    elif user_ch==3:
        blist=[]
        date=date.today()
        day=str(date)
        today=day[8:10]+"-"+day[5:8]+day[0:4]
        cgstList=[]
        sgstList=[]
        row_contents=[]
        earnings_index=list(earnings.index.values)
        ex=earnings_index[-1]
        billno=earnings.iloc[ex]['Billno']+1
        while True:
            ch=input("Enter item: ")
            ch=ch.upper()
            ch_list=mod1.choice_list(ch,item_list)
            itm=mod1.item_select(ch_list,ch,item_list)
            if itm in ch_list:
                qty=int(input("Enter Quantity:"))
                if qty>df.loc[itm]['Qty']:
                    if df.loc[itm]['Qty']==0:
                        print('ITEM OUT OF STOCK')
                        continue
                    print("The entered quantity exceeds the current stock[",
                          df.loc[itm]['Qty'],']')
    
                    buy=input("Would like to proceed buying the item [Y/N]:")
                    if buy=='Y' or buy=='y':
                        qty=df.loc[itm]['Qty']
                    elif buy=='N' or buy=='n':
                        qty=0
                        continue
                i=itm.title()
                p=df.loc[itm,"Price"]
                gst=df.loc[itm,"GST"]*p
                cgst=df.loc[itm,"CGST"]*qty
                sgst=df.loc[itm,"SGST"]*qty
                amt=p*qty
                df.loc[itm,"Qty"]=df.loc[itm,"Qty"]-qty
                cgstList.append(cgst)
                sgstList.append(sgst)
                ilist=[i,p,qty,amt]
                blist.append(ilist)
            elif ch=='':
                pass
            elif ch=='*':
                break
        
        
        #creating dataframe from the newly created list(blist)
        bill=pd.DataFrame(blist,columns=["Item Description","Price"
                                         ,"Quantity","Amount"])
        total=pd.DataFrame(columns=["Item Description","Price"
                                    ,"Quantity","Amount"],
                           data=[["TOTAL AMOUNT","---","---",bill["Amount"].sum()]])

        #creating dataframe of the earnings
        if bill.empty==False:
            row_contents=[billno,today,bill["Amount"].sum()]
            append_list_as_row('C:\\Users\\user\\Desktop\\billing\\data.csv',row_contents)
            earnings=earnings=pd.read_csv('C:\\Users\\user\\Desktop\\billing\\data.csv')
            
        else:
            pass
        #addind new row called total using append function
        bill=bill.append(total)

        bill.set_index("Item Description",inplace=True)
        print()
        print("-----------------------------------------------------------------------------")
        print("\n\n        \t\t      MORE\n",
              "            \t\t  QUALITY 1st\n",
              "  \t\t(Formerly known as Aditya Birla limited)\n",
              "           \t\tPoonkunnam Thrissur\n",
              "            \t\tTEL : 0487-2700800\n",
              "Dated:",today )
        print("Bill No:",billno)

        print(bill)
        print("-----------------------------------------------------------------------------")
        print("Tax Desc                        Tax Amt\n",
              "CGST                           ",round(sum(cgstList),2),"\n",
              "SGST                           ",round(sum(sgstList),2))
        print("-----------------------------------------------------------------------------")
        print("Total Tax Value                 ",round(sum(cgstList),2)+round(sum(sgstList),2))
        print("-----------------------------------------------------------------------------")

        print("\n\nThank You For Shopping With us.\nTerms & Conditions Apply.")
        
        df.to_csv("item_directory.py")

    elif user_ch==4:
        print("1.Sales Summary for a particular day\n2.Display SalesSummary Data\n3.Display Sales Summary Garph")
        Sales_summary=earnings.groupby('Date').sum()
        choice=int(input("Your Choice:"))
        if choice==2:
            sales_summary=Sales_summary.iloc[:,1]
            print(sales_summary)
        elif choice==3:
            sns.lineplot(data=Sales_summary,x='Date',y='Amount',color='red')
            plt.show()

        elif choice==1:
            date=input("Date: ")
            
            date_list=list(earnings.loc[:,'Date'])
            todays_earnings=earnings.groupby('Date').sum()
            earnings.set_index('Date',inplace=True)
            if date in date_list:
                print(earnings.loc[date,:])
                print("Total:",todays_earnings.loc[date,'Amount'])
            else:
                print("Data for the entered date not found")
            earnings.reset_index(inplace=True)

    
        
        
        
            
