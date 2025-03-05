Part 1: Upload File to UCM
------------------------------------------------------------------------------------------------------------------------------------
Objective: Upload a file to Oracle’s Universal Content Management (UCM) repository so it can be used in further ESS job processing.
Steps:
1.	Prepare File for Upload:
o	Encode your file (e.g., Validate.zip) in Base64 format. This encoded string will go into the payload.
2.	Set Document Parameters:
o	Document Account: This depends on the type of data. For planning data, use "scm$/planningDataLoader$/import$".
o	Content Type: Use "zip" if the file is a .zip.
o	File Name: Name of the file (e.g., Validate.zip).
o	DocumentId: Set to null for initial upload.
3.	Make the Upload API Call:
o	Endpoint: https://elbq-dev2.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05/erpintegrations
o	Method: POST
4.	Request Payload: Replace "DocumentContent" with the Base64 encoded string of your file.
{
  "OperationName": "uploadFileToUCM",
  "DocumentContent": "Base64-encoded-content-of-your-file",
  "DocumentAccount": "scm$/planningDataLoader$/import$",
  "ContentType": "zip",
  "FileName": "Validate.zip",
  "DocumentId": null
}
1.	Get DocumentId from the Response:
o	The response will include a DocumentId for the uploaded file. Note this ID for future steps.
2.	Verify File Upload in Oracle Cloud:
o	Go to File Import and Export in Oracle Cloud.
o	Confirm the file is uploaded by checking the ContentID (use View > Columns > Show All to display all information).
o	Note down this ContentID as it will be used in the ESS job request.
________________________________________
Part 2: Submit ESS Job Request
Objective: Use the uploaded file in a scheduled ESS job to load data from the flat file.
Steps:
1.	Set ESS Job Parameters:
o	JobPackageName: "oracle/apps/ess/scm/advancedPlanning/collection/configuration"
o	JobDefName: "CSVController"
o	ESSParameters: This includes specific arguments, described below.
2.	ESSParameters Breakdown: Replace each parameter in the ESSParameters field as follows:
o	argument1: Source System - e.g., "OPS". Find this under Supply Chain Planning > Plan Input.
o	argument2: Collection Type - use "NET Change" (replace in payload).
o	argument3: Uploaded File Name - the file name, e.g., Validate.zip.
o	argument4: ContentID - obtained from File Import and Export after upload verification.
o	argument5: DocumentId - obtained from the upload response payload.
o	argument6: Source System instance_id - find this ID in the MSC_APPS_INSTANCES table.
3.	Construct the ESS Job Request Payload:
{
  "OperationName": "submitESSJobRequest",
  "JobPackageName": "oracle/apps/ess/scm/advancedPlanning/collection/configuration",
  "JobDefName": "CSVController",
  "ESSParameters": "OPS, 2, Validate.zip, UCMFA02730766, #NULL, 300000000234546, 2, 2, #NULL, 2, 2, 0, 0",
  "ReqstId": null
}
1.	Submit the ESS Job Request:
o	Endpoint: https://elbq-dev2.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05/erpintegrations/submitESSJobRequest
o	Method: POST
2.	Verify Job Submission:
o	The response will contain a ReqstId, which is the ID for the job request. Use this ID to track and confirm the job’s progress.
________________________________________
Quick Reference for Payload Parameters
Parameter	Description	Example
DocumentAccount	Type of data (e.g., "scm$/planningDataLoader$/import$")	"scm$/planningDataLoader$/import$"
ContentType	File type, usually "zip" for ZIP files	"zip"
FileName	Name of the uploaded file	"Validate.zip"
DocumentId	Retrieved from upload response	"2755690"
ContentID	Retrieved from File Import and Export	"UCMFA02730766"
________________________________________
Documentation and Troubleshooting
Refer to Oracle Doc ID 2635805.1 for full troubleshooting guidelines for the Load Planning Data from Flat File process. This document provides detailed instructions for dealing with any errors encountered during the ESS job execution.


