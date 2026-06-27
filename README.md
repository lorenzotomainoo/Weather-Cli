# Weather CLI

Weather CLI is a command-line application written in Python that retrieves current weather conditions and multi-day forecasts using the Visual Crossing Weather API.

The application supports automatic location detection based on the user's public IP address, allows manual city input, and implements local caching to reduce unnecessary API requests.

## Features

- Retrieve current weather data for any city.
- Display temperature, humidity, wind speed, and general weather conditions.
- Retrieve multi-day weather forecasts with configurable duration.
- Automatically detect user location via IP address when no city is provided.
- Cache API responses locally for 30 minutes.
- Secure API key management using a `.env` file.

## Requirements

- Python 3.10 or later
- A Visual Crossing Weather API key

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/weather-cli.git
cd weather-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory and add your API key:

```env
API_KEY=your_api_key
```

An API key can be obtained from the Visual Crossing Weather website.

## Usage

Get weather data using automatic location detection:

```bash
python weather.py
```

Get weather data for a specific city:

```bash
python weather.py --city Rome
```

Specify the number of forecast days:

```bash
python weather.py --city London --day 5
```

Short argument format:

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

To reduce the number of API requests, responses are stored locally inside the `cache` directory.

Cached data remains valid for 30 minutes. After this period, a new request is made and the cache is updated automatically.

## Dependencies

- requests
- python-dotenv

You can generate the requirements file using:

```bash
pip freeze > requirements.txt
```

## License

This project is released under the MIT License.