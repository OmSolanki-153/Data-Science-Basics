import pandas as pd
sFileName='C:/MScITPracs/MU-DATA-SCIENCE/shipping_data.txt'
RouteDataRaw=pd.read_csv(sFileName,header=0,low_memory=False, sep='|',encoding="latin-1")
RouteStart=RouteDataRaw[RouteDataRaw['StartAt']=='Mumbai']
RouteDistance=RouteStart[RouteStart['Cost']=='DistanceMiles']
RouteDistance=RouteDistance.sort_values(by=['Measure'],ascending=False) 
RouteMax=RouteStart["Measure"].max()
RouteMaxCost=round((((RouteMax/1000)*1.5*2)),2)
print('Maximum (Rs.) per day:') 
print(RouteMaxCost)
RouteMean=RouteStart["Measure"].mean()
RouteMeanMonth=round((((RouteMean/1000)*2*30)),6) 
print('Mean per Month (Miles):') 
print(RouteMeanMonth)
