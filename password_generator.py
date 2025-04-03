#!/usr/bin/env python3
# Password Generator
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Customizable output. Generates random passwords.

import random
import string
import argparse
import logging
import json

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='password_generator.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"charset": string.ascii_letters + string.digits + string.punctuation}

def generate_password(length: int, charset: str) -> str:
    """Generate a random password."""
    try:
        return ''.join(random.choice(charset) for _ in range(length))
    except Exception as e:
        logging.error(f"Password generation failed: {e}")
        return ""

def main():
    """Main function to parse args and generate passwords."""
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("--length", type=int, default=12, help="Password length")
    parser.add_argument("--count", type=int, default=1, help="Number of passwords")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)

    if args.length <= 0 or args.count <= 0:
        logging.error("Length and count must be positive")
        print("Error: Length and count must be positive integers")
        return

    logging.info(f"Generating {args.count} passwords of length {args.length}")
    for i in range(args.count):
        password = generate_password(args.length, config["charset"])
        if password:
            logging.info(f"Generated password {i+1}: {password}")
            print(f"Password {i+1}: {password}")
        else:
            print(f"Error: Failed to generate password {i+1}")

if __name__ == "__main__":
    main()
