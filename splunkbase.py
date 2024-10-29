import sys
import os
import requests


def get_splunkbase_app_url(app_id: str) -> str:
    release_details = f"https://splunkbase.splunk.com/api/v1/app/{app_id}/release"

    try:
        response = requests.get(release_details)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        details = response.json()

        # Check if details is not empty and contains the expected structure
        if details and "name" in details[0]:
            release = details[0]["name"]
            return (
                f"https://splunkbase.splunk.com/app/{app_id}/release/{release}/download"
            )

    except requests.RequestException as e:
        print(f"Error fetching details for Splunkbase app {app_id}")
    except (IndexError, KeyError):
        print(f"Unexpected response structure for Splunkbase app {app_id}")

    return ""


def get_splunkbase_urls(app_ids: list):
    # Use a list comprehension to filter and create the list of URLs
    splunkbase_urls = [
        url
        for app_id in app_ids
        if (url := get_splunkbase_app_url(app_id))  # Call once and assign to url
    ]

    return splunkbase_urls


def process_app_ids(filename: str) -> list:
    """Reads a list of app IDs from a file and returns a list of corresponding Splunkbase download URLs."""
    try:
        with open(filename, "r") as file:
            lines = [
                stripped_line
                for line in file
                if (stripped_line := line.strip())
                and not stripped_line.startswith("#")  # Ignore comments and empty lines
            ]
        return get_splunkbase_urls(lines)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return []  # Return an empty list in case of an error


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(__file__)} <filename>")
        return  # Early return if the usage is incorrect

    filename = sys.argv[1]
    urls = process_app_ids(filename)
    print(*urls, sep=", ")


if __name__ == "__main__":
    main()
