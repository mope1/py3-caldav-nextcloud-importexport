# py3-caldav-nextcloud-importexport
Minimal script to export and import caldav ics files using the caldav pypi package. Preconfigured for Nextcloud. **I think it has some minor bugs, don't trust it blindly!**

Examples:  
- `caldav.py example.com username passw0rd export`  
  Creates a folder `export` with individual ics files for editing or whatever.  
- `caldav.py example.com username passw0rd import`  
  Reads the `export` folder contents and tries to create events and todos from there. Make sure the calendars exist on the target. Does not override existing entries.

You should be able to use the script for non-nextcloud caldav servers, just edit the `cal_url_suf` variable in the script.
