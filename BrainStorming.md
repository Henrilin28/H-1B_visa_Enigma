## BrainStroming

There are some intreresting questions come up my mind and I divided them into two parts, which are listed as follows:

Predictive modeling:

- Who will get a H-1B? 

  Even H-1B is randomly selected by the government, the role of job and cmpany still play some roles during the process. Here I want to build a model when you put information related to application to the model and it will return the probability that your application can be certified.

  First and foremost, clean the data but keep missing value in the data. Due to the fact that there are possibility that people submitting missing iuformation. This information should be considereas as inputs as well. Secondly, randomforest model can be used as a classifier for this problem. It will return feature importance for each attributes and return the probability of being certified

  please see further information in Who_will_certified_the _H-1B.ipynb

Exploratory Data Analysis

- Spatial Info visualization:

  spatial information can be visualized  by summarizing the city information. shapely, fiona and geopandas can be used to discover the spatial pattern of the data.

- How long should an employee  work for a  the company

  There are certain deadline for H-1B applications. Through visualizing the application timeline, It can clear show you when is the right time to get the job in case you miss the application this year!

  ​

- What kind of job should international search for? 

  jobs title and SOC code can provide information about what are the top applicants' job are. By using groupy by function. Plot can be easily generate. Moreover, Words can be also visualized by wordcloud.

  ![word_graph](/Users/Henrilin28/Dropbox/CUSP_2016/H-1B_visa_Enigma/word_graph.png)