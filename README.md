# Leave AI Service

An Agentic AI microservice for intelligent HR leave management.

## Agents

- **Observation Agent**
  - Collects employee information, leave history, attendance data, and leave usage patterns.
  - Observes employee leave behaviour to provide context for AI decisions.

- **Reasoning Agent**
  - Analyses leave requests using company policies, employee history, attendance, and risk factors.
  - Evaluates whether requests align with organisational leave rules.

- **Decision Agent**
  - Evaluates requests and generates approval/rejection recommendations.
  - Produces confidence scores and explanations for every decision.

- **Confidence Agent**
  - Calculates the system's certainty in its recommendation.
  - Uses policy evaluation scores and risk assessment results to determine confidence.
  - A high confidence score indicates that the request strongly satisfies leave rules, while a low confidence score indicates uncertainty or detected risks.

- **Reminder Agent**
  - Proactively identifies employees with unused leave days.
  - Analyses leave usage patterns and recommends when employees should plan their leave.

- **Action Agent**
  - Executes actions such as saving decisions and generating employee leave reminders/notifications.

## Current Data Source

- Local database provider (SQLAlchemy)
- Test employee records
- Leave history records
- Attendance records

## Supported Integrations

- Database provider
- CheckinPro provider architecture (ready for integration)

## Future Data Source

- CheckinPro Database/API integration
- Real employee records
- Real leave policies
- Real attendance information
- CheckinPro notification services

## Current Capabilities

- AI-powered leave request evaluation
- Policy compliance checking
- Employee leave risk analysis
- Confidence-based recommendations
- Decision explanations
- Proactive leave usage reminders
- Employee notification workflow
- Agent-based decision-making using LangGraph workflow

## Confidence Scoring

The Confidence Agent determines how certain the AI system is about a leave decision.

The confidence score is generated using:

- Policy evaluation score
- Risk assessment score

Example:
Leave Request
|
↓
Policy Evaluation
|
↓
Risk Analysis
|
↓
Confidence Calculation
|
↓
Final Recommendation

Example outcomes:


Policy Score: 100
Risk Score: 0

Confidence: 100%
Recommendation: AUTO_APPROVE


Meaning:
> The AI is highly confident because the request follows leave policies and no risks were identified.



Policy Score: 50
Risk Score: 30

Confidence: 20%
Recommendation: REJECT


Meaning:
> The AI detected policy concerns and risks, therefore confidence in approval is low.

## Architecture


Employee Data
|
↓
Leave AI Service
|
├── Observation Agent
|
├── Reasoning Agent
|
├── Decision Agent
|
├── Confidence Agent
|
├── Reminder Agent
|
└── Action Agent
|
↓
Notifications