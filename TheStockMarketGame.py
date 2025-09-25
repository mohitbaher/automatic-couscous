import random
import time
import matplotlib.pyplot as plt # type: ignore
import sys
import numpy as np # type: ignore
stocka = 500
stockb = 700
stockc = 350
balance = 7000    # total amount one owns
investment = 0    # total value of investment(i.e. total  value of all shares)
stockaown = 0  # the no of shares one own
stockbown = 0 # the no of shares one own
stockcown = 0 # the no of shares one own
investmenta = 0
investmentb = 0
investmentc = 0
count = 0
stockalist = [500,]
stockblist = [700,]
stockclist = [350,]
for i in range (5):
  stocka = stocka + random.randint(-20, 20)
  stockb = stockb + random.randint(-15,15)
  stockc = stockc + random.randint(-30, 30)
  count += 1
  stockalist.append(stocka)
  stockblist.append(stockb)
  stockclist.append(stockc)
  
  y1points = np.array(stockalist)
  plt.plot(y1points, marker="o", ls = '-', )


  y2points = np.array(stockblist)
  plt.plot(y2points, marker="o", ls = '-')


  y3points = np.array(stockclist)
  plt.plot(y3points,marker="o", ls = '-')

  plt.xlabel("Time")
  plt.ylabel("Stock Value")
  plt.title("Stock Market")
  plt.legend(["Stock A", "Stock B", "Stock C"])

  plt.grid()
  plt.show()

  print()
  print()
  print()
  print(count,"=>", stocka, "...........", stockb, ".............", stockc,"------------", balance, "..............", investment)
  print()


  print("---------START-----------")
  selectstock = input("Enter 'a' for stock a, 'b' for stock b, 'c' for stock c, or 'x' for no trade:-")
  if selectstock == "a":
    selectdecision = input("Enter s for sell and b for buy:-")
    if selectdecision == "b":
      selecttrade = input("type 1  for amount oriented trade or 0 for number oriented trade:-")
      if selecttrade == "0":
        noofstocka = int(input("Enter the number of shares you want to trade:-"))
        if noofstocka*stocka <= balance:
          balance = balance - noofstocka*stocka
          stockaown = stockaown + noofstocka
          investment = investment + noofstocka*stocka
          investmenta = investmenta + noofstocka*stocka
        else:
          print("Insufficient Balance")
      if selecttrade == "1":
        amount = int(input("Enter the amount you want to trade:-"))
        if amount <= balance:
          units = amount//stocka
          balance = balance - units*stocka
          stockaown = stockaown + units
          investment = investment + units*stocka
        else:
          print("Insufficient Balance")
    if selectdecision == "s":
      selldecision = int(input("Enter '1' for amount oriented selling and '0' for number oriented selling:-" ))
      if selldecision == "0":
        noofstocka = int(input("Enter the number of shares you want to sell:-"))
        if noofstocka <= stockaown:
          balance = balance + noofstocka*stocka
          stockaown = stockaown - noofstocka
          investment = investment - noofstocka*stocka
        else:
          print("Insufficient Shares")
      if selldecision == "1":
        amount = int(input("Enter the amount you want to sell:-"))
        units = amount//stocka
        if amount <=investmenta:
          balance = balance + units*stocka
          stockaown = stockaown - units
          investment = investment - units*stocka
          investmenta = investmenta - units*stocka
        else:
          print("Insufficient Investment")
      #-------------------ShereA part ends-----------------------
      
  if selectstock == "b":
    selectdecision = input("Enter s for sell and b for buy:-")
    if selectdecision == "b":
      selecttrade = input("type 1  for amount oriented trade or 0 for number oriented trade:-")
      if selecttrade == "0":
        noofstockb = int(input("Enter the number of shares you want to trade"))
        if noofstockb*stockb <= balance:
          balance = balance - noofstockb*stockb
          stockbown = stockbown + noofstockb
          investment = investment + noofstockb*stockb
          investmentb = investmentb + noofstockb*stockb
        else:
          print("Insufficient Balance")
      if selecttrade == "1":
        amount = int(input("Enter the amount you want to trade:-"))
        if amount <= balance:
          units = amount//stockb
          balance = balance - units*stockb
          stockbown = stockbown + units
          investment = investment + units*stockb
        else:
          print("Insufficient Balance")
    if selectdecision == "s":
      selldecision = int(input("Enter '1' for amount oriented selling and '0' for number oriented selling:-" ))
      if selldecision == "0":
        noofstockb = int(input("Enter the number of shares you want to sell:-"))
        if noofstockb <= stockbown:
          balance = balance + noofstockb*stockb
          stockbown = stockbown - noofstockb
          investment = investment - noofstockb*stockb
        else:
          print("Insufficient Shares")
      if selldecision == "1":
        amount = int(input("Enter the amount you want to sell:-"))
        units = amount//stockb
        if amount <= investmentb:
          balance = balance + units*stockb
          stockbown = stockbown - units
          investment = investment - units*stockb
          investmentb = investmentb - units*stockb
        else:
          print("Insufficient Investment")
      #-----Share B part ENDS----------------------------------

  if selectstock == "c":
    selectdecision = input("Enter s for sell and b for buy:-")
    if selectdecision == "b":
      selecttrade = input("type 1  for amount oriented trade or 0 for number oriented trade:-")
      if selecttrade == "0":
        noofstockc = int(input("Enter the number of shares you want to trade:-"))
        if noofstockc*stockc <= balance:
          balance = balance - noofstockc*stockc
          stockcown = stockcown + noofstockc
          investment = investment + noofstockc*stockc
          investmentc = investmentc + noofstockc*stockc
        else:
          print("Insufficient Balance")
      if selecttrade == "1":
        amount = int(input("Enter the amount you want to trade:-"))
        if amount <= balance:
          units = amount//stockc
          balance = balance - units*stockc
          stockcown = stockcown + units
          investment = investment + units*stockc
        else:
          print("Insufficient Balance")
    if selectdecision == "s":
      selldecision = int(input("Enter '1' for amount oriented selling and '0' for number oriented selling:-" ))
      if selldecision == "0":
        noofstockc = int(input("Enter the number of shares you want to sell:-"))
        if noofstockc <= stockcown:
          balance = balance + noofstockc*stockc
          stockcown = stockcown - noofstockc
          investment = investment - noofstockc*stockc
        else:
          print("Insufficient Shares")
      if selldecision == "1":
        amount = int(input("Enter the amount you want to sell:-"))
        units = amount//stockc
        if amount <=investmentc:
          balance = balance + units*stockc
          stockcown = stockcown - units
          investment = investment - units*stockc
          investmenta = investmentc - units*stockc
        else:
          print("Insufficient Investment")


  #--------Graph code----------

  #------------graph code------------------



#Two  lines to make our compiler able to draw