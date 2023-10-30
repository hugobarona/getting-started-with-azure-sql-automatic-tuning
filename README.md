# Getting started with Azure SQL Automatic Tuning

This sample provides a demo to enable you to explore the Azure SQL Automatic Tuning and its capabilities. You can also use it to demo this service to your teams and organization.

## Introduction

Automatic tuning is a fully managed, smart performance service that leverages inherent intelligence to consistently observe and enhance the performance of queries running on your databases. It achieves this by adapting to fluctuating workloads and implementing tuning suggestions in real time. Benefiting from AI, automatic tuning continuously enhances its actions by learning from a collective pool of knowledge gathered from all databases hosted on Azure. The performance of a database improves progressively the more it operates under automatic tuning.

The core principles of Azure SQL automatic tuning are similar to those found in the SQL Server automatic tuning feature within the database engine. For more detailed information on the underlying intelligent mechanisms, please take a look at [SQL Server automatic tuning](https://learn.microsoft.com/en-us/sql/relational-databases/automatic-tuning/automatic-tuning).

If you want to learn more about Azure SQL Automatic Tuning, visit [this link](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview?WT.mc_id=AZ-MVP-5004069).

## What can it do for us?

- **Automated performance tuning of databases**: You can enable the automatic tuning settings to apply the tuning recommendations automatically, so it does not require any manual action.
- **Automated verification of performance gains**: Once the tuning recommendations are applied, the service monitors the performance of your database to ensure there were improvements in its performance.
- **Automated rollback and self-correction**: If no performance improvement is verified, the service reverts the change to the original state to avoid impacting your database's performance.
- **Tuning history**: All actions performed by the service or anyone interacting with the service are logged into the tuning history so anytime you can verify the actions performed against your database.
- **Tuning action Transact-SQL (T-SQL) scripts for manual deployments**: All performance recommendations allow you to download the T-SQL script and apply them manually in your preferred way.
- **Scale-out capability on hundreds of thousands of databases**: By leveraging the automatic tuning service, you can easily scale the number of databases you can monitor and enhance the performance.

## Demo

The idea of this demo is to create an [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database?WT.mc_id=AZ-MVP-5004069) using the sample database _AdventureWorksLT_. Once you have the database, you can install the Azure Data Studio and connect to your created database. Once you can connect to your database, you can run the provided queries in this repository and analyze the query execution plan to assess if the queries that you are going to use and run on your database require optimizations and database tuning. Then, you must decide which way to run your queries: on Azure using Azure Functions or Automation or locally using SQLQueryStress or VS Code. I

![demo-diagram drawio](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/2de6d741-1b7e-46d6-b1a8-a28d337e56ff)

### Prerequisites
To run and test this demo, you must configure and meet the following prerequisites.

- **Azure account**: If you're new to Azure, get an [Azure account for free](https://azure.microsoft.com/free/cognitive-search/), and you'll get some free Azure credits to use with this demo.
- **Azure account permissions**: You must ensure you have enough permissions at the subscription level to deploy the resources in this demo and modify them accordingly.
  - Your Azure account needs _Microsoft.Resources/deployments/write_ permissions on the subscription level.
- Azure Functions extension for VS Code (in case you are using VS Code. Alternatively, you can use Visual Studio and install the extension on the Visual Studio). - **This is only required if you are running your SQL queries using Azure Functions**
  ![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/ef563dec-7583-4af6-86c0-039c73e914cd)
- SQLQueryStress - [https://apps.microsoft.com/detail/9N46QJ5SBGKB](https://apps.microsoft.com/detail/9N46QJ5SBGKB) (**in case you want to run your queries locally and avoid additional costs to run your queries using Azure Functions or Azure Automation, you can install and use the app SQLQueryStress on your local environment, configure the database settings and run the desired queries.**

### Cost estimation

Pricing varies per region and usage, so it isn't possible to predict exact costs for your usage. 
However, you can try the [Azure pricing calculator](https://azure.com/e/018606173b374c8e8f7c499dee27b328) for the resources below.

### Deployment Steps

- Run the deployment to create your Azure SQL database

> **Warning**
> This button will only create the Azure SQL database using the sample dataset _AdventureWorksLT_. Verify the costs of using this service before creating it.

Click the Deploy to Azure button to deploy the Azure resources for the demo.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fhugobarona%2Fgetting-started-with-azure-sql-automatic-tuning%2Fmain%2Finfra%2Fmain.json)

- Configure Azure SQL Server Firewall rules
  You need to configure the firewall rules to whitelist at least your IP address so you can access the database.
  If you are unfamiliar with this configuration, please refer [to this link](https://learn.microsoft.com/en-us/azure/azure-sql/database/secure-database-tutorial?WT.mc_id=AZ-MVP-5004069).
  ![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/e10aa350-815a-49dc-9c03-b78cd6a65339)

- Connect to your Azure SQL database using the Azure Portal
  Once you configure the firewall rules, you can use the Azure Portal to connect to your Azure SQL Database as per the image below.
  ![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/5ae685ee-acba-40c8-910a-1fd622a056ca)

- [Enable Automatic Tuning on Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-enable?WT.mc_id=AZ-MVP-5004069)
  You have different ways to enable automatic tuning on your Azure SQL database. Please refer to the link provided above to enable the automatic tuning. By default, automatic tuning is only enabled to force the last good plan to ensure your queries run on your database using the best query plan.

- Run your queries against your database
   - Run queries using Azure Functions
     If you decide to use an Azure Function to run the queries to your databases for 24+ hours, then you need to perform two steps:
     - [Create an Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal)
       **NOTE: Please ensure that you select the runtime stack as Python and version 3.9.**
     - [Deploy the Azure Function's source code available in this repo to your newly created function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=node-v3%2Cpython-v2%2Cisolated-process&pivots=programming-language-python#republish-project-files)
   - Run queries using SQLQueryStress
     In case you want to run your queries from your local environment, an easy way is to use the SQLQueryStress app, by doing the following steps:
     - [Install the SQLQueryStress app](https://apps.microsoft.com/detail/9N46QJ5SBGKB)
     - Configure the app as per image below. Don't forget to copy the connection details from the Azure SQL database you created.
       Note I am setting a big number for the _number of iterations_ so it can stay running for a couple of days before finalizing all iterations. Also, you can set a delay between queries to wait after completing the current query, before starting the new query.
       In terms of configuring the database settings, you can copy all details from the Azure Portal, by accessing your database's connection strings setting.
        ![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/bd5f3876-faec-4c2a-bc0d-ce7e4bdd1a56)
![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/39fc7e1f-4b25-49ee-8c8a-d72bf8e03d27)

     - Run the queries available in this repo and wait for the results.
       You have different queries you can run to test out different scenarios, but I am going to give you this example so you can get inspired to write your own queries and try out the service. **Note: Keep in mind that the queries you run should be queries that require some optimization/tuning in your database, so the service is able to identify the performance recommendations for those queries.**
 
      Copy content from the _SQLQueries.sql_ file and paste it in SQLQueryStress app and run it.
     **Note: In case you want to run multiple queries at same time, open separate instances of the SQLQueryStress app and configure the queries accordingly.**
       
       In case you are not sure if your query is unoptimized, you can run the query using the _Azure Data Studio _ and enable the query execution plan so you can analyze the plan and the results presented in the plan, as per image below.

       ![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/6beb2668-ad6b-43aa-9f7f-16fbf7e2ffde)


- Verify results
  After running your queries for at least 24 hours continuously, you should see performance recommendations for your database. You need to run your unoptimized queries for a significant time so the AI used by the service is able to learn from it and provide recommendations to improve the performance of your queries and database.

  If you set your automatic tuning settings to **ON** for the _create index_ and _drop index_, then you should see after a while logs on the tuning history showing the actions performed by the service to your database. Those actions will include applying and verifying the recommendations on your database.

  ![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/b77e9bde-262c-4df9-ad2a-953c372f8717)


### Contributing

You are welcome to contribute to this repository. If you find any issues or have suggestions/improvements to provide, please create a Pull request and provide all relevant information.
Additionally, you can connect with me on LinkedIn and report any issues or discuss any suggestions and ideas.

[![Connect with me](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg)](https://www.linkedin.com/in/hugomiguelbarona/)
