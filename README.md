# Getting started with Azure SQL Automatic Tuning

This sample provides an example of trying out and demoing the Azure SQL Automatic Tuning to your teams and organization.

## Introduction

Automatic tuning is a fully managed, smart performance service that leverages inherent intelligence to consistently observe and enhance the performance of queries running on your databases. It achieves this by adapting to fluctuating workloads and implementing tuning suggestions in real time. Benefiting from AI, automatic tuning continuously enhances its actions by learning from a collective pool of knowledge gathered from all databases hosted on Azure. The performance of a database improves progressively the more it operates under automatic tuning.

The core principles of Azure SQL automatic tuning are similar to those found in the SQL Server automatic tuning feature within the database engine. For more detailed information on the underlying intelligent mechanisms, please take a look at [SQL Server automatic tuning](https://learn.microsoft.com/en-us/sql/relational-databases/automatic-tuning/automatic-tuning).

## What can it do for us?

- **Automated performance tuning of databases** : You can enable the automatic tuning settings to apply the tuning recommendations automatically, so it does not require any manual action.
- **Automated verification of performance gains**: Once the tuning recommendations are applied, the service monitors the performance of your database to ensure that there was an improvements in its performance.
- **Automated rollback and self-correction**: If no performance improvement is verified, then the service reverts the change to the original state, to avoid impacting your database's performance.
- **Tuning history**: All actions performend by the service or anyone interacting with the service are logged to the tuning history, so anytime you can verify the actions performed against your database.
- **Tuning action Transact-SQL (T-SQL) scripts for manual deployments**: All performance recommendations provide you an option to download the T-SQL script and apply them manually in your prefered way.
- **Scale-out capability on hundreds of thousands of databases**: By leveraging the automatic tuning service, you can easily scale the number of databases you can monitor and enhance the performance.

## Prerequisites
In order to run and test this demo, you need to configure and meet the following prerequisites.

- **Azure account**: If you're new to Azure, get an [Azure account for free](https://azure.microsoft.com/free/cognitive-search/), and you'll get some free Azure credits to use with this demo.
- **Azure account permissions**: You need to ensure you have enough permissions at the subscription level to deploy the resources in this demo and modify them accordingly.
  - Your Azure account needs _Microsoft.Resources/deployments/write_ permissions on the subscription level.
- Azure Functions extension for VS Code (in case you are using VS Code. Alternatively, you can use Visual Studio and install the extension on the Visual Studio). - **This is only required if you are running your SQL queries using Azure Functions**
  ![image](https://github.com/hugobarona/getting-started-with-azure-sql-automatic-tuning/assets/5125006/ef563dec-7583-4af6-86c0-039c73e914cd)

- 
## Deployment


## Cost estimation

Pricing varies per region and usage, so it isn't possible to predict exact costs for your usage. 
However, you can try the [Azure pricing calculator](https://azure.com/e/018606173b374c8e8f7c499dee27b328) for the resources below.
