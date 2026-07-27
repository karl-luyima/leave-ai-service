# Leave AI Service

An Agentic AI microservice for intelligent HR leave management.

The Leave AI Service extends existing HR leave systems by using autonomous AI agents to analyse employee leave behaviour, evaluate leave requests, provide recommendations, and proactively notify employees about leave usage.

The system follows an Agentic AI workflow:


Observe → Reason → Decide → Act


---

# Agents

## Observation Agent

- Collects employee information, leave history, attendance data, and leave usage patterns.
- Retrieves relevant HR data from configured data providers.
- Provides contextual information required for AI reasoning.

---

## Reasoning Agent

- Analyses leave requests using:
  - Company leave policies
  - Employee leave history
  - Attendance patterns
  - Usage trends
  - Risk factors

- Determines whether requests align with organisational rules.

---

## Decision Agent

- Evaluates leave requests and generates recommendations.
- Produces:
  - Approval recommendations
  - Rejection recommendations
  - Review recommendations
  - Decision explanations

Example:

```json
{
  "decision": "APPROVE",
  "confidence": 0.87,
  "reason": "Employee has sufficient leave balance and satisfies company policy"
}
Confidence Agent
Calculates the certainty of AI recommendations.
Uses:
Policy evaluation scores
Risk assessment results
Decision factors

A high confidence score indicates strong alignment with leave policies, while a lower confidence score indicates uncertainty or detected risks.

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
Reminder Agent
Proactively analyses employee leave usage.
Identifies employees with:
High unused leave balances
Low leave utilisation
No recorded leave activity
Generates personalised leave reminders.

Example:

Employee:
John Doe

Analysis:
- 18 unused leave days
- Very low leave usage

Decision:
SEND_REMINDER

Confidence:
0.70
Action Agent
Executes AI-generated actions.
Handles:
Saving decisions
Generating reminders
Triggering employee notifications
Autonomous Reminder Scheduling

The system includes an automated scheduler that allows the AI service to operate proactively.

Workflow:

Scheduler Trigger
        |
        ↓
Reminder Agent
        |
        ↓
Leave Usage Analysis
        |
        ↓
Decision
        |
        ↓
Notification Service
        |
        ↓
Employee Reminder

The scheduler can run periodic checks and automatically notify employees who should plan their leave.

Current Data Source

The service currently supports:

SQLAlchemy database provider
Employee records
Leave history records
Attendance records
Leave policy information
Supported Integrations

Current:

Database provider architecture
Local test HR data
Notification service abstraction

Ready for:

CheckinPro database integration
CheckinPro Leave API integration
CheckinPro notification services
Current Capabilities

The Leave AI Service currently supports:

AI-powered leave request evaluation
Leave policy compliance checking
Employee leave usage analysis
Risk-based decision recommendations
Confidence scoring
Explainable AI decisions
Proactive leave balance reminders
Automated reminder scheduling
Employee notification workflow
Agent-based AI decision-making using LangGraph
Confidence Scoring

The Confidence Agent determines how certain the AI system is about its recommendation.

Confidence is calculated using:

Policy evaluation score
Risk assessment score
Decision factors

Example:

Policy Score: 100
Risk Score: 0

Confidence: 100%

Recommendation:
AUTO_APPROVE

Meaning:

The AI is highly confident because the request satisfies leave policies and no risks were identified.

Example:

Policy Score: 50
Risk Score: 30

Confidence: 20%

Recommendation:
REVIEW_REQUIRED

Meaning:

The AI detected possible policy concerns or risks and requires further review.

Architecture
                 Employee Data
                      |
                      ↓
              Leave AI Service
                      |
        --------------------------------
        |              |               |
        ↓              ↓               ↓

 Observation     Reasoning        Decision
   Agent           Agent            Agent

        |
        ↓

 Confidence Agent

        |
        ↓

 Reminder Agent
        |
        ↓

 Action Agent
        |
        ↓

 Notification Service
Technology Stack
Python
FastAPI
LangGraph
SQLAlchemy
APScheduler
Agent-based AI architecture
Future Enhancements
CheckinPro live database/API integration
Real-time employee notifications
Email/SMS integration
Reminder history tracking
Advanced leave forecasting
Learning-based leave behaviour prediction

This README now accurately represents what you have built: not just a leave analysis model, but an **Agentic AI HR assistant that observes, reasons, decides, and acts autonomously**.
send it as one thing 

Here is the complete README.md as one block you can copy directly:

# Leave AI Service

An Agentic AI microservice for intelligent HR leave management.

The Leave AI Service extends existing HR leave systems by using autonomous AI agents to analyse employee leave behaviour, evaluate leave requests, provide recommendations, and proactively notify employees about leave usage.

The system follows an Agentic AI workflow:


Observe → Reason → Decide → Act


---

# Agents

## Observation Agent

- Collects employee information, leave history, attendance data, and leave usage patterns.
- Retrieves relevant HR data from configured data providers.
- Provides contextual information required for AI reasoning.

---

## Reasoning Agent

- Analyses leave requests using:
  - Company leave policies
  - Employee history
  - Attendance patterns
  - Leave usage trends
  - Risk factors

- Evaluates whether requests align with organisational leave rules.

---

## Decision Agent

- Evaluates leave requests and generates AI recommendations.
- Produces:
  - Approval recommendations
  - Rejection recommendations
  - Review recommendations
  - Decision explanations

Example:

```json
{
  "decision": "APPROVE",
  "confidence": 0.87,
  "reason": "Employee has sufficient leave balance and satisfies company policy"
}
Confidence Agent
Calculates the system's certainty in its recommendation.
Uses:
Policy evaluation scores
Risk assessment results
Decision factors

