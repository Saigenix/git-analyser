import json


def parse_json(json_str):
    try:
        # Remove markdown formatting and clean up the string
        clean_json = json_str.strip('"""')  # Remove triple quotes
        clean_json = clean_json.replace("```json\n", "")  # Remove ```json
        clean_json = clean_json.replace("\n```\n", "")  # Remove closing ```
        clean_json = clean_json.replace("\\n", "\n")  # Replace \n with actual newlines
        clean_json = clean_json.replace(
            '\\"', '"'
        )  # Replace escaped quotes with regular quotes

        # Parse the cleaned JSON
        parsed_json = json.loads(clean_json)

        # Convert back to a properly formatted JSON string
        formatted_json = json.dumps(parsed_json, indent=2, ensure_ascii=False)

        return formatted_json

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return json_str
    except Exception as e:
        print(f"Error: {e}")
        return json_str
