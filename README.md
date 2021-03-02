# ENE425 Emissions Personal App - MyCapture
My Personal App MyCapture [Link to the app](https://mycapture.herokuapp.com/)

Emissions DB collector for ENE425: [Emissions calculator](http://ene425.gabrielfuentes.org/login?next=%2F)

## Section 1: App Development Journal

### WEEK 5 - Task 1: Cloud environment

I learned to:
1. Set a cooperative coding environment and manage a project in GitHub
1. Create my logbook/diary setting via README and the important syntax.
Syntax for README edit can be found in this link [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
1. Recognize the most favorable License for my project
1. Deploy a cloud environment for running an app in Heroku
1. Create a DB to feed my app in real time

### WEEK 6 - Task 2: App Structure

I learned to:
1. Upload files or copy files from a repository to my repository
I uploaded and copy the files from [Gabriel's repository](https://github.com/gabrielfuenmar/ene425_emissions_app)
1. Read a directory tree from other developers
1. Create a directory tree for my Emission's app
File Explorer > cmd > tree /a /f > tree.doc
1. Learn what is a fork in Github and what does it do
1. Create a new repository with the emissions app for my own account

### WEEK 7 - Task 3: App design

I learned:
1. How the design aligns with the code machinery in Flask
1. Different ways of editing my falsk app design
1. How to change colors and text in my existing app design
Colors standards for html
* RGB. e.g. rgb(0,0,0) is black
  * A fourth digit stands for opacity rgb(R,G,B,a) a from 0.0 to 1.0
* Hex #000000 is also black
  * Opacity in here goes with 2 additional digits at the end. e.g. 00 is 0% and FF is 100% #000000FF
We can find nice color mixes on this website: [Coolors](https://coolors.co/)

### WEEK 8 - Task 4: App deployment
I learned 
1. To sync a database in Heroku
1. To sync my Github repository with a cloud machinery
1. To definie my environmental variables and use it as a first stage security measure
We used a key to point directly to a hidden value. It is not the safest but the easiest (common practice)
1. Heroku basic function


#### Week questions

##### Question 1: What other cloud service can be used to deploy apps from github repositories?



##### Question 2: What option would you consider to make your app safer against attacks (abusive requests that could crash your server, passford theft, ...)?




### WEEK 9 - Task 5: Emissions calculation methodology (responsible diary)
I learned 

1. Mathematical operators in Python
2. Select methodology for my app
3. Criteria for selecting a method that feeds an app

#### Week questions

##### Question 1: What other input values would you use to improve your calculations?

1. Brand, age, size and weight of the mean of transport
2. Number of passengers
3. Car maintenance
4. How it is driven (speed, idling, starting and stopping, acceleration, braking)
5. Energy mix of specific country
6. Connect the app to GPS services
7. Include other greenhouse gasses in the calculators (“CO2 equivalents”)
8. Include CO2 produced indirectly, for example during the manufacturing or disposal of a car

##### Question 2: How would you get them?
1. International Energy Agency and other institutions
1. Scientific papers
1. Cooperation with service providers (for example map services)

### WEEK 10 - Task 6: App URL Redirection

I learned to 
1. get a domain and a web host provider
2. sync your app to your domain URL
        
## Section 2: Different methodologies to calculate CO2 emissions

### List of different methodologies we can use:

1. Methods for calculating the emissions of transport in the Netherlands: [Link to paper](https://english.rvo.nl/sites/default/files/2018/04/Klein-et-al-2018-%20Methods-for-calculating-emissions-transport-Netherlands-2018.pdf)
- actuality of the data / covered time period:
  - 2018
- country of origin:
  - Netherlands (Statistics Netherlands / PBL Netherlands Environmental Assessment Agency / TNO / RWS Water, Transport and Environment (WVL))
- This report covers the methodologies used for calculating both the greenhouse gas emissions and the emissions of air pollutants by mobile sources in the Netherlands. This report only covers emissions to air. Mobile sources include:
  - Road transportation
  - Railways
  - Civil aviation
  - Inland navigation
  - Maritime navigation
  - Fisheries
  - Non-Road Mobile Machinery
  - Military shipping and aviation
- For each source category, various processes are distinguished that result in emissions of greenhouse gases and air pollutants:
  - Combustion of motor fuels for propulsion;
  - Evaporation of motor fuels from the fuel system of vehicles;
  - Wear of tyres, brake linings and road surfaces;
  - Leakage and consumption of motor oil;
  - Wear of overhead contact lines and carbon brushes on trains, trams and metros;
  - Support systems on board ships (heating, electricity generation, refrigeration and pumping).
- Recommendation/assessment: detailed formulas to calculate the greehouse gas emissions per mobile sources can be found in the report. Data is specific to the Netherlands. There is a risk that one may not be able to find the same data for Norway given the granularity of the data. 

2. This document presents a general methodology developed for estimating the amount of
carbon emissions (CO2) generated by a passenger in a flight: [Link to paper](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v11-2018.pdf).
General methodology (ICAO - International Civil Aviation Organization, June 2018):
- input the airports of origin and destination for a direct flight
- compare with the published scheduled flights to obtain the aircraft types used to serve the two airports concerned and the number of departures per aircraft
- associate fuel consumption based on the aircraft type and the distance
- calculate the average fuel consumption for the journey weighted by the frequency of departure of each equivalent aircraft type
- divide by the total number of economy class equivalent passengers, giving an average fuel burn per economy class passenger
- multiply by 3.16 in order to obtain the amount of CO2 footprint attributed to each passenger travelling between those two airports.

<img src="notes/ICAO flight calculation.PNG" width="500" height="300"/>

Formula : CO2 per pax = 3.16 * (total fuel * pax-to-freight factor)/(number of y-seats * pax load factor)

3. How to calculate CO2 emissions from fuel consumption (typical fuels used in cars and busses): [Link to website](https://ecoscore.be/en/info/ecoscore/co2)
  - website provides information onyl for diesel, petrol, CNG and LPG and uses very basic assumptions without any differentiation between typ and size of vehicle and similiar aspects
  - recommendation/assessment: the information are not valuable for our project --> use of another method

4. CO2 emissions data UK
[Here](https://ourworldindata.org/grapher/co2-transport-mode?tab=chart&stackMode=absolute&time=latest&country=Domestic%20flight~Eurostar%20(international%20rail)~Medium%20car%20(diesel)~Medium%20car%20(petrol)~Short-haul%20flight%20(economy)~Long-haul%20flight%20(economy)~Motorcycle%20(medium)~National%20rail~Bus~Small%20electric%20vehicle%20(UK%20electricity)&region=World) Under link we can find CO₂ emissions (in grams per passenger kilometer) by mode of transport, 2018 based on data of UK Department for Business, Energy & Industrial Strategy (BEIS). Different modes of transport can be selected. This can serve as a basis, but can at best be supplemented by data for Norway or more up-to-date data.

The updated conversation factors and detailed methdology for 2020 can be found [Here](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2020) --> methodology file: "Conversion factors 2020: methodology"; conversation factors spreadsheet: "Conversion factors 2020: flat file (for automatic processing only)"

- actuality of the data / covered time period: 
  - June 2020, latest data included, application preferable for activties within 2020 
- country of origin: 
  - UK, Department for Business, Energy & Industrial Strategy (BEIS)
- GHG conversation factors:
  - Values for the non-carbon dioxide (CO2) GHGs, methane (CH4) and nitrous oxide (N2O), are presented as CO2 equivalents (CO2e), using Global Warming Potential (GWP) factors from the Intergovernmental Panel on Climate Change (IPCC)’s fourth assessment report (GWP for CH4 = 25, GWP for N2O = 298), consistent with United Nations Framework Convention on Climate Change (UNFCCC)
  - detailed explanations for each mean of transport
- means of transport:
  - Car Petrol (mini, supermini, lower medium , upper medium, executive, luxury saloon, specialist sport, dual purpose, multi purpose; period 2003-2019) 
  - Car Diesel (mini, supermini, lower medium , upper medium, executive, luxury saloon, specialist sport, dual purpose, multi purpose; period 2003-2019) 
  - Car Unknown Fuel (Diesel + Petrol) (mini, supermini, lower medium , upper medium, executive, luxury saloon, specialist sport, dual purpose, multi purpose; period 2003-2019)
  - Car Battery Electric Vehicle (BEV) (mini, supermini, lower medium , upper medium, executive, luxury saloon, specialist sport, dual purpose, multi purpose; all until 2018)
  - Car Plug-in Hybrid Electric (PHEV) (mini, supermini, lower medium , upper medium, executive, luxury saloon, specialist sport, dual purpose, multi purpose; all until 2018)
  - van Petrol (Class 1, Class 2, Class 3; period 2012-2018)
  - Van Diesel (Class 1, Class 2, Class 3; period 2012-2018)
  - van LPG (Class 1, Class 2, Class 3; period 2012-2018)
  - van CNG (Class 1, Class 2, Class 3; period 2012-2018)
  - Taxis (average passenger occupancy of 1.5; period 2007)
  - Motorbike (small, medium, large, period
  - Buses (local (not London), local London, long-distance)
  - Passenger rail (international rail, national rail, light rail, tram, underground)
  - passenger air transport (domestic, short-haul, long-haul)
  - ferries (passenger with and without car)
- energy mix of the country respectively
  - no information here
- Specialities:
  - uplift factor is applied to car conversion factors to approach gap between regulatory test and real-world estimates for CO2/km
  - conversation factors for BEV are dependend on UK electricity conversation factors --> we should, if possible, consider the Norwegian energy mix in our final method
  - calculations are specific for UK (based on registrations, averages passengers on board, ...)

5. Norway data of alternative fuels vehicles [Here](https://www.eafo.eu/countries/Norway/1747/summary)
The European Alternative Fuel Observatory (EAFO) provides detailed information from 2008 to 2020 about the different mode of transport using electricity, hydrogen, LPG or natural gas such as fleet, market share, infrastructures. We can fin data for every european states.

- level of detail: Mostly aggregate data on fleet and fuel type. Infrastructure, e.g., charging points,
Electricity, Hydrogen, LPG, Natural Gas
- means of transport: Passenger cars, light electric vehicles, buses, light commercial vehicles, heavy duty
- Country of origin: EU, the site can compare countries.
- Time period: 2008 to 2020
- information on infrastructure and types of vehicles might be interesting. e.g., M2+M3 (buses), and N1 (light commercial vehicles). Site also includes incentives of legislation such as financial benefits for electric vehicles. The souce isn't really that relevant for methodology

6. Information about Norway's energy mix [Here](https://www.iea.org/countries/norway)

IEA has very comprehensive data on energy mix, energy balance, energy sources and CO2 emissions by sector, product, source etc. IEA provides solutions and proprietary frameworks for energy and carbon tracking, but unfortunately, other than a user guide and a free demo, its very expensive to access. A lot of the complete data sets, e.g., "CO2 Emissions From Fuel Consumption" are also paywalled, but the free "highlights" document appears to be very detailed and sufficient for our use.

- level of detail: virtually endless. Best data is from the 30 member countries, but there is data for approximately 9/10 countries in the world. Data set includes e.g.,: CO2 emissions by sector and product, energy-related socio-economic indicators, total energy supply by source and product, drivers of CO2 emissions, end-use energy consumption by sector, Energy sources share of power generation. Data for vehicle and technology types, transport consumption, fuel consumption, carbon intensity, transport energy by products, sector type etc.
-  country of origin: Global data
-  actuality of data: Variyng, but in most cases fully up to date

7. The Norwegian Ministry of Climate and Environment has made this overview of emissions https://www.miljodirektoratet.no/tjenester/klimagassutslipp-kommuner/?area=618&sector=-2sorted. It contains the emissions per use within a lot of different categories (including transport) in Norway. It is also quite interesting to see the development of emissions per km over the last ten years. The downside is that the page is in Norwegian.

8. Calculations of carbon emissions of passenger cars based on travel characteristics in China https://iopscience.iop.org/article/10.1088/1755-1315/227/6/062001/pdf.
  - Means of transport: passenger cars (low level of detail, except case study from Harbin)
  - Country of origin: China
  - Energy mix of country respectively: not specified (but acknowledge China's issues regarding fast increase in carbon emissions)
  - Article and research from 2019 (high actuality)

Recommendation: Use of method number one and/or four but including the information on Norway energy mix (method 6) since the other methods are for UK or the Netherlands respectively.

### Criteria for calculation method

- means of transport 
  - level of detail (e.g. car: combustion engine, hybrid, electrical)
- country of origin
- energy mix of the country respectively
- actuality of the data / covered time period
- GHG conversation factors
- ...




1. A basic understanding requires having a classification of transport as urban transport or industrial transport (e.g maritime, air).
A more segregated classification of "vehicles" under EC standards can be found at this [Link 1](https://www.eafo.eu/knowledge-center/european-vehicle-categories), which is connected to the last study of ["Determining the environmental impacts of conventional
and alternatively fuelled vehicles through LCA"](https://ec.europa.eu/clima/sites/clima/files/transport/vehicles/docs/2020_study_main_report_en.pdf) by Ricardo Energy and Environment for the European Comission. Our observations o this study is that the segregation is practical for our purpouses, but the methodology is on a higher scale than what we are intending to do with the app (local direct emission per km rather than Life Cycle Analysis (LCA)).

2. Global footprint Network
[Link 3](https://www.footprintnetwork.org/resources/data/)

3. Methods for calculating the emissions of transport in the Netherlands: [Link to paper](https://english.rvo.nl/sites/default/files/2018/04/Klein-et-al-2018-%20Methods-for-calculating-emissions-transport-Netherlands-2018.pdf)

4. This document presents a general methodology developed for estimating the amount of
carbon emissions (CO2) generated by a passenger in a flight: [Link to paper](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v11-2018.pdf)

5. How to calculate CO2 emissions from fuel consumption (typical fuels used in cars and busses): [Link to website](https://ecoscore.be/en/info/ecoscore/co2)

6. CO2 emissions data
[Here](https://ourworldindata.org/grapher/co2-transport-mode?tab=chart&stackMode=absolute&time=latest&country=Domestic%20flight~Eurostar%20(international%20rail)~Medium%20car%20(diesel)~Medium%20car%20(petrol)~Short-haul%20flight%20(economy)~Long-haul%20flight%20(economy)~Motorcycle%20(medium)~National%20rail~Bus~Small%20electric%20vehicle%20(UK%20electricity)&region=World) Under link we can find CO₂ emissions (in grams per passenger kilometer) by mode of transport, 2018 based on data of UK Department for Business, Energy & Industrial Strategy (BEIS). Different modes of transport can be selected. This can serve as a basis, but can at best be supplemented by data for Norway or more up-to-date data.

## Section 3: Directory Tree

                
                +--- Emissions_App
                |   app.py
                |   LICENSE
                |   Procfile
                |   python-app.yml
                |   requirements.txt
                |   tree_output.doc
                |   
                +---notes
                |       .gitkeep
                |       module_design_v2.png
                |       
                +---static
                |       favicon.png
                |       
                \---templates
                        add_record.html
                        edit_or_delete.html
                        error.html

