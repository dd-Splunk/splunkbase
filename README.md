# Splunkbase download URLs script

Create a list of Splunkbase download URLs from a list of application IDs stored in a file.

Based on this [Splunk Community](https://community.splunk.com/t5/Splunk-Enterprise/Is-there-Rest-API-for-splunkbase-to-get-list-of-all-apps-and/m-p/631828) article.

## Usage

```bash
python3 splunkbase.py "file_containing_app_ids"
```

and with the test file `app_list.txt` the ouput of

```bash
 python3 splunkbase.py app_list.txt
```

is:

`https://splunkbase.splunk.com/app/4353/release/1.7.16/download, https://splunkbase.splunk.com/app/833/release/9.2.0/download`

as of Oct 2024.
