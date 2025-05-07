# a2a_gateway_cli.py

import argparse
import json
import requests
import os

BASE_URL = os.getenv("A2A_GATEWAY_URL", "http://localhost:8000")

def publish_agent(agent_card_path):
    try:
        with open(agent_card_path, 'r') as f:
            agent_card = json.load(f)
        response = requests.post(f"{BASE_URL}/register", json=agent_card)
        response.raise_for_status()
        print("✅ Agent published successfully:", response.json())
    except Exception as e:
        print("❌ Failed to publish agent:", e)

def send_task(agent_id, input_data):
    try:
        payload = {
            "agent_id": agent_id,
            "input": input_data
        }
        response = requests.post(f"{BASE_URL}/task", json=payload)
        response.raise_for_status()
        print("🛰️ Task sent successfully:", response.json())
    except Exception as e:
        print("❌ Failed to send task:", e)

def check_status(task_id):
    try:
        response = requests.get(f"{BASE_URL}/status/{task_id}")
        response.raise_for_status()
        print("📊 Task status:", response.json())
    except Exception as e:
        print("❌ Failed to check task status:", e)

def main():
    parser = argparse.ArgumentParser(description="A2A Gateway CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # publish
    publish_parser = subparsers.add_parser("publish", help="Publish an agent card")
    publish_parser.add_argument("--file", required=True, help="Path to agent_card.json")

    # task
    task_parser = subparsers.add_parser("task", help="Send a task to an agent")
    task_parser.add_argument("--to", required=True, help="Agent ID")
    task_parser.add_argument("--input", required=True, help="Input string")

    # status
    status_parser = subparsers.add_parser("status", help="Check task status")
    status_parser.add_argument("--id", required=True, help="Task ID")

    args = parser.parse_args()

    if args.command == "publish":
        publish_agent(args.file)
    elif args.command == "task":
        send_task(args.to, args.input)
    elif args.command == "status":
        check_status(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
