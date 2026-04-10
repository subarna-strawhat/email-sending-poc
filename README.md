# High-Volume Email Sending POC

## Overview
This project demonstrates a simplified email sending system designed to simulate a scalable outbound email infrastructure.

## Features
- CSV-based input
- Batch queue processing
- Basic personalization
- Simulated email sending
- Conceptual domain rotation
- Bounce & reputation handling (explained)

## Architecture
<img width="652" height="952" alt="architecture png" src="https://github.com/user-attachments/assets/a4898fc9-06db-4305-90e8-e98ec461f0e0" />

## How It Works
1. Upload CSV file
2. Parse user data
3. Process users in batches
4. Personalize email content
5. Send emails via simulated function

## Scalability Considerations
- Queue system can be replaced with Redis/Kafka
- Email sending can integrate with SendGrid/AWS SES
- Domain/IP rotation can be automated
- Bounce handling can be integrated with webhook listeners

## Tech Used
- Python
- CSV processing
- Basic queue simulation

## Future Improvements
- Add real ESP integration
- Add UI dashboard
- Implement real-time analytics
