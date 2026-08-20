"""
Church Management System (CMS) - Core Classes
A comprehensive Python-based system for managing church operations.
"""

from datetime import datetime
from typing import List, Optional


class Member:
    """Represents a church member."""
    
    def __init__(self, member_id: int, name: str, email: str, phone: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.join_date = datetime.now()
        self.attendance_count = 0
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"
    
    def mark_attendance(self):
        """Record member attendance."""
        self.attendance_count += 1
        return f"{self.name} marked present. Total attendance: {self.attendance_count}"


class Event:
    """Represents a church event or service."""
    
    def __init__(self, event_id: int, title: str, date: str, time: str, location: str):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.attendees: List[Member] = []
        self.created_at = datetime.now()
    
    def __str__(self):
        return f"Event: {self.title} on {self.date} at {self.time}"
    
    def add_attendee(self, member: Member):
        """Add a member to event attendees."""
        if member not in self.attendees:
            self.attendees.append(member)
            return f"{member.name} added to {self.title}"
        return f"{member.name} is already attending"
    
    def get_attendee_count(self) -> int:
        """Get total attendees for this event."""
        return len(self.attendees)


class Church:
    """Represents the main church entity."""
    
    def __init__(self, church_name: str, location: str, pastor_name: str):
        self.church_name = church_name
        self.location = location
        self.pastor_name = pastor_name
        self.members: List[Member] = []
        self.events: List[Event] = []
        self.founded_date = datetime.now()
    
    def __str__(self):
        return f"{self.church_name} - Pastor: {self.pastor_name}"
    
    def add_member(self, member: Member):
        """Add a new member to the church."""
        if member not in self.members:
            self.members.append(member)
            return f"{member.name} has been added as a member"
        return f"{member.name} is already a member"
    
    def create_event(self, event: Event):
        """Create a new church event."""
        self.events.append(event)
        return f"Event '{event.title}' created successfully"
    
    def get_total_members(self) -> int:
        """Get total church members."""
        return len(self.members)
    
    def get_total_events(self) -> int:
        """Get total events."""
        return len(self.events)
    
    def get_member_by_id(self, member_id: int) -> Optional[Member]:
        """Find a member by ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def display_members(self):
        """Display all church members."""
        if not self.members:
            return "No members yet"
        return "\n".join([str(member) for member in self.members])
    
    def display_events(self):
        """Display all events."""
        if not self.events:
            return "No events scheduled"
        return "\n".join([str(event) for event in self.events])


# Welcome message
if __name__ == "__main__":
    print("=" * 50)
    print("🏰 CHURCH MANAGEMENT SYSTEM (CMS) 🏰")
    print("=" * 50)
    print("Welcome to the Church Management System!")
    print("Designed to streamline church operations.")
    print("=" * 50)
