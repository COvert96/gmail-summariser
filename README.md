# Email Summariser

This project provides a desktop notification system that summarises emails received over the last 12 hours using Python and ChatGPT.

## Features

- Fetches emails from Gmail for the past 12 hours.
    - This can be changed in the config.yaml file.
- Summarises the content of emails using ChatGPT.
- Saves summarised content in 'summaries' folder and sends desktop notification.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10 or higher
- Gmail API credentials saved as `credentials.json` in the `config/` directory

## Installation & Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/email-summariser.git
    ```
2. Navigate to the project directory and install the required Python packages:
    ```sh
    cd gmail-summariser
    pip install -r requirements.txt
    ```
3. Set up the Gmail API:
   * Follow the setup steps mentioned in [this section](#setting-up-gmail-api).
   
## Usage
Run the summariser with:
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
