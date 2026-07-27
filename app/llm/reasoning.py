import os


USE_OPENAI = bool(
    os.getenv("OPENAI_API_KEY")
)


if USE_OPENAI:

    from openai import OpenAI

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )



def generate_explanation(decision):


    # Use OpenAI only if a key exists

    if USE_OPENAI:

        try:

            prompt = f"""
You are an HR leave management AI assistant.

Explain this leave decision professionally.

Employee:
{decision["employee"]}

Days requested:
{decision["days_requested"]}

Decision:
{"Approved" if decision["approved"] else "Rejected"}

Confidence:
{decision["confidence"]}

Policy score:
{decision.get("policy_score")}

Risk score:
{decision.get("risk_score")}

Recommendation:
{decision.get("recommendation")}

Reasons:
{decision["reasons"]}

Risks:
{decision.get("risks")}
"""


            response = client.chat.completions.create(

                model=os.getenv(
                    "MODEL_NAME",
                    "gpt-4o-mini"
                ),

                messages=[
                    {
                        "role": "system",
                        "content":
                        "You explain HR decisions."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.3
            )


            return response.choices[0].message.content


        except Exception as e:

            print(
                "OpenAI failed:",
                e
            )



    # Local fallback reasoning

    status = (
        "approved"
        if decision["approved"]
        else "rejected"
    )


    explanation = (
        f"The leave request for "
        f"{decision['employee']} "
        f"has been {status}. "
        f"The decision was based on "
        f"a confidence score of "
        f"{decision['confidence']}."
    )


    if decision.get("reasons"):

        explanation += (
            " Key considerations: "
            +
            ", ".join(
                decision["reasons"]
            )
        )


    if decision.get("risks"):

        explanation += (
            " Identified risks: "
            +
            ", ".join(
                decision["risks"]
            )
        )


    return explanation