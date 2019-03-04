# py3-caldav-nextcloud-importexport
Script to export and import caldav ics files using the caldav pypi package. Preconfigured for Nextcloud.

Examples:  
- `caldav.py example.com username passw0rd export`  
  Creates a folder `export` with individual ics files for editing or whatever.  
- `caldav.py example.com username passw0rd import`  
  Reads the `export` folder contents and tries to create events and todos from there. Make sure the calendars exist on the target.

You can use the script for non-nextcloud caldav servers, just edit this line appropriately: `cal_url_suf="/remote.php/dav/calendars/"`
