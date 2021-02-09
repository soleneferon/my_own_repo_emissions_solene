# ENE425 Emissions Personal App
Emissions DB collector for ENE425: [Emissions calculator](http://ene425.gabrielfuentes.org/login?next=%2F)

## Section 1: App Development Journal

### WEEK 5 - Task 1: Cloud environment
_The App Developement set up the environment. The Diary Team set up the README structure and project management setup.
The Emissions methodology crew start identifying sources and uploaded to diary when accepted in GitHub environment._

I learned to:
1. Set a cooperative codind environment and manage a project in GitHub
1. Create my logbook/diary setting via README and the important syntax.
Syntax for README edit can be found in this link [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
1. Recognize the most favorable License for my project
1. Deploy a cloud environment for running an app in Heroku
1. Create a DB to feed my app in real time

### WEEK 6 - Task 2: App Structure
_The App Development Team copied and uploaded repository files taken from Gabriel's example repository to structure our own repository. The team also created a directory tree for our repository that is located in this README file.
The diary team updated on the project section and in the README file
The Methodology team kept adding methods to the README file._

I learned to:
1. Upload files or copy files from a repository to my repository
I uploaded and copy the files from [Gabriel's repository](https://github.com/gabrielfuenmar/ene425_emissions_app)
1. Read a directory tree from other developers
1. Create a directory tree for my Emission's app
File Explorer > cmd > tree /a /f > tree.doc
1. Learn what is a fork in Github and what does it do
1. Create a new repository with the emissions app for my own account

### WEEK 7 - Task 3: App design
_The app development team will dive into App Design this week as we start to learn the basics of customizing our Emissions Calculator, we will work on the colors, the text and the favicon inside app.
The diary Group will propose with pics and text in the repo diary what would we adjust design-wise of the app to make it look cooler.
The Methodology Group will keep adding the methods to the diary._

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

### WEEK 9 - Task 5: Emissions calculation methodology (responsible diary)

### WEEK 10 - Task 6: App URL Redirection


## Section 2: Emissions Methodology

### Within this section we are gathering information on emissions calculation method for transport sources:
#### 1) Classification of vehicles (from Gabriel) 

A basic understanding requires having a classification of transport as urban transport or industrial transport (e.g maritime, air).
A more segregated classification of "vehicles" under EC standards can be found at this [Link 1](https://www.eafo.eu/knowledge-center/european-vehicle-categories), which is connected to the last study of ["Determining the environmental impacts of conventional
and alternatively fuelled vehicles through LCA"](https://ec.europa.eu/clima/sites/clima/files/transport/vehicles/docs/2020_study_main_report_en.pdf) by Ricardo Energy and Environment for the European Comission. Our observations o this study is that the segregation is practical for our purpouses, but the methodology is on a higher scale than what we are intending to do with the app (local direct emission per km rather than Life Cycle Analysis (LCA)).


#### 2) Our World in Data

[Link 2](https://ourworldindata.org/grapher/co2-transport-mode?tab=chart&stackMode=absolute&time=latest&country=Domestic%20flight~Eurostar%20(international%20rail)~Medium%20car%20(diesel)~Medium%20car%20(petrol)~Short-haul%20flight%20(economy)~Long-haul%20flight%20(economy)~Motorcycle%20(medium)~National%20rail~Bus~Small%20electric%20vehicle%20(UK%20electricity)&region=World)

Under link we can find CO₂ emissions (in grams per passenger kilometer) by mode of transport, 2018 based on data of UK Department for Business, Energy & Industrial Strategy (BEIS). Different modes of transport can be selected. This can serve as a basis, but can at best be supplemented by data for Norway or more up-to-date data.
        
#### 3) Global footprint Network
[Link 3](https://www.footprintnetwork.org/resources/data/)
        
        
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

