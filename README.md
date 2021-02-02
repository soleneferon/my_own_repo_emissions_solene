# ENE425 Emissions Personal App
Emissions DB collector for ENE425

## Emissions Methodology

### Within this section we are gathering information on emissions calculation method for transport sources:
CO2 emissions data 1 (from Gabriel) 
A basic understanding requires having a classification of transport as urban transport or industrial transport (e.g maritime, air).
A more segregated classification of "vehicles" under EC standards can be found at this [link](https://www.eafo.eu/knowledge-center/european-vehicle-categories), which is connected to the last study of ["Determining the environmental impacts of conventional
and alternatively fuelled vehicles through LCA"](https://ec.europa.eu/clima/sites/clima/files/transport/vehicles/docs/2020_study_main_report_en.pdf) by Ricardo Energy and Environment for the European Comission. Our observations o this study is that the segregation is practical for our purpouses, but the methodology is on a higher scale than what we are intending to do with the app (local direct emission per km rather than Life Cycle Analysis (LCA)).


CO2 emissions data 2 (found by another student)
[Here](https://ourworldindata.org/grapher/co2-transport-mode?tab=chart&stackMode=absolute&time=latest&country=Domestic%20flight~Eurostar%20(international%20rail)~Medium%20car%20(diesel)~Medium%20car%20(petrol)~Short-haul%20flight%20(economy)~Long-haul%20flight%20(economy)~Motorcycle%20(medium)~National%20rail~Bus~Small%20electric%20vehicle%20(UK%20electricity)&region=World)
        Under link we can find CO₂ emissions (in grams per passenger kilometer) by mode of transport, 2018 based on data of UK Department for Business, Energy & Industrial Strategy (BEIS). Different modes of transport can be selected. This can serve as a basis, but can at best be supplemented by data for Norway or more up-to-date data.


## Directory Tree:

                
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
