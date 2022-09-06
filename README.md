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

Several ways: 

1/ what means on workflow dispatch [link_1 on workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
                                   [link_2 on event triggers](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)

2/ How to manually run it [not same UI](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)
