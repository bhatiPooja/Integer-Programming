import pandas as pd
import math

class WeightCalculationForPyfolio:
    def __init__(self,wtsDF,returnsDF):
        self.wtsDF=wtsDF
        self.returnsDF=returnsDF
       
    def returnsCalculation(self,strategyName):
        returnsDFCopied = self.returnsDF.copy() 
        for idx,i in self.wtsDF.iterrows():
            startDate=i['Out_Sample_Start_Date']
            endDate=i['Out_Sample_End_Date']
            startegyWt=i[strategyName]
            #print(startegyWt,startDate,endDate)            
            if startegyWt == 0: 
                abs(returnsDFCopied[startDate:endDate]*0)
                #print(abs(returnsDFCopied[startDate:endDate]*0))                
            elif startegyWt < 0: 
                returnsDFCopied[startDate:endDate]*(-1)
                #print(returnsDFCopied[startDate:endDate]*(-1))               
            else:   
                returnsDFCopied[startDate:endDate]*1
                #print(returnsDFCopied[startDate:endDate]*1)
        return returnsDFCopied

    def PositionCalculation():      
        pass
    
    def TransactionCalculation():
        pass

wtsDF=pd.read_csv("IPStrategy.csv")
returnsDF=pd.read_csv("Return BRACKET_ORDER_STR.csv", names=["DateTime","Returns"])
returnsDF["DateTime"]=returnsDF["DateTime"].apply(lambda x: x.split(" ")[0])
returnsDF.index = returnsDF['DateTime'] 
del returnsDF['DateTime']
###################################################################################################### 
transactionDF=pd.read_csv("Transactions BRACKET_ORDER_STR.csv")
transactionDF["date"]=transactionDF["date"].apply(lambda x: x.split(" ")[0])
transactionDF.index = transactionDF['date'] 
del transactionDF['date']


transactionDFCopied = transactionDF.copy() 
prevWeight=0
strategyName="BRACKET_ORDER_STR"
transactionInRange = pd.DataFrame()


for idx,i in wtsDF.iterrows():
    startDate=i['Out_Sample_Start_Date']
    endDate=i['Out_Sample_End_Date']
    startegyWt=i[strategyName]

#    sumOfPreviousSet = sum(transactionInRange["amount"])   
#    weightDiff = 0
#    if sumOfPreviousSet != 0:
#        weightDiff = math.copysign(1,sumOfPreviousSet) * (startegyWt - prevWeight)
    transactionInRange = transactionDFCopied[startDate:endDate]
    print(transactionInRange)
    if startegyWt != 0:
        transactionInRange["amount"] =  transactionInRange["amount"] * startegyWt 
        prevWeight = startegyWt
        
#    transactionInRange.iloc[0]["amount"] = transactionInRange.iloc[0]["amount"] + weightDiff        
#return returnsDFCopied
for index, row in weights.iterrows():
   fr = weights.loc[i]
   dt = data[fr["Out_Sample_Start_Date"]: fr["Out_Sample_End_Date"]]
   if fr["BRACKET_ORDER_SG"] is not 0:
       dt["amount"] = dt["amount"] * fr["BRACKET_ORDER_SG"]
       print(dt["amount"])



######################################################################################################    
object1=WeightCalculationForPyfolio(wtsDF,returnsDF)
#object1.to_csv("updated_return_file.csv")
#object1.getReturns()
#getTransactions()
#getPositions()
z=object1.returnsCalculation("BRACKET_ORDER_STR")
z.to_csv("updated_return_file.csv")

