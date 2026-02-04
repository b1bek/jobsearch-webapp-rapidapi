# Job Search Web App

A Flask web application for searching jobs using the JSearch API from RapidAPI.

## Features

- Search jobs by keyword and location
- Filter by date posted, remote jobs, and employment type
- View detailed job information
- Salary estimation tool

## Requirements

- Python 3.14+
- RapidAPI Key (JSearch API)

## Installation

1. Clone the repository

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Add your RapidAPI key to `.env`:
   ```
   RAPIDAPI_KEY=your_rapidapi_key_here
   ```

## Usage

Run the application:
```bash
uv run main.py
```

The app will be available at `http://localhost:5001`

## Tech Stack

- Flask
- JSearch API (RapidAPI)
- Python-dotenv
- Requests
