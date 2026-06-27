## Asset 8 — SharePoint feedback forms  
## Form 1 — Resource feedback  
## Title  
Take Control of Your Inbox: Outlook on iPadOS resource feedback  
## Description  
Tell IT Training & Enablement whether this resource was useful, clear and easy to apply on the company-issued iPad.  
Do not include customer, producer, employee or other sensitive information.  
## Questions  
**1. Which resource are you reviewing?**
Choice, required  
* Outlook on iPadOS detailed guide  
* Outlook on iPadOS task map  
* Which Outlook am I using? card  
* iPad quick-fixes card  
* Shared mailbox mini-QRG  
* Copilot troubleshooting card  
* Search, gestures and shortcuts card  
* Demonstration video  
* Other  
**2. Which task or section did you use?**
Short answer  
**3. Were you able to complete the task?**
Choice, required  
* Yes, without help  
* Yes, with some help  
* No  
* I reviewed the information only  
**4. How clear were the instructions?**
Rating 1–5  
**5. How useful were the screenshots or visuals?**
Rating 1–5  
**6. Which input method did you use?**
Choice  
* Touch  
* Magic Keyboard  
* Trackpad  
* More than one  
* Not sure  
**7. Which orientation were you using?**
Choice  
* Landscape  
* Portrait  
* Both  
**8. What was most helpful?**
Long answer  
**9. What was confusing or missing?**
Long answer  
**10. Did an organization-managed setting affect the task?**
Choice  
* Yes  
* No  
* Not sure  
**11. What should be improved?**
Long answer  
**12. May IT Training & Enablement contact you?**
Yes/No  
**13. Contact information**
Show only when Question 12 = Yes  
## Confirmation message  
Thank you for helping us improve Outlook on iPadOS resources. IT Training & Enablement will review your feedback.  
  
## Form 2 — Report outdated instructions  
## Title  
Report outdated Outlook on iPadOS instructions  
## Description  
Use this form when a guide, screenshot, video or job aid no longer matches the company-issued iPad or the steps do not work.  
Remove or blur sensitive information before uploading a screenshot.  
## Questions  
**1. Which resource appears outdated?**
Choice, required  
* Outlook on iPadOS detailed guide  
* Outlook on iPadOS task map  
* Which Outlook am I using? card  
* iPad quick-fixes card  
* Shared mailbox mini-QRG  
* Copilot troubleshooting card  
* Search, gestures and shortcuts card  
* Demonstration video  
* SharePoint resource page  
* Other  
**2. What is the page, section, video or task name?**
Short answer, required  
**3. What type of issue did you find?**
Choice, required  
* Step does not work  
* Button or menu moved  
* Screenshot does not match  
* Feature is missing  
* Gesture behaves differently  
* Keyboard shortcut is incorrect  
* Managed setting blocks the task  
* Shared mailbox behavior differs  
* Copilot behavior differs  
* Link is broken  
* Support contact is incorrect  
* Accessibility issue  
* Other  
**4. What did the instructions tell you to do?**
Long answer, required  
**5. What happened instead?**
Long answer, required  
**6. Which device orientation were you using?**
Choice  
* Landscape  
* Portrait  
* Both  
**7. Which input method were you using?**
Choice  
* Touch  
* Magic Keyboard  
* Trackpad  
* More than one  
**8. Which Outlook account or mailbox type was involved?**
Choice  
* Primary mailbox  
* Shared mailbox  
* Not sure  
**9. What date did you notice the problem?**
Date  
**10. Upload a screenshot**
Optional file upload  
**Screenshot note:**
Remove or blur names, email addresses, customer information, message content, verification codes, device identifiers and account details that are not required.  
**11. How urgent is the issue?**
Choice, required  
* Critical — Instructions could create risk or data loss  
* High — The task cannot be completed  
* Medium — The task is partly incorrect or confusing  
* Low — Minor wording, visual or link issue  
**12. Additional details**
Long answer  
## Confirmation message  
Thank you. IT Training & Enablement will review the issue and update the resource when needed.  
  
## Internal response workflow  
1. Submission received.  
2. Owner reviews severity.  
3. Device, orientation and input method are confirmed.  
4. Outlook and iPadOS versions are recorded.  
5. Jamf or permission impact is reviewed.  
6. Technical validation is completed.  
7. Copy, screenshot, video or link is corrected.  
8. Accessibility is rechecked.  
9. Updated version is approved.  
10. New version is published.  
11. Replaced version is archived.  
12. Submitter is notified when requested.  
13. Version record is updated.  
## Recommended tracking columns  

| Column              | Type           |
| ------------------- | -------------- |
| Submission ID       | Text           |
| Resource            | Choice         |
| Page or task        | Text           |
| Issue type          | Choice         |
| Orientation         | Choice         |
| Input method        | Choice         |
| Mailbox type        | Choice         |
| iPadOS version      | Text           |
| Outlook version     | Text           |
| Managed restriction | Yes/No/Unknown |
| Severity            | Choice         |
| Description         | Multiple lines |
| Owner               | Person         |
| Status              | Choice         |
| Date submitted      | Date           |
| Target resolution   | Date           |
| Resolution          | Multiple lines |
| Corrected version   | Text           |
| Submitter notified  | Yes/No         |
  
**Status values**  
* New  
* Under review  
* Device validation  
* Outlook validation  
* Jamf review  
* Revision in progress  
* Accessibility review  
* Ready to publish  
* Closed  
* No change required

## Deployment status
Forms were not deployed or approved in this repository-only build.
