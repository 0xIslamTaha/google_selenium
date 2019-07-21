## QA Process:
#### Where would you start? What would be your first steps?
- My testing journey will start with **reviewing the requirements** 
- Collect information about all REST APIs.
- Make sure that there are unit and integration testing cover those APIs. 
- Set the **testing plan** driving from the requirements.  
- Design different **test scenarios** and **test cases**.
- Release the **Traceability Matrix** to make sure that our test cases are covering the requirements.


#### Which process would you establish around testing new functionality? How would you want the features to be tested?
- Testing should start by reviewing the feature requirements.
- Review the related APIs test cases and make sure that the API layer is working as expected.
- Make sure that there are unit tests cover this feature.
- Designing different test cases to test the feature and the impact of this new feature on the whole system from an end-to-end perspective.
- Automate test cases and make sure that the code coverage is greater than 90%.
- Execute those test cases and report bugs and at the end, we need to automate test cases to cover this feature in our test suite. 

#### Which tools would you suggest using to help your team with a daily work?
- OS: Linux
- Programming IDE: Pycharm or VCode
- API Testing: Postman(manual) and Requests(Automation)
- UI Testing: Selenium
- Performance Testing: Locust or Jmeter
- CI: TravisCI or Jenkins
- Version Control: Github
 
 
 #### If you would do a test automation which techniques or best practices would you use the application?
 - Follow a design pattern to make sure that the test suite is maintainable and scalable. I prefer **Page-Object design pattern** for front end testing and **Facade design pattern** for API testing.
- Make sure that all elements are separated in a file away from the code.
- I prefer to use id, name, class etc. more than xpath.
- I suggest to follow the testing pyramid and set most of the test cases in the unit level with cheap cost and less running time.
- I suggest using a separate testing environment.
- CI is important to make sure that there is a running for each commit and PR to catch the bug as soon as possible.

 