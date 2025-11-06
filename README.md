# DataCleaning
To clean categorical data - Removes records containing numerical entry or empty value in categorical field in cl.py. For NAME field also check for special characters except white space or . in clupdated.py
```mermaid
graph TD
  A[Start] --> B[Read CSV file]
  B --> C{Is 'NAME' numeric or empty or specical char space or .?}
  C -- Yes --> D[Drop the row]
  C -- No --> E[Keep the row]
  D --> F[Print cleaned DataFrame]
  E --> F
