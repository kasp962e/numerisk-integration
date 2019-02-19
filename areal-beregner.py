import math
import matplotlib.pyplot as plt
def venstre_sum(a,b,n,func): #a = starting point, b = end point, n = intervals
    returnlist = []
    h = (b-a)/n #Interval length.
    #Lists for plotting
    xs = []
    ys = []
    for i in range(n):
        x = h*i+a #"Rotating" x
        xs.append(x)
        y = h*eval(func) #Area of each interval/pillar
        ys.append(y)
        returnlist.append(y)
    #Plot area-bars for used method, if amount of interval is less than 101.
    if n < 101:
        widths = [h for i in range(n)]
        xbars = [x+0.5*h for x in xs]
        ybars = [y for y in ys]
        plt.bar(xbars,ybars,width=widths,color = 'green',label = "area under function")
    #Make the graph extend beyond the pillars:
    x = h*n+a
    xs.append(x)
    y = h*eval(func)
    ys.append(y)
    #Plot the graph
    plt.plot(xs,ys,ls = 'solid',label = (func,"venstre-sum"))
    plt.plot(xs,ys,'b*',label = ("x,y cords"))
    plt.legend(loc = "best")
    plt.show()
    return sum(returnlist)


def hoejre_sum(a,b,n,func): #a = starting point, b = end point, n = intervals
    returnlist = []
    h = (b-a)/n #Interval length.
    #Lists for plotting
    xs = []
    ys = []
    for i in range(n):
        x = h*i+a+h #"Rotating" x
        print(x)
        xs.append(x)
        y = h*eval(func) #Area of each interval/pillar
        ys.append(y)
        print("y",y)
        returnlist.append(y)
    #Plot area-bars for used method, if amount of interval is less than 101.
    if n < 101:
        widths = [h for i in range(n)]
        xbars = [x-0.5*h for x in xs]
        ybars = [y for y in ys]
        plt.bar(xbars,ybars,width=widths,color = 'green',label = "area under function")
    #Make the graph extend beyond the pillars:
    x = h*n+a
    xs.append(x)
    y = h*eval(func)
    ys.append(y)
    #Plot the graph
    plt.plot(xs,ys,ls = 'solid',label = (func,"højre-sum"))
    plt.plot(xs,ys,'b*',label = ("x,y cords"))
    plt.legend(loc = "best")
    plt.show()
    return sum(returnlist)


def trapez(a,b,n,func): #a = starting point, b = end point, n = intervals
    returnv  = (venstre_sum(a,b,n,func)+hoejre_sum(a,b,n,func))/2
    return returnv


def midtsum(a,b,n,func): #a = starting point, b = end point, n = intervals
    returnlist = []
    #Lists for plotting
    xs = []
    ys = []
    h = (b-a)/n #Interval length.
    for i in range(n):
        x = h*(i+0.5)+a #"Rotating" x
        xs.append(x)
        y = h*eval(func) #Area of each interval/pillar
        ys.append(y)
        returnlist.append(y)
    #Plot area-bars for used method, if amount of interval is less than 101.
    if n < 101:
        widths = [h for i in range(n)]
        xbars = [x*h for x in xs]
        ybars = [y for y in ys]
        plt.bar(xbars,ybars,width=widths,color = 'green',label = "area under function")
    #Make the graph extend beyond the pillars:
    x = h*(n+0.5)+a
    xs.append(x)
    y = h*eval(func)
    ys.append(y)
    print(xs)
    print(ys)
    #Plot the graph
    plt.plot(xs,ys,ls = 'solid',label = (func,"midt-sum"))
    plt.plot(xs,ys,'b*',label = ("x,y cords"))
    plt.legend(loc = "best")
    plt.show()
    return sum(returnlist)



while True:
    state = input("Which method would you like to use? (v,h,t,m)")
    if state == "break":
        break
    f = (input("Give the function: ")) #Function as input
    ranges1 = int(input("Give a x0:")) #Start-point
    ranges2 = int(input("Give a xn:")) #End point
    inv = int(input("Amount of intervals:")) #Amount of intervals

    if state == "v":
        print("###########VENSTRESUMS-RESULTAT:")
        print(inv,"intervaller",f,"A=",venstre_sum(ranges1,ranges2,inv,f))

    elif state == "h":
        print("###########HØJRESUMS-RESULTAT:")
        print(inv,"intervaller",f,"A=",hoejre_sum(ranges1,ranges2,inv,f))


    elif state == "t":
        print("###########TRAPEZ-RESULTAT:")
        print(inv,"intervaller",f,"A=",trapez(ranges1,ranges2,inv,f))


    elif state == "m":
        print("###########MIDTSUMS-RESULTATER:")
        print(inv,"intervaller",f,"A=",midtsum(ranges1,ranges2,inv,f))