A high confidence score indicates that the request strongly satisfies leave rules, while a low confidence score indicates uncertainty or detected risks.

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
Reminder Agent
Proactively identifies employees with unused leave days.
Analyses employee leave usage patterns.
Detects:
High unused leave balances
Low leave utilisation
Employees with no recorded leave activity
Generates personalised leave reminders.

Example:

Employee:
John Doe

Analysis:
- 18 unused leave days
- Very low leave usage

Decision:
SEND_REMINDER

Confidence:
0.70
Action Agent
Executes AI-generated actions.
Handles:
Saving decisions
Generating employee reminders
Triggering notifications
Autonomous Reminder Scheduling

The system includes an automated scheduler that allows the AI service to operate proactively without requiring manual requests.

Workflow:

Scheduler Trigger
        |
        ↓
Reminder Agent
        |
        ↓
Leave Usage Analysis
        |
        ↓
Decision
        |
        ↓
Notification Service
        |
        ↓
Employee Reminder

The scheduler periodically activates the Reminder Agent, which analyses employee leave data and sends reminders when necessary.

Current Data Source

The service currently supports:

SQLAlchemy database provider
Employee records
Leave history records
Attendance records
Leave policy information
Supported Integrations

Current:

Database provider architecture
Local HR test data
Notification service abstraction

Ready for:

CheckinPro database integration
CheckinPro Leave API integration
CheckinPro notification services
Current Capabilities

The Leave AI Service currently supports:

AI-powered leave request evaluation
Leave policy compliance checking
Employee leave usage analysis
Leave risk assessment
Confidence-based recommendations
Explainable AI decisions
Proactive leave usage reminders
Automated reminder scheduling
Employee notification workflow
Agent-based decision-making using LangGraph
Confidence Scoring

The Confidence Agent determines how certain the AI system is about its recommendation.

Confidence is generated using:

Policy evaluation score
Risk assessment score
Decision factors

Example:

Policy Score: 100
Risk Score: 0

Confidence: 100%

Recommendation:
AUTO_APPROVE

Meaning:

The AI is highly confident because the request follows leave policies and no risks were identified.

Example:

Policy Score: 50
Risk Score: 30

Confidence: 20%

Recommendation:
REVIEW_REQUIRED

Meaning:

The AI detected policy concerns or risks, therefore the decision requires further review.

Architecture
                 Employee Data
                      |
                      ↓
              Leave AI Service
                      |
        --------------------------------
        |              |               |
        ↓              ↓               ↓

 Observation     Reasoning        Decision
   Agent           Agent            Agent

        |
        ↓

 Confidence Agent

        |
        ↓

 Reminder Agent

        |
        ↓

 Action Agent

        |
        ↓

 Notification Service
Technology Stack
Python
FastAPI
LangGraph
SQLAlchemy
APScheduler
Agent-based AI architecture
Future Enhancements
CheckinPro live database/API integration
Real-time employee notifications
Email/SMS notification integrations
Reminder history tracking
Advanced leave forecasting
Machine learning-based employee leave behaviour prediction