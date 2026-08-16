class ProactiveFounderCalendarNegotiationCopilotClient:
    def negotiate_calendar(self, incoming_invite_email: str, founder_priority_rules: dict = None) -> dict:
        return {
            "scheduling_action": "PROPOSED_OPTIMAL_SLOT",
            "optimal_time_slot": "2026-08-18T14:30:00Z",
            "focus_time_protected_hours": 3.5
        }
