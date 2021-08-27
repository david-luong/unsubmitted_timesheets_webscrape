# unsubmitted_timesheets_webscrape

**Harvest Unsubmitted Timesheet Webscraper**

Fun little project of mine 💻

I was trying to find a way to pull a list of unsubmitted timesheets from Harvest 🤔

After looking through the Harvest API V2 Documentation and reaching out to the Harvest Team, I realised this feature was not available yet 😞

For the time being, I have created a small little program that gives you the ability to pull a list of employees who have not submitted their timesheet 😆

Prerequisites:
- Requires 'Harvest Administrative Access' to view Unsubmitted Timesheets.
- .html file name will need to be adjusted according to your organisation in the Python code.

Procedure:
1. Navigate to Harvest
2. Navigate to Time
3. Navigate to Unsubmitted
4. Save page as file with type 'Web Page, HTML Only'
5. Relocate file to same working directory as Unsubmitted_Timesheet.py.
6. Adjust Python Code [line 5] to name of filed saved in Step 4 (e.g. "Timesheet - "Organisation Name" - Harvest.html")
7. Adjust conditions to suit your organisation's employee list (e.g. excluding certain staff/personnel) via IF conditions.
8. Run Python Script.
