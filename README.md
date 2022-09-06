# GH-Actions_INFA_basic_pipeline

[Instructions](https://knowledge.informatica.com/s/article/Automated-Deployment-of-IICS-Assets-CI-CD-using-Informatica-API-s?language=en_US) I'm trying to repeat

How it functions as of 05/09/2022: 

1. User makes changes in INFA UI DEV

2. User commits changes to GitHub

3. Even without workflow, from GitHub we can merge from DEV to UAT

4. From INFA UI UAT user makes Pull, and confirms connections

As of 06/09/2022: 

It logs in with secrets from GHA

PB: it requires commit sha

# TO DO : 

What means on workflow dispatch 

1/ [Workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)

2/ [Event triggers](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)

3/ How to manually run workflows [not same UI](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)

4/ INFA API docs

5/ postman didn't work with v3 API. Versions have different functionalities
