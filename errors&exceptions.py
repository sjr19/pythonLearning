try:
    # Attempt this code, may have error
    result = 10 + '10'
except:
    print("There is an error in adding the two numbers.")
else:
    print("The add worked")
finally:
    print("This line always runs")
