#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=10&category=11&difficulty=medium&type=multiple"

def main():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        for result in data['results']:
            print("Question:", result['question'])
            print("Coreect Answer:", result['correct_answer'])
            print("Incorrect Answers:", result['incorrect_answers'])
            print()

        else:
            print("Failed to fetch data from the API. Status code:", response.status_code)


if __name__ == "__main__":
    main()

