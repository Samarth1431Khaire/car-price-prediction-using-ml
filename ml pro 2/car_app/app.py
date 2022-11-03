from flask import Flask, render_template, request, url_for, redirect, session
from sqlite3 import*

import pickle
app=Flask(__name__)
app.secret_key="hello brother"



@app.route("/", methods=["GET","POST"])
def home():
  if "un" in session:
        
      if request.method=="POST":
         if request.form['action']=="Show Price":
                 f=None
                 model=None
                 try:
                      f=open("car.model", "rb")
                      model=pickle.load(f)
                 except Exception as e:
                       msg="f issue" + str(e)
                       return render_template("home.html", msg=msg)
                 finally:
                       if f is not None:
                               f.close()
                 if model is not None:
                       k=float(request.form["k"])
                       y=float(request.form["y"])
                       data=[k,y]

                       n=float(request.form["n"])
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

                       t=float(request.form["t"])
                       if t==1:
                              data.extend([1,0])
                       else:
                              data.extend([0,1])

                       s=float(request.form["s"])
                       if s==1:
                               data.extend([1,0,0])
                       elif s==2:
                               data.extend([0,1,0])
                       else:
                               data.extend([0,0,1])

                       f=float(request.form["f"])
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
                       
                       o=float(request.form["o"])

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
                       msg="Price Of Car is" +" "+u'\u20B9'+str(round(ans[0],2))
                       return render_template("home.html", msg=msg)
                 else:
                       return render_template("home.html", msg="model issue")
         elif request.form['action']=="Logout":
                  session.pop('un', None)
                  return redirect(url_for('login'))
                  
         else:
                  return render_template("home.html")
                  
                  
      else:
               return render_template("home.html")
  else:
          return redirect(url_for('login'))
 

 
              

@app.route("/signup",methods=["GET","POST"])
def signup():
      if "un" in session:
             return redirect(url_for('home'))
      
      if request.method=="POST":
               un=request.form["un"]
               pw1=request.form["pw1"] 
               pw2=request.form["pw2"]
               if pw1==pw2:
                      con=None
                      try:
                           con=connect("sam.db")
                           cursor=con.cursor()
                           sql="insert into users values('%s','%s')"
                           cursor.execute(sql%(un,pw1))
                           con.commit()
                           return redirect(url_for('login'))

                      except Exception as e:
                             con.rollback()
                             return render_template("signup.html", msg="user already exits" + str(e))
                      finally:
                              if con is not None:
                                      con.close()
               else:
                    return render_template("signup.html", msg="passwords did not match")

      else:
             return render_template("signup.html")

@app.route("/login",methods=["GET","POST"])
def login():
       if "un" in session:
             return redirect(url_for('home'))
      
       if request.method=="POST":
               un=request.form["un"]
               pw=request.form["pw"] 
               con=None
               try:
                        con=connect("sam.db")
                        cursor=con.cursor()
                        sql="select * from users where username='%s' and password='%s'"

                        cursor.execute(sql % (un,pw))
                        data=cursor.fetchall()
                        if len(data)==0:
                              return render_template("login.html", msg="invalid login")
                        else:
                             session["un"]=un
                             return redirect(url_for('home'))
               except Exception as e:
                           return render_template("login.html", msg=str(e))
               finally:
                          if con is not None:
                              con.close()
       else:
               return render_template("login.html")

@app.route("/readme", methods=["GET","POST"])
def readme():
        if "un" in session:
             return redirect(url_for('home'))

        return render_template("readme.html")
     
  
     

@app.errorhandler(404)
def not_found(e):
        return redirect(url_for('login'))



if __name__=="__main__":
        app.run(debug=True, use_reloader=True)