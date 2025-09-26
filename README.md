# Paper Publication Checker & Email Notifier (GitHub Actions Enabled)

This project automatically checks whether a target academic paper has been published in a conference proceeding (e.g., 2025) and notifies recipients via email once it is available.  

It combines **web scraping (BeautifulSoup + requests)** with an **automated email sender (SMTP)** and integrates with **GitHub Actions** to run on a schedule without manual execution.

---

## Project Structure

- **`check.py`**  
  - Scrapes the target conference proceeding website: 
  - Searches for a paper with:
    - A specified keyword in the title (e.g., *Learning*)  
    - A target author name  
  - Returns whether the paper is published and its details  

- **`send_email.py`**  
  - Imports `check_author` from `check.py`:
  - Uses Gmail SMTP (SSL) to send notification emails  
  - Reads configuration from environment variables:
    - `EMAIL_USER` – sender Gmail account  
    - `EMAIL_PASS` – Gmail App password  
    - `TO_ADDR` / `TO_ADDR_2` – recipients  
    - `NAME` – target author name  
    - `URL` – conference proceeding page  
  - Defines a `job()` function to:
    1. Check if the target paper is published  
    2. Send email(s) if the condition is met  

- **`requirements.txt`**:
  Required dependencies:
  ```txt
  schedule
  bs4
  requests

- **`main.yml`**:
Runs the send_email.py job on a cron schedule



## USAGE

- Add the following secrets in your GitHub repository settings: EMAIL_USER, EMAIL_PASS, TO_ADDR, TO_ADDR_2, NAME, URL

- The workflow will run automatically on the defined cron schedule by enabling the GitHub Actions
