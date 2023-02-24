#github.com/Digiraft
#List of available cars and their prices
cars={"2023 BMW 7 series":368392,
      "Audi S8":6638382,
      "Mercedes SCLASS":4267872,
      "2023 LAMBORGHINI URUS PERFORMANTE":6773983,
      "2023 Honda accord":652839302,
      "Rivian R1S":6320900,
      "2023 Corvette Z06":42156372,
      "GTR NISMO":673892,
      "Acuara integra":90879557,
       "Nissan 370Z":778278,
       "Mustang GT":986757,
       "Ford F-150":78955357,
       "CT5-V":8754689,
       "ferrari testarossa":789678,
       "Bronco Raptor":4743467,
      "1000hp R34 GTR":98656,
      "Lamboghini Urus":689892972,
      "Shelby F-150 super snake":6872907652,
      "Mitsubishi Pajero":9821778,
      "2023 honda Civic type R":7393028237,
      "2023 Toyata Prius":3322212344221,
      "Audi RS5": 7829732,
      "Toyata crown":8927281,
      "Cadillac escalade":4567687,
      "Durango hellcat":788654,
      "BMW M4 CSL":789865,
      "Audi A4":797439,
      "Audi RS3":683785,
      "Genesis G90":9735266,
      "Acuara integra":90879557,
      "Nissan 370Z":778278,
      "Mustang GT":986757,
      "Ford F-150":78955357,
      "CT5-V":8754689,
      "ferrari testarossa":789678}
#get user input for car name
Car_name=input("Enter a Car_name")
# Check if car name is in the list of available cars
if Car_name in cars:
    print("yes")
    #if car name is present, get its price
    Car_price=cars[Car_name]
    print(f"The price of {Car_name} is ${Car_price}.")
else:
    #if car name is not present, inform the user
    print(f"lo siento,{Car_name} is not available.")