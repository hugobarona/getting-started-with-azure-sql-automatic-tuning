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
- SQLQueryStress - https://apps.microsoft.com/detail/9N46QJ5SBGKB (**in case you want to run your queries locally and avoid additional costs to run your queries using Azure Functions or Azure Automation, you can install and use the app SQLQueryStress on your local environment, configure the database settings and run the desired queries.**

### Deployment Steps

- Run the deployment to create your Azure SQL database

> **Warning**
> This button will only create the Azure SQL database using the sample dataset _AdventureWorksLT_.

Click on the Deploy to Azure button to deploy the Azure resources for the demo.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)]()

- [Enable Automatic Tuning on Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-enable?WT.mc_id=AZ-MVP-5004069)
  You have different ways to enable automatic tuning on your Azure SQL database. Please refer to the link provided above to enable the automatic tuning. By default, automatic tuning is only enabled to force the last good plan to ensure your queries run on your database using the best query plan.


### Cost estimation

Pricing varies per region and usage, so it isn't possible to predict exact costs for your usage. 
However, you can try the [Azure pricing calculator](https://azure.com/e/018606173b374c8e8f7c499dee27b328) for the resources below.
