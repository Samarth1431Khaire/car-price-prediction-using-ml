import pickle

f=None
model=None
try:
       f=open("car.model", "rb")
       model=pickle.load(f)
except Exception as e:
       print("issue", e)
finally:
       if f is not None:
               f.close()

if model is not None:
           k=float(input("enter the km driven"))
           y=float(input("enter the model year"))
           data=[k,y]
           
           n=float(input("1 Maruti, 2 Hyundai, 3 Datsun, 4 Honda, 5 Tata, 6 Chevrolet, 7 Toyota, 8 Jaguar, 9 Mercedes, 10 Audi, 11 Skoda, 12 Jeep, 13 BMW, 14 Mahindra, 15 Ford, 16 Nissan, 17 Renault, 18 Fiat, 19 Volkswagen, 20 Volvo, 21 Mitsubishi, 22 Land Rover, 23 Daewoo, 24 MG Hector, 25 Force, 26 Isuzu, 27 OpelCorsa, 28 Ambassador, 29 Kia"))
           if n==1:
               data.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==2:
               data.extend([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==3:
               data.extend([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	   
           elif n==4:
               data.extend([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==5:
               data.extend([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==6:
               data.extend([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==7:
               data.extend([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==8:
               data.extend([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==9:
               data.extend([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==10:
               data.extend([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==11:
               data.extend([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==12:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==13:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==14:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==15:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==16:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==17:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
           elif n==18:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
           elif n==19:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
           elif n==20:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])
           elif n==21:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
           elif n==22:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
           elif n==23:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
           elif n==24:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
           elif n==25:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
           elif n==26:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
           elif n==27:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
           elif n==28:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
           else:
               data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

           t=float(input("1 for automatic and 2 for manual"))
           if t==1:
               data.extend([1,0])
           else:
               data.extend([0,1])
           s=float(input("1 for Dealer and 2 for Individual 3 for TrustmarkDealer"))
           if s==1:
               data.extend([1,0,0])
           elif s==2:
               data.extend([0,1,0])
           else:
               data.extend([0,0,1])
           f=float(input("1 for CNG, 2 for Diesel, 3 for Electric , 4 for LPG and 5 for Petrol"))

           if f==1:
               data.extend([1,0,0,0,0])
           elif f==2:
               data.extend([0,1,0,0,0])
           elif f==3:
               data.extend([0,0,1,0,0])
           elif f==4:
               data.extend([0,0,0,1,0])
           else:
               data.extend([0,0,0,0,1])
           
           o=float(input("1 for first owner, 2 for second owner, 3 for third owner, 4 for fourth owner and above and test drive car"))

           if o==1:
               data.extend([1,0,0,0,0])
           elif o==2:
               data.extend([0,1,0,0,0])
           elif o==3:
               data.extend([0,0,1,0,0])
           elif o==4:
               data.extend([0,0,0,1,0])
           else:
               data.extend([0,0,0,0,1])
          
           
                    
              
           
           ans=model.predict([data])
           
           print(ans[0])
else:
        print("model issue")
