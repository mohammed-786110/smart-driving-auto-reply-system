Smart Driving Mode Auto-Response System
Overview

This project is a context-aware communication system that automatically handles incoming WhatsApp messages when the user is in driving mode.

It reduces the need for manual phone interaction by detecting messages, processing them through a backend system, and sending appropriate replies.

Problem Statement

Using mobile phones while driving is a major cause of distraction and can lead to unsafe situations.

Most existing solutions either:

Block notifications completely, or
Provide basic auto-replies without context

There is a need for a system that can manage communication intelligently without interrupting the driver.

Solution:

The system integrates:

Selenium automation to interact with WhatsApp Web
Django backend for decision-making
Google Gemini API for generating smart replies

It detects incoming messages and responds automatically based on:

Driving status
Contact type (family, others)
Context (AI-generated replies)


Key Features:
Automatic detection of incoming messages
Driving mode activation
Personalized auto-replies
AI-based response generation (Gemini)
Anti-spam mechanism (cooldown system)
Message-based duplicate filtering
Real-time automation



System Architecture:
WhatsApp Web
     ↓
Selenium Automation (Detection & Reply)
     ↓
Django Backend (Decision Engine)
     ↓
Database (User State + Contacts)
     ↓
Google Gemini API (AI Reply Generation)
     ↓
Response sent via Selenium



Workflow:
User receives a message on WhatsApp Web
Selenium detects the new message
Sender details are extracted
Backend checks:
Driving mode status
Contact information
Reply is generated (rule-based / AI-based)
Message is sent automatically



Tech Stack:
Python
Django
Selenium
MySQL
Google Gemini API
REST APIs

 
Cloud Deployment:
Backend deployed on cloud platform (e.g., Render)
Selenium bot runs locally due to browser dependency
Cloud backend handles logic and AI integration


Cost:
Development: Free (open-source tools)
Cloud: Free tier
AI API: Free tier



Future Scope
Mobile app integration
Real-time driving detection using sensors/GPS
Advanced AI conversation handling
Multi-platform support (Telegram, SMS)
Voice assistant integration


Author

Mohammed Rangwala
B.Tech CSE Student
