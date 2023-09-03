# Email Summarizer

This project provides a desktop notification system that summarizes emails received over the last 12 hours using Python and ChatGPT.

## Features

- Fetches emails from Gmail for the past 12 hours.
- Summarizes the content of emails using ChatGPT.
- Displays summarized content as desktop notifications.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- Gmail API credentials saved as `credentials.json` in the `config/` directory

## Installation & Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/email-summarizer.git
    ```
2. Navigate to the project directory and install the required Python packages:
    ```sh
    cd gmail-summariser
    pip install -r requirements.txt
    ```
3. Set up the Gmail API:
   * Follow the setup steps mentioned in [this section](#setting-up-gmail-api).
   
## Usage
Run the summarizer with:
```sh
python main.py
```

## Setting Up Gmail API
1. Go to the Google Developers Console.
2. Create a new project.
3. Navigate to the "Library" and search for the Gmail API. Enable it.
4. Create OAuth 2.0 credentials. Save the downloaded credentials.json in the config/ directory.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See LICENSE for details.
