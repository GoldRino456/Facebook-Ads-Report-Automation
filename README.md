# Facebook Ads Report Automation

## Description
A console application that retrieves Facebook campaign data, exports data into an excel document, and does basic formatting. Search criteria can be tweaked to include or exclude additional fields, limit search to a specified date range, and include multiple ad accounts.

This was created to assist in defining campaign performance metrics, mainly by retriving campaign data in bulk and taking a lot of the headache out of formatting correctly for excel.

Through creating this application, I quickly discovered the Facebook Business SDK for Python (as well as Facebook's API in general) can be rather confusing at first glance (especially for newer developers), so I hope this at the very least helps someone else better understand how to work with Facebook's API. :)

## Getting Started

### Prerequisites
* Ensure Python 3 is installed on your system (3.12 or newer is recommended)
* Install [openpyxl](https://pypi.org/project/openpyxl/) and Facebook Business SDK for Python ([facebook_business](https://github.com/facebook/facebook-python-business-sdk)). Be sure to follow installation instructions for both libraries.
* Register an app on [developers.facebook.com](https://developers.facebook.com) and add the Marketing API to that app
* On [developers.facebook.com](https://developers.facebook.com), grant your app the following permissions and copy the Access Token: ads_read and read_insights. This can be found in the "Tools" of the Marketing API on your app.

### Installing

* Clone the repository: 
   git clone https://github.com/GoldRino456/Facebook-Ads-Report-Automation

   Alternatively, download and extract the ZIP file of the repository from GitHub.

* Set the Access Token and Ad Account ID values in "Main.py". This can be found near the top of the file under "Required Fields".

### Usage

To run the Python application, follow these steps:
* Open Command Line / Terminal.

* Navigate to the project directory:
   ```
   cd your-repository
   ```

* Run the application:
   - On Windows:
     ```
     python Main.py
     ```

   - On Mac and Linux:
     ```
     python3 Main.py
     ```

* The application should now run and display its output in the command line.

## Authors

[Ethan H. Eastwood](https://www.linkedin.com/in/ethan-eastwood-37a994171/)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details