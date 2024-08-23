# Automibile Data Analysis
## (By Alonge Daniel)


- GitHub: [Alonge 9500](https://github.com/Alonge9500)
- LinkedIn: [Alonge Daniel](https://www.linkedin.com/in/alonge-daniel-27b4b4139/)
- Email: [Alonge Daniel](mailto:alongedaniel19@gmail.com)

I' will appreciate any comment and correction on this work 

![alt text](https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGNhcnN8ZW58MHx8MHx8&w=1000&q=80)
[Image Source:unsplach.com](https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGNhcnN8ZW58MHx8MHx8&w=1000&q=80)
### Objective
The main objective of the project is to analysis the automobile and predict the price of cars base on some specific features

### Installations
Run the code bellow to install the mlxtend which might not come with anaconda by default
> pip install mlxtend


### Methods
* Data Cleaning
* Data Visualization
* Inferential Statistics 
* Machine Learning(LinearRegression)
* Web Development (Web App)

### Technologies
* Python
* Jupyter
* Pandas
* Sklearn
* Flask
* E.t.c

### Project Description 
* [Source of dataset: UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Automobile)
* Carry out some few visualization and draw insights from the dataset
    *Counts of categorical features
    *Relation between categorical features and price
    *Correlation between numerical features using heatmap
    
* Formulate and accept or reject at least a single hypothesis
    *Null Hypothesis: There's no relation between the number of doors a car has and the body style
    *Accept or reject hypothesis using Chi2_contigency
    
* Select the best 10 features relating to price using sequential forward selection in sklearn
    *The top 10 features are 'width', 'height', 'curb_weight', 'engine_size', 'highway_mpg', 'make', 'body_style', 'drive_wheels', 'engine_location', 'engine_type'
    
* Create a LinearRegression model base on the 10 features selected and evaluate with R2 score
* Create a simple flask web app for the deployment of the model
    *Create a single page web page 
    *Collect users car features and return their predicted price

