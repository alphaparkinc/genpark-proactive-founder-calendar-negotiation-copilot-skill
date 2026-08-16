from client import ProactiveFounderCalendarNegotiationCopilotClient

def main():
    client = ProactiveFounderCalendarNegotiationCopilotClient()
    invite = "Hey Chris, can we grab 45 mins this Tuesday afternoon to discuss Series A partnership?"
    res = client.negotiate_calendar(invite)
    print(f"Action: {res['scheduling_action']}")
    print(f"Proposed Slot: {res['optimal_time_slot']}")
    print(f"Focus Time Preserved: {res['focus_time_protected_hours']} hrs")

if __name__ == "__main__":
    main()
