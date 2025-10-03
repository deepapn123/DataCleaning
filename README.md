# DataCleaning
To clean categorical data
Removes records containing numerical entry or empty value in categorical field.
```mermaid
graph TD
  A[Start] --> B[Read CSV file]
  B --> C{Is 'NAME' numeric or empty?}
  C -- Yes --> D[Drop the row]
  C -- No --> E[Keep the row]
  D --> F[Print cleaned DataFrame]
  E --> F
