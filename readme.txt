# Weather CLI

Weather CLI is a command-line application written in Python that retrieves current weather conditions and multi-day forecasts using the Visual Crossing Weather API.

The application supports automatic location detection through the user's public IP address, allows manual city selection, and caches responses locally to reduce unnecessary API requests.

## Features

- Retrieve the current weather for any city.
- Display temperature, humidity, wind speed, and weather conditions.
- Display a weather forecast for a configurable number of days.
- Automatically detect the user's location using their IP address when no city is provided.
- Cache API responses locally for 30 minutes.
- Store the API key securely using a `.env` file.

## Requirements

- Python 3.10 or later
- A Visual Crossing Weather API key

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/weather-cli.git
cd weather-cli
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root directory and add your API key:

```env
API_KEY=your_api_key
```

A free API key can be obtained from the Visual Crossing Weather website.

## Usage

Retrieve weather using your current location:

```bash
python weather.py
```

Retrieve weather for a specific city:

```bash
python weather.py --city Rome
```

Specify the number of forecast days:

```bash
python weather.py --city London --day 5
```

Short option equivalents:

```bash
python weather.py -c Paris -d 7
```

## Project Structure

```
weather-cli/
│
├── cache/
│   └── .cache_<city>.json
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── weather.py
```

## Caching

To minimize API usage, weather data is cached locally inside the `cache` directory.

Cached data remains valid for 30 minutes. After that period, a new request is automatically sent to the API and the cache is updated.

## Dependencies

- requests
- python-dotenv

Generate the `requirements.txt` file with:

```bash
pip freeze > requirements.txt
```

## License

This project is released under the MIT License.