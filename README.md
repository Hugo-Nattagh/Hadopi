# HADOPI

### Data visualization - A closer look at the efficiency of the french anti-piracy law

I wanted to see what is the efficiency of the HADOPI law, knowing its cost each year.  
The official data representations are nice, but I felt like another point of view could be helpful.  
I wrote an [article] (in french) for more details.

#### What's going on

I used **matplotlib** for the time series charts.  
I reproduced the inverted triangle charts with a proportional scale.
To do so, I used **Inkscape**.

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

#### The data

I got the data from the [government](https://www.data.gouv.fr/fr/search/?q=hadopi).  
For the law budget, I created a dataframe from the data found in [Numerama](https://www.numerama.com/politique/167402-budget-hadopi.html) and [EconomieMatin](http://www.economiematin.fr/news-hadopi-telechargement-illegal-rapport-activite-riposte-graduee-echec-cout-argent)


#### Files Description

- `hadopi.py`: Script to get the charts
- `hadopi_chiffres_bruts.csv`: Original main dataset
- `hadopi_chiffres_bruts2.csv`: Main dataset after minor changes
- `HADOPI_Bulletin_information_trimestriel_Mars_2018.pdf`: Information pdf file from the official HADOPI website
